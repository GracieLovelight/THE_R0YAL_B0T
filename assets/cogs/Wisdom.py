from discord.ext import commands

class Wisdom(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(aliases=["wordsofwisdom"])
  async def wisdom(self, ctx):
    await ctx.send("This command is coming soon!")

def setup(bot):
  bot.add_cog(Wisdom(bot))