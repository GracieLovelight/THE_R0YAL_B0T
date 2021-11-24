from discord import Intents
import discord
from discord.ext import commands, tasks
from discord.utils import get
from datetime import datetime
from pytz import timezone

class Deleter(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  async def on_message_delete(self, ctx, message):
        channel = self.bot.get_channel(802057981184704542)
        if not ctx.author.bot:
            async for entry in discord.audit_logs(limit=1, user=discord.AuditLogEntry.user, action=discord.AuditLogAction.message_delete):
                if entry.created_at.now():
                      embed = discord.Embed(title="Message Deleted...", description=f"The following message from {message.author} was deleted from {ctx.channel.mention} by {entry.user}")
                      embed.add_field(name="The Complete Message: ", value=ctx.content, inline=False)
        
        await channel.send(embed=embed)

def setup(bot):
  bot.add_cog(Deleter(bot))