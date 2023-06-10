import disnake
import disnake.ext
from disnake.ext import commands
from pathlib import Path

bot = commands.Bot(
    command_prefix=disnake.ext.commands.when_mentioned,
    activity=disnake.Activity(type=disnake.ActivityType.watching, name="made by FQQD.ᴅᴇ")  # "watching" status
)

# Spits out stuff in the console when ready to use
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# The "/message" command
@bot.slash_command(name="message", description="Post an anonymous message")
async def add(interaction: disnake.Interaction, message: str):
    await interaction.channel.send(message)

    creator = await bot.get_user(856509084563275786)  # look in cache before making api request
    if creator is None:
        creator = await bot.fetch_user(856509084563275786)

    # response embed
    embed = disnake.Embed(
        title="Your message was sent:",
        description=f"'{message}'",
        colour=disnake.Colour.yellow(),
    )

    embed.set_footer(
        text=f"Hey! This bot was made by {creator}", icon_url=creator.display_avatar #Little bit of self advertising yk
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)


# Get the token from a file named "token.txt"
tokenfile = Path(__file__).with_name('token.txt')
with open(tokenfile, 'r') as token:
    TOKEN = token.read()

# Runs the bot
bot.run(TOKEN)
