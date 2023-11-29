import random

def generate_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

valid_ips = [generate_ip() for _ in range(10000)]

for i in valid_ips:
    print(i)
