from discord.ext import commands

class Poetry(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def poetry(ctx):
    await ctx.send("Patience is a virtue, my friend. This command is coming soon!")

def setup(bot):
  bot.add_cog(Poetry(bot))