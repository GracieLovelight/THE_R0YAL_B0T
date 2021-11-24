from discord.ext import commands

class Cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=["cogs"])
  async def cog(self, ctx):
    await ctx.send("This command was made using Cogs in Discord.py!")

def setup(bot):
  bot.add_cog(Cog(bot))