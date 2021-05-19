import random
import string

import requests
from bs4 import BeautifulSoup
from celery import Celery


CHARACTERS = string.ascii_letters + string.digits + '-_'


def get_random_string():
    return ''.join(random.choice(CHARACTERS) for _ in range(8))


def analyze_html(url):
    if 'http://' not in url and 'https://' not in url:
        url = 'http://' + url
    try:
        source = requests.get(url)
    except:
        raise
    tags_quantity = {}
    soup = BeautifulSoup(source.content, 'html.parser')
    for tag in soup.find_all():
        nested_quantity = len(tag.find_all())
        tag_name = tag.name
        if tag_name in tags_quantity:
            tags_quantity[tag_name]["count"] += 1
            tags_quantity[tag_name]["nested"] += nested_quantity
        else:
            tags_quantity[tag_name] = {"count": 1, "nested": nested_quantity}

    return tags_quantity
