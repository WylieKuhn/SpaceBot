import requests

async def next_five(ctx) -> str:
    
    """
    Returns the next few spacecraft launches
    """
    launches = requests.get(
        "https://fdo.rocketlaunch.live/json/launches/next/5",
        timeout=3
        )
    launches_json = launches.json()
    print(launches_json)

    response_string = "Here is the data for the next upcoming spacecraft launches\n"

    for launch in launches_json['result']:
        next_launch_string = ""
        next_launch_string = next_launch_string + f"""
        ```
        Company/Agency: {launch['provider']['name']}
        Mission Name: {launch['name']}
        Vehicle: {launch['vehicle']['name']}
        Launch Site: {launch['pad']['location']['name']}, {launch['pad']['location']['state']}, {launch['pad']['location']['country']}
        Suborbital: {launch['suborbital']}
        """
        if launch['missions'][0]['name'] is not None:
            next_launch_string = next_launch_string + \
                f"{launch['missions'][0]['name']}\n"
        if launch['missions'][0]['description'] is not None:
            next_launch_string = next_launch_string + \
                f"        {launch['missions'][0]['description']}"
        next_launch_string = next_launch_string + \
            f"        {launch['launch_description']}\n        ```"
        if len(next_launch_string) + len(response_string) > 2000:
            break
        else:
            response_string = response_string + next_launch_string
        await ctx.send(response_string)
        
    await ctx.respond("response_string")
