# imports
import discord
import random
import asyncio
import aiohttp
import json
from discord.ext.commands import Bot
import chalk
import os


# main things
BOT_PREFIX = '!'
TOKEN = 'NTM4MTI3OTA0NTgwODI5MjA0.DyvSSQ.Fys8kK9amF5xNQwJL9elSwgWJpo'

# bot
client = Bot(command_prefix=BOT_PREFIX)
commands = discord.ext.commands

api = str(os.environ.get('RIOT_KEY'))

# events are something that happen with the bot
@client.event
async def on_ready():
    print(chalk.green('Logged in as'))
    print(chalk.magenta(client.user.name))
    print(chalk.magenta(client.user.id))
    print(chalk.green('-------------------'))


# commands are something that are created by the client


@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])


@client.command(pass_context=True)
async def eightball(ctx):
    embed = discord.Embed(colour=discord.Colour.orange())
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        'Come back later and ask again'
        ]

    answer = random.choice(possible_responses)

    embed.set_footer(text='Bot created by craig#5366 ⚬ Japan by Will.3774')
    embed.add_field(name='My Prediction is...', value=" " + answer + ctx.message.author.mention)
    await client.say(embed=embed)


# embed commands
@client.command()
@commands.has_any_role('Embed', 'Moderator', 'His Majesty Emperor of Japan')
async def ssu():
    embed = discord.Embed(
        title='Tokyo Server Startup',
        description='Server Startup in the Capital of Japan',
        colour=discord.Colour.blue()
    )

    embed.set_footer(text='Bot created by craig#5366 ⚬ Japan by Will.#3774')
    embed.set_author(name='Japan Service Helper')
    embed.add_field(name='**[SSU]** in Tokyo.',
                    value='https://www.roblox.com/games/2584751739/JP-Tokyo-Japan#!/game-instances', inline=True)

    await client.send_message(client.get_channel('336313710106902529'), '@here', embed=embed)


@client.command()
@commands.has_role('His Majesty Emperor of Japan')
async def raid():
    embed = discord.Embed(
        title='**Raid!**',
        description='Japan Self Defense Force',
        colour=discord.Colour.gold()
    )

    embed.set_footer(text='Bot created by craig#5366 ⚬ Japan by Will.#3774')
    embed.set_author(name='Japan Service Helper')
    embed.add_field(name='Raid in Camp Jinmachi!',
                    value='https://www.roblox.com/games/2646337427/Camp-Jinmachi-Japan', inline=True)

    await client.send_message(client.get_channel('336313710106902529'), '@here', embed=embed)


@client.command(pass_context=True)
@commands.has_any_role('Moderator', 'His Majesty Emperor of Japan')
async def announce(ctx, *, msg):
    embed = discord.Embed(title='**Announcement**', colour=discord.Colour.dark_red())
    embed.add_field(name='Announcement from {}'.format(ctx.message.author), value=msg)
    embed.set_footer(text='Bot created by craig#4366 ⚬ Japan by Will.3774')
    await client.send_message(client.get_channel('336313710106902529'), embed=embed)


# shows how many servers your bot is in.
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print(chalk.red('Current servers: '))
        for server in client.servers:
            print(chalk.red(server.name))
        await asyncio.sleep(600)  # 600 is 10 minutes in seconds, change this to whatever you want but 600 recommended

client.loop.create_task(list_servers())
client.run(str(os.environ.get(TOKEN)))
