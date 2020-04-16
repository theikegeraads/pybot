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
import googletrans
from googletrans import Translator
from googletrans import LANGUAGES
from twilio.rest import Client
import dotenv
from dotenv import load_dotenv
from musixmatch import Musixmatch


# setup for prefix and general stuff
client = commands.Bot(command_prefix = '>')

bulbIP = open("./tokenstuff/bulbIP.txt").read()
bulb = Bulb(bulbIP)

accsid = open('./tokenstuff/twilio.txt').read(1)
authtoken = open('./tokenstuff/twilio.txt').read(2)
twilliapp = Client(accsid, authtoken)

mmtoken = open('./tokenstuff/musixmatch.txt').read()
musixmatch = Musixmatch()
trans = Translator()

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
    if limit < 6:
        await ctx.send("Minimum amount is 6!")
    else:
        count = random.randint(1, limit)
        diceembed = discord.Embed(title="Dice roll", color=0x6495ed)
        diceembed.add_field(name="Range:", value=f'6 - {limit}')
        diceembed.add_field(name="You rolled:", value=count)
        await ctx.send(embed=diceembed)

    

# python calculator / python math
@client.command()
async def calc(ctx, n1, operator, n2=0):
    if str(operator) == '+':
        answer = int(n1) + int(n2)
    elif str(operator) == '-':
        answer = int(n1) - int(n2)
    elif str(operator) == '*' or str(operator).upper() == 'X':
        answer = int(n1) * int(n2)
    elif str(operator) == '/':
        answer = int(n1) / int(n2)
    elif str(operator) == "pow":
        answer = pow(int(n1), int(n2))
    elif str(operator) == "sqrt":
        answer = math.sqrt(int(n1))
    calculation = str(n1) + " " + operator + " " + str(n2)
    if "sqrt 0" in calculation:
      calculation = calculation.replace("sqrt 0", "sqrt")
    calculatorembed = discord.Embed(title="Calculator", color=0x6495ed)
    calculatorembed.add_field(name="Calculation:", value=calculation)
    calculatorembed.add_field(name="Answer:", value=answer)
    await ctx.send(embed=calculatorembed)

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

# yeelight control
@client.command()
@commands.check(am_i_owner)
async def light(ctx, state, red=0, green=0, blue=0):
    if state == "on":
        bulb.turn_on()
        await ctx.send(f'Turning the light {state}.')
    elif state == "off":
        bulb.turn_off()
        await ctx.send(f'Turning the light {state}.')
    elif state == "red":
        bulb.set_rgb(255, 0, 0)
        await ctx.send(f'Turning the light {state}.')
    elif state == "green":
        bulb.set_rgb(0, 255, 0)
        await ctx.send(f'Turning the light {state}.')
    elif state == "blue":
        bulb.set_rgb(0, 0, 255)
        await ctx.send(f'Turning the light {state}.')
    elif state == "stats":
        properties = bulb.get_properties()
        power = properties["power"]
        color = properties["rgb"]
        brightness = properties["current_brightness"] + "%"
        mode = properties['color_mode']
        colorhex = hex(int(color))
        colorhex = colorhex.replace("0x", "#")
        lightembed = discord.Embed(title="Light status", color=0x6495ed)
        lightembed.add_field(name="Power:", value=power)
        lightembed.add_field(name="Color:", value=colorhex)
        lightembed.add_field(name="Brightness:", value=brightness)
        lightembed.add_field(name="Color mode:", value=mode)
        lightembed.set_footer(text=bulbIP)
        await ctx.send(embed=lightembed)
    elif state == "rgb":
        if red > 255 or green > 255 or blue > 255:
            await ctx.send("Please use values between 0 - 255.")
        else: 
            bulb.set_rgb(red, green, blue)
            await ctx.send(f'Set RGB value to: {red}, {green}, {blue}')
    else:
        await ctx.send(f'{state} is not a valid state!')

# translator
@client.command()
async def translate(ctx, *, word):
    langcodes = googletrans.LANGUAGES
    translatedtstring = trans.translate(word)
    translatedword = translatedtstring.text
    originword = translatedtstring.origin
    srclangcode = translatedtstring.src
    destlangcode = translatedtstring.dest
    srclang = langcodes[srclangcode]
    destlang = langcodes[destlangcode]
    translateembed = discord.Embed(title="Translate", color=0x6495ed)
    translateembed.add_field(name='From: ' + srclang, value=originword)
    translateembed.add_field(name="To: " + destlang, value=translatedword)
    await ctx.send(embed=translateembed)

@client.command()
@commands.check(am_i_owner)
async def whatsapp(ctx, message):
    from_whatsapp_number='whatsapp:+14155238886'
    to_whatsapp_number='whatsapp:+31621713391'
    twillapp.messages.create(body=message, from_=from_whatsapp_number, to=to_whatsapp_number)

@client.command()
async def lyrics(ctx, q_track, q_artist):

    lyrics = musixmatch.matcher_lyrics_get(q_track, q_artist)
    await ctx.send(lyrics)

# bot login (put token in token.txt)
tokenfile = open("./tokenstuff/pybot.txt")
token = tokenfile.read()
client.run(token)