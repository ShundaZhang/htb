import os
from faker import Faker

fake = Faker()

generate = lambda x: os.urandom(x).hex()

invalid_chars = ["{{", "}}", ".", "_", "[", "]","\\", "x"]

def generate_user():
    return fake.user_name()
