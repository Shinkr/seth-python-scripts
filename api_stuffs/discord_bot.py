# Source for documentations : https://discordpy.readthedocs.io/
# Guide Followed : https://realpython.com/how-to-make-a-discord-bot-python/
# Api Testing : https://fakerestapi.azurewebsites.net/api/v1/Activities

# OS Functions
import os

# General Discord Bot 
import discord

# For the bot commands function
from discord.ext.commands import Bot

# .env files for security
from dotenv import load_dotenv

# http requests
import requests

# Json functions
import json

# .env for security
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = Bot(command_prefix='!')

@bot.command()
async def call_specific(ctx, args):

    print("API is Called")
    resp = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/{}'.format(args))

    data_in_json = resp.json()

    error = "status" in data_in_json

    # If error key exists
    if error is True:
        await ctx.send("Error : {}".format(data_in_json['status']))
        return

    # If not
    for x in data_in_json.keys():
        await ctx.send("{} : {}".format(x, data_in_json[x]))


@bot.event
async def on_ready():
    print("We have logged in as: {0.user}".format(bot))


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if message.content.startswith("shrug"):
        print("shrug")
        await message.channel.send('¯\_(ツ)_/¯')

    await bot.process_commands(message)

bot.run(TOKEN)

