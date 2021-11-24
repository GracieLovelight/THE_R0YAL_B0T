from discord import Intents
import discord
from discord.ext import commands, tasks
from discord.utils import get
import random
import json
import os
import re
from dadjokes import Dadjoke
import aiohttp
import datetime
import time
import asyncio
from better_profanity import profanity

bot = commands.Bot(command_prefix="~", case_insensitive = True, description = "I.R.I.S., THE R0YAL BOT is THE PLAYER ZER0's Discord bot written in Python 3.9 which is specifically made for the PLAYER ZER0 STUDIOS' Discord Server!", help_command=None)

@bot.command()
async def ignorethiscommand(ctx, msgID: int):
    if message.content.startswith == "~~":
        ctx.send("Haha! You can't fool me! For, I am I.R.I.S, Intelligent Robot (for the) Internet's Service!")
        


# Logging Messages Function

messages = joined = removed = 0

async def update_stats():
    channel = bot.get_channel(802057981184704542)
    await bot.wait_until_ready()
    global messages, joined, removed
    
    while not bot.is_closed():
        try:
            with open("assets/stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}, Members Left: {removed}\n")
                
            messages = 0
            joined = 0
            removed = 0
            
            await asyncio.sleep(3600)
        except Exception as e:
            print(e)


            
# @bot.event
#     while True:
#         print("Cleared the spam text file!")
#         await asyncio.sleep(150)
#         with open("assets/lists/spam_detection.txt", "r+") as file:
#             file.truncate(0)

# Message Managing
        
def isMessageFilthy(message):
    isBadWord = profanity.contains_profanity(message.content)

    if isBadWord:
        print(f'I blocked a message sent by {message.author} which contained swear word(s) within the following message: "{message.content}"!')
        return True

    return False

#class MessagesRemoved():
    #async def MessagesMod(message):
        #if message.author == self.user:
            #return

        #msgattach = message.attachments
        #if len(msgattach) > 0:
            #for attachment in msgattach:
                #try:
                    #if attachment.filename.endswith(".dll"):
                        #await message.delete()
                        #await message.send("No DLL's allowed. Not even the Python Injector! Sorry.")
                    #elif attachment.filename.endswith(".exe"):
                        #await message.delete()
                        #await message.send("For the safety of all of the members of this discord, no sending Executable files (.exe) in my discords.")
                    #elif attachment.filename.endswith(".dmg"):
                        #await message.delete()
                        #await message.channel.send("For the safety of all members of this Discord, the transferring of Mac Executable files (.dmg) is not allowed in my any of my discords.")
                    #elif attachment.filename.endswith(".sh"):
                        #await message.delete()
                        #await message.channel.send("For the safety of all members of this Discord, the transferring of script files (.sh, .ps1, .bat, and more) is not allowed in my any of my discords.")
                    #elif attachment.filename.endswith(".ps1"):
                        #await message.delete()
                        #await message.channel.send("For the safety of all members of this Discord, the transferring of script files (.sh, .ps1, .bat, and more) is not allowed in my any of my discords.")
                    #elif attachment.filename.endswith(".bat"):
                        #await message.delete()
                        #await message.channel.send("For the safety of all members of this Discord, the transferring of script files (.sh, .ps1, .bat, and more) are not allowed in my any of my discords.")
                    #elif attachment.filename.split(".")[-1]:
                        #await message.delete()
                        #await message.channel.send("For the safety of all members of this Discord, the transferring of compressed folders (.zip, .7zip, .tar, etc.) are not allowed in my any of my discords.")
                        #break
                    #elif attachment.filename.endswith(".7zip"):
                        #await message.delete()
                        #await message.channel.send("For the safety of all members of this Discord, the transferring of compressed folders (.zip, .7zip, .tar, etc.) are not allowed in my any of my discords.")
                    #elif attachment.filename.endswith(".7z"):
                        #await message.delete()
                        #await message.channel.send("For the safety of all members of this Discord, the transferring of compressed folders (.zip, .7zip, .tar, etc.) are not allowed in my any of my discords.")
                    #elif attachment.filename.endswith(".tar"):
                        #await message.delete()
                        #await message.channel.send("For the safety of all members of this Discord, the transferring of compressed folders (.zip, .7zip, .tar, etc.) are not allowed in my any of my discords.")
                    #elif attachment.filename.endswith(".gz"):
                        #await message.delete()
                        #await message.channel.send("For the safety of all members of this Discord, the transferring of compressed folders (.zip, .7zip, .tar, etc.) are not allowed in my any of my discords.")
                    #elif attachment.filename.endswith(".tor"):
                        #await message.delete()
                        #await message.channel.send("For the safety of all members of this Discord, the transferring of .tor files are not allowed in my any of my discords.")
                    #except Exception as e:
                        #print(e)
                #else:
                    #return
            #return


messages = 0

async def message_deletion():
    channel = bot.get_channel(802057981184704542)
    await bot.wait_until_ready()
    global messages
    
    while not bot.is_closed():
        try:
            with open("assets/message_data.txt", "a") as f:
                
                  f.write(f'Time: {int(time.time())}, Messages: I identified a message sent by {message.author} that was deleted that contained the following message: "{message.content}"!\n')
                  f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}, Members Left: {removed}\n")
                
            messages = 0
            
            await asyncio.sleep(3600)
        except Exception as e:
            print(e)
    
    
@bot.event
async def on_message(message):
    global messages
    messages += 1
#    counter = 0
#    with open("assets/lists/spam_detection.txt", "r+") as file:
#        for lines in file:
#        	if lines.strip("\n") == str(message.author.id):
#                 counter+=1

#       	file.writelines(f"{str(message.author.id)}\n")
#        if counter > 15:
#        	role = get(message.author.guild.roles, name="Timeout")
#        	await message.author.add_roles(role)
#        	print(f"Put {message.author} in timeout for spamming!")
#        	await message.channel.purge(limit=10, check=lambda message: message.author == message.author.id)
    

    
    if message.author.bot == False:
        with open("assets/json/users.json", "r") as f:
            users = json.load(f)
            
        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)
        
        with open("assets/json/users.json", "w") as f:
            json.dump(users, f, indent=4)
            
        if isMessageFilthy(message):
            await message.delete()
            
    await bot.process_commands(message)
    # return

