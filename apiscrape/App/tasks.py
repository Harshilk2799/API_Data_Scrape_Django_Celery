from celery import shared_task
from .models import Comments
import requests

@shared_task
def api_scrape(url):
    response = requests.get(url)
    records = response.json()

    for record in records:
        obj = Comments()

        obj.name = record["name"]
        obj.email = record["email"]
        obj.description = record["body"]


        obj.save()

    return "Scrape All the records from API"