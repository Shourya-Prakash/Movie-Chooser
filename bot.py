import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


ping = ["<@!359264609963868161>"]


client = discord.Client()

@client.event
async def on_ready():
    print (f"{client.user.name} has been connected to the Discord!")


@client.event
async def on_message(message):
    if message.content == '<@!359264609963868161>':
        await message.create_dm()
        await message.dm_channel.send(ping)    

client.run(TOKEN)