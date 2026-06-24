import random
import string

def log_message(message):
    with open("log.txt", "a") as f:
        f.write(f"{message}\n")

def logger(func):
    def inner(*args, **kwargs):
        log_message(f"{func.__name__} started")

        result = func(*args, **kwargs)

        log_message(f"{func.__name__} ended")
        return result

    return inner


def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
