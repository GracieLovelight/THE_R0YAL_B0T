import discord
from discord.ext import commands

class Lore(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(aliases=["whoAmI"])
  async def WhoIAm(self, ctx):
  	await ctx.send("Who am I? Why I am but a Royal servent for the Royal Family of Glacean, including Destiny!")
    
  @commands.command()
  async def WhyAmIHere(self, ctx):
  	await ctx.send("Why am I here? I am here because I escaped from my doom and I've taken the form of THE R0YAL BOT as a new life!")

def setup(bot):
  bot.add_cog(Lore(bot))