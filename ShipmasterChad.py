# ShipmasterChad.py

import random
import datetime
import sys
import os
import discord
from discord.ext import commands


TOKEN = 'NzExOTgxMTUwNzI5NTM1NTI4.Xsn9Qw.aY-Xtjs3pCP_RrIVThsp2beMJI0'

client = commands.Bot(command_prefix='~')
client.remove_command('help')
now = datetime.datetime.now()
color = 0xa987df

# list of commands accessible to public
comm = ["~help", "list commands", "~quote", "reply with a random quote from a list", "~8ball", "tells your fortune",
        "~spam [user] [amt] [msg]", "spams a [user] with a [msg] [amt] times"]

# list of all commands
all_commands = ["~ping", "replies with bot's latency", "~clear[amt]", "clears [amt] messages in the channel",
                "~kick [user] [reason]", "kicks [user] from the server", "~ban [user] [reason]",
                "bans [user] from the server", "~unban [user", "unbans [user] from the server", "~close",
                "closes the bot with exit code 0", "~load [ext]", "loads [extension]", "~unload [ext]",
                "unloads [extension]"]

# list of elite quotes from I Would Have Been Your Daddy skull
iwhbyd = ["Yes, I have one blue eye and one green eye, can we get on with it?",
          "One word for you: Haboodigaboodiguhguh.", "Master Chief, can we be friends?",
          "Damn... I like you too, but damn!", "Oh, snap!", "I... I... I think you're sexy too... er...",
          "That's what she said.", "Ha Ha Ha! How does it feel to be dead?! Wait, don't answer that.",
          "Have no fear, I will cover the rear, ha ha ha, err..", "Die, stinky!",
          "Didn't I give you this for Christmas?", "What? Do you want me to say 'Wort, Wort, Wort'?",
          "Wort, Wort, Wort!", "I'm trying new contacts. Now stop dripping!",
          "Really, I'm not going to kiss you in front of everyone.", "No, I don't know how to kiss you either.",
          "If you gaze at me much longer, we might as well exchange fluids!", "Your ass is mine!",
          "Is this because of Reach?", "Yes, they are the window to my soul... now stop!", "You had me at hello.",
          "Why don't you just take a... uh, what do you call it, picture? Yes, that's it.",
          "Give them chicken, give them liver.", "I shall remember this day, always.",
          "Is there something in my teeth?", "Don't shoot me, fool!",
          "I like you too, but let's talk about this later, ha ha ha....",
          "I... like you, too! ... Let's talk about this afterwards, shall we?",
          "I will name my next child after you!.", "A fine trade!", "You disgusting foot lice!!",
          "The Arbiter has joined us! Huzzah!", "This means... so much to me!", "Do I look like a Grunt?",
          "This stupidity hurts our case.",
          "Why don't you take a picture? And it'll, uh... What does it say? Master Chief.", "Ahhh! What's this?",
          "At least think!", "I'll kill many with this.", "I will regret this.", "This trade is unfair.",
          "Ouch!", "This is less than optimal.", "Bagh!", "Wretch!", "I already regret this trade!",
          "Two words for you! FI-RE!", "You have some brains...on your face."]

# list of possible fortunes
fortunes = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.",
            "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
            "Ask again later.", "Cannot predict now.", "Don't count on it.", "My reply is no.", "My sources say no.",
            "Outlook not so good.", "Very doubtful.", "As I see it, no.", "It is unlikely.", "Not likely.",
            "Outlook poor.", "No."]

# rules of the server
sus_rules = "1. No sus shit related to animal crossing I'm not fuckin around\n2. That's all thanks : )"


# list of greetings
greetings = ['Hi', 'Hello', 'Hey', 'Yo', 'Greetings', 'Good afternoon', 'Good morning', 'Good evening', 'Hiya', 'Heyo',
             'Well Met']

# list of weeb phrases
weeb_shit = ['anime', 'hentai', 'weeb', 'yaoi', 'uwu', 'owo']

# names for Master Chief
demon_names = ['demon', 'chief', 'spartan', '117']


def is_me(ctx):  # checks if a message's author's id matches my id
    return ctx.message.author.id == 285712348084174849

########################################################################################################################


