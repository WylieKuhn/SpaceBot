import requests
import datetime


async def flyover(ctx, message, key):
    """
    Returns the start, middle, and end date and times of when the ISS will be visible from the provided address.
    Includes azmuth and altitude as well as ISS brightness.
    """
    print("!flyover request")
    splitted = message.split(',')
    street = '+'.join(splitted[0].split(' '))
    city = '+'.join(splitted[1][1:].split())
    state = splitted[2][1:]
    zip_code = splitted[3][1:]

    census_code = requests.get(
        f'https://geocoding.geo.census.gov/geocoder/locations/address?street={street}&city={city}&state={state}&zip={zip_code}&benchmark=Public_AR_Census2020&format=json')
    response = census_code.json()
    visual = requests.get(
        f"https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/{response['result']['addressMatches'][0]['coordinates']['y']}/{response['result']['addressMatches'][0]['coordinates']['x']}/0/2/300/&apiKey={key}")
    visual = visual.json()

    information = f"""
        Next ISS flyover schedule information for your area \n
            Time Visible {round(visual['passes'][0]['duration'] / 60, 2)} minutes \n
            Max visual magnitude: {visual['passes'][0]['mag']} \n
            Start Date & Time: {datetime.datetime.fromtimestamp(visual['passes'][0]['startUTC'])} EST
            Start Azmuth: {visual['passes'][0]['startAz']}, {visual['passes'][0]['startAzCompass']}
            Start Elevation: {str(visual['passes'][0]['startEl'])} \n
            Max Azmuth Start Date & Time: {datetime.datetime.fromtimestamp(visual['passes'][0]['maxUTC'])} EST
            Max Azmuth: {visual['passes'][0]['maxAz']}, {visual['passes'][0]['maxAzCompass']}
            Max Elevation: {str(visual['passes'][0]['maxEl'])} \n 
            End Date & Time: {datetime.datetime.fromtimestamp(visual['passes'][0]['endUTC'])} EST
            End Azmuth: {visual['passes'][0]['endAz']}, {visual['passes'][0]['endAzCompass']}
            End Elevation: {str(visual['passes'][0]['endEl'])} \n
        
    """
    await ctx.respond(information)