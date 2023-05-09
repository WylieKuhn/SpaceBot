import requests


async def overhead(ctx, message, key):
    """
    Returns basic information about all objects in space over the entered address in a 2 degree radius
    """

    # parses the address into its individual parts to insert into the census api
    splitted = message.split(',')
    street = '+'.join(splitted[0].split(' '))
    city = '+'.join(splitted[1][1:].split())
    state = splitted[2][1:]
    zip_code = splitted[3][1:]

    census_code = requests.get(
        f'https://geocoding.geo.census.gov/geocoder/locations/address?street={street}&city={city}&state={state}&zip={zip_code}&benchmark=Public_AR_Census2020&format=json',
        timeout=3
        )
    response = census_code.json()
    
    

    # Passes GPS coordinates to N2YO API to retrieve all overhead objects in a 2 degree radius
    visual = requests.get(
        f"https://api.n2yo.com/rest/v1/satellite/above/{response['result']['addressMatches'][0]['coordinates']['y']}/{response['result']['addressMatches'][0]['coordinates']['x']}/0.0/2/0&apiKey={key}",
        timeout=3
    )
    visual = visual.json()
    print(visual)

    output = ""

    if visual is None:
        await ctx.send("There are no objects currently overhead")
    elif len(visual['above']) == 1:
        await ctx.send(f"There is currently 1 object overhead\n Name: {visual['above'][0]['satname']}.\n Date Launched: {visual['above'][0]['launchDate']}.\n Altitude: {round(visual['above'][0]['satalt'], 2)} kilometers, or {round(visual['above'][0]['satalt'] / 1.609, 2)} miles.")
    elif len(visual['above']) > 1:
        await ctx.send(f"There are currently {len(visual['above'])} objects overhead\n\n")
        
        async with ctx.typing():
            for sat in visual['above']:
                output = f"Name: {sat['satname']}.\n Date Launched: {sat['launchDate']}.\n Altitude: {round(sat['satalt'], 2)} kilometers, or {round(sat['satalt'] / 1.609, 2)} miles.\n\n"
                await ctx.send(output)
    