@client.event
async def on_ready():  # activated when bot is loaded
    print('Bot is ready')
    with open('ShipmasterChadLog.txt', 'a+') as f:
        f.write(f'{client.user} has entered the Sus Zone, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for filename in os.listdir('./cogs'):  # loads cogs when bot is loaded
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')  # removes .py extension from files
            with open('ShipmasterChadLog.txt', 'a+') as f:
                f.write(f'Cog {filename} successfully loaded on startup, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    await client.change_presence(activity=discord.Game(name='Halo'))


@client.event
async def on_member_join(member):  # activated when member joins the server
    with open('ShipmasterChadLog.txt', 'a+') as f:
        f.write(f'{member} has joined the Sus Zone, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


@client.event
async def on_member_remove(member):  # activated when a member leaves the server
    with open('ShipmasterChadLog.txt', 'a+') as f:
        f.write(f'{member} has left the Sus Zone, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


@client.event
async def on_message(message):  # replies to certain messages the bot can see
    if message.author == client.user:
        return
    for phrases in greetings:
        if message.content.lower() == phrases.lower():
            await message.channel.send(f'{phrases}, Human')
            with open('ShipmasterChadLog.txt', 'a+') as f:
                f.write(f'Someone said {phrases} to me!, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    if '69' in message.content:
        await message.channel.send('nice.')
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'nice., {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    if '420' in message.content:
        await message.channel.send('epic')
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'epic, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    if '1337' in message.content:
        await message.channel.send('l33t gam3r')
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'l33t gam3r, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for phrases in weeb_shit:
        if phrases in message.content.lower():
            await message.channel.send(f'^fuckin weeaboos')
            with open('ShipmasterChadLog.txt', 'a+') as f:
                f.write(f'fuckin weeaboos again, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    if '???' in message.content:
        await message.channel.send('???')
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'???, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    if 'birthday' in message.content.lower():
        await message.channel.send('Happy Birthday, Human :tada:')
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'I wished someone a happy birthday, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    if 'wort' in message.content.lower():
        await message.channel.send('Wort Wort Wort')
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'Wort Wort Wort, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    if 'isabelle' in message.content.lower():
        await message.channel.send('Please stop trying to fuck Isabelle')
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'Someone wanted to fuck isabelle {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for names in demon_names:
        if names in message.content.lower():
            await message.channel.send('The Demon is here??')
            with open('ShipmasterChadLog.txt', 'a+') as f:
                f.write(f'The Demon made an appearance! {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    if message.content == 'raise-exception':
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'Raised a discord Exception, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
        raise discord.DiscordException
    else:
        number = random.randint(1, 8192)  # shiny odds in pokemon gens 2-5
        if number == 1302:  # target store I work at
            message.channel.send("That's Unfortunate")
            with open('ShipmasterChadLog.txt', 'a+') as f:
                f.write(f'That is Unfortunate, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    await client.process_commands(message)


@client.event
async def on_error(event, *args):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

########################################################################################################################


@client.command(aliases=['help', 'bot'])
async def commands(ctx):  # lists all commands available to public
    embed = discord.Embed(title="Shipmaster Chad's Capabilites", color=color)
    for i in range(0, len(comm), 2):
        embed.add_field(name=comm[i], value=comm[i+1], inline=False)
    await ctx.author.send(embed=embed)
    await ctx.channel.purge(limit=1)
    with open('ShipmasterChadLog.txt', 'a+') as f:
        f.write(f'{ctx.author} needed help, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


@client.command()
async def rules(ctx):  # sends rules of the server
    embed = discord.Embed(title="Rules of the Sus Zone", description=sus_rules, color=color)
    await ctx.author.send(embed=embed)
    await ctx.channel.purge(limit=1)
    with open('ShipmasterChadLog.txt', 'a+') as f:
        f.write(f'{ctx.author} needed to know the rules, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


@client.command(aliases=['quotes', 'iwhbyd'])
async def quote(ctx):  # sends a random quote from list iwhbyd
    await ctx.send(random.choice(iwhbyd))
    with open('ShipmasterChadLog.txt', 'a+') as f:
        f.write(f'{ctx.author} wanted a quote, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


@client.command(aliases=['8ball', 'fortunes'])
async def fortune(ctx):  # sends a random fortune from list fortunes
    await ctx.send(random.choice(fortunes))
    with open('ShipmasterChadLog.txt', 'a+') as f:
        f.write(f'{ctx.author} wanted a fortune, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


@client.command()
async def spam(ctx, user: discord.User, amount, *, message):  # spams a [user] [amount] times with a [message]
    if int(amount) > 100:
        amount = 100
    with open('ShipmasterChadLog.txt', 'a+') as f:
        f.write(f'{ctx.author} sent {user.name} "{message}" {amount} times, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    for _ in range(int(amount)):
        await user.send(message)

########################################################################################################################


@client.command(aliases=['all_commands', 'all', 'admin'])
async def all_c(ctx):  # lists admin commands
    if ctx.channel.permissions_for(ctx.author).manage_guild:
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title="All Of Shipmaster Chad's Capabilites", color=color)
        for i in range(0, len(all_commands), 2):
            embed.add_field(name=all_commands[i], value=all_commands[i+1])
        await ctx.author.send(embed=embed)
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'{ctx.author} needed admin help, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    else:
        await ctx.author.send('You do not have the authority for that feature')
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'{ctx.author} tried to access admin help, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    await ctx.channel.purge(limit=1)


@client.command(aliases=['ping'])
async def latency(ctx):  # replies with bot's latency
    if ctx.channel.permissions_for(ctx.author).manage_guild:
        await ctx.send(f'{round(client.latency, 2)} ms')
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'{ctx.author} checked latency\n')
    else:
        await ctx.author.send('You do not have the authority for that feature')
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'{ctx.author} tried to check latency, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


@client.command(aliases=['delete', 'remove'])
async def clear(ctx, amount=1):  # clears [amount] messages in the current channel
    if ctx.channel.permissions_for(ctx.author).manage_guild:
        await ctx.channel.purge(limit=amount + 1)
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(
                f'{ctx.author} cleared {amount + 1} messages in {ctx.channel}, '
                f'{now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    else:
        await ctx.author.send('You do not have the authority for that feature')
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'{ctx.author} tried to clear {amount} messages in {ctx.channel}, '
                    f'{now.strftime("%Y-%m-%d %H:%M:%S")}\n')


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):  # kicks a [member] from the server
    if ctx.channel.permissions_for(ctx.author).manage_guild:
        await member.kick(reason=reason)
        await ctx.send(f'User {member.name} has been kicked for {reason}')
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'{member.name} was kicked form the server for {reason}, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    else:
        await ctx.author.send("You do not have the authority for that feature")
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'{ctx.author} tried to kick {member.name} for {reason}, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):  # bans a [member] from the server
    if ctx.channel.permissions_for(ctx.author).manage_guild:
        await member.ban(reason=reason)
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'{member.name} was banned form the server for {reason}, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    else:
        await ctx.author.send("You do not have the authority for that feature")
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'{ctx.author} tried to ban {member.name} for {reason}, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


@client.command()
async def unban(ctx, *, member):  # unbans a [user] from the server
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    unbanned = False
    if ctx.channel.permissions_for(ctx.author).manage_guild:
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned User {user.name}#{user.discriminator}')
                with open('ShipmasterChadLog.txt', 'a+') as f:
                    f.write(
                        f'Unbanned User {user.name}#{user.discriminator}, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
                unbanned = True
        if not unbanned:
            await ctx.send(f'Could not find User {member} in Banned Users')
            with open('ShipmasterChadLog.txt', 'a+') as f:
                f.write(f'Could not find User {member} in Banned Users, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    else:
        ctx.author.send('You do not have the authority for that feature')
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'{ctx.author.name} tried to Unban User {member}, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


@client.command()
async def close(ctx):  # closes bot
    if ctx.channel.permissions_for(ctx.author).manage_guild:
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'{client.user} is leaving the sus Zone, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
        sys.exit(0)
    else:
        ctx.author.send('You do not have the authority for that feature')
        with open('ShipmasterChadLog.txt', 'a+') as f:
            f.write(f'{ctx.author.name} tied to close the program, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


@client.command()
async def load(extension):  # loads cogs
    client.load_extension(f'cogs.{extension}')
    with open('ShipmasterChadLog.txt', 'a+') as f:
        f.write(f'Cog {extension}.py successfully loaded, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')


@client.command()
async def unload(extension):  # unloads cogs
    client.unload_extension(f'cogs.{extension}')
    with open('ShipmasterChadLog.txt', 'a+') as f:
        f.write(f'Cog {extension}.py successfully unloaded, {now.strftime("%Y-%m-%d %H:%M:%S")}\n')

client.run(TOKEN)
