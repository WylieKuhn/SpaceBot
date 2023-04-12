async def info(ctx):
    """
    Returns information about the use of the bot to the user
    """
    information = """Welcome to SpaceBot! The following commands are availible: 
    ```
    /info: This command 
    /iss: See where the International Space Station currently is!
    /people: See all the people in space and what craft they are on board
    /overhead: Returns a list of all objects over the provided address in space in a 2 degree radius
    /flyover: Returns information for when the ISS whill next be visible from the provided address. Get your telescopes ready!
    
    IMPORTANT: ALL ADDRESSES MUST BE IN THE FOLLOWING FORMAT: Street Address, City, State, ZIP.
    EXAMPLE: 123 Some Street, Some Town, NY, 12345
    ```
    """
    await ctx.respond(information)
    