from discord.ext import commands

class Poster(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def poster(self, ctx):
    await ctx.send("This command is under construction!\n\nWhen finished, this command should make a poster from the text given using various images as letters. The poster is the original Lily and the Amulet of the Goddess poster but I plan to add more than one type of poster to the mix as time goes on.")

def setup(bot):
  bot.add_cog(Poster(bot))