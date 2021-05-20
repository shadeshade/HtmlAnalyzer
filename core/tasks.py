import requests
from bs4 import BeautifulSoup

from HtmlAnalyzer.celery import app
from core.helpers import normalize_url
from core.models import Task


@app.task
def analyze_html(identifier):
    task = Task.objects.get(identifier=identifier)
    url = normalize_url(task.url)
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
