from .. import schema
import hashlib
import random

url_mappings = {
    "yt": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}

def is_alias_exist(alias,url):
    return alias in url_mappings and url_mappings[alias] != url

def generate_random_number():
    return str(random.randint(1, 9999))

def generate_hash(url):
    hash_object = hashlib.sha256(url.encode())
    hex_hash = hash_object.hexdigest()
    return hex_hash

def get_unique_alias(url):
    hash = generate_hash(url)
    alias = hash[:7]
    while is_alias_exist(alias,url):
        random_number = generate_random_number()
        url = f"{url}{random_number}"
        hash = generate_hash(url)
        alias = hash[:7]
    return alias

def get(alias: str) -> str:
    return url_mappings.get(alias)

def set(data: schema.CreateRequest) -> str:
    alias = get_unique_alias(data.url)
    url_mappings[alias] = data.url
    return alias