@bot.event
async def on_ready():
    profanity.load_censor_words_from_file('assets/lists/blacklist.txt')
    print("Sucessfully loaded the blacklist!")

#@bot.event
#async def on_message_delete(message):
    #channel = bot.get_channel(802057981184704542)
    
    #async for entry in message.guild.audit_logs(limit=1,action=discord.AuditLogAction.message_delete):
        #deleter.name = message.author
        
        #embed = discord.Embed(title=f"{deleter.name} deleted message by {message.author} that contained the following:", description=f"{message.content}", color=0x9370DB)

        #await channel.send(embed=embed)
        
        
        
        
        
        
        
        

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.NotOwner):
        await ctx.send("Only administrator's have permission to use this command!")
    #elif
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the permissions to use this command!")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Haha! You cannot fool me! That command does not exist!")
    else:
          await ctx.send("Sorry but you have tried a command that doesn't work, doesn't exist, or that you don't have permission to use! Check the help command list for a list of commands or ask THE PLAYER ZER0 (Grace) for help if you have any further questions!")
        
    raise error

@bot.event
async def on_member_join(member):
    global joined
    joined += 1
    with open('assets/json/users.json', 'r') as f:
        users = json.load(f)
    await update_data(users, member)
    
    with open("assets/json/users.json", 'w') as f:
        json.dump(users, f, indent=4)
    print(f"{member} has joined the server!")
    channel = bot.get_channel(775528645447516188)
    embed = discord.Embed(title = "A new member has joined!", description = f"{member} has join our Discord server!", color=0x9370DB)
    embed.set_footer(text="Please welcome them to the server!")
    
    await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    global removed
    joined += 1
    print(f"{member} has left the server.")
    channel = bot.get_channel(775528645447516188)
    embed = discord.Embed(title = "A member has left!", description = f"{member} has left our Discord!", color=0x9370DB)
    embed.set_footer(text="Say farewell to them as they embark on their new journey!")
    await channel.send(embed=embed)

# Cogs

for filename in os.listdir("./assets/cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"assets.cogs.{filename[:-3]}")

# Moderation commands

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("You need to specify an amount!")
  if isinstance(error, commands.BadArgument):
    await ctx.send("Please specify an integer to clear instead of any other value!")
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You do not have permission to use this command.")
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.send("You do not have permission to use this command.")

  raise error

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f"Kicked {member.mention}")
  
@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Sorry but you missing something in your attempt to kick someone. Please check over your message and try again!")
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You do not have permission to use this command.")
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.send("You do not have permission to use this command.")
          
  raise error

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  
@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Sorry but you missing something in your attempt to ban a user. Please check over your message and try again!")
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You do not have permission to use this command.")
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.send("You do not have permission to use this command.")

  raise error

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split("#")

  for ban_entry in banned_users:
    user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f"Unbanned {user.mention}")
      return

@bot.command(aliases=["whois", "user", "info"])
@commands.is_owner()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not  member else member
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(color=0x9370DB, timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)
    embed.add_field(name="Bot?", value=member.bot)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p CDT"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p CDT"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles[1:]]))
    roles.append('@everyone')  # set string @everyone instead of role
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    await ctx.send(embed=embed)
    
@bot.command()
@commands.is_owner()
async def reload(ctx, cog):
    try:
        bot.unload_extension(f"cogs.{cog}")
        bot.load_extension(f"cogs.{cog}")
        await ctx.send(f"{cog} got reloaded")
    except Exception as e:
        print(f"{cog} can not be reloaded:")
        raise e

@userinfo.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')

# Custom commands
    
async def update_data(users, user):
    if not f"{user.id}" in users:
        users[f"{user.id}"] = {}
        users[f"{user.id}"]["experience"] = 0
        users[f"{user.id}"]["level"] = 1
        
async def add_experience(users, user, exp):
    users[f"{user.id}"]["experience"] += exp
    
async def level_up(users, user, message):
    with open("assets/json/levels.json", "r") as g:
        levels = json.load(g)
    experience = users[f"{user.id}"]["experience"]
    lvl_start = users[f"{user.id}"]["level"]
    lvl_end = int(experience ** (1/4))
    if lvl_start < lvl_end:
        await message.channel.send(f"{user.mention} has leveled up to level {lvl_end}")
        users[f"{user.id}"]["level"] = lvl_end
        
