import discord
import asyncio
import random
import json
import os
import time

client = discord.Client()

@client.event
async def on_ready():
    print('Connnected! Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

@client.event
async def on_message(message):
    if message.content.startswith('!status'):
        await client.send_message(message.channel, 'I am here.')
    elif message.content.startswith('!flip'):
        flip = random.choice(['Head','Coin'])
        await client.send_message(message.channel, flip)
    elif message.content.startswith('!addquote'):
        if not os.path.isfile("quote_file.pk1"):
            quote_list = []
        else:
            with open("quote_file.pk1", "rb") as quote_file:
                quote_list = json.load(quote_file)
        quote_list.append(message.content[9:])
        with open("quote_file.pk1", "wb") as quote_file:
            json.dump(quote_list, quote_file)
    elif message.content.startswith('!quote'):
        with open("quote_file.pk1", "rb") as quote_file:
            quote_list = json.load(quote_file)  
        await client.send_message(message.channel, random.choice(quote_list))    

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))
        

@client.event
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!guess'):
        await client.send_message(message.channel, 'Guess a number between 1 and 10.')

        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'Sorry, the answer you were looking for was {}.'
            await client.send_message(message.channel, fmt.format(answer))
            return
        if int(guess.content) == answer:
            await client.send_message(message.channel, 'You got it, congratulations!')
        else:
            await client.send_message(message.channel, 'Sorry. It was actually {}.'.format(answer))
client.run('MzUxMzk4ODk2MTU4NzY5MTUz.DISByA.42FfN2pC9JIo0yJZb5F01gy3cbE')
client.close()