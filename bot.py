import discord
from discord.ext import commands

TOKEN = config.TOKEN

client = commands.Bot(commands_prefix = "prefix-here")


@client.even
async def on_ready():
	print("Bot Is Ready")



@client.command()
@commnds.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member , *, reason = f"Kicked by {ctx.author.name}"):
	await ctx.send(f"{member.mention} has been kicked from {ctx.guild.name}. ")
	
	#remove the "#" below if you also want to dm the user who is kicked
	#await member.send(f"You Have Been Kicked from {ctx.guild.name} . Reason = {reason}")
	
	#if no reason is provided then the reason will be kicked by <name of the person who kicked>
	await member.kick(reason = reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason = f"Banned By {ctx.auhtor.name}"):
	await ctx.send(f"{member.Mention} has been banned from {ctx.guild.name}")

	#remove the "#" below if you also want to dm the user that he is banned from the server
	#await member.send(f"You Have Been Banned from {ctx.guild.name}. Reason: {reason}")

	#if no reason is provided then the reason will be banned by <the person who bans>
	await member.ban(reason = reason)

@client.command
@commands.has_permissions(manage_messages = True)
async def mute(ctx, member: discord.Member):
	#copy the id of muted role, make sure to place it above the members role and select the perms to send_meessges = false
	muted_role = ctx.guild.get_role(id of the role)
	await member.add_roles(muted_role)

@client.command
@commands.has_permissions(manage_messages = True)
async def unmute(ctx, member = discord.Member):
	#copy the id of muted role, make sure to place it above the members role and select the perms to send_meessges = false
	muted_role = ctx.guild.get_role(id of the role)
	await member.remove_roles(muted_role)

#to get the token, refer to the README File
client.run(TOKEN)

