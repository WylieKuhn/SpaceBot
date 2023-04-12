
import json
from dateutil import parser


async def spaceXLaunches(ctx):

    file = open("nextlaunch.json", encoding="utf-8")
    json_file = json.load(file)
    launches = ""

    # revamp from here down
    launch_string = "Upcoming SpaceX Launches:\n"
    for launch in json_file['results']:
        launch_string = launch_string + f"""
		```
		Name: {launch['name']}
		Description: {launch['status']['description']}
		Mission Type: {launch['mission']['type']}
		Location: {launch['pad']['name']}, {launch['pad']['location']['name']}, {launch['pad']['location']['country_code']}
		Launch Window (YYYY-MM-DD: 24 Hour Time Format): {parser.parse(launch['window_start'])} to {parser.parse(launch['window_end'])}
		```
		"""
        if len(launches) + len(launch_string) < 2000:
            launches = launch_string
        if len(launches) + len(launch_string) > 2000:
            break
    await ctx.respond(launches)
