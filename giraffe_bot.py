import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game('with your grades'))
	print('Bot is ready.')

@client.event
async def on_message(message):
	if 'hi' in message.content:
		channel = message.channel
		await channel.send('Hello!')

client.run(TOKEN)