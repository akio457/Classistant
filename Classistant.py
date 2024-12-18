import discord
from discord.ext import commands
import json  # For handling user data
import sqlite3  # Uncomment if using SQLite instead of JSON

# Intents setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

# Load user data from JSON
with open("data.json", "r") as file:
    user_data = json.load(file)

# Bot commands
@bot.command()
async def reputation(ctx, user: str):
    """Check a user's reputation."""
    if user in user_data:
        reputation = user_data[user].get("reputation", "Data not found")
        await ctx.send(f"Your current reputation is {reputation}")
    else:
        await ctx.send("Sorry, user not found or unavailable.")

@bot.command()
async def warnings(ctx, user: str):
    """Check a user's warnings."""
    if user == ctx.author.name:  # Ensure the user can only check their own warnings
        warnings = user_data[user].get("warnings", "No warnings found.")
        await ctx.send(f"You have received {warnings}")
    else:
        await ctx.send("Sorry, you cannot access this information.")

@bot.command()
async def sanctions(ctx, user: str):
    """Check a user's sanctions."""
    if user == ctx.author.name:
        sanctions = user_data[user].get("sanctions", "No sanctions found.")
        await ctx.send(f"Your sanctions: {', '.join(sanctions)}")
    else:
        await ctx.send("Sorry, but data regarding this user’s sanctions is unavailable.")

@bot.command()
async def awards(ctx, user: str):
    """Check a user's awards."""
    if user == ctx.author.name:
        awards = user_data[user].get("awards", {})
        award_list = "\n".join([f"{k}: {v}" for k, v in awards.items()])
        total_awards = len(awards)
        await ctx.send(f"Your awards:\n{award_list}\nTotal Awards = {total_awards}\nGood job!! :clap:")
    else:
        await ctx.send("Sorry, you cannot access this information.")

@bot.command()
async def grades(ctx, user: str):
    """Check a user's grades."""
    if user == ctx.author.name:
        grades = user_data[user].get("grades", {})
        grade_list = "\n".join([f"For {k}, you had {v}" for k, v in grades.items()])
        await ctx.send(f"Your grades:\n{grade_list}\nKeep improving, but always remember that you don’t have to force yourself.")
    else:
        await ctx.send("Sorry, you cannot access this information.")

@bot.command()
async def memories(ctx):
    """Display photos of class memories."""
    # This is a placeholder; replace with actual file handling logic
    await ctx.send("*displays photos of your class memories*")

@bot.command()
async def dymotivation(ctx):
    """Provide a motivational quote."""
    await ctx.send("Always believe that you can do it.")

# Run the bot
bot.run("MTMxODkyMDU0NDgxMjI3MzcyNg.GityvC.tk2W8YcSNjtT6OiQJ1UkX9gM4AuEEAPseQJ-vY")