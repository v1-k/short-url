import hashlib
import random
from sqlalchemy.orm import Session
from .. import schema
from . import model

n = 8

def get(short_url: str, db: Session):
    return db.query(model.Alias).filter(model.Alias.short_url == short_url).first()

def set(data: schema.CreateRequest, db: Session):
    short_url, url_exist  = get_unique_alias(data.url, db)
    if not url_exist:
        data.short_url = short_url
        new_short_url = model.Alias(**data.model_dump())
        db.add(new_short_url)
        db.commit()
        db.refresh(new_short_url)
    return short_url

def generate_random_number():
    return str(random.randint(1, 9999))

def generate_hash(url):
    hash_object = hashlib.sha256(url.encode())
    hex_hash = hash_object.hexdigest()
    return hex_hash

def get_short_hash(hash):
    return hash[:n]

def is_pair_exist(short_url, url, db: Session):
    existing_alias = db.query(model.Alias).filter(model.Alias.short_url == short_url).first()
    if existing_alias:
        if existing_alias.url == url:
            return True, True
        return True, False
    return False, False

def get_unique_alias(url, db: Session):
    hash = generate_hash(url)
    short_url = get_short_hash(hash)
    alias_exist, url_exist = is_pair_exist(short_url, url, db)
    while alias_exist and not url_exist:
        random_number = generate_random_number()
        url = f"{url}{random_number}"
        hash = generate_hash(url)
        short_url = get_short_hash(hash)
        alias_exist, url_exist = is_pair_exist(short_url, url, db)
    return ( short_url, url_exist )