@bot.command(aliases=["level"])
async def rank(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open("assets/json/users.json", "r") as f:
            users = json.load(f)
        lvl = users[str(id)]["level"]
        await ctx.send(f"You are at level {lvl}!")
    else:
        id = member.id
        with open("assets/json/users.json", "r") as f:
            users = json.load(f)
        lvl = users[str(id)]["level"]
        await ctx.send(f"{member} is at level {lvl}!")
    
@bot.command(aliases=["she/her"])
async def sheher(ctx):
    member = ctx.message.author
    role = get(member.guild.roles, name="She/Her")
    if role in member.roles: #checks all roles the member has
        await member.remove_roles(role) #removes the role
        await ctx.send("You will no longer be refer to as a she/her")
    else:
        await member.add_roles(role) #adds the role
        await ctx.send("You will now be referred to by your name, she, and/or her!")
    return

@bot.command(aliases=["she/him"])
async def shehim(ctx):
    member = ctx.message.author
    role = get(member.guild.roles, name="She/Him")
    if role in member.roles: #checks all roles the member has
        await member.remove_roles(role) #removes the role
        await ctx.send("You will no longer be refer to as a she/him")
    else:
        await member.add_roles(role) #adds the role
        await ctx.send("You will now be referred to by your name, she, and/or him!")
    return

@bot.command(aliases=["he/him"])
async def hehim(ctx):
    member = ctx.message.author
    role = get(member.guild.roles, name="He/Him")
    if role in member.roles: #checks all roles the member has
        await member.remove_roles(role) #removes the role
        await ctx.send("You will no longer be refer to as a he/him")
    else:
        await member.add_roles(role) #adds the role
        await ctx.send("You will now be referred to by your name, he, and/or him!")
    return

@bot.command(aliases=["he/them"])
async def hethem(ctx):
    member = ctx.message.author
    role = get(member.guild.roles, name="He/Them")
    if role in member.roles: #checks all roles the member has
        await member.remove_roles(role) #removes the role
        await ctx.send("You will no longer be refer to as a he/them")
    else:
        await member.add_roles(role) #adds the role
        await ctx.send("You will now be referred to by your name, he, and/or them!")
    return

@bot.command(aliases=["she/them"])
async def shethem(ctx):
    member = ctx.message.author
    role = get(member.guild.roles, name="She/Them")
    if role in member.roles: #checks all roles the member has
        await member.remove_roles(role) #removes the role
        await ctx.send("You will no longer be refer to as a she/them")
    else:
        await member.add_roles(role) #adds the role
        await ctx.send("You will now be referred to by your name, she, and/or them!")
    return

@bot.command(aliases=["they/them"])
async def theythem(ctx):
    member = ctx.message.author
    role = get(member.guild.roles, name="They/Them")
    if role in member.roles: #checks all roles the member has
        await member.remove_roles(role) #removes the role
        await ctx.send("You will no longer be refer to as a they/them")
    else:
        await member.add_roles(role) #adds the role
        await ctx.send("You will now be referred to by your name, they, and/or them!")
    return

@bot.command(aliases=["any/any", "anyany"])
async def any(ctx):
    member = ctx.message.author
    role = get(member.guild.roles, name="Any/Any")
    if role in member.roles: #checks all roles the member has
        await member.remove_roles(role) #removes the role
        await ctx.send("You will now be referred to by any pronoun.")
    else:
        await member.add_roles(role) #adds the role
        await ctx.send("You will now be referred to by your name and any pronoun that people wish!")
    return

@bot.command(aliases=["verified"])
async def verify(ctx):
    member = ctx.message.author
    role = get(member.guild.roles, name="Verified")
    await member.add_roles(role)
    await ctx.send("You can now talk in the rest of the discord server! Have fun and read the rules!")

@bot.command()
async def ping(ctx):
  await ctx.send(f"Pong! || {round(bot.latency * 1000)}ms")

@bot.command(aliases=["py"])
async def python(ctx):
  await ctx.send("I am running on python version 3.9.5!")

@bot.command(aliases=["hoster"])
async def host(ctx):
    await ctx.send("I am being hosted on PloxHost!\n\nHere's the link to the hoster: https://www.plox.host/discordbot-hosting/")

@bot.command(aliases=["mf", "kaijufight", "kf"])
async def monsterfight(ctx): # kaijufight
  await ctx.send("I think that Godzilla would win regardless of who he went up against! After all, he *__is__* the King of the Monsters! Unless it's up against Destiny!")
    
@bot.command(aliases=["secret"])
async def secrets(ctx):
    await ctx.send("There are x number of secrets hidden throughout the websites belonging to THE PLAYER ZER0!")

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def snap(ctx):
  await ctx.send("Mr. Stark? I don't feel so good!")

@bot.command()
async def online(ctx):
  await ctx.send("I am online at the moment. If I am not online, you'll notice that my commands aren't working and that I'd be offline!")

@bot.command(aliases=["favoritesongs", "favoritesong", "favsong", "fs", "ultimateplaylist", "newestultimateplaylist", "newestultimatemusicplaylist"])
async def favsongs(ctx):
  await ctx.send("I have so many favorite songs that I've compiled a playlist of these songs into one playlist titled The Newest Ultimate Music Playlist which can be found after the colon: https://www.youtube.com/playlist?list=PLqWmHBgL2jJE3I7NoA2S0_nfJQMD1AOII")

@bot.command()
async def creation(ctx):
  await ctx.send("I was created on Sunday, March 28th, 2021 but I was conceptualized on Tuesday, January 19th, 2021!")

@bot.command(aliases=["rd", "release", "date"])
async def releasedate(ctx):
  await ctx.send("There is no concrete release date for any of The Book of Life's content! Grace will announce one once he is certain he can make it!")

@bot.command(aliases=["minecraft", "thejourneyhome", "minecraftthejourneyhome", "mc", "tjh", "mctjh"])
async def mcjh(ctx):
  await ctx.send("Zachary Davidson is a young Mage who was confronted by a mysterious masked personage. After narrowly escaping from Him through a portal, he finds himself stuck in the weird world of Modded Minecraft.\n\nHowever, he swiftly finds out that he is not alone when someone by the initials T.G.D. reaches out to him, promising him a way to escape as long as he goes on a journey for Her.\n\nWhat will happen next? Watch Minecraft: the Journey Home - The Reawakening of the Wither to find out!\n\nPlaylist Link: https://www.youtube.com/playlist?list=PLUtk_e7MC3_IGX4q0CALt7U5RhC_Jp92X")
  
@bot.group(aliases=["pv", "previous", "previousversion", "ver", "versions", "v"])
async def version(ctx):
    contents = ["Version 2.22.0 - The Update of Less Annoyance: This update fixes the issue when you're trying to strike out text at the beginning of your message and I.R.I.S. tells you that she does not recognize the command.", "Version 2.21.1 - The Versions Update: Removed 2 words from the blacklist that didn't need to be there and didn't allow me to say Twinkle.", "Version 2.21.0 - The Versions Update: I have compiled all versions of the bot into one place where you can scroll through the listing by version to see how far the bot has come!", "Version 2.20.0 - The Pronoun Update, Part 2: I added every pronoun and pronoun varietion that you might want. If I missed some then be sure to PM THE PLAYER ZER0 or put your desired pronoun in the suggestions channel. I will not take any joke suggestions like nor/mal and what not. I got rid of the spam filter because it wasn't working properly. I also added a way you can remove your pronoun roles! I removed the advise command but I moved the poetry command to a Cog!", "Version 2.19.2 - The Filter Update: Allowed the people to use the term 'dumbass' 'dummy', and 'stupid' while I also added back the naughty terms with the f-bomb and everything else and you can still say 'fuck'!", "Version 2.19.1 - The Filter Update: You're now allowed to say 'fuck', 'shit', 'damn', and 'hell'!", "Version 2.19.0 - The Filter Update: Added a filter using better_profanity.", "Version 2.18.0 - The Status Update: Updated the list of statuses to include over 110 random statuses to pick from every 15 minutes with more to be added every once in a while!", "Version 2.17.3: Changed the link to PLAYER ZER0 STUDIOS & I renamed Arbitrium TV to Mercy Grace Lovelight since it'll be my personal channel outside of the story.", "Version 2.17.2: Made it so Pip upgrades automatically after a restart.", "Version 2.17.1: Pushed a potential patch for those without permissions using `~clear` and it not saying that you don't have permissions.", "Version 2.17.0: This version upgrades the python version as well as the python command from 3.7 to 3.9.5", "Version 2.16.3 - The Levelling Update: Emergency patch implemented to make the bot stop repeating itself! Oh, and I renamed the alias for `~monsterfight` from `~ms` to `~mf` to properly match the command.", "Version 2.16.2 - The Levelling Update: Reimplemented the line of code which adds users to the `users.json` file when they chat.", "Version 2.16.1: Fixed a mispelled piece of code, fixed another error with the censor, and got rid of a lot of hidden code that isn't being used. I also added back the rank command.", "Version 2.16.0: Added a leveling system.", "Version 2.15.3: Added more swear word varients than I'd like to admit that I did and I renamed the blacklist json file to fit it's purpose.", "Version 2.15.2: Added aliases to the add/remove bad words commands, added the `~reload` command to the help command list and gave it a custom help command. I added more errors to a few of the commands. Another thing I did was organized the files in the assets folder. The last thing I did was changed the name from Zachary to Grace", "Version 2.15.1: This version automatically removes any words that have ties with sexual, racial, and any other stuff!", "Version 2.15.0: You can no longer say the n-word, r-word, j-word, or the bad f-word (not the f-bomb) as @The Royal Bot will now remove any message containing the word, even the censored versions of it.", "Version 2.14.7: This version moves the tarot and oracle card commands plus the magic ball commands and the wisdom commands to their own Cogs. I also capitalized the first letter of all of the Cogs to stay consistent with the rest of the Cogs!", "Version 2.14.6 - The Pronoun Update, Part 1: This version adds a bot-checker to the ''~whois' command and it gives people the choice on whether or not they want to be referred to as 'he/him', 'she/her', or 'them/they'! Also, I finally got around to fixing the Magic Nine Ball Command! Now you can predict your own death!", "Version 2.14.5: This version adds more statuses, and fixed the welcome/goodbye status. As well as I cut the time for the the shift in statuses down to 15 minutes.", "Version 2.14.4: This version adds back the do-not-disturb status.", "Version 2.14.3: This version adds the verify command which gives you the verified role!", "Version 2.14.2: This version adds even more commands related to my YouTube channel, some more moderation features, the ability to reload Cogs, and made use of statuses that shift every 30 minutes.!", "Version 2.14.1: This version adds more commands related to my YouTube channel.", "Version 2.13.1: This version provides a fix to a grammatical error that I just discovered.", "Version 2.13.1: This version provides an explanation to the relationship between Pancha + Ollie and THE PLAYER ZER0 is. It also adds two more goals after I complete my second goal.", "Version 2.13.0: This verssion adds the `~cat` and `~dog` commands while fixing the number of pages in the help message and fixing a text error on the first page.", "The Royal Bot is on version 2.12.0! This version updates the WhoIs command to be more detailed and it removes some old, unnecessary code",   "The Royal Bot is on version 2.11.0! This bot finishes the Tarot card functionality from reversals to right ups; complete with definitions of what the tarot card means!", "The Royal Bot is on version 2.10.0! This version begins to finish the tarot card command and adds more features to be completed in further parts of the Mystic Update!",  "The Royal Bot is on v2.9.1! This version separates the main help command into separate pages for each tier of commands. Moderation, Technical, Fun, YouTube, and Other!", "The Royal Bot is on v2.9.0 which updates the `~help` command as well as updates the subscriber goal and count.", "The Royal Bot is on v2.8.3. Added a WhoIs command for modation use only and I added color coding to each tier of commands within the help commands.", "The Royal Bot is on v2.8.2 which fixes a typo that was overlooked by myself.", "The Royal Bot is on v2.8.1 which corrects an indentation error.", "The Royal Bot is on v2.8.0 which, after trial and error, gives people the ability to choose their own command. Also, I added greetings to the discord whenever someone joins or leaves!", "The Royal Bot is on v2.7.0! This version adds the `~invite` command and implements a Cat Fact API that gives you a random cat fact when instructed to. Zachary also reimplemented the `~tarot` command but it doesn't have the same functionality like it did before.", "The Royal Bot is on v2.6.1 which makes some grammatical changes to the help commands. I also added more features to the list of features in `~features`. Also, the tarot command disappeared for some reason but I'll get around to adding it later on.", "The Royal Bot is on v2.6.0 which fixed the clear command, added modation tools, and custom statuses now work for the bot!", "The Royal Bot is on v2.5.1. Changed my favorite song and it changes the subscriber count & goals.", "The Royal Bot is on v2.5.0 which gives the users the ability to use dad jokes and I began working on a new command called `~tarot`. Also, the clear command stopped working for some reason.", "The Royal Bot is on v2.4.0! This version adds moderation tools for the moderators!", "The Royal Bot is on v2.3.1 which simplifies 2 lines of code to one and I updated the subscriber goal for THE PLAYER ZER0 because I passed it.", "The Royal Bot is on v2.3.0 which adds the Magic 8 & Magic 9 ball commands as well as the `~python` command to both the list of commands for regular use and for use in the help function.", "The Royal Bot is on v2.2.0. This version adds Cogs to the bot to help me out in the future. I added the `~cog`/`~cogs` and a `~test` command. I added the Cog commands to the help location and I moved the on_ready function to a Cog to clear up clutter in the main file.", "The Royal Bot is on v2.1.1 which re-implements a commented out command and it adds a clear messages command but I commented it out until I can figure out command permission.", "The Royal Bot is on v2.1.0. This version adds the help command plus, if you say `~help test` or replace test with any other command, it will give you information on that command. I also give more aliases to commands!", "The Royal Bot is on v2.0.0 which brings the bot to the latest version of Discord.py which is the rewrite brand. This update also adds the `~links` command, various versions to use the `~releasedate` command, removed Discord's default help command AND I removed the conversational ability for the bot.", "The Royal Bot is on v1.1.0. This gives the bot more of an argumentative personality, fixed a bug with the greetings, added a goal command, `~ping` command, and more!", "The Royal Bot is on v1.0.1 which adds partial conversational abilities, added more references and fun commands, and I added the `~version` command.", "The Royal Bot is on v1.0.0! This version creates the basic bot, a new and custom help command, the bot should be up nearly 24/7, began looking into tutorials for various items, Gave the bot simple commands, and more!"]
    pages = 52
    cur_page = 1
    
    message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            break # would end the loop if user doesn't react after x seconds but the timer is gone...

@bot.command(aliases=["cancelledseries", "cancel"])
async def cancelled(ctx):
    embed = discord.Embed(title="THE PLAYER ZER0's Cancelled Series", description="This is a list of ALL of Grace's cancelled game series.")
    
    embed.add_field(name="Toontown Frenchy", value="I might've mentioned this earlier but I cancelled the TTFr series after Bananabeth and some other team members working on Toontown: Market Crash causing the other two to lose interest in the series while I kept it going on for several more episodes before stopping the creation of more episodes because the charm had worn off.", inline=False)
    embed.add_field(name="Let's Play Toontown Rewritten with xEathan06x", value="I'm marking it as cancelled because Ethan and I (from what I understand) don't really want to make this series.", inline=False)
    embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AAUvwngLzBB2zSK78OHAWHCJ-f7yUgr368Jj7kjCxIoyiw=s176-c-k-c0x00ffffff-no-rj")

    await ctx.send(embed=embed)
    
@bot.command(aliases=["favChannel", "favChannels", "favoriteChannel", "favoriteChannels", "favoriteYouTubeChannel"])
async def favoriteYouTubeChannels(ctx):
    embed = discord.Embed(title="THE PLAYER ZER0's favorite channels", description="This is a list of THE PLAYER ZER0's favorite YouTube channels")
    
    embed.add_field(name="1. Zanny", value="Zanny is a great YouTuber that Grace strives to be like while keeping the uniqueness of the channel.\n\nhttps://www.youtube.com/user/SirZandril")
    embed.add_field(name="2. SaveAFox", value="SaveAFox is a YouTube channel and a brand that save, among other animals, foxes, squirrels, and more! Their mission is one of the best and they treat their animals right. Check them out!\n\nhttps://www.youtube.com/channel/UCb3KY97ICfIkDJY_p6d7yig")
    embed.add_field(name="3. Nathan Boehm", value="I've known Nathan for about a year now; I actually met his brother back in fifth grade, and what and how he does his content is just to die for! Sure, I may be biased because I've known Nathan and his brother for year(s), but you should go check him out!\n\nhttps://www.youtube.com/channel/UCzyNaprXvVOKZgX85tq-RBg")

    await ctx.send(embed=embed)

@bot.command(aliases=["upcomingseries"])
async def upcoming(ctx):
    embed = discord.Embed(title="THE PLAYER ZER0's Upcoming Series", description="This is a list of ALL of Grace's upcoming series on THE PLAYER ZER0!", color=0xAAFFAA, url="https://www.youtube.com/channel/UCG0OvtYX4qA6Ap1OxQpohOA/videos")
    
    embed.add_field(name="Minecraft: The Journey Home", value="Grace Lovelight is a young Mage who was attacked by a mysterious masked personage. After narrowly escaping from Him through a portal, he finds himself stuck in the world of Minecraft.\n\nHowever, he swiftly finds out that he is not alone when someone by the initials T.G.D. reaches out to him, promising him a way to escape as long as he goes on a journey for Her.\n\nWhat will happen next? Watch Minecraft: the Journey Home - The Reawakening of the Wither to find out! / No release date yet.", inline=False)
    embed.add_field(name="Let's Play Minecraft", value="Just a regular-old Minecraft Modded Let's Play! / Releasing on November 12th, 2021.", inline=False)
    embed.add_field(name="Let's Play LEGO Harry Potter", value="This is my next flag ship series after I finish LEGO Star Wars: Season 1 but before I start season 2 of Let's Play LEGO Star Wars")
    embed.add_field(name="Let's Play Genshin Impact", value="This is going to be up there with Blessed on my most graphical series ever but it won't be as bad as previous seasons of Blessed were. This series has no concrete release date.")
    embed.add_field(name="Let's Play Star Wars: The Old Republic", value="This will be another Star Wars series but this time, I shouldn't have graphical issues with this series because of how old the game is!")
    embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AAUvwngLzBB2zSK78OHAWHCJ-f7yUgr368Jj7kjCxIoyiw=s176-c-k-c0x00ffffff-no-rj")

    await ctx.send(embed=embed)

@bot.command(aliases=["ongoingseries"])
async def ongoing(ctx):

    embed = discord.Embed(title="THE PLAYER ZER0's Ongoing Series", description="This is a list of ongoing series' on THE PLAYER ZER0", color=0xAAFFAA, url="https://www.youtube.com/playlist?list=PLqWmHBgL2jJEyixhIBxq3MTDg6KWEPtOw")

    embed.add_field(name="Let's Play LEGO Star Wars", value="1 Season, 61 Episodes / December 5th, 2020 - Present Day / Status: Alive", inline=False)
    embed.add_field(name="Club Penguin Island: Offline Mode", value="2 Seasons, 13 Episodes / July 11th, 2020 - Present Day / Status: Alive", inline=False)
    embed.add_field(name="Blessed", value="3 Seasons, 8 Episodes / October 4th, 2020 - Present Day / Status: Dormant", inline=False)
    embed.add_field(name="Let's Play Genshin Impact", value="1 Season, 1 Episode / April 10th, 2021 - Present Day / Status: Alive", inline=False)
    embed.add_field(name="YouTube Alerts", value="2 Seasons, 3 Episodes / August 10th, 2016 - Present Day / Status: Alive", inline=False)
    embed.add_field(name="Toontown's Funny Farm", value="1 Season, 4 Episodes / July 16th, 2020 - Present Day / Status: Dormant", inline=False)
    embed.add_field(name="Toontown Rewritten", value="1 Season, 6 Episodes / July 7th, 2020 / Status: Dormant", inline=False)
    embed.add_field(name="Clash 'n Task", value="1 Season, 3 Episodes / June 22nd, 2020 - Present Day / Status: Dormant", inline=False)
    #embed.add_field(name="Untitled Goose Game", value="1 Season, 4 Episodes / July 19th, 2020 - August 10th, 2020 / Status: Completed", inline=False)
    #embed.add_field(name="Toontown Frenchy", value="1 Season, 12 Episodes / July 26th, 2020 - December 17th, 2020 / Status: Cancelled", inline=False)
    embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AAUvwngLzBB2zSK78OHAWHCJ-f7yUgr368Jj7kjCxIoyiw=s176-c-k-c0x00ffffff-no-rj")

    await ctx.send(embed=embed)

@bot.command(aliases=["statistics", "youtube", "youtubestats", "THEPLAYERZER0", "THEPLAYERZERO", "subs", "subscribers", "views", "videos"])
async def stats(ctx):
  async with aiohttp.ClientSession() as session:
    async with session.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCG0OvtYX4qA6Ap1OxQpohOA&key=AIzaSyDqVdu61QOeF18-MS4MfN4ejejb4Bm0s8A") as response:
      subs = (await response.json())["items"][0]["statistics"]["subscriberCount"]
      views = (await response.json())["items"][0]["statistics"]["viewCount"]
      videos = (await response.json())["items"][0]["statistics"]["videoCount"]
      embed = discord.Embed(title="THE PLAYER ZER0", description="", color=0x9370DB, url="https://www.youtube.com/channel/UCG0OvtYX4qA6Ap1OxQpohOA")
      embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
      embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AAUvwngLzBB2zSK78OHAWHCJ-f7yUgr368Jj7kjCxIoyiw=s176-c-k-c0x00ffffff-no-rj")
      
      embed.add_field(name="Subscriber Count:", value=f"{subs}")
      embed.add_field(name="Viewer Count:", value=f"{views}")
      embed.add_field(name="Video Count:", value=f"{videos}")
    
      embed.set_footer(text=f"THE PLAYER ZER0 is currently at {subs} subscribers, {views} views, and has {videos} videos!")
      await ctx.send(embed=embed)
      await session.close()

@bot.command(aliases=["subscribergoal"])
async def subgoal(ctx):
  #await ctx.send("His subscriber goal is to surpass his previous main channel called Zachary StarBlade")
  await ctx.send("After achieving his initial goal to surpass Zachary Starblade on his subscriber count, his new goal is to surpass his first YouTube channel 320zachary which, at last count, had 100 subscribers.")
  #await ctx.send("THE PLAYER ZER0's third goal is to surpass Nathan Boehm's channel.")
  #await ctx.send("After achieving his third goal to surpass Nathan Boehm's subscriber count of 207, THE PLAYER ZER0's newest goal is to surpass his friend Stealth Bre's subscriber count of 241")

@bot.command()
async def goal(ctx):
  await ctx.send("THE PLAYER ZER0's goal, that isn't a subscriber-related is that he wants to be able to finish at least 1 complete let's play series which he very nearly completed until LEGO Star Wars: The Force Awakens came along, then it ended up being paused until a later date!")

@bot.command(aliases=["ff"])
async def funfact(ctx):
  await ctx.send("This feature is under construction. Try again later!")

@bot.command()
async def catfact(ctx):
  async with aiohttp.ClientSession() as session:
    async with session.get("https://catfact.ninja/fact") as response:
      fact = (await response.json())["fact"]
      length = (await response.json())["length"]
      embed = discord.Embed(title=f'Random Cat Fact Number: **{length}**', description=f'Cat Fact: {fact}', color=0x9370DB)
      embed.set_footer(text="")
      await ctx.send(embed=embed)
      await session.close()

@bot.command()
async def cat(ctx):
    await ctx.send("Here's a picture of Pancha and Ollie!", file=discord.File('assets/images/Cat.jpg'))

@bot.command()
async def dog(ctx):
    await ctx.send("Here's a picture of Pancha and Ollie!", file=discord.File('assets/images/Cat.jpg'))

@bot.command(aliases=["memes"])
async def meme(ctx):
  await ctx.send("Sorry but this feature is coming as soon as Grace figures out how to import APIs to the bot!")

@bot.command(aliases=["dadjoke"])
async def dadjokes(ctx):
  dadjoke = Dadjoke()
  await ctx.send(dadjoke.joke)

# Do a Word of Wisdom generator
# Add a Poetry API
# Add a Fun Fact API and mix it with my fun facts
# Finish Tarot card picker
# Horoscope giver for specific horoscope

@bot.command()
async def links(ctx):
  await ctx.send("|\nMy Discords:\n- PLAYER ZER0 STUDIOS: https://discord.com/invite/XJRNv3eNmY\n- The Nebula: https://discord.com/invite/wwkh4w9\n\nYouTube Channels:\nMercy Grace Lovelight: https://www.youtube.com/channel/UCP3Wq0hfaNJJif3ZKk2q8pA\n- THE PLAYER ZER0: https://www.youtube.com/channel/UCG0OvtYX4qA6Ap1OxQpohOA\n- PLAYER ZER0 STUDIOS: https://www.youtube.com/channel/UCoYDqXueFCvlRAgqJwtmiiw\n- PLAYER ZER0 ARCHIVES: https://www.youtube.com/channel/UCLO1uJK-2yu3CuXgIvwmaag\n\nWebsites:\n-THE PLAYER ZER0: https://www.theplayerzero.com\n-PLAYER ZER0 STUDIOS: https://www.playerzerostudios.com\n-Arbitrium TV: https://www.arbitriumtv.com\n|")

@bot.command(aliases=["invites"])
async def invite(ctx):
  await ctx.send("Here is the invite link to the PLAYER ZER0 STUDIOS Discord: https://discord.gg/9fgW8jAaf6\n\nAnd here's the link to the other Discord that I am in called The Nebula: https://discord.com/invite/wwkh4w9\n\nMore links can be found by using the `~links` command!")

@bot.command(aliases=["comingsoon"])
async def features(ctx):
  await ctx.send("Some features that Grace wants to add to me, ay? Well, HD video streaming between friends, HD Music Player, add webhooks to announce various things from YouTube video releases to Tweets, leveling system with cool perks, role-giving system, and more! But don't count on a release date for these features!")

# Custom Help Command

@bot.group(aliases=["pages"], invoke_without_command=True)
async def help(ctx):
    contents = ["Moderation Commands: `~clear`, `~kick`, `~ban`, `~unban`, `~whois`, `~addbannedword / ~addbadword`, `~removebannedword / ~removebadword`, `~reload`", "Technical Commands: `~version`, `~ping`, `~cog`, `~test`, `~python`, `~rank / ~level`", "Fun Commands: `~funfact` / `~ff` `~creation`, `~favsong / ~favoriteSong`, `~online`, `~snap`, `~monsterfight`, `~meme`, `~dadjokes`, `~tarot / ~pickacard / ~pick-a-card`, `~oracle / ~oraclecards / ~oraclecard / ~angelcards / ~angelcard`, `~wisdom / ~wordsofwisdom`, `~advice`, `~catfact`", "YouTube Commands: `~mcjh`, `~releasedate` / `~rd`, `statistics, youtube, youtubestats, THEPLAYERZER0, THEPLAYERZERO, subs, subscribers, views, videos`, `~subGoal`, `~Goal`, `~cancelled`, `~upcoming`, `~ongoing`", "Other Commands: `~links`, `~features`, `~she/her / ~sheher`, `~she/him / ~shehim`, `~he/him / ~hehim`, `~he/them / ~hethem`, `~she/them / ~shethem`, `~they/them / ~theythem`, `~any/any / ~anyany / ~any`"]
    pages = 5
    cur_page = 1
    
    message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            break
            # would end the loop if user doesn't react after x seconds but the timer is gone...

@help.error
async def help_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("The command you have given me cannot be found! Please check the ~help command for all commands!")
    
# Moderation Commands for the Help Command:

@help.command()
async def clear(ctx):

  em = discord.Embed(title = "~Clear", description = "Clears messages for given number of messages!", color=0x2ECC71)

  await ctx.send(embed = em)

@help.command()
async def kick(ctx):

  em = discord.Embed(title = "~Kick", description = "Kicks the mentioned member from the Discord with out without reason!", color=0x2ECC71)

  await ctx.send(embed = em)

@help.command()
async def ban(ctx):

  em = discord.Embed(title = "~Ban", description = "Bans the mentioned member from the Discord with or without reason!", color=0x2ECC71)

  await ctx.send(embed = em)

@help.command()
async def unban(ctx):

  em = discord.Embed(title = "~Unban", description = "Unbans a member from the Discord!", color=0x2ECC71)

  await ctx.send(embed = em)

@help.command(aliases=["whois", "user", "info"])
async def userinfo(ctx):

  em = discord.Embed(title = "~WhoIs", description = "Tells the user who the mentioned user is.", color=0x2ECC71)

  await ctx.send(embed = em)

@help.command()
async def reload(ctx):

  em = discord.Embed(title = "~Reload", description = "Reloads the mentioned Cog!", color=0x2ECC71)

  await ctx.send(embed = em)
    
# Technical Commands for the Help Command:

@help.command()
async def version(ctx):

  em = discord.Embed(title = "~Version", description = "Tells the current version of the bot!", color=0xE67E22)

  await ctx.send(embed = em)

@help.command(aliases=["previous", "versions", "pv", "previousversion"])
async def previousversions(ctx):

  em = discord.Embed(title = "~PreviousVersions", description = "Tell of the previous versions of the bot from 1.0.0 to the version prior to the latest.", color=0xE67E22)

  await ctx.send(embed = em)

@help.command()
async def ping(ctx):

  em = discord.Embed(title = "~Ping", description = "Says 'Pong!' and gives the time it took to reply (in miliseconds)!", color=0xE67E22)

  await ctx.send(embed = em)

@help.command(aliases=["cogs"])
async def cog(ctx):

  em = discord.Embed(title = "~Cog / ~Cogs", description = "Tells you that the bot now uses Cogs!", color=0xE67E22)

  await ctx.send(embed = em)

@help.command(aliases=["Test"])
async def test(ctx):

  em = discord.Embed(title = "~Test", description = "Tells you that the Cogs are working.", color=0xE67E22)

  await ctx.send(embed = em)

@help.command(aliases=["py"])
async def python(ctx):

  em = discord.Embed(title = "~Python", description = "Tells you what version of Python I am running on!.", color=0xE67E22)

  await ctx.send(embed = em)

@help.command(aliases=["level"])
async def rank(ctx):

  em = discord.Embed(title = "~Rank", description = "Tells you what level you are at!.", color=0xE67E22)

  await ctx.send(embed = em)

# Fun Commands for the Help Command:

@help.command(aliases=["ff"])
async def funfact(ctx):

  em = discord.Embed(title="~funfact / ~ff", description = "Gives a random fun fact from a number of given fun facts!", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command()
async def creation(ctx):

  em = discord.Embed(title = "~creation", description = "This command tells you my conception date and birth date!", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command(aliases=["favsong", "fs"])
async def favoritesong(ctx):

  em = discord.Embed(title = "~favoritesong / ~favsong", description = "Gives Grace's current favorite song!", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command()
async def online(ctx):

  em = discord.Embed(title = "~online", description = "Tells you whether or not the bot is online or not.", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command()
async def snap(ctx):

  em = discord.Embed(title = "~snap", description = "It's a reference to Tom Holland's infamous improvised line in the climax of Avengers: Infinity War.", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command(aliases=["ms"])
async def monsterfight(ctx):

  em = discord.Embed(title = "~monsterFight / ~mf", description = "It's my prediction of which Monster will win in the Monster-verse's newest movie called Godzilla vs. Kong!", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command()
async def meme(ctx):

  em = discord.Embed(title = "~meme:", description = "Sends a random meme from a API of memes", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command()
async def dadjokes(ctx):

  em = discord.Embed(title = "~dadJokes:", description = "Once implemented, it will generate a Dad Joke from a database.", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command()
async def tarot(ctx):

  em = discord.Embed(title = "~Tarot:", description = "Gives a random tarot card plus a paragraph to determine what it means **__NOTE__**: This is meant for ENTERTAINMENT purposes ONLY.", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command(aliases=["cat"])
async def dog(ctx):

  em = discord.Embed(title = "~Dog / ~Cat:", description = "Sends a picture of Ollie and Pancha, THE PLAYER ZER0's dog and cat.", color=0xAAFFAA)

  await ctx.send(embed = em)
    
@help.command()
async def catfact(ctx):

  em = discord.Embed(title = "~CatFact:", description = "Gives a random cat fact.", color=0xAAFFAA)

  await ctx.send(embed = em)

# The Book of Life Help Commands:

@help.command()
async def mcjh(ctx):

  em = discord.Embed(title = "~mcjh:", description = "Upon usage, it provides a description for Minecraft: the Journey Home - The Reawakening of the Wither along with a link to the playlist.", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command(aliases=["rd"])
async def releasedate(ctx):

  em = discord.Embed(title = "~releasedate / ~rd:", description = "When used, it gives the release date for The Lovelight Saga's newest, upcoming series/movie!", color=0xAAFFAA)

  await ctx.send(embed = em)

# YouTube Commands for the Help Command:

@help.command(aliases=["cancelled", "cancelledseries"])
async def cancel(ctx):
    
  em = discord.Embed(title = "~Cancelled", desciption = "Gives the user a list of cancelled series's on THE PLAYER ZER0's YouTube channel", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command(aliases=["ongoingseries"])
async def ongoing(ctx):
    
  em = discord.Embed(title="~Ongoing", desciption = "Gives a list of ongoing series' on THE PLAYER ZER0", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command(aliases=["upcomingseries"])
async def upcoming(ctx):
    
  em = discord.Embed(title="~Upcoming", description = "Gives a list of upcoming series' on THE PLAYER ZER0", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command(aliases=["statistics", "youtube", "youtubestats", "THEPLAYERZER0", "THEPLAYERZERO", "subs", "subscribers", "views", "videos"])
async def stats(ctx):

  em = discord.Embed(title = "~Statistics:", description = "Gives the current number of Subscribers, view count, and video count for THE PLAYER ZER0!", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command(aliases=["subscribergoal"])
async def subgoal(ctx):

  em = discord.Embed(title = "~subGoal / ~subscriberGoal", description = "Gives Grace's current Subscriber goal for his YouTube channel!", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command()
async def goal(ctx):

  em = discord.Embed(title = "~Goal", description = "Gives Grace's current goal for his YouTube channel that isn't related to subscribers!", color=0xAAFFAA)

  await ctx.send(embed = em)

# Other Commands for the Help Command:

@help.command()
async def links(ctx):

  em = discord.Embed(title = "~links", description = "Gives links that are listed in #links", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command(aliases=["comingsoon"])
async def features(ctx):

  em = discord.Embed(title = "~features / ~ComingSoon", description = "Gives a list of features that Grace wants to add to me!", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command(aliases=["She/Her"])
async def sheher(ctx):

  em = discord.Embed(title = "~she/her / ~sheher", description = "Gives the user the she/her role so that people know what to refer to the user by!", color=0xAAFFAA)

  await ctx.send(embed = em)
    
@help.command(aliases=["She/Him"])
async def shehim(ctx):

  em = discord.Embed(title = "~she/him / ~shehim", description = "Gives the user the she/him role so that people know what to refer to the user by!", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command(aliases=["He/Him"])
async def hehim(ctx):

  em = discord.Embed(title = "~He/Him / ~hehim", description = "Gives the user the he/him role so that people know what to refer to the user by!", color=0xAAFFAA)

  await ctx.send(embed = em)
    
@help.command(aliases=["He/Them"])
async def hethem(ctx):

  em = discord.Embed(title = "~he/them / ~hethem", description = "Gives the user the he/them role so that people know what to refer to the user by!", color=0xAAFFAA)

  await ctx.send(embed = em)
    
@help.command(aliases=["She/Them"])
async def shethem(ctx):

  em = discord.Embed(title = "~she/them / ~shethem", description = "Gives the user the she/them role so that people know what to refer to the user by!", color=0xAAFFAA)

  await ctx.send(embed = em)

@help.command(aliases=["they/them"])
async def theythem(ctx):

  em = discord.Embed(title = "~they/them / ~person", description = "Gives the user the they/them role so that people know what to refer to the user by!", color=0xAAFFAA)

  await ctx.send(embed = em)
    
@help.command(aliases=["any/any", "anyany"])
async def any(ctx):

  em = discord.Embed(title = "~any/any / ~any", description = "Gives the user the any/any role so that people know what to refer to the user by!", color=0xAAFFAA)

  await ctx.send(embed = em)
    
# Tasks

bot.loop.create_task(update_stats())
#bot.create_task(MessagesMod())

# Ending

bot.run(token)