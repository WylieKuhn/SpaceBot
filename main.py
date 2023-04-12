import discord
from iss import iss
from people import people
from flyover import flyover
from info import info
from nearEarthObjects import near_earth_objects
from overhead import overhead
from launches import next_five
from spacex import spacex_launches
from neo_query import get_neo_data
import logging
from spacexjson import get_spacex_launch_data
from keys import n2yoKey, positionKey, discordToken, nasa_key
from discord.ext import tasks

logging.basicConfig(level=logging.INFO)


n2Key = n2yoKey
pKey = positionKey
dToken = discordToken
nasakey = nasa_key
get_spacex_launch_data()
get_neo_data(key=nasakey)


# load all the variables from the env file
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hello!")


@bot.slash_command(name="people", description = "See a list of people in space and what craft they are on")
async def people_in_space(ctx):
    await people(ctx)


@bot.slash_command(name="info", description = "for debugging")
async def information(ctx):
    await info(ctx)


@bot.slash_command(name="flyover", description="Enter your address and see when the ISS will be in your area!")
async def fly(ctx, message):
    await flyover(ctx, message, n2Key)


@bot.slash_command(name="iss", description = "get the current location of the International Space Station")
async def position(ctx):
    await iss(ctx, pKey)


@bot.slash_command(name="overhead", description="Shows a list of all objects in space over the given address in a 2 degree radius")
async def over(ctx, message):
    await overhead(ctx, message, n2Key)


@bot.slash_command(name="lasers", description="Do you even need to ask?")
async def lasers(ctx):
    await ctx.respond("https://i.giphy.com/media/3oKIPuM1xeVUMZqbq8/giphy.gif")

@bot.slash_command(name="launches", description="See upcoming spacecraft launches")
async def launch(ctx):
    await next_five(ctx)

@bot.slash_command(name="author", description="For debugging")
async def person(ctx):
    print(f"Author Command From {ctx.author.name}")
    await ctx.respond("Done")
    
@bot.slash_command(name="spacexlaunches", description="Next SpaceX Launches")
async def next_launch(ctx):
    await spacex_launches(ctx)
    
@bot.slash_command(name="nearearthobjects", description="Show all objects coming close to earth between two dates")
async def neo(ctx):
    await near_earth_objects(ctx)
    
@tasks.loop(hours=2)
async def get_spacex_launches():
    await get_spacex_launch_data()
    
@tasks.loop(hours=24)
async def neo_display(ctx):
    await get_neo_data(key=nasakey)

bot.run(discordToken)  # run the bot with the token