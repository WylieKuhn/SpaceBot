import datetime
from datetime import timedelta
import json
import requests


def get_neo_data(key):
    """
    Queries the NASA near earth object API and saves it to a local JSON file.
    """
    response = requests.get(
        f"https://api.nasa.gov/neo/rest/v1/feed?start_date={datetime.date.today()}&end_date={datetime.date.today() + timedelta(days=7)}&api_key={key}", 
        timeout=30
        )
    response = response.json()
    json_to_write = response
    json_to_file = json.dumps(json_to_write, indent=4)
    with open("neo.json", "w", encoding="utf-8") as out:
        out.write(json_to_file)