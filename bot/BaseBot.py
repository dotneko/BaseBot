# BaseBot
# Kudos to Sidpatchy - adapted and forked from : https://github.com/Sidpatchy/RomeBot

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as DT       # Imports datetime as DT so instead of typing 'datetime.datetime.now()' you type 'DT.datetime.now()' it saves time and looks less dumb than 'datetime.datetime.now()'
from time import sleep      # Imports sleep because time.sleep() doesn't work
import os
import sLOUT as lout

# Checks time that bot was started
botStartTime = DT.datetime.now()

# Store the bot version and release date
ver = ['v0.0.1', '2021-10-28']

# Define a config file for use in the log commands. 
config = 'config.yml'

# Prefix to be entered before commmands. Ex. !test
bot = commands.Bot(command_prefix='!')      # In this case the prefix is '!' so before typing a command you type '!' and then 'info'
bot.remove_command('help')                  # Removes the default help command

# Creates a log file if it doesn't already exist, and then writes to the file.
lout.writeFile('BaseBotLogs.txt', '\nBaseBot Initialized Successfully!', True)

# Things to run when the bot successfully connects to Discord
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=2, name='!info', url='', platform=''))
    lout.log(config, botStartTime, None, None, True)

# Command template
# @bot.command(pass_context=True)
# async def command_template(ctx):
#     startTime = DT.datetime.now()
#     await ctx.send('Message text', file=discord.File('images/image-file_file.jpg'))
#     lout.log(config, startTime, 'command_template')

# Command template target a mentioned @user
# @bot.command(pass_context=True)
# async def target(ctx, user: discord.Member):
#     startTime = DT.datetime.now()
#     await ctx.send('{} has been targeted'.format(user.display_name), file=discord.File('images/image-file.jpg'))
#     lout.log(config, startTime, 'target')

# Info Command
@bot.command(pass_context=True)
async def info(ctx):
    startTime = DT.datetime.now()       # Get the time the command was initiated at
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name='Need Help?', value='Help info')
    # embed.add_field(name='Add Me to a Server', value='Adding me to a server is simple, all you have to do is click [here](https://discord.bots.gg/bots/511050489928876052)')
    # embed.add_field(name='GitHub', value='BaseBot is open source, that means you can view all of its code! Check out its [GitHub!](https://github.com/Sidpatchy/BaseBot)')
    await ctx.send(embed=embed)             # Send the embed created above in the channel the command was run in.
    lout.log(config, startTime, 'info')     # Write to log

# !joined @user - Joined command
@bot.command(pass_context=True)
async def joined(ctx, user: discord.Member):
    startTime = DT.datetime.now()
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name=user.display_name, value='Join date: {}'.format(user.joined_at))
    await ctx.send(embed=embed)
    lout.log(config, startTime, 'joined')       # Use slout to write to the log and console

# !version
@bot.command(pass_context=True)
async def version(ctx):
    startTime = DT.datetime.now()
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name='BaseBot {}'.format(ver[0]), value='Released {}'.format(ver[1]))
    await ctx.send(embed=embed)
    lout.log(config, startTime, 'version ({})'.format(ver[0]))

# !time, states the server time
@bot.command(pass_context=True)
async def time(ctx):
    startTime = DT.datetime.now()
    await ctx.send('Server time is: {}'.format(DT.datetime.now()))
    lout.log(config, startTime, 'time')


# !uptime - Uptime, reports how long the bot has gone without a crash (or restart)
@bot.command(pass_context=True)
async def uptime(ctx):
    startTime = DT.datetime.now()
    runTime = startTime.replace(microsecond=0) - botStartTime.replace(microsecond=0)
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name='Uptime:', value=runTime)
    await ctx.send(embed=embed)
    lout.log(config, startTime, 'uptime')

# !servers - Servers, lists the number of servers the bot is in
@bot.command(pass_context=True)
async def servers(ctx):
    startTime = DT.datetime.now()
    numServers = len(bot.guilds)
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name='Number of servers enlightened:', value=numServers, inline=False)
    await ctx.send(embed=embed)
    lout.log(config, startTime, 'servers')

# !help - Adds a help command that sends a message to the user rather than spamming the chat with a long message
@bot.command(pass_context=True)
async def help(ctx):
    startTime = DT.datetime.now()
    author = ctx.message.author
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.set_author(name='Help')
    embed.add_field(name='!info', value='Get help', inline=False)
    embed.add_field(name='!joined @user', value='States when a user joined the server', inline=False)
    embed.add_field(name='!time', value='States what time it is on the server that the bot is hosted on', inline=False)
    embed.add_field(name='!uptime', value='BaseBot reports how long it has gone without crashing, previously', inline=False)
    embed.add_field(name='!servers', value='BaseBot states how many servers it is a member of', inline=False)
    embed.add_field(name='!version', value='Gives the version (and its release date) being run', inline=False)
    await author.send(embed=embed)
    lout.log(config, startTime, 'help')

# Remind me to install windows and then update compiler.bat
bot.run(lout.fetchToken(config))       # User defined bot token, get one here: https://discordapp.com/developers/applications/, then place it inside config.yml