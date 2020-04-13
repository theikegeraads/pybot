import discord
from discord.ext import commands
import math
import random
import yeelight
from yeelight import Bulb
import time


def split(word): 
    return [":regional_indicator_" + char + ":" for char in word]
bwlist = open("./command resources/word/badword.txt")
badword = bwlist.read()

client = commands.Bot(command_prefix = '.')
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
async def say(ctx, *, txt):
    await ctx.send(f'{txt}')
    # if markup == "bold":
    #     await ctx.send(f'**{txt}**')
    # elif markup == "italic":
    #     await ctx.send(f"*{txt}*")
    # elif markup == "strikethrough":
    #     await ctx.send(f"~~{txt}~~")
    # elif markup == "underline":
    #     await ctx.send(f"__{txt}__")
    # elif markup == 'all':
    #     await ctx.send(f'__~~***{txt}***~~__')
    # elif markup == "code":
    #     await ctx.send(f'```{txt}```')
    # elif markup == "everyone":
    #     await ctx.send(f'@everyone {txt}')
    # elif markup == "normal":
    #     await ctx.send(f"{txt}")
    # else:
    #     await ctx.send(f'{markup} {txt}')

# random word
@client.command()
async def word(ctx, amount=1):
    f = open('./command resources/word/words.txt')
    line = f.readlines()
    f.close
    last = len(line)-1
    rnd = random.randint(0, last)
    await ctx.send(line[rnd])

# neko 
@client.command()
async def neko(ctx):
    num = random.randint(1, 5)
    if num == 1:
        await ctx.send(file=discord.File('./command resources/nekoimages/meme.png'))
    elif num == 2:
        await ctx.send(file=discord.File('./command resources/nekoimages/nekoderp1.png'))
    elif num == 3:
        await ctx.send(file=discord.File('./command resources/nekoimages/nekoderp2.jpg'))
    elif num == 4:
        await ctx.send(file=discord.File('./command resources/nekoimages/nekofry.jpg'))
    elif num == 5:
        await ctx.send(file=discord.File('./command resources/nekoimages/heilneko.png'))
    else:
        await ctx.send("Something went wrong. (", num, ")" )

# calculator
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
# aldioder kids
@client.command()
async def kids(ctx):
   await ctx.send("Aldioder kids guida pamparaqui \nyubeder ran deder ram \nautron may gon :gun: \naldioder kids guida pamparaqui \nyubeder ran deder ram \nfaster dan may ballet")
   await ctx.send(file=discord.File('./command resources/kids/Aldioder kids.mp3'))
@client.command()
async def light(ctx, state):
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
    await ctx.send(f'Turning the light {state}.')

@client.command()
async def seizure(ctx, amount=1):
    times = 1
    while times <= int(amount):
        bulb.set_rgb(255, 0, 0, effect="sudden")
        time.sleep(0.125)
        bulb.set_rgb(0, 255, 0, effect="sudden")
        time.sleep(0.125)
        bulb.set_rgb(0,0 ,255, effect="sudden")
        time.sleep(0.125)
        times += 1
    await ctx.send("pls have seizure")

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

@client.command()
async def cf(ctx):
    side = random.randint(0,1)
    if side == 0:
        cside = "Heads!"
    elif side == 1:
        cside = "Tails!"
    await ctx.send("You flipped " + cside)

@client.command()
async def dice(ctx, limit=6):
    count = random.randint(1, limit)
    if limit < 6:
        await ctx.send("Minimum amount is 6!")
    else: 
        await ctx.send("You rolled " + str(count) + "!")

@client.command()
async def writefile(ctx, *, write):
    if write == "clear":
        db = open("list.txt", "w")
        db.write("")
        db.close()
        await ctx.send("File cleared.")
    else:
        db = open('list.txt', "a")
        db.write(f"\n{write}")
        await ctx.send(f'"{write}" written to file.')
        db.close()
        

@client.command()
async def readfile(ctx):
    db2 = open("list.txt", "r")
    db2text = db2.read()
    if db2text == "":
        await ctx.send("Cannot send empty message!")
    else:
        await ctx.send("\n" + db2text)
        db2.close()

@client.command()
async def cc(ctx, cname, state="normal"):
    if state == "normal":
        guild = ctx.message.guild
        await guild.create_text_channel(f'{cname}')
        await ctx.send(f"'{cname}' text channel created!")
    elif state == "s" or state == "silent":
        guild = ctx.message.guild
        await guild.create_text_channel(f'{cname}')

# @client.command()
# async def dc(ctx, dcname)

def am_i_owner(ctx):
    return ctx.author.id == 464733215903580160

@client.command(hidden=True)
@commands.check(am_i_owner)
async def owner(ctx):
    await ctx.send('yes')

@client.command(hidden=True)
@commands.check(am_i_owner)
async def status(ctx, status):
    if status == "online":
        await client.change_presence(status=discord.Status.online)
    if status == "idle":
        await client.change_presence(status=discord.Status.idle)
    if status == 'dnd': 
        await client.change_presence(status=discord.Status.dnd)
    if status == "invisible":
        await client.change_presence(status=discord.Status.invisible)
    
uptime = True
uptimed = 0
while uptime == True:
    time.sleep(60)
    uptimed += 1



@client.command()
async def uptime(ctx):
    await ctx.send(f'Bot has been up for', uptimed )




 







tokenfile = open("token.txt")
token = tokenfile.read()
client.run(token)