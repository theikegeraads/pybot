# imports
import discord
from discord.ext import commands
import math
import random
import yeelight
from yeelight import Bulb
import time
import json
import sys
import psutil
import os

# setup for prefix and Yeelight bulb
client = commands.Bot(command_prefix = '.')
bulb = Bulb('192.168.178.11')

# word split function for regional command
def split(word): 
    return [":regional_indicator_" + char + ":" for char in word]

# check for bot owner
def am_i_owner(ctx):
    return ctx.author.id == 464733215903580160

# global command prefix
client = commands.Bot(command_prefix = '.')

# on_ready event
@client.event
async def on_ready():
    print("Bot online!")

# say
@client.command()
async def say(ctx, *, txt):
    await ctx.send(f'{txt}')

# purge
@client.command()
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

# python randomization
# random word from english dictionary
@client.command()
async def word(ctx, amount=1):
    f = open('./command resources/word/words.txt')
    line = f.readlines()
    f.close
    last = len(line)-1
    rnd = random.randint(0, last)
    await ctx.send(line[rnd])

# rock paper scissors
@client.command()
async def rpc(ctx, play):
    sd = random.randint(0, 2)
    if sd == 0:
        cplay = "Rock!"
    elif sd == 1:
        cplay = "Paper!"
    elif sd == 2:
        cplay = "Scissors!"
    if play.upper() == "ROCK":
        if cplay == "Rock!":
            await ctx.send(cplay + " It's a tie!")
        elif cplay == "Paper!":
            await ctx.send(cplay + " I win!")
        elif cplay == "Scissors!":
            await ctx.send(cplay + " You win!")
    elif play.upper() == "PAPER":
        if cplay == "Rock!":
            await ctx.send(cplay + " You win!")
        elif cplay == "Paper!":
            await ctx.send(cplay + "It's a tie!")
        elif cplay == "Scissors!":
            await ctx.send(cplay + " I win!!")
    elif play.upper() == "SCISSORS":
        if cplay == "Rock!":
            await ctx.send(cplay + " I win!")
        elif cplay == "Paper!":
            await ctx.send(cplay + " You win!")
        elif cplay == "Scissors!":
            await ctx.send(cplay + " It's a tie!")
    else:
        await ctx.send("Something went wrong, try again!")
    
# coin flip
@client.command()
async def cf(ctx):
    side = random.randint(0,1)
    if side == 0:
        cside = "Heads!"
    elif side == 1:
        cside = "Tails!"
    await ctx.send("You flipped " + cside)

# dice roll
@client.command()
async def dice(ctx, limit=6):
    count = random.randint(1, limit)
    if limit < 6:
        await ctx.send("Minimum amount is 6!")
    else: 
        await ctx.send("You rolled " + str(count) + "!")

# python calculator / python math
@client.command()
async def calc(ctx, n1, operator, n2=0):
    if str(operator) == '+':
        await ctx.send(int(n1) + int(n2))
    elif str(operator) == '-':
        await ctx.send(int(n1) - int(n2))
    elif str(operator) == '*' or str(operator).upper() == 'X':
        await ctx.send(int(n1) * int(n2))
    elif str(operator) == '/':
        await ctx.send(int(n1) / int(n2))
    elif str(operator) == "pow":
        await ctx.send(pow(int(n1), int(n2)))
    elif str(operator) == "sqrt":
        await ctx.send(math.sqrt(int(n1)))

# word to regional text [uses split function]
@client.command()
async def regional(ctx, *, regio):
    if " " in regio:
     saferegio = regio.replace(" ", '')
     regchar = split(saferegio)    
    else:
     regchar = split(regio)
    upreg = ''.join(regchar)
    lowreg = upreg.lower()
    if "regional_indicator_b" in lowreg:
        send = lowreg.replace("regional_indicator_b", 'b')
        await ctx.send(send)
    else:
        await ctx.send(lowreg)

# file system
# write to file
@client.command()
async def writefile(ctx, *, write):
    if write == "clear":
        db = open("./command resources/rwfile/list.txt", "w")
        db.write("")
        db.close()
        await ctx.send("File cleared.")
    else:
        db = open('./command resources/rwfile/list.txt', "a")
        db.write(f"\n{write}")
        await ctx.send(f'"{write}" written to file.')
        db.close()

# read from file
@client.command()
async def readfile(ctx):
    db2 = open("./command resources/rwfile/list.txt", "r")
    db2text = db2.read()
    if db2text == "":
        await ctx.send("Cannot send empty message!")
    else:
        await ctx.send("\n" + db2text)
        db2.close()

#change bot presence
@client.command(hidden=True)
@commands.check(am_i_owner)
async def status(ctx, status):
    if status == "online":
        await client.change_presence(status=discord.Status.online)
        await ctx.send(f"Changed bot presence to: online.")
    if status == "idle":
        await client.change_presence(status=discord.Status.idle)
        await ctx.send(f"Changed bot presence to: idle.")
    if status == 'dnd': 
        await client.change_presence(status=discord.Status.dnd)
        await ctx.send(f"Changed bot presence to: do not disturb.")
    if status == "invisible":
        await client.change_presence(status=discord.Status.invisible)
        await ctx.send(f"Changed bot presence to: invisible.")

# python version check
@client.command()
async def version(ctx):
    version = sys.version
    await ctx.send('Bot is running on python ' + version) 

# bot login (put token in token.txt)
tokenfile = open("token.txt")
token = tokenfile.read()
client.run(token)