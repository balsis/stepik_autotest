import random
from pytils.translit import RU_ALPHABET
from faker import Faker


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


wrong_email = generate_email()
wrong_password = generate_password()
invalid_email = generate_invalid_email()
random_invalid_search_keyword = random_cyrillic_string()
