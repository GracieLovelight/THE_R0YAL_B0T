from discord.ext import commands

class Oracle(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=["oraclecards", "oraclecard", "angelcard", "angelcards"])
  async def oracle(self, ctx):
    await ctx.send("This command is coming soon!")

def setup(bot):
  bot.add_cog(Oracle(bot))