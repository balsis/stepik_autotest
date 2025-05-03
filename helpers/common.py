import os

import tests


def file_path(file_name: str):
    test_dir = os.path.dirname(tests.__file__)

    if file_name.endswith('apk'):
        return os.path.abspath(
            os.path.join(test_dir, f'../resources/{file_name}')
        )
    else:
        return os.path.abspath(
            os.path.join(test_dir, f'../{file_name}')
        )
