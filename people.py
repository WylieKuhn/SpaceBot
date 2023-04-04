import requests


async def people(ctx):
    space_get = requests.get('http://api.open-notify.org/astros.json')
    space_response = space_get.json()
    my_data = {}

    for item in space_response['people']:
        if not my_data.get(item['craft']):
            my_data[item['craft']] = [item['name']]
            continue

        my_data[item['craft']].append(item['name'])

    total_counter = 0

    stations, current = '', ''

    for station, names in my_data.items():
        total_counter += len(names)
        current = f"{len(names)} on board the {station}:\n"

        for name in names:
            current += f"-{name}\n"

        stations += f"{current}\n"

    total = f"There are currently {space_response['number']} people in space on board the following spacecrafts\n\n{stations}"

    await ctx.respond(total)
