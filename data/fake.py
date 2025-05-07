import random
import secrets
import string

from faker import Faker
from pytils.translit import RU_ALPHABET


fake = Faker()


def generate_email():
    return fake.email()


def generate_invalid_email():
    return fake.user_name()


def generate_password():
    return fake.password(length = random.randint(4, 10))


def random_cyrillic_string():
    random_cyrillic = "".join(random.choices(RU_ALPHABET, k = random.randint(10, 20)))
    return random_cyrillic


def generate_secret_token(length=128):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


wrong_email = generate_email()
wrong_password = generate_password()
invalid_email = generate_invalid_email()
random_invalid_search_keyword = random_cyrillic_string()
invalid_secret = generate_secret_token()
