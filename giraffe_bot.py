import discord
from discord.ext import commands
from quotes import aaron, homework, mia, ian, matt
from random import randint
from dotenv import load_dotenv
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game('with your grades'))
	print('Bot is ready.')

@client.event
async def on_message(message):
	# Makes sure bot doesn't reply to itself
	if message.author.bot:
			return;
	# Custom Responses for Mia
	if str(message.author) == "kombuchan#7339":
		if randint(1,100) <= 15:
			channel = message.channel
			quote = mia()
			await channel.send(quote)
	# Custom Responses for Ian
	if str(message.author) == "purple_onion#8914":
		if randint(1,100) <= 15:
			channel = message.channel
			quote = ian()
			await channel.send(quote)
	# Custom Responses for Matthew	
	if str(message.author) == "tracerbullet#3290":
		if randint(1,100) <= 15:
			channel = message.channel
			quote = matt()
			await channel.send(quote)
	# 1/100th Chance or Giraffe Praise
	if str(message.author) != "Warlus#6272":
		if randint(1,100) == 1:
			channel = message.channel
			await channel.send("Giraffe's are literally the coolest animals ngl")						
	# Aaron/Kaloti Quotes (Calls Sarah's Bot)
	msg = message.content.lower()
	if ('aaron' in msg) or ('kaloti' in msg):
		if randint(1,100) <= 35:
			channel = message.channel
			quote = aaron()
			await channel.send(quote)
	# Homework/Assignment/Test/Quiz Quotes (Call's Matthew's Bot)
	if ('homework' in msg) or ('test' in msg) or ('assignment' in msg) or ('quiz' in msg):
		if randint(1,100) <= 25:
			channel = message.channel
			quote = homework()
			await channel.send(quote)

load_dotenv()
DISCORD_TOKEN_KEY = os.getenv("DISCORD_TOKEN_KEY")
client.run(DISCORD_TOKEN_KEY)