# Imports&Run

import discord

discord.__version__
from discord.ext import commands
import asyncio
import random
import time
import datetime
from itertools import cycle
from discord import Member
from discord.ext.commands import has_permissions
from discord.utils import get
import youtube_dl

TOKEN = "NTcxMzM5NzE2MjQzNDg4Nzg4.XMQseg.xrGhICMum_jQRj_QERDD7bWLEaQ"

bot = commands.Bot(command_prefix='+')
bot.remove_command('help')


# Bot Setup

@bot.event
async def on_ready():
    print('Der Bot ist bereit!')
    print('-----------------')
    print('Eingeloggt als:')
    print(bot.user.name)
    print(bot.user.id)
    print('Programmiert von @Desaw.Lennard#1883')
    print('-----------------')


#   await bot.change_presence(game=discord.Game(name='/help | /invite'))

# Background Task
status = ["+help | +invite", "Testing", "auf Discord"]


async def change_status():
    await bot.wait_until_ready()
    msgs = cycle(status)

    while not bot.is_closed:
        current_status = next(msgs)
        await bot.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(60)


bot.loop.create_task(change_status())


# Ping Command
@bot.command()
async def ping():
    ping = random.randint(1, 100)
    await bot.say(':ping_pong: pong **{}**'.format(ping))


# Say Command
@bot.command(pass_context=True)
async def say(ctx, *, message: str):
    if ctx.message.author.id == "393423879126646785":
        await bot.say(message)
    else:
        await bot.say('Hey! Du bist nicht dafür Autorisiert das zu tun!')
        return


# Error Handling
# @bot.event
# async def on_command_error():
#   print('Error')

# love Command
@bot.command()
async def love(arg1, arg2):
    number = random.randint(0, 100)
    output1 = ''
    output2 = ''
    for word in arg1:
        output1 += word
        output1 += ''

    for word in arg2:
        output2 += word
        output2 += ''
    if number < 25:
        love = "{} und {} mögen sich nicht so :broken_heart:".format(output1, output2)
    if number > 25 and number < 50:
        love = "{} und {} mögen sich :heart:".format(output1, output2)
    if number > 50 and number < 75:
        love = "{} und {} sind verliebt :sparkling_heart:".format(output1, output2)
    if number > 75 and number < 100:
        love = "{} und {} sind ein Ehepaar :cupid:".format(output1, output2)

    embed = discord.Embed(
        title=':heartpulse: Liebes Rechner :heartpulse:',
        color=0xff00ff,
        description=':small_red_triangle_down: {}\n**{}**%\n:small_red_triangle: {}\n{}'.format(
            output1, number, output2, love)
    )
    await bot.say(embed=embed)


# ssp Command
@bot.command()
async def ssp(arg1):
    choice_User = ''
    for word in arg1:
        choice_User += word
        choice_User += ''

        ssp = ["Schere", "Papier", "Stein"]
        choice_bot = random.randint(1, 3)

    # Bot hat Schere
    if choice_bot == 1 and choice_User == 'Stein':
        await bot.say('Du hast gewonnen, ich hatte leider Schere :scissors:')
    if choice_bot == 1 and choice_User == 'Papier':
        await bot.say('Ich habe gewonnen, ich hatte nämlich Schere :scissors:')
    if choice_bot == 1 and choice_User == 'Schere':
        await bot.say('Unentschieden, ich hatte auch Schere :scissors:')

    # Bot hat Papier
    if choice_bot == 2 and choice_User == 'Schere':
        await bot.say('Du hast gewonnen, ich hatte leider Papier :page_facing_up:')
    if choice_bot == 2 and choice_User == 'Stein':
        await bot.say('Ich habe gewonnen, ich hatte nämlich Papier :page_facing_up:')
    if choice_bot == 2 and choice_User == 'Papier':
        await bot.say('Unentschieden, ich hatte auch Papier :page_facing_up:')

    # Bot hat Stein
    if choice_bot == 3 and choice_User == 'Papier':
        await bot.say('Du hast gewonnen, ich hatte leider Stein')
    if choice_bot == 3 and choice_User == 'Schere':
        await bot.say('Ich habe gewonnen, ich hatte nämlich Stein')
    if choice_bot == 3 and choice_User == 'Stein':
        await bot.say('Unentschieden, ich hatte auch Stein')


