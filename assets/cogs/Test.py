from discord.ext import commands

class Test(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=["tests"])
  async def test(self, ctx):
    await ctx.send("I passed the test!")

def setup(bot):
  bot.add_cog(Test(bot))