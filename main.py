import string
import discord
import colorama
from colorama import Fore, init, Back, Style
from discord.ext import (
    commands,
    tasks
)
import time


token = input("Digite o token da conta aqui: \n")
client = discord.Client()
client = commands.Bot(
    description='a',
    command_prefix='s.',
    self_bot=True
)


@client.command()
async def adv(ctx): 
    with open('adv.txt', 'r') as f: 
        for line in f:
            time.sleep(3.2)
            adv = line.rstrip("\n")
            await ctx.send("lc!adv " + adv + " não foi a reunião de mov")


@client.command()
async def tiraradv(ctx): 
    with open('tiraradv.txt', 'r') as f: 
        for line in f:
            time.sleep(3.2)
            adv = line.rstrip("\n")
            await ctx.send("lc!tiraradv " + adv)


client.run(token, bot=False)