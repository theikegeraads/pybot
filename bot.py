import discord
from discord.ext import commands
import math
import random
import yeelight
from yeelight import Bulb
import time


client = commands.Bot(command_prefix = ".")
bulb = Bulb('192.168.178.11')

# on_ready event
@client.event
async def on_ready():
    print("Ready!")

# purge
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

# say
@client.command()
async def say(ctx, markup, *, txt):
    if markup == "bold":
        await ctx.send(f'**{txt}**')
    elif markup == "italic":
        await ctx.send(f"*{txt}*")
    elif markup == "strikethrough":
        await ctx.send(f"~~{txt}~~")
    elif markup == "underline":
        await ctx.send(f"__{txt}__")
    elif markup == 'all':
        await ctx.send(f'__~~***{txt}***~~__')
    elif markup == "code":
        await ctx.send(f'```{txt}```')
    elif markup == "everyone":
        await ctx.send(f'@everyone {txt}')
    else:
        await ctx.send(f'{markup} {txt}')

# random word
@client.command()
async def word(cxt, amount=1):
    f = open('./command resources/word/words.txt')
    line = f.readlines()
    f.close
    last = len(line)-1
    rnd = random.randint(0, last)
    await cxt.send(line[rnd])

# neko 
@client.command()
async def neko(cxt):
    num = random.randint(1, 5)
    if num == 1:
        await cxt.send(file=discord.File('./command resources/nekoimages/meme.png'))
    elif num == 2:
        await cxt.send(file=discord.File('./command resources/nekoimages/nekoderp1.png'))
    elif num == 3:
        await cxt.send(file=discord.File('./command resources/nekoimages/nekoderp2.jpg'))
    elif num == 4:
        await cxt.send(file=discord.File('./command resources/nekoimages/nekofry.jpg'))
    elif num == 5:
        await cxt.send(file=discord.File('./command resources/nekoimages/heilneko.png'))
    else:
        await cxt.send("try again pls (", num, ")" )

# calculator
@client.command()
async def calc(cxt, n1, operator, n2=0):
    if str(operator) == '+':
        await cxt.send(int(n1) + int(n2))
    elif str(operator) == '-':
        await cxt.send(int(n1) - int(n2))
    elif str(operator) == '*' or str(operator).upper() == 'X':
        await cxt.send(int(n1) * int(n2))
    elif str(operator) == '/':
        await cxt.send(int(n1) / int(n2))
    elif str(operator) == "pow":
        await cxt.send(pow(int(n1), int(n2)))
    elif str(operator) == "sqrt":
        await cxt.send(math.sqrt(int(n1)))
# aldioder kids
@client.command()
async def kids(cxt):
   await cxt.send("Aldioder kids guida pamparaqui \nyubeder ran deder ram \nautron may gon :gun: \naldioder kids guida pamparaqui \nyubeder ran deder ram \nfaster dan may ballet")

@client.command()
async def light(cxt, state):
    if state == "on":
        bulb.turn_on()
    elif state == "off":
        bulb.turn_off()
    elif state == "red":
        bulb.set_rgb(255, 0, 0)
    elif state == "green":
        bulb.set_rgb(0, 255, 0)
    elif state == "blue":
        bulb.set_rgb(0, 0, 255)
    await cxt.send(f'Turning the light {state}.')

@client.command()
async def seizure(cxt, amount=1):
    times = 1
    while times <= int(amount):
        bulb.set_rgb(255, 0, 0, effect="sudden")
        time.sleep(0.125)
        bulb.set_rgb(0, 255, 0, effect="sudden")
        time.sleep(0.125)
        bulb.set_rgb(0,0 ,255, effect="sudden")
        time.sleep(0.125)
        times += 1
    await cxt.send("pls have seizure")

tokenfile = open("token.txt")
token = tokenfile.read()
client.run(token)