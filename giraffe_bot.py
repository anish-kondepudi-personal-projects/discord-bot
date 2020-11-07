import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game('with your grades'))
	print('Bot is ready.')

@client.command(aliases=['hi','bye','shy','my'])
async def ping(ctx):
	await ctx.send("hi!")




client.run(TOKEN)