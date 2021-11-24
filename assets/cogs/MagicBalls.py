import discord
from discord.ext import commands
import random

class MagicBalls(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=["8ball", "magic8ball", "m8b", "MEB"])
  async def _8ball(self, ctx, *, question):
    responses = ["It is certain.",
                        "It is decidedly so.",
                        "Without a doubt!",
                        "Yes!",
                        "Definitely!",
                        "Absolutely!",
                        "Outlook good.",
                        "I'd say, yes!",
                        "Signs point to yes.",
                        "The Divine says Yes!",
                        "Idk? Ask God.",
                        "Reply Hazy, try again!",
                        "Ask again later.",
                        "The Cogs stole the answer. Try again!",
                        "Error 404: Content not found! Try again later!",
                        "Better not tell you now.",
                        "Cannot predict now.",
                        "Concentrate and ask again.",
                        "Try again",
                        "Meh. Idk!",
                        "Don't count on it!",
                        "My reply is no.",
                        "My sources say no.",
                        "Outlook not so good.",
                        "Doubtfully.",
                        "Very doubtful!",
                        "Haha, loser!"]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

  @_8ball.error
  async def _8ball_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please ask a question.")
        print(f"Someone didn't ask a question")
        
    raise error

  @commands.command(aliases=["9ball", "magic9ball", "M9B", "MNB"])
  async def _9ball(self, ctx):
    responses = ["You will die!",
                        "You will die a horrible death!",
                        "You will die a goofy death",
                        "YOU WILL BURN! THE WORLD IS GOING TO BURN!!!",
                        "You will die a short and peaceful death.",
                        "Your going to be shreaded to death.",
                        "You will die inside of a Star",
                        "You will die by the hands of the gods / goddesses",
                        "You will die by the hands of the Angels",
                        "You will die by the hands of Demons",
                        "You will die by the hands of TarTarians",
                        "You will die by the hands of Mother Nature!",
                        "You will die by the hands of the Mother of the Seas!",
                        "You will die goofing off",
                        "You will die in a car accident",
                        "You will be run over by an ambulance and die",
                        "You will die a swift and painless death!"]
    await ctx.send(f"Answer: {random.choice(responses)}")

def setup(bot):
  bot.add_cog(MagicBalls(bot))