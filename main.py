# DON'T TOUCH THIS

from datetime import datetime

import keep_alive

from random import randint

from dotenv import load_dotenv
load_dotenv()

import os
TOKEN = os.getenv("TOKEN")

import discord


client = discord.Client()

# DON'T TOUCH THIS

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="everyone like life is a miracle"))
    
keep_alive.keep_alive()


@client.event
async def on_message(message):

    message.content.lower()
    if message.author == client.user:
        return

    userinput = message.content.lower()


    greetingtriggers = ['hi', 'hey', 'hello', 'heyya', 'hewwo']

    if userinput in greetingtriggers:
        replies = ['Hello there!', 'Hi!', 'Hey!', 'What\'s up?', 'Sup!']
        result = replies[randint(0, 4)]
        await message.channel.send(result)

    byetriggers = ['bye', 'cya', 'gtg']

    if userinput in byetriggers:
        replies = ['See you later!', 'Bye!', 'Cya!']
        result = replies[randint(0, 2)]
        await message.channel.send(result)
       
    thankyou = ['thanks', 'thank you', 'Thanks a lot', 'thank you so much', 'thanks', 'thanks a lot', 'thank you very much']
    
    if userinput in thankyou:
      replies = ['np', 'your welcome', 'welcome']
      result = replies[randint(0,2)]
      await message.channel.send(result)


    if userinput == 'lol':
      reply = ['HaHa','Laugh Out Loud', 'that was funny', 'What a joke']
      result = reply[randint(0,3)]
      await message.channel.send(result)

    
    

    # else: 
    #     await message.channel.send("I don't know how to respond to that! You could check the list of triggers I can respond to by doing `!replies`!")

# YOU CAN EDIT THIS

client.run(TOKEN)