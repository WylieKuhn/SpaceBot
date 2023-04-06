import requests
import discord

async def iss(ctx,key):
    """
    Returns the current GPS coordinates of the ISS, as well as a google maps link showing the visual location.
    """
    
    len_check = 1
    quit_counter = 0
    location_get = requests.get('http://api.open-notify.org/iss-now.json')
    location_get_response = location_get.json()

    while len_check <= 1:
        if quit_counter < 6:
            try:
                location_data = requests.get(f"http://api.positionstack.com/v1/reverse?access_key={key}&query={location_get_response['iss_position']['latitude']},{location_get_response['iss_position']['longitude']}&output=json")
                finaldata = location_data.json()
                len_check = len(finaldata['data'][0])

                if finaldata['data'][0]['country'] is None:
                    location = f"""The current location of the ISS is:
                    Latitude: {location_get_response['iss_position']['latitude']}
                    Longitude: {location_get_response['iss_position']['longitude']}
                    Which is over the {finaldata['data'][0]['name']}
                    https://www.google.com/maps/search/?api=1&query={location_get_response['iss_position']['latitude']},{location_get_response['iss_position']['longitude']}"""
                    await ctx.respond(location)

                if finaldata['data'][0]['country'] is not None:
                    location = f"The current location of the ISS is:\n Latitude: {location_get_response['iss_position']['latitude']}\n Longitude: {location_get_response['iss_position']['longitude']}\n Which is over {finaldata['data'][0]['name']} in {finaldata['data'][0]['country']}\n https://www.google.com/maps/search/?api=1&query={location_get_response['iss_position']['latitude']},{location_get_response['iss_position']['longitude']}"
                    await ctx.respond(location)

            except RuntimeError as APIFailure:
                quit_counter = quit_counter+1
                print(f"Failed because of {APIFailure}. Trying {6-quit_counter} more times")

        if quit_counter >= 6:
            break
