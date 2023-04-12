import json


async def near_earth_objects(ctx):
    file = open("neo.json", encoding="utf-8")
    data = json.load(file)

    count = 0
    response_string = f"{len(data['near_earth_objects'])} Objects passing close to earth in the next 7 days, probably showing fewer due to discord message length restrictions. \n Refreshes every 24 hours.\n"

    for neo_object in data['near_earth_objects']:
        object_string = f"""
        ID: {data['near_earth_objects'][neo_object][0]['id']}
        Name: {data["near_earth_objects"][neo_object][0]["name"]}
        Close Approach Date: {data["near_earth_objects"][neo_object][0]['close_approach_data'][0]['close_approach_date_full']}
        Potentially Hazardous: {data["near_earth_objects"][neo_object][0]['is_potentially_hazardous_asteroid']} 
        Miss Distance: {data["near_earth_objects"][neo_object][0]['close_approach_data'][0]['miss_distance']['kilometers']} kilometers
        Velocity: {data["near_earth_objects"][neo_object][0]['close_approach_data'][0]['relative_velocity']['kilometers_per_second']} kilometers per second
        Minimum Diameter: {data["near_earth_objects"][neo_object][0]
              ["estimated_diameter"]["meters"]["estimated_diameter_min"]} meters
        Maximum Diameter: {data["near_earth_objects"][neo_object][0]
              ["estimated_diameter"]["meters"]["estimated_diameter_max"]} meters
        JPL URL: https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr={data['near_earth_objects'][neo_object][0]['neo_reference_id']}
              
        """
        if len(object_string) + len(response_string) < 2000:
            response_string = response_string + object_string
        elif len(object_string) + len(response_string) > 2000:
            break
    await ctx.respond(response_string)
