from discord.ext import commands

class Quotes(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(aliases=["favoriteQuotes"])
  async def quotes(self, ctx):
      responses = ["IT'LL BE A COLD DAY IN HELL BEFORE I GIVE UP EATING BANANA SKELETONS! -- Bogleech",
                 "Run. Run because of what's out there. -- Nike",
                 "There are approximately 1,010,300 words in the English language, but I could never string enough words together to properly express how much I want to hit you with a chair. -- Alexander Hamilton, to Thomas Jefferson",	
                "It's spoopy time! -- Oz Media"]
      await ctx.send(f"Answer: {random.choice(responses)}")

def setup(bot):
  bot.add_cog(Quotes(bot))