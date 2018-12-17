import discord
import asyncio
from discord.ext import commands
import os
import requests

token = "NTI0MDIzODg1NjE2Nzc1MTcz.DviH7w.BNkFQMsAscCm8pB1nPyGBkPFxeE"
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("- Bot Enabled -")
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    game = discord.Game("!help | Official Dragon City Community Bot")
    await bot.change_presence(activity=game)

@bot.command()
async def online(ctx):
    await ctx.send("I am **online**.")

bot.remove_command("help")
@bot.command()
async def help(ctx):
    await ctx.send("**Hey, this is the list of commands:**\n!online | Check if the discord bot is online\n!help | Shows list of commands\n!info | Shows info about this discord\n!botinfo | Shows info about the bot")

@bot.command()
async def info(ctx):
    await ctx.send("**Hey!** This discord was made by **Jamiy#9590** to hopefully create a helpful place for Dragon City players!")

@bot.command()
async def botinfo(ctx):
    await ctx.send("Bot Developed by: **Jamiy#9590**")
    print("aa")


bot.run(token)