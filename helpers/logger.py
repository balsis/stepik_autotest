import json
import logging
from functools import wraps

import allure
import curlify
from allure_commons.types import AttachmentType

from config import project_config


def setup_logger(module_name: str) -> logging.Logger:
    log_level = project_config.base.log_level
    my_logger = logging.getLogger(module_name)

    if not my_logger.handlers:
        my_logger.setLevel(log_level)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(
            logging.Formatter(
                "\n%(asctime)s %(filename)-15s %(real_func)-25s - %(levelname)-6s - %(message)s"
            )
        )
        my_logger.addHandler(console_handler)
        my_logger.propagate = False

    return my_logger


logger = setup_logger(__name__)


def http_logger(max_body_length=2000):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            base_url = project_config.base.base_url
            response = func(self, *args, **kwargs)
            full_url = response.request.url
            if full_url.startswith(base_url):
                path = full_url.removeprefix(base_url)

            request_curl = curlify.to_curl(response.request)
            status_line = f"{response.status_code} {response.reason}"
            headers = "\n".join(f"{k}: {v}" for k, v in response.headers.items())

            try:
                body = json.dumps(response.json(), indent = 2, ensure_ascii = False)
            except ValueError:
                body = response.text

            if len(body) > max_body_length:
                truncated_body = body[:max_body_length] + ("\n<<...truncated output...>>")
            else:
                truncated_body = body

            http_request = f"\n{request_curl}\n\n"
            http_response = f"\n{status_line}\n{headers}\n\n{body}"
            http_truncated_response = f"\n{status_line}\n{headers}\n\n{truncated_body}"
            logger.debug(
                f"[HTTP request for {path}]{http_request}",
                extra = {"real_func": func.__qualname__}
            )
            logger.debug(
                f"[HTTP response from {path}]{http_truncated_response}",
                extra = {"real_func": func.__qualname__}
            )
            allure.attach(body = http_request, name = f'HTTP request for {path}', attachment_type = AttachmentType.TEXT, extension = 'txt')
            allure.attach(body = http_response, name = f'HTTP response from {path}', attachment_type = AttachmentType.TEXT, extension = 'txt')
            return response

        return wrapper

    return decorator
