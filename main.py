#Importing the needed stuff
import disnake
import disnake.ext
from disnake.ext import commands
from pathlib import Path

Bot = commands.Bot(
    command_prefix=disnake.ext.commands.when_mentioned, #So the code doesn't cry about it
    activity=disnake.Activity(type=disnake.ActivityType.watching, name="made by FQQD.ᴅᴇ") #The Discord status of the bot
)

#Spits out stuff in the console when ready to use
@Bot.event
async def on_ready():
    print(f'{Bot.user} has connected to Discord!')

#The "/message" command
@Bot.slash_command(name="message", description="Post an anonymous message")
async def add(inter, message):
    await inter.channel.send(message) #Sends the actual message
    #Making a beautiful embed for the response
    responseembed = disnake.Embed(
        title = f"Your message was sent:",
        description = f"'{message}'",
        colour = disnake.Colour.yellow(), #OHHH make it yellow
    )
    creator = await Bot.fetch_user(856509084563275786) #Get stuff from my discord profile so the stuff is accurate even if i change someting
    responseembed.set_footer(
        text=f"Hey! This bot was made by {creator.name}#{creator.discriminator}", icon_url='{}'.format(creator.avatar) #Little bit of self advertising yk
    )
    await inter.response.send_message(embed=responseembed, ephemeral=True) #Send the response embed, but only the author can see


#Get the token from a file named "token.txt"
tokenfile = Path(__file__).with_name('token.txt')
with open(tokenfile, 'r') as token:
    TOKEN = token.read()

#Runs the bot
Bot.run(TOKEN)