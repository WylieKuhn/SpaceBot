
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
    

    await ctx.send(f"Upcoming SpaceX Launches As requested By {ctx.author.mention}")
    for launch in json_file['results']:
        launch_string = f"""
		```
		Name: {launch['name']}
		Description: {launch['status']['description']}
		Mission Type: {launch['mission']['type']}
		Location: {launch['pad']['name']}, {launch['pad']['location']['name']}, {launch['pad']['location']['country_code']}
		Launch Window (YYYY-MM-DD: 24 Hour Time Format): {parser.parse(launch['window_start'])} to {parser.parse(launch['window_end'])}
		```
		"""
        await ctx.respond(launch_string)
