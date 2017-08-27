import discord
import asyncio
import random
import pickle
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Connected! Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

@client.event
async def on_message(message):
    if message.content.startswith('!botconnected'):
        await client.send_message(message.channel, 'Yes, i am connected.')
    elif message.content.startswith('!flip'):
        flip = random.choice(['Cap','Pajura'])
        await client.send_message(message.channel, flip)
    elif message.content.startswith('!addquote'):
        if not os.path.isfile("quote_file.pk1"):
            quote_list = []
        else:
            with open("quote_file.pk1", "rb") as quote_file:
                quote_list = pickle.load(quote_file)
        quote_list.append(message.content[9:])
        with open("quote_file.pk1", "wb") as quote_file:
            pickle.dump(quote_list, quote_file)
    elif message.content.startswith('!quote'):
        with open("quote_file.pk1", "rb") as quote_file:
            quote_list = pickle.load(quote_file)  
        await client.send_message(message.channel, random.choice(quote_list))    

client.run('MzUxMzk4ODk2MTU4NzY5MTUz.DISByA.42FfN2pC9JIo0yJZb5F01gy3cbE')
