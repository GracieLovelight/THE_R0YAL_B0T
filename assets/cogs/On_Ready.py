import discord
from discord.ext import commands
import random
import asyncio

class Ready(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_ready(self):
    print('THE R0YAL BOT is ready to server Her magesty!')
    
    statuses = [" '~' to use my commands!", " `~help` to get a list of my commands!", " around with Witchcraft!", " around with Superpowers", " around with magic", " with The Goddess", " a chill game", " an exciting game", " a happy game", " a VR game", " with THE PLAYERs", " Wizard101", " Wizard101 Test", " Pirate101", " Pirate101 Test", " The Gateway", " Toontown in VR", " with Tarot Cards", " Minecraft: Java Edition", " Minecraft: Bedrock Edition", " Minecraft: Console Edition", " Minecraft: Story Mode - Season 1", " Minecraft: Story Mode - Season 2", " Minecraft Dungeons", " LEGO Star Wars: The Video Game", " LEGO Star Wars II: The Original Trilogy", " LEGO Star Wars: The Complete Saga", " LEGO Star Wars III: The Clone Wars", " LEGO Star Wars: The Force Awakens", " LEGO Star Wars: The Skywalker Saga", " LEGO Batman: The Video Game", " LEGO Batman 2: DC Super Heroes", " LEGO Batman 3: Beyond Gotham", " LEGO DC: Super-Villains", " LEGO Harry Potter: Years 1-4", " LEGO Harry Potter: Years 5-7", " LEGO Harry Potter: Years 1-7", " LEGO Jurassic World", " LEGO Indiana Jones: The Original Adventures", " LEGO Indiana Jones 2: The Adventure Continues", " LEGO Indiana Jones: The Complete Adventure", " LEGO Marvel Super Heroes", " LEGO Marvel Super Heroes 2", " LEGO Marvel's Avengers", " LEGO Marvel's Avengers: The Infinity Saga", " The LEGO Movie Videogame", " The LEGO Movie 2: the Videogame", " The LEGO Ninjago Movie Videogame", " LEGO Pirates of the Caribbean: The Video Game", " LEGO The Hobbit", " LEGO The Lord of the Rings", " LEGO Middle Earth", " LEGO The Incredibles", " LEGO Worlds", " Doki Doki: Literature Club", " Genshin Impact", " Club Penguin", " Club Penguin Island", " Halo", " Halo: The Master Chief Collection", " Halo 5", " Halo Infinite", " LEGO Universe", " Star Wars Jedi: Fallen Order", " Star Wars: The Force Unleashed - Ultimate Sith Edition", " Star Wars: The Force Unleashed II", " Star Wars Jedi Knight: Dark Forces", " Star Wars Jedi Knight: Dark Forces II", " Star Wars Jedi Knight: Mysteries of the Sith", " Star Wars Jedi Knight II: Jedi Outcast", " Star Wars Jedi Knight: Jedi Academy", " Star Wars: The Old Republic", " Star Wars: The Knights of the Old Republic", " Star Wars: The Knights of the Old Republic II", " Sonic the Hedgehog", " Sonic the Hedgehog 2", " Sonic CD", " Sonic the Hedgehog 3 & Knuckles", " Sonic the Hedgehog 4 - Episode I", " Sonic the Hedgehog 4 - Episode II", " Sonic Mania", " Sonic Generations", " Among Us", " Amogsus", " Pirates of the Caribbean Online", " Discord", " Toontown: Corporate Clash", " Disney's Toontown Online", " Toontown Rewritten", " Toontown Storm", " Toontown Fantasy", " Toontown: Operation Dessert Storm", " Rocket's Toontown Online", " Sunrise Game's Toontown Online", " Toontown Japan", " Toontown Brazil", " Toontown Japan", " Toontown Germany", "Toontown Online: UK Edition", " Disney's Toontown Online for the New Nintendo 3DS", " Toontown's Funny Farm", " Toontown: Flash Games", " with the Code of Reality", " Chess", " 4D Chess", " 5D Chess + Time Travel", " Visual Studio Code", " Visual Studio", " Star Wars Jedi II", " with holograms", " with Miss Minutes", " with Lokigator", " with the timeline", " Microsoft Edge", " (Classic) Microsoft Edge", " Firefox", " Opera", " Google Chrome", " Internet Explorer"]
    
    while not self.bot.is_closed():
        status = random.choice(statuses)
        
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(status))
        
        await asyncio.sleep(900)

  #game = discord.Game("around with Witchcraft!")
  #await bot.change_presence(status=discord.Status.dnd, activity=game)

def setup(bot):
  bot.add_cog(Ready(bot))