# Clear-Command

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    if not ctx.message.author.server_permissions.administrator:
        embed = discord.Embed(
            colour=discord.Colour.red()
        )
        embed.add_field(name=":x: Fehler!", value="Du hast nicht Berechtigt das zu tun!", inline=True)
        await bot.say(embed=embed)
    if ctx.message.author.server_permissions.administrator:
        channel = ctx.message.channel
        messages = []
        async for message in bot.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
            await bot.delete_messages(messages)
            await bot.say('{} Nachrichten gelöscht'.format(amount))


# ID Command
@bot.command()
async def id(arg1):
    id = ' '
    for word in arg1:
        id += word
        id += ' '
    await bot.say(id)


# Help Command
@bot.command(pass_context=True)
async def help(ctx, arg1=None):
    server = ctx.message.server
    blue = discord.Color.blue()
    dark_blue = discord.Color.dark_blue()
    purple = discord.Color.purple()
    dark_purple = discord.Color.dark_purple()
    magenta = discord.Color.magenta()
    dark_magenta = discord.Color.dark_magenta()
    orange = discord.Color.orange()
    dark_orange = discord.Color.dark_orange()

    color_list = [blue, dark_blue, purple, dark_purple, magenta,
                  dark_magenta, orange, dark_orange]
    random_color = random.choice(color_list)

    if server.name == "Bot Testing Server" or server.name == "Tryde Bot Development":
        if not arg1:
            embed = discord.Embed(color=random_color)
            embed.add_field(name='Command Übersicht',
                            value='1 - Allgemeine Commands \n2 - Admin Commands \n3 - Fun Commands\n4 - Musik Commands\n5 - Server Commands',
                            inline=True)
            await bot.say(embed=embed)
        if arg1:
            if arg1 == '1':
                embed = discord.Embed(color=random_color)
                embed.add_field(name="Allgemeine Commands",
                                value="`+help` - Bekomme die Help Liste \n`+invite` - Bekomme den Einladungs dieses Bots \n`+serverinfo` - Bekomme Infos über diesen Server \n`+userinfo [@User]` - Bekomme infos über diesen User\n`+botinfo` - Bekomme Infos über den Bot\n`+guilds` - Zeigt dir ale Server wo ich drauf bin\n`+gchat` - Schreibe mit anderen User auf anderen Servern",
                                inline=False)
                await bot.say(embed=embed)
            if arg1 == '2':
                embed = discord.Embed(color=random_color)
                embed.add_field(name="Admin Commands",
                                value="`+kick [@User]` - Kicke einen User \n`+ban [@User]` - Banne einen User \n`+news [text]` - Sende News \n`+umfrage [frage]` - Erstellt eine Umfrage \n`+clear [Zahl]` - Löscht eine Anzahl an Nachrichten",
                                inline=True)
                await bot.say(embed=embed)
            if arg1 == '3':
                embed = discord.Embed(color=random_color)
                embed.add_field(name="Fun Commands",
                                value="`+emolets` - Screibe einen Text in Emojies\n:warning: Achtung : Beta Command :warning:\nAlles kein Schreiben und nur ein Wort\n`+münze` - Wirft eine Münze \n`+love [@User] [@User]` - Rechnet zwischen 2 Usern die Liebe aus. \n`+ssp` - Spiele Schere, Stein, Papier gegen den Bot \n`+embed [text]` - Sendet deine Nachricht als Embed\n`+8ball` - Frage den Bot eine Frage",
                                inline=True)
                await bot.say(embed=embed)
            if arg1 == '4':
                embed = discord.Embed(color=random_color)
                embed.add_field(name="Musik Commands",
                                value="`+play [url]` - Spielt ein Lied\n`+pause` - Pausiert das Lied\n`+resume` - Spielt das Lied weiter\n`+stop` - Beendet das Lied\n`+volume [zahl oder +,-]` - Stellt die Lautstärke ein\n(+ und - ändern die Lautstärke jeweills +5 oder -5)",
                                inline=True)
                await bot.say(embed=embed)
            if arg1 == '5':
                embed = discord.Embed(color=random_color)
                embed.add_field(name="Server Command",
                                value="`+idee [Command Idee] [Beschreibung]` - Hast du eine neue Idee für den Bot. Schlage Sie vor",
                                inline=True)
                await bot.say(embed=embed)
    else:
        if not arg1:
            embed = discord.Embed(color=random_color)
            embed.add_field(name='Command Übersicht',
                            value='1 - Allgemeine Commands \n2 - Admin Commands \n3 - Fun Commands\n4 - Musik Commands',
                            inline=True)
            await bot.say(embed=embed)
        if arg1:
            if arg1 == '1':
                embed = discord.Embed(color=random_color)
                embed.add_field(name="Allgemeine Commands",
                                value="`+help` - Bekomme die Help Liste \n`+invite` - Bekomme den Einladungs dieses Bots \n`+serverinfo` - Bekomme Infos über diesen Server \n`+userinfo [@User]` - Bekomme infos über diesen User\n`+botinfo` - Bekomme Infos über den Bot\n`+gchat` - Schreibe mit anderen User auf anderen Servern",
                                inline=False)
                await bot.say(embed=embed)
            if arg1 == '2':
                embed = discord.Embed(color=random_color)
                embed.add_field(name="Admin Commands",
                                value="`+kick [@User]` - Kicke einen User \n`+ban [@User]` - Banne einen User \n`+news [text]` - Sende News \n`+umfrage [frage]` - Erstellt eine Umfrage \n`+clear [Zahl]` - Löscht eine Anzahl an Nachrichten",
                                inline=True)
                await bot.say(embed=embed)
            if arg1 == '3':
                embed = discord.Embed(color=random_color)
                embed.add_field(name="Fun Commands",
                                value="`+emolets` - Screibe einen Text in Emojies\n:warning: Achtung : Beta Command :warning:\nAlles klein Schreiben und nur ein Wort\n`+münze` - Wirft eine Münze \n`+love [@User] [@User]` - Rechnet zwischen 2 Usern die Liebe aus. \n`+ssp` - Spiele Schere, Stein, Papier gegen den Bot \n`+embed [text]` - Sendet deine Nachricht als Embed\n`+8ball` - Frage den Bot eine Frage",
                                inline=True)
                await bot.say(embed=embed)
            if arg1 == '4':
                embed = discord.Embed(color=random_color)
                embed.add_field(name="Musik Commands",
                                value="`+play [url]` - Spielt ein Lied\n`+pause` - Pausiert das Lied\n`+resume` - Spielt das Lied weiter\n`+stop` - Beendet das Lied\n`+volume [zahl oder +,-]` - Stellt die Lautstärke ein\n(+ und - ändern die Lautstärke jeweills +5 oder -5)",
                                inline=True)
                await bot.say(embed=embed)


# News Command
@bot.command(pass_context=True)
async def news(ctx, *, message):
    if not ctx.message.author.server_permissions.administrator:
        embed = discord.Embed(
            colour=discord.Colour.red()
        )
        embed.add_field(name=":x: Fehler!", value="Du hast nicht Berechtigt das zu tun!", inline=True)
        await bot.say(embed=embed)
    if ctx.message.author.server_permissions.administrator:
        blue = discord.Color.blue()
        dark_blue = discord.Color.dark_blue()
        purple = discord.Color.purple()
        dark_purple = discord.Color.dark_purple()
        magenta = discord.Color.magenta()
        dark_magenta = discord.Color.dark_magenta()
        orange = discord.Color.orange()
        dark_orange = discord.Color.dark_orange()

        color_list = [blue, dark_blue, purple, dark_purple, magenta,
                      dark_magenta, orange, dark_orange]
        random_color = random.choice(color_list)

        #    channel = bot.get_channel("547410165100576768")
        embed = discord.Embed(
            title=':incoming_envelope: Neuigkeiten ',
            description='{}'.format(message),
            colour=random_color
        )
        embed.set_footer(text='Neuigkeiten gesendet von {}'.format(ctx.message.author),
                         icon_url='{}'.format(ctx.message.author.avatar_url))
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)
        await bot.say('@everyone')


# Userinfo
@bot.command(pass_context=True)
async def userinfo(ctx, userName: discord.Member):
    blue = discord.Color.blue()
    dark_blue = discord.Color.dark_blue()
    purple = discord.Color.purple()
    dark_purple = discord.Color.dark_purple()
    magenta = discord.Color.magenta()
    dark_magenta = discord.Color.dark_magenta()
    orange = discord.Color.orange()
    dark_orange = discord.Color.dark_orange()

    color_list = [blue, dark_blue, purple, dark_purple, magenta,
                  dark_magenta, orange, dark_orange]
    random_color = random.choice(color_list)
    user = userName

    embed = discord.Embed(title="{}'s info".format(user.name),
                          color=random_color)
    embed.add_field(name='Name: ', value='{}'.format(user.name))
    embed.add_field(name='Tag: ', value='{}'.format(user.discriminator), inline=True)
    embed.add_field(name='ID: ', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status: ', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Spielt gerade', value='{}'.format(user.game))
    embed.add_field(name='Hat Discord seit dem', value='{:%d/%h/%y um %H:%M}'.format(user.created_at), inline=True)
    embed.add_field(name='Höchste Rolle(auf diesen Server) :', value='<@&{}>'.format(user.top_role.id), inline=True)
    embed.add_field(name='Ist auf diesem Server seit dem', value='{:%d/%h/%y um %H:%M}'.format(user.joined_at),
                    inline=True)
    embed.set_footer(text="Gefragt von {}".format(ctx.message.author),
                     icon_url='{}'.format(ctx.message.author.avatar_url))
    embed.set_thumbnail(url=userName.avatar_url)

    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def serverinfo(ctx):
    blue = discord.Color.blue()
    dark_blue = discord.Color.dark_blue()
    purple = discord.Color.purple()
    dark_purple = discord.Color.dark_purple()
    magenta = discord.Color.magenta()
    dark_magenta = discord.Color.dark_magenta()
    orange = discord.Color.orange()
    dark_orange = discord.Color.dark_orange()

    color_list = [blue, dark_blue, purple, dark_purple, magenta,
                  dark_magenta, orange, dark_orange]
    random_color = random.choice(color_list)
    embed = discord.Embed(title="Info zum {} Server".format(ctx.message.server.name),color=random_color)
    embed.add_field(name="Name", value=ctx.message.server.name)
    embed.add_field(name="Server ID", value="{}".format(ctx.message.server.id))
    embed.add_field(name="User", value="{}".format(len(ctx.message.server.members)))
    embed.add_field(name="Rolen", value='{}'.format(len(ctx.message.server.roles)))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.set_footer(
        text="Gefragt von {}".format(ctx.message.author.name) + "#{}".format(ctx.message.author.discriminator),
        icon_url='{}'.format(ctx.message.author.avatar_url))
    await bot.say(embed=embed)


# Moderation
# Ban
# @bot.command(pass_context=True )
# async def ban(ctx, member: discord.Member=None):
#   if not member:
#       embed = discord.Embed(
#           colour = discord.Colour.red()
#       )
#       embed.add_field(name=':x: Fehler!', value='Bitte wähle einen User aus!')
#       await bot.say(embed=embed)
#       return
#   if not ctx.message.author.server_permissions.administrator:
#       embed = discord.Embed(
#           colour = discord.Colour.red()
#       )
#       embed.add_field(name=":x: Fehler!", value="Du hast nicht Berechtigt das zu tun!",inline=True )
#       await bot.say(embed=embed)
#   if ctx.message.author.server_permissions.administrator:
#       await bot.ban(member)
#       embed = discord.Embed(
#           colour = discord.Colour.red()
#       )
#       embed.set_author(name='User gebannt!')
#       embed.add_field(name='Gebannt von', value=ctx.message.author,inline=False)
#       embed.add_field(name='User', value=member.mention, inline=False)
#       await bot.delete_message(ctx.message)
#       await bot.say(embed=embed)

# Kick
# @bot.command(pass_context=True )
# async def kick(ctx, member: discord.Member=None):
#   if not member:
#       embed = discord.Embed(
#           colour = discord.Colour.red()
#       )
#       embed.add_field(name=":x: Fehler!", value="Bitte wähle einen User aus!",inline=True )
#       await bot.say(embed=embed)
#       return
#   if not ctx.message.author.server_permissions.administrator:
#       embed = discord.Embed(
#           colour = discord.Colour.red()
#       )
#       embed.add_field(name=":x: Fehler!", value="Du hast nicht Berechtigt das zu tun!",inline=True )
#       await bot.say(embed=embed)
#   if ctx.message.author.server_permissions.administrator:
#       await bot.kick(member)
#       embed = discord.Embed(
#           colour = discord.Colour.red()
#       )
#       embed.set_author(name='User gekickt!')
#       embed.add_field(name='Gekickt von', value="@{}".format(ctx.message.author),inline=False)
#       embed.add_field(name='User', value=member.mention, inline=False)
#       await bot.delete_message(ctx.message)
#       await bot.say(embed=embed)


# Ideen Command

@bot.command(pass_context=True)
async def idee(ctx, arg1, *args):
    blue = discord.Color.blue()
    dark_blue = discord.Color.dark_blue()
    purple = discord.Color.purple()
    dark_purple = discord.Color.dark_purple()
    magenta = discord.Color.magenta()
    dark_magenta = discord.Color.dark_magenta()
    orange = discord.Color.orange()
    dark_orange = discord.Color.dark_orange()

    color_list = [blue, dark_blue, purple, dark_purple, magenta,
                  dark_magenta, orange, dark_orange]
    random_color = random.choice(color_list)
    channel = bot.get_channel("547409354123640843")
    output1 = ''
    for word in arg1:
        output1 += word
        output1 += ''
    output2 = ' '
    for word in args:
        output2 += word
        output2 += ' '

    emoji1 = "\U0001F44D"
    emoji2 = "\U0001F44E"

    embed = discord.Embed(color=random_color)
    embed.set_author(name="Neuer Vorschlag: {}".format(output1))
    embed.add_field(name="Beschreibung:", value="{}".format(output2), inline=False)
    embed.set_footer(text='Idee vorgeschlagen von {}'.format(ctx.message.author),
                     icon_url='{}'.format(ctx.message.author.avatar_url))

    await bot.delete_message(ctx.message)
    msg = await bot.send_message(channel, embed=embed)
    await bot.add_reaction(msg, emoji1)
    await bot.add_reaction(msg, emoji2)


# Umfragen Command
@bot.command(pass_context=True)
async def umfrage(ctx, *args):
    if not ctx.message.author.server_permissions.administrator:
        embed = discord.Embed(
            colour=discord.Colour.red()
        )
        embed.add_field(name=":x: Fehler!", value="Du hast nicht Berechtigt das zu tun!", inline=True)
        await bot.say(embed=embed)
    if ctx.message.author.server_permissions.administrator:
        #   channel = bot.get_channel("547410165100576768")
        output = ' '
        for word in args:
            output += word
            output += ' '

        emoji1 = "\u2705"  # "\u2714"
        emoji2 = "\u274C"  # "\u274E" #"\u2716"
        embed = discord.Embed(color=0x8c8c00)
        embed.set_author(name="Umfrage")
        embed.add_field(name="Frage:", value=output, inline=True)
        embed.set_footer(text='Umfrage erstellt von {}'.format(ctx.message.author),
                         icon_url='{}'.format(ctx.message.author.avatar_url))
        await bot.delete_message(ctx.message)
        msg = await bot.say(embed=embed)
        await bot.add_reaction(msg, emoji1)
        await bot.add_reaction(msg, emoji2)


# logout Command
@bot.command(pass_context=True)
async def logout(ctx):
    if ctx.message.author.id == "393423879126646785":
        await bot.delete_message(ctx.message)
        print("Bot wurde heruntergefahren")
        await bot.logout()
    else:
        await bot.say('Hey! Du bist nicht dafür Autorisiert das zu tun!')
        return


# Embed Command
@bot.command(pass_context=True)
async def embed(ctx, *args):
    output = ""
    for word in args:
        output += word
        output += " "
    embed = discord.Embed(color=ctx.message.author.color, description=output)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    await bot.delete_message(ctx.message)
    await bot.say(embed=embed)


# Münzen Command
@bot.command(pass_context=True)
async def münze(ctx):
    user = ctx.message.author
    KZ = ["Kopf", "Zahl"]
    C_KZ = random.choice(KZ)
    RN = [":zero:", ":one:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:", ":keycap_ten:"]
    C_RN = random.choice(RN)
    text1 = "{} wirft eine Münze".format(user)
    text2 = "Sie ist in der Luft"
    if C_KZ == "Zahl":
        text3 = "Kopf :bust_in_silhouette:"
    if C_KZ == "Kopf":
        text3 = "Zahl {}".format(C_RN)
    channel = ctx.message.channel
    msg = await bot.send_message(channel, text1)
    await asyncio.sleep(1, 5)
    await bot.edit_message(msg, text2)
    await asyncio.sleep(1, 5)
    await bot.edit_message(msg, text3)


# Invite Command
@bot.command(pass_context=True)
async def invite(ctx):
    invite = "https://discordapp.com/api/oauth2/authorize?client_id=571339716243488788&permissions=8&scope=bot"
    text = "Hol dir den **Tryde** Bot auch auf deinem Server! \n \n{}".format(invite)
    author = ctx.message.author
    channel = ctx.message.channel
    msg = await bot.send_message(author, text)
    await bot.say("Checke deine Privat Nachrichten :envelope:")

#emolets Command
@bot.command(pass_context=True)
async def emolets(ctx, *, message: str):
    text = message
    text_split = text.split()
    text_split_finish1 = len(text_split)
    text_split2 = ''.join(text_split)
    text_split_finish2 = len(text_split2)
    value1 = 0
    ri = ""
    while value1 < text_split_finish2:
        x = text[value1]
        value1 += 1
        r_i = ':regional_indicator_{}:'.format(x)
        ri += r_i
    await bot.say(ri)


# Global/Tryde Chat
@bot.command(aliases=["tchat"],pass_context=True )
async def gchat(ctx, *args):
    n=""
    for word in args:
        n += word
        n+= ""
    text = n
    text_split = text.split()
    text_split_finish1=len(text_split)
    text_split2 = ''.join(text_split)
    text_split_finish2=len(text_split2)
    if text_split_finish2>0:
        sm_in_arg_var=True
    if text_split_finish2==0:
        sm_in_arg_var=False
    if sm_in_arg_var==False:
        embed = discord.Embed(
            colour = discord.Colour.red()
        )
        embed.add_field(name=':x: **Fehler**! :', value="Du musst eine Nachricht schreiben\n[z.B.: `+gchat Hi`]", inline=True )
        embed.set_footer(text='Bitte versuche es erneut.')
        await bot.say(embed=embed)

    server = discord.utils.get(bot.servers)
    x = datetime.datetime.now()
    time = x.strftime("%I:%M")
    all_server_channel = discord.utils.get(server.channels, name="tryde-chat")
    server_channel = discord.utils.get(ctx.message.server.channels, name="tryde-chat")

    if server_channel == None and sm_in_arg_var==True :
        embed = discord.Embed(
            colour = discord.Colour.red()
        )
        embed.add_field(name=':x: **Fehler**!:', value="Der Channel `tryde-chat` existiert nicht!", inline=True )
        embed.set_footer(text='Bitte versuche es erneut.')
        await bot.say(embed=embed)
        #tryde_channel_create()

    if server_channel == server_channel and sm_in_arg_var == True:
        embed=discord.Embed(title="Tryde Chat", color=0x737373)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.add_field(name="Name des User:", value=ctx.message.author, inline=False )
        embed.add_field(name="Gesendet vom Server:", value=ctx.message.server, inline=False )
        embed.add_field(name="Nachricht:", value=n, inline=False )
        embed.set_footer(text=time)
        await bot.send_message(all_server_channel, embed=embed)
        await bot.send_message(server_channel, embed=embed)
        await bot.delete_message(ctx.message)

# CodeUpdate
@bot.command(pass_context=True)
async def CU(ctx):
    if ctx.message.author.id == "393423879126646785":
        DoktorReeperk = "191600452712792065"
        user = get(bot.get_all_members(), id=DoktorReeperk)
        if user:
            text = "Hey <@191600452712792065> !\nEs gibt eine neue Version des Tryde Bots :tada:\nSchau sie dir an :\nhttps://www.dropbox.com/s/iqxapq2d4ryq0ft/trydebot.py?dl=0"
            msg = await bot.send_message(user, text)
            await bot.say("Update erfolgreich abgeschickt !")
    else:
        await bot.say('Hey! Du bist nicht dafür Autorisiert das zu tun!')
        return


# Version Command
@bot.command(pass_context=True)
async def version(ctx):
    if ctx.message.author.id == "393423879126646785":
        await bot.delete_message(ctx.message)
        msg = await bot.say("Bot version : `1.3.9`")
        await asyncio.sleep(5)
        await bot.delete_message(msg)
    else:
        await bot.say('Hey! Du bist nicht dafür Autorisiert das zu tun!')
        return

@bot.command(pass_context=True)
async def botinfo(ctx):
    ping = random.randint(1, 100)
    servercounter = len(bot.servers)
    blue = discord.Color.blue()
    dark_blue = discord.Color.dark_blue()
    purple = discord.Color.purple()
    dark_purple = discord.Color.dark_purple()
    magenta = discord.Color.magenta()
    dark_magenta = discord.Color.dark_magenta()
    orange = discord.Color.orange()
    dark_orange = discord.Color.dark_orange()

    color_list = [blue, dark_blue, purple, dark_purple, magenta,
                  dark_magenta, orange, dark_orange]
    random_color = random.choice(color_list)
    server = ctx.message.server

    if server.name == "Bot Testing Server" or server.name == "Tryde Bot Development":
        embed = discord.Embed(title="<:tryde_icon:571635965102391316> Bot-Infos", color=random_color,
                              description="Libary : **discord.py** \nPing : **{} ms** \nPrefix : **+** \nServer : {}\nWebsite : /\nDiscord : https://discord.gg/7Degfu5\nInvite : https://discordapp.com/api/oauth2/authorize?client_id=571339716243488788&permissions=8&scope=bot".format(ping, servercounter))
        embed.set_footer(text="Bot programmiert von @Desaw.Lennard#1833")
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Bot-Infos", color=random_color,
                              description="Libary : **discord.py** \nPing : **{} ms** \nPrefix : **+** \nServer : {}\nWebsite : /\nDiscord : https://discord.gg/7Degfu5\nInvite : https://discordapp.com/api/oauth2/authorize?client_id=571339716243488788&permissions=8&scope=bot".format(ping, servercounter))
        embed.set_footer(text="Bot programmiert von @Desaw.Lennard#1833")
        await bot.say(embed=embed)


# 8ball
@bot.command(aliases=["8ball"])
async def eightball():
    answer_list = ["Ja", "Nein", "Ja, wenn du es willst",
                   "Nein ... ich meine ja ... Nun ... Bitte fragen sie später nochmal...",
                   "Die Antwort ist unklar ... Ernsthaft habe ich das doppelt Überprüft", "Ich habe gewonnen",
                   "Tut mir leid das habe ich nicht verstanden", "Es ist wirklich ein Münzwurf ... ",
                   "Ja, das wird er ... Tut mir Leid, ich habe nicht wirklich zugehört ",
                   "Ich könnte es Ihnen sagen, aber sie müssen mir was dafür bieten ",
                   "Ja, nein, vielleicht ... ich weiß nicht, könnten Sie die Frage wiederholen? ",
                   "Wenn Sie denken, dass ich das beantworte, verwechseln Sie mich eindeutig mit jemand anderen",
                   "Willst du wirklich, dass ich das beantworte? OK ... Vielleicht",
                   "Ja...Nein...Ja...Nein...Ja...Nein... ok ich weiß es nicht",
                   "Stellen Sie sich diese Frage dreimal im Spiegel, dann wird ihnen die Antwort klar",
                   "Sie wollen eine Antwort? OK, hier ist deine Antwort : /"]
    blue = discord.Color.blue()
    dark_blue = discord.Color.dark_blue()
    purple = discord.Color.purple()
    dark_purple = discord.Color.dark_purple()
    magenta = discord.Color.magenta()
    dark_magenta = discord.Color.dark_magenta()
    orange = discord.Color.orange()
    dark_orange = discord.Color.dark_orange()

    color_list = [blue, dark_blue, purple, dark_purple, magenta,
                  dark_magenta, orange, dark_orange]
    random_color = random.choice(color_list)
    answer = random.choice(answer_list)
    embed = discord.Embed(color=random_color, description=answer)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def guilds(ctx):
    blue = discord.Color.blue()
    dark_blue = discord.Color.dark_blue()
    purple = discord.Color.purple()
    dark_purple = discord.Color.dark_purple()
    magenta = discord.Color.magenta()
    dark_magenta = discord.Color.dark_magenta()
    orange = discord.Color.orange()
    dark_orange = discord.Color.dark_orange()

    color_list = [blue, dark_blue, purple, dark_purple, magenta,
                  dark_magenta, orange, dark_orange]
    random_color = random.choice(color_list)
    server = ""
    for s in bot.servers:
        server += "- %s (%s)\n" % (s.name, s.id)

    embed = discord.Embed(color=random_color, description=server)
    await bot.say(embed=embed)



# Command nicht im Betrieb
@bot.command()
async def kick():
    embed = discord.Embed(
        colour=discord.Colour.red()
    )

    embed.add_field(name='**Fehler**!:', value="Tut mir leid doch der Command funktioniert im Moment nicht",
                    inline=True)

    embed.set_footer(text='Bitte versuche es erneut.')

    await bot.say(embed=embed)


@bot.command()
async def ban():
    embed = discord.Embed(
        colour=discord.Colour.red()
    )

    embed.add_field(name='**Fehler**!:', value="Tut mir leid doch der Command funktioniert im Moment nicht",
                    inline=True)

    embed.set_footer(text='Bitte versuche es erneut.')

    await bot.say(embed=embed)

#Musik
player_dict = dict()

@bot.command(pass_context=True)
async def play(ctx, url):
    await bot.say("Suche Lied :mag_right:")
    channel=ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)
    server = ctx.message.server
    voice = bot.voice_client_in(server)
    player = await voice.create_ytdl_player(url)
    player_dict[server.id]=player
    await bot.say("Spiele nun `%s` ab :notes:" % player.title)
    player.start()

@bot.command(pass_context=True)
async def stop(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    await bot.say("`%s` wurde beendet :stop_button:" % player.title)
    player.stop()
    del player_dict[server.id]

@bot.command(pass_context=True)
async def pause(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.pause()
    await bot.send_message(ctx.message.channel, "`%s` wurde pausiert :pause_button:" % player.title)


@bot.command(pass_context=True)
async def resume(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.resume()
    await bot.send_message(ctx.message.channel, "`%s` wird fortgesetzt :arrow_forward:" % player.title)


@bot.command(pass_context=True)
async def volume(ctx, sound_volume=None):
    server = ctx.message.server
    player = player_dict[server.id]
    if sound_volume is None:
        await bot.send_message(ctx.message.channel, "Lautstärke ist auf **{}%** eingestellt".format(player.volume * 100))
    else:
        if sound_volume.isnumeric():
            player.volume = int(sound_volume) / 100
        elif sound_volume == "-":
            player.volume = player.volume - 0.05
        elif sound_volume == "+":
            player.volume = player.volume + 0.05
        await bot.send_message(ctx.message.channel, "Lautstärke wurde auf **{}%** eingestellt".format(player.volume * 100))




bot.run(TOKEN)
