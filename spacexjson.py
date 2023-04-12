import json
from datetime import datetime
import requests

def get_spacex_launch_data() -> None:
    now_ts = datetime.now().timestamp()
    response = requests.get(
        "https://lldev.thespacedevs.com/2.2.0/launch/upcoming/?search=SpaceX", 
        timeout=3
        )
    response = response.json()
    json_to_write = response
    json_to_write['time_queried'] = now_ts
    json_to_file = json.dumps(json_to_write, indent=4)
    with open("nextlaunch.json", "w", encoding="utf-8") as out:
        out.write(json_to_file)
