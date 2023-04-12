
import json
from dateutil import parser


async def spacex_launches(ctx):
    """
    Returns the next few upcoming SpaceX launches to the discord channel. 
    It is ependent on the amount of information in the response fields
    how many responses can be returned due to Discord's 2000 character message limit.
    """

    file = open("nextlaunch.json", encoding="utf-8")
    json_file = json.load(file)
    launches = ""

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
