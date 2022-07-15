import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord import Member
from discord.ext.commands import MissingPermissions
from discord.ext.commands import CommandNotFound
from urllib.request import urlopen, Request
from covid import Covid
import datetime
import asyncio
from urllib import parse, request
import requests
import re
import random
import string
import os
import aiohttp
import sys
import traceback
import smtplib
import ssl
from bs4 import BeautifulSoup
import json
import wikipedia

intents = discord.Intents.default()  
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("w!", "W!"), description="Wersef", intents=intents)

TOKEN = "ODE5NzQzMzU1NjYzNTQ4NDQ3.YErDfg.NQJNCdgMV3JEVUcsmYXBeDg7q3A"
bot.remove_command("help")

bot_adı = "Wersef"
bot_id = "819743355663548447"
prefix = "w!"
bot_avatar = "https://cdn.discordapp.com/avatars/819743355663548447/93b04f1275bc6f1b9c5fcac9dd97802f.webp?size=1024"
bot_yapımcısı = "Weyaxi"
destek_sunucusu = "https://discord.gg/ewGpWsx454"
önerilen_yetki_davet = "https://discord.com/oauth2/authorize?client_id=819743355663548447&permissions=415244438&scope=bot"
discord_iletişim = "Weyaxi#0001"
telegram_iletişim = "SS_w_o_R_d"

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'*+,-./<=>?@\_`|~"
number = int(1)
lenght = int(10)

@bot.event
async def on_ready():
    channel = bot.get_channel(848198926830141480)

    print('-------------------------')
    print(f'Logged in as {bot_adı}')
    print(f'Discord Versiyonu {discord.__version__}')
    print('-------------------------')
    await channel.send(f' ```python\n------------------------- \n Logged in as {bot_adı} \n Discord Versiyonu {discord.__version__} \n-------------------------``` ')

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"w!yardım"))                              


@bot.event
async def on_command_error(ctx, error):
    channel = bot.get_channel(848198926830141480)

    if isinstance(error, CommandNotFound):
        await ctx.send(f'Komut bulunamadı. Eğer böyle bir komutun olduğunu gerçekten düşünüyorsanız lütfen yapımcım ile iritibata geçiniz.')
        print(f'{ctx.invoked_with} Adlı Komut Bulunamadı ({str(ctx.author)} Tarafından Kullanıldı)')
        await channel.send(f' ```{ctx.invoked_with} Adlı Komut Bulunamadı ({str(ctx.author)} Tarafından Kullanıldı)``` ')
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        await channel.send('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)      


@bot.event
async def on_guild_join(guild):
    channel = bot.get_channel(841766204284469298)
    id = str(guild.id)

    embed = discord.Embed(title="<:nametag:841951946650812426> │ Eklenen Sunucu", description=f"{guild.name}", color=0xff8800)
    embed.add_field(name="🆔 │ Sunucu ID'si", value=id, inline=False)
    embed.add_field(name="👤 │ Sunucu Sahibi", value=f"<@!{guild.owner_id}>", inline=False)

    await channel.send(embed=embed)


@bot.event
async def on_guild_remove(guild):
    channel = bot.get_channel(841766204284469298)
    id = str(guild.id)

    embed = discord.Embed(title="<:nametag:841951946650812426> │ Atılan Sunucu", description=f"{guild.name}", color=0xff0000)
    embed.add_field(name="🆔 │ Sunucu ID'si", value=id, inline=False)
    embed.add_field(name="👤 │ Sunucu Sahibi", value=f"<@!{guild.owner_id}>", inline=False)

    await channel.send(embed=embed)      


@bot.command(aliases=['yardım'])
async def help(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    embed = discord.Embed(
        title=f"▬▬▬▬▬▬[ :dizzy: {bot_adı} :dizzy: ]▬▬▬▬▬▬   ",
        description=f"> <:maviok:843149816401100832> **Prefix:** {prefix} \n > _ _ \n > <:maviok:843149816401100832> **Botun Destek Sunucusu:** [Tıkla]({destek_sunucusu}) \n > _ _ \n > <:maviok:843149816401100832> **Botun Davet Bağlantısı:** [Tıkla]({önerilen_yetki_davet})",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Yardım Komutları 🔐  ]▬▬▬▬▬▬", value="> <:yesilok:843149816880037899> **w!moderasyon:** Moderason komutlarını gösterir. \n > _ _ \n > <:yesilok:843149816880037899> **w!kullanıcıkomutları:** Kullanıcı komutlarını size gösterir. \n > _ _ \n > <:yesilok:843149816880037899> **w!sunucukomutları:** Sunucu ile ilgili komutları size sunar. \n > _ _ \n  > <:yesilok:843149816880037899> **w!hesapla:** Bot hesaplama komutlarını size sunar. \n > _ _ \n > <:yesilok:843149816880037899> **w!eğlence:** Bot eğlence komutlarını sunar. \n > _ _ \n > <:yesilok:843149816880037899> **w!işeyarar:** Bot, işe yarar komutları size sunar. \n > _ _ \n > <:yesilok:843149816880037899> **w!bothakkında:** Bot hakkındaki komutları gösterir. (Bakmanız Önerilir) ", inline=False)
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **<:pembeok:843149816724848710> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:843149816724848710> Botun Yazıldığı Dil:** **`Python`**", inline=False)


    await ctx.send(embed=embed)        

@bot.command()
async def ping(ctx):
    description = str(ctx.guild.description)
    embed = discord.Embed(title="", description=f"", color=0x00ff33)
    embed.add_field(name=f":hourglass: {round(bot.latency * 1000)} ms", value="\n\u200b", inline=False)
    embed.add_field(name=f":hourglass: {round(bot.latency * 1000)} ms", value="\n\u200b", inline=False)
    embed.add_field(name=f":hourglass: {round(bot.latency * 1000)} ms", value="\n\u200b", inline=False)

    await ctx.send(embed=embed)

  
@bot.command()
async def wersefdavet(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="Botun Davet Linkleri", description=f"<:kral:830058307351478282> **Gerekli İzinlerle (Önerilen):** ➠ [Tıkla]({önerilen_yetki_davet}) \n <:kral:830058307351478282> **Bütün İzinlerle (Önerilen):** ➠ [Tıkla](https://discord.com/api/oauth2/authorize?client_id={bot_id}&permissions=4294967287&scope=bot) \n <:kral:830058307351478282> **Yönetici İzinleriyle (Bazı Komutlar Çalışmayabilir):** ➠ [Tıkla](https://discord.com/oauth2/authorize?client_id={bot_id}&permissions=8&scope=bot) \n <:robo:833610842410450964> **Yetkisiz Şekilde (Önerilmez):** ➠ [Tıkla](https://discord.com/oauth2/authorize?client_id={bot_id}&permissions=0&scope=bot) ", color=0x14ffd8)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    
    await ctx.send(embed=embed)


@bot.command(pass_context=True, aliases=['roller', 'sunucurolleri'])
async def roles(ctx):
        guild = ctx.guild
        roles = [role for role in guild.roles if role != ctx.guild.default_role]
        roles.reverse()
        embed = discord.Embed(title="", description=f"\n \n".join([role.mention for role in roles]), color=0x14ffd8)
        await ctx.send(embed=embed)



@commands.has_permissions(administrator=True)
@bot.command()
async def sunucukur3(ctx):
    guild = ctx.guild
    owner = ctx.guild.owner
    
    await guild.create_role(name="─────Üst Yönetim─────", color=14988288)   
    role1 = await guild.create_role(name="🛡️│Admin", color=16711680) 
    role2 = await guild.create_role(name="👑│Sunucu Kurucusu", color=15105570) 
    await guild.create_role(name="──────Yönetim──────", color=14988288) 
    role3 = await guild.create_role(name="👑│Moderatör", color=15105570) 
    role4 = await guild.create_role(name="👮‍♂️│Denetmen", color=19905) 
    await guild.create_role(name="──────Botlar──────", color=14988288) 
    await guild.create_role(name="BOT", color=2116844) 
    await guild.create_role(name="BOT", color=2116844) 
    await guild.create_role(name="BOT", color=2116844)
    await guild.create_role(name="BOT", color=2116844)
    await guild.create_role(name="BOT", color=2116844) 

    await asyncio.sleep(1)

    await guild.create_role(name="──────Özel──────", color=14988288) 
    role = await guild.create_role(name="🔐│VİP", color=15105570)
    await guild.create_role(name="👲│Sunucu Takviyecisi", color=16711863) 
    await guild.create_role(name="──────Diğer──────", color=14988288) 
    await guild.create_role(name="🎧│Müziksever", color=3447003) 
    await guild.create_role(name="🎮│Oyuncu", color=15105570) 
    await guild.create_role(name="──────Bot Rolleri──────", color=14988288) 
    await guild.create_role(name="🤖│Özel Bot", color=2116844) 
    await guild.create_role(name="🤖│Botçuk", color=2116844) 
    await guild.create_role(name="──────Discord──────", color=14988288) 

    for c in ctx.guild.channels:
        await c.delete()
    for category in ctx.guild.categories:
        await category.delete()  

    await asyncio.sleep(1)

    category9 = await guild.create_category('☞Yönetici Kategorisi ☜')    
    await category9.create_text_channel('「💬」yönetim-sohbet')  
    await category9.create_text_channel('「🤖」yönetim-bot-komut')    
    await category9.create_voice_channel('「📁」Yönetim Odası¹') 
    await category9.create_voice_channel('「📁」Yönetim Odası²')
    await category9.create_voice_channel('「📁」Yönetim Odası³')

    await category9.set_permissions(role1, read_messages=True, send_messages=True, connect=True, speak=True)
    await category9.set_permissions(role2, read_messages=True, send_messages=True, connect=True, speak=True)
    await category9.set_permissions(role3, read_messages=True, send_messages=True, connect=True, speak=True)
    await category9.set_permissions(role4, read_messages=True, send_messages=True, connect=True, speak=True)
    await category9.set_permissions(ctx.guild.self_role, read_messages=True, send_messages=True)
    await category9.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)

    await asyncio.sleep(1)

    category1 = await guild.create_category('☞ Bilgi Kategorisi ☜')    
    await category1.create_text_channel('「📖」kurallar')    
    await category1.create_text_channel('「📜」hakkında')    
    await category1.create_text_channel('「📢」duyuru')    
    await category1.create_text_channel('「📡」giriş-çıkış')
    await category1.create_text_channel('「🔖」seviye')

    await asyncio.sleep(1)

    category2 = await guild.create_category('☞ Genel Kategori ☜')    
    await category2.create_text_channel('「💬」sohbet')    
    await category2.create_text_channel('「🎨」görsel')    
    await category2.create_text_channel('「🎥」video')
    await category2.create_text_channel('「👻」gif')
    await category2.create_text_channel('「🤖」bot-komut') 
    await category2.create_text_channel('「✅」öneri') 

    await asyncio.sleep(1) 

    category10 = await guild.create_category('☞ Eğlence Kategorisi ☜')    
    await category10.create_text_channel('「😜」meme')    
    await category10.create_text_channel('「😜」espri')    
    await category10.create_text_channel('「🎉」spam-kanalı')  

    await asyncio.sleep(1)

    category3 = await guild.create_category('☞ Genel Ses Kategorisi ☜')    
    await category3.create_voice_channel('「🎙」 Sohbet¹')    
    await category3.create_voice_channel('「🎙」 Sohbet²')
    await category3.create_voice_channel('「🎙」 Sohbet³')
    await category3.create_voice_channel('「🎙」 Sohbet⁴')
    await category3.create_voice_channel('「🎙」 Sohbet⁵')

    await asyncio.sleep(1)

    category4 = await guild.create_category('☞ Özel Ses Kategorisi ☜')    
    await category4.create_voice_channel(name='「🔐」 2 Kişilik Oda', user_limit=2)  
    await category4.create_voice_channel(name='「🔐」 2 Kişilik Oda', user_limit=2)  
    await category4.create_voice_channel(name='「🔐」 4 Kişilik Oda', user_limit=4)  
    await category4.create_voice_channel(name='「🔐」 4 Kişilik Oda', user_limit=4)  
    await category4.create_voice_channel(name='「🔐」 6 Kişilik Oda', user_limit=6)  
    await category4.create_voice_channel(name='「🔐」 6 Kişilik Oda', user_limit=6)  

    await asyncio.sleep(1)

    category7 = await guild.create_category('☞ AFK Kategorisi ☜')    
    await category7.create_voice_channel(name='「🔉」 AFK¹') 
    await category7.create_voice_channel(name='「🔉」 AFK²') 
    await category7.create_voice_channel(name='「🔉」 AFK³') 
    await category7.create_voice_channel(name='「🔉」 AFK⁴') 
    await category7.create_voice_channel(name='「🔉」 AFK⁵')  

    await asyncio.sleep(1)

    category5 = await guild.create_category('☞ Müzik Kategorisi ☜')    
    await category5.create_text_channel('「🎵」müzik-öneri')    
    await category5.create_text_channel('「🎵」müzik-komut')    
    await category5.create_voice_channel('「🎵」 Müzik Odası¹')
    await category5.create_voice_channel('「🎵」 Müzik Odası²')
    await category5.create_voice_channel('「🎵」 Müzik Odası³')

    await asyncio.sleep(1)

    category6 = await guild.create_category('☞ Oyun Kategorisi ☜')    
    await category6.create_text_channel('「🎮」sohbet')       
    await category6.create_voice_channel('「🎮」Oyun Odası¹')
    await category6.create_voice_channel('「🎮」Oyun Odası²')
    await category6.create_voice_channel('「🎮」Oyun Odası³')
    await category6.create_voice_channel('「🎮」Oyun Odası⁴')
    await category6.create_voice_channel('「🎮」Oyun Odası⁵')

    await asyncio.sleep(1)

    category8 = await guild.create_category('☞VİP Kategorisi ☜')    
    await category8.create_text_channel('「🔐」vip-sohbet')  
    await category8.create_text_channel('「🔐」vip-bot-komut')    
    await category8.create_voice_channel('「🔐」VİP Odası¹') 
    await category8.create_voice_channel('「🔐」VİP Odası²')
    await category8.create_voice_channel('「🔐」VİP Odası³')

    await category8.set_permissions(role, read_messages=True, send_messages=True, connect=True, speak=True)
    await category8.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False, connect=False)
    await category8.set_permissions(ctx.guild.self_role, read_messages=True, send_messages=True)

    await asyncio.sleep(1)

    embed = discord.Embed(title=":warning: Önemli Uyarı", description=f"Merhabalar, yakın zamanda {ctx.guild.name} adlı sunucunuzda sunucukur komutu kullanılldı. Eğer bunu yapan siz değilseniz veya bu olay hakkında bilgi sahibi değilseniz, lütfen bir dahaki sefere gerekli önlemleri alınız.", color=0xff0000)
    embed.add_field(name=":warning: Yapan Kişi", value=f"<@!{ctx.author.id}>", inline=False)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await owner.send(embed=embed)    

@sunucukur3.error
async def sunucukur3_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")      


@commands.has_permissions(administrator=True)
@bot.command()
async def sunucukur2(ctx):
    guild = ctx.guild
    owner = ctx.guild.owner

    await guild.create_role(name="─────Üst Yönetim─────", color=14988288)   
    role1 = await guild.create_role(name="🛡️│Admin", color=16711680) 
    role2 = await guild.create_role(name="👑│Sunucu Kurucusu", color=15105570) 
    await guild.create_role(name="──────Yönetim──────", color=14988288) 
    role3 = await guild.create_role(name="👑│Moderatör", color=15105570) 
    role4 = await guild.create_role(name="👮‍♂️│Denetmen", color=19905) 
    await guild.create_role(name="──────Botlar──────", color=14988288) 
    await guild.create_role(name="BOT", color=2116844) 
    await guild.create_role(name="BOT", color=2116844) 
    await guild.create_role(name="BOT", color=2116844)
    await guild.create_role(name="BOT", color=2116844)
    await guild.create_role(name="BOT", color=2116844) 

    await asyncio.sleep(1)

    await guild.create_role(name="──────Özel──────", color=14988288) 
    role = await guild.create_role(name="🔐│VİP", color=15105570)
    await guild.create_role(name="👲│Sunucu Takviyecisi", color=16711863) 
    await guild.create_role(name="──────Diğer──────", color=14988288) 
    await guild.create_role(name="🎧│Müziksever", color=3447003) 
    await guild.create_role(name="🎮│Oyuncu", color=15105570) 
    await guild.create_role(name="──────Bot Rolleri──────", color=14988288) 
    await guild.create_role(name="🤖│Özel Bot", color=2116844) 
    await guild.create_role(name="🤖│Botçuk", color=2116844) 
    await guild.create_role(name="──────Discord──────", color=14988288) 

    for c in ctx.guild.channels:
        await c.delete()
    for category in ctx.guild.categories:
        await category.delete()  

    await asyncio.sleep(1)

    category9 = await guild.create_category('☞Yönetici Kategorisi ☜')    
    await category9.create_text_channel('💬│yönetim-sohbet')  
    await category9.create_text_channel('🤖│yönetim-bot-komut')    
    await category9.create_voice_channel('📁│Yönetim Odası¹') 
    await category9.create_voice_channel('📁│Yönetim Odası²')
    await category9.create_voice_channel('📁│Yönetim Odası³')

    await category9.set_permissions(role1, read_messages=True, send_messages=True, connect=True, speak=True)
    await category9.set_permissions(role2, read_messages=True, send_messages=True, connect=True, speak=True)
    await category9.set_permissions(role3, read_messages=True, send_messages=True, connect=True, speak=True)
    await category9.set_permissions(role4, read_messages=True, send_messages=True, connect=True, speak=True)
    await category9.set_permissions(ctx.guild.self_role, read_messages=True, send_messages=True)
    await category9.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)

    await asyncio.sleep(1)

    category1 = await guild.create_category('☞ Bilgi Kategorisi ☜')    
    await category1.create_text_channel('📖│kurallar')    
    await category1.create_text_channel('📜│hakkında')    
    await category1.create_text_channel('📢│duyuru')    
    await category1.create_text_channel('📡│giriş-çıkış')
    await category1.create_text_channel('🔖│seviye')
    
    await asyncio.sleep(1)

    category2 = await guild.create_category('☞ Genel Kategori ☜')    
    await category2.create_text_channel('💬│sohbet')    
    await category2.create_text_channel('🎨│görsel')    
    await category2.create_text_channel('🎥│video')
    await category2.create_text_channel('👻│gif')
    await category2.create_text_channel('🤖│bot-komut') 
    await category2.create_text_channel('✅│öneri') 

    await asyncio.sleep(1)
    
    category10 = await guild.create_category('☞ Eğlence Kategorisi ☜')    
    await category10.create_text_channel('😜│meme')    
    await category10.create_text_channel('😜│espri')    
    await category10.create_text_channel('🎉│spam-kanalı')

    await asyncio.sleep(1)    

    category3 = await guild.create_category('☞ Genel Ses Kategorisi ☜')    
    await category3.create_voice_channel('🎙│ Sohbet¹')    
    await category3.create_voice_channel('🎙│ Sohbet²')
    await category3.create_voice_channel('🎙│ Sohbet³')
    await category3.create_voice_channel('🎙│ Sohbet⁴')
    await category3.create_voice_channel('🎙│ Sohbet⁵')

    await asyncio.sleep(1)

    category4 = await guild.create_category('☞ Özel Ses Kategorisi ☜')    
    await category4.create_voice_channel(name='🔐 │ 2 Kişilik Oda', user_limit=2)  
    await category4.create_voice_channel(name='🔐 │ 2 Kişilik Oda', user_limit=2)  
    await category4.create_voice_channel(name='🔐 │ 4 Kişilik Oda', user_limit=4)  
    await category4.create_voice_channel(name='🔐 │ 4 Kişilik Oda', user_limit=4)  
    await category4.create_voice_channel(name='🔐 │ 6 Kişilik Oda', user_limit=6)  
    await category4.create_voice_channel(name='🔐 │ 6 Kişilik Oda', user_limit=6)  

    await asyncio.sleep(1)

    category7 = await guild.create_category('☞ AFK Kategorisi ☜')    
    await category7.create_voice_channel(name='🔉 │ AFK¹') 
    await category7.create_voice_channel(name='🔉 │ AFK²') 
    await category7.create_voice_channel(name='🔉 │ AFK³') 
    await category7.create_voice_channel(name='🔉 │ AFK⁴') 
    await category7.create_voice_channel(name='🔉 │ AFK⁵')  

    await asyncio.sleep(1)

    category5 = await guild.create_category('☞ Müzik Kategorisi ☜')    
    await category5.create_text_channel('🎵│müzik-öneri')    
    await category5.create_text_channel('🎵│müzik-komut')    
    await category5.create_voice_channel('🎵 │ Müzik Odası¹')
    await category5.create_voice_channel('🎵 │ Müzik Odası²')
    await category5.create_voice_channel('🎵 │ Müzik Odası³')
    
    await asyncio.sleep(1)

    category6 = await guild.create_category('☞ Oyun Kategorisi ☜')    
    await category6.create_text_channel('🎮│sohbet')       
    await category6.create_voice_channel('🎮│Oyun Odası¹')
    await category6.create_voice_channel('🎮│Oyun Odası²')
    await category6.create_voice_channel('🎮│Oyun Odası³')
    await category6.create_voice_channel('🎮│Oyun Odası⁴')
    await category6.create_voice_channel('🎮│Oyun Odası⁵')

    await asyncio.sleep(1)

    category8 = await guild.create_category('☞ VİP Kategorisi ☜')    
    await category8.create_text_channel('🔐│vip-sohbet')  
    await category8.create_text_channel('🔐│vip-bot-komut')    
    await category8.create_voice_channel('🔐│VİP Odası¹') 
    await category8.create_voice_channel('🔐│VİP Odası²')
    await category8.create_voice_channel('🔐│VİP Odası³')

    await category8.set_permissions(role, read_messages=True, send_messages=True, connect=True, speak=True)
    await category8.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False, connect=False)
    await category8.set_permissions(ctx.guild.self_role, read_messages=True, send_messages=True)

    await asyncio.sleep(1)

    embed = discord.Embed(title=":warning: Önemli Uyarı", description=f"Merhabalar, yakın zamanda {ctx.guild.name} adlı sunucunuzda sunucukur komutu kullanılldı. Eğer bunu yapan siz değilseniz veya bu olay hakkında bilgi sahibi değilseniz, lütfen bir dahaki sefere gerekli önlemleri alınız.", color=0xff0000)
    embed.add_field(name=":warning: Yapan Kişi", value=f"<@!{ctx.author.id}>", inline=False)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await owner.send(embed=embed)    
    

@sunucukur2.error
async def sunucukur2_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")  

@commands.has_permissions(administrator=True)
@bot.command()
async def sunucukur1(ctx):
    guild = ctx.guild
    owner = ctx.guild.owner
    
    await guild.create_role(name="─────Üst Yönetim─────", color=14988288)   
    role1 = await guild.create_role(name="Admin", color=16711680) 
    role2 = await guild.create_role(name="Sunucu Kurucusu", color=15105570) 
    await guild.create_role(name="──────Yönetim──────", color=14988288) 
    role3 = await guild.create_role(name="Moderatör", color=15105570) 
    role4 = await guild.create_role(name="‍Denetmen", color=19905) 
    await guild.create_role(name="──────Botlar──────", color=14988288) 
    await guild.create_role(name="BOT", color=2116844) 
    await guild.create_role(name="BOT", color=2116844) 
    await guild.create_role(name="BOT", color=2116844)
    await guild.create_role(name="BOT", color=2116844)
    await guild.create_role(name="BOT", color=2116844) 

    await asyncio.sleep(1)

    await guild.create_role(name="──────Özel──────", color=14988288) 
    role = await guild.create_role(name="VİP", color=15105570)
    await guild.create_role(name="Sunucu Takviyecisi", color=16711863) 
    await guild.create_role(name="──────Diğer──────", color=14988288) 
    await guild.create_role(name="Müziksever", color=3447003) 
    await guild.create_role(name="Oyuncu", color=15105570) 
    await guild.create_role(name="──────Bot Rolleri──────", color=14988288) 
    await guild.create_role(name="Özel Bot", color=2116844) 
    await guild.create_role(name="Botçuk", color=2116844) 
    await guild.create_role(name="──────Discord──────", color=14988288) 

    for c in ctx.guild.channels:
        await c.delete()
    for category in ctx.guild.categories:
        await category.delete()  

    await asyncio.sleep(1)

    category9 = await guild.create_category('☞Yönetici Kategorisi ☜')    
    await category9.create_text_channel('yönetim-sohbet')  
    await category9.create_text_channel('yönetim-bot-komut')    
    await category9.create_voice_channel('Yönetim Odası¹') 
    await category9.create_voice_channel('Yönetim Odası²')
    await category9.create_voice_channel('Yönetim Odası³')

    await category9.set_permissions(role1, read_messages=True, send_messages=True, connect=True, speak=True)
    await category9.set_permissions(role2, read_messages=True, send_messages=True, connect=True, speak=True)
    await category9.set_permissions(role3, read_messages=True, send_messages=True, connect=True, speak=True)
    await category9.set_permissions(role4, read_messages=True, send_messages=True, connect=True, speak=True)
    await category9.set_permissions(ctx.guild.self_role, read_messages=True, send_messages=True)
    await category9.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)

    await asyncio.sleep(1)

    category1 = await guild.create_category('☞ Bilgi Kategorisi ☜')    
    await category1.create_text_channel('kurallar')    
    await category1.create_text_channel('hakkında')    
    await category1.create_text_channel('duyuru')    
    await category1.create_text_channel('giriş-çıkış')
    await category1.create_text_channel('seviye')
    
    await asyncio.sleep(1)

    category2 = await guild.create_category('☞ Genel Kategori ☜')    
    await category2.create_text_channel('sohbet')    
    await category2.create_text_channel('görsel')    
    await category2.create_text_channel('video')
    await category2.create_text_channel('gif')
    await category2.create_text_channel('bot-komut') 
    await category2.create_text_channel('öneri') 

    await asyncio.sleep(1)

    category10 = await guild.create_category('☞ Eğlence Kategorisi ☜')    
    await category10.create_text_channel('meme')    
    await category10.create_text_channel('espri')    
    await category10.create_text_channel('spam-kanalı')

    await asyncio.sleep(1)

    category3 = await guild.create_category('☞ Genel Ses Kategorisi ☜')    
    await category3.create_voice_channel('Sohbet¹')    
    await category3.create_voice_channel('Sohbet²')
    await category3.create_voice_channel('Sohbet³')
    await category3.create_voice_channel('Sohbet⁴')
    await category3.create_voice_channel('Sohbet⁵')

    await asyncio.sleep(1)

    category4 = await guild.create_category('☞ Özel Ses Kategorisi ☜')    
    await category4.create_voice_channel(name='2 Kişilik Oda', user_limit=2)  
    await category4.create_voice_channel(name='2 Kişilik Oda', user_limit=2)  
    await category4.create_voice_channel(name='4 Kişilik Oda', user_limit=4)  
    await category4.create_voice_channel(name='4 Kişilik Oda', user_limit=4)  
    await category4.create_voice_channel(name='6 Kişilik Oda', user_limit=6)  
    await category4.create_voice_channel(name='6 Kişilik Oda', user_limit=6)  

    await asyncio.sleep(1)

    category7 = await guild.create_category('☞ AFK Kategorisi ☜')    
    await category7.create_voice_channel(name='AFK¹') 
    await category7.create_voice_channel(name='AFK²') 
    await category7.create_voice_channel(name='AFK³') 
    await category7.create_voice_channel(name='AFK⁴') 
    await category7.create_voice_channel(name='AFK⁵')  

    await asyncio.sleep(1)

    category5 = await guild.create_category('☞ Müzik Kategorisi ☜')    
    await category5.create_text_channel('müzik-öneri')    
    await category5.create_text_channel('müzik-komut')    
    await category5.create_voice_channel('Müzik Odası¹')
    await category5.create_voice_channel('Müzik Odası²')
    await category5.create_voice_channel('Müzik Odası³')
    
    await asyncio.sleep(1)

    category6 = await guild.create_category('☞ Oyun Kategorisi ☜')    
    await category6.create_text_channel('sohbet')       
    await category6.create_voice_channel('Oyun Odası¹')
    await category6.create_voice_channel('Oyun Odası²')
    await category6.create_voice_channel('Oyun Odası³')
    await category6.create_voice_channel('Oyun Odası⁴')
    await category6.create_voice_channel('Oyun Odası⁵')

    await asyncio.sleep(1)

    category8 = await guild.create_category('☞VİP Kategorisi ☜')    
    await category8.create_text_channel('vip-sohbet')  
    await category8.create_text_channel('vip-bot-komut')    
    await category8.create_voice_channel('VİP Odası¹') 
    await category8.create_voice_channel('VİP Odası²')
    await category8.create_voice_channel('VİP Odası³')

    await category8.set_permissions(role, read_messages=True, send_messages=True, connect=True, speak=True)
    await category8.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False, connect=False)
    await category8.set_permissions(ctx.guild.self_role, read_messages=True, send_messages=True)

    await asyncio.sleep(1)

    embed = discord.Embed(title=":warning: Önemli Uyarı", description=f"Merhabalar, yakın zamanda {ctx.guild.name} adlı sunucunuzda sunucukur komutu kullanılldı. Eğer bunu yapan siz değilseniz veya bu olay hakkında bilgi sahibi değilseniz, lütfen bir dahaki sefere gerekli önlemleri alınız.", color=0xff0000)
    embed.add_field(name=":warning: Yapan Kişi", value=f"<@!{ctx.author.id}>", inline=False)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await owner.send(embed=embed)

@sunucukur1.error
async def sunucukur1_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")  


@bot.command()
async def sunucukur(ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Sunucu Kurma Komutu 🔐  ]▬▬▬▬▬▬",
            description="> **<:maviok:837983169579712532> Görünüşe bakılırsa bu komutu yanlış kullanmısınız.** \n > _ _ \n > **<:maviok:837983169579712532> İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:**",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> <:yesilok:771731154159796241> **w!sunucukur** <sayı_birleşik>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> <:yesilok:771731154159796241> **w!sunucukur1:** Sade, renksiz bir sunucu sizin için kurulur. \n > _ _ \n > <:yesilok:771731154159796241> **w!sunucukur2:** Renkli ve modern bir sunucu sizin için kurulur. \n > _ _ \n > <:yesilok:771731154159796241> **w!sunucukur3:** Renkli ve lüks bir sunucu sizin için kurulur. ", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
        
        await ctx.send(embed=embed)   


@commands.has_permissions(administrator=True)
@bot.command()
async def sunucuyutemizle(ctx):
    guild = ctx.guild
    owner = ctx.guild.owner

    for c in ctx.guild.channels:
        await c.delete()
    for category in ctx.guild.categories:
        await category.delete()

    await asyncio.sleep(1)

    embed = discord.Embed(title=":warning: Önemli Uyarı", description=f"Merhabalar, yakın zamanda {ctx.guild.name} adlı sunucunuzda sunucyu temizle komutu kullanılldı. Eğer bunu yapan siz değilseniz veya bu olay hakkında bilgi sahibi değilseniz, lütfen bir dahaki sefere gerekli önlemleri alınız.", color=0xff0000)
    embed.add_field(name=":warning: Yapan Kişi", value=f"<@!{ctx.author.id}>", inline=False)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await owner.send(embed=embed)        

@sunucuyutemizle.error
async def sunucuyutemizle_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")          
        

@bot.command()
async def hack(ctx, user: discord.Member):
    description = str(ctx.guild.description)
    
    if user.id == 470599096487510016:
        await ctx.send("Yapımcım beni öyle bir programlamış ki kendinin hacklenmesine izin vermiyor. :sunglasses: ")   
    else:    
        if user.id == 819743355663548447:
            await ctx.send("Yapımcım beni öyle bir programlamış ki kimse beni hackleyemiyor. :sunglasses: ")     
        else:    
            embed1 = discord.Embed(title="<:bilgi:830857146702888961> Kullanıcıyı Hackleme İşlemi Başlıyor", description=f"{ctx.author.display_name}, {user.name} Adlı Kullanıcıyı Hacklemeye Başlıyor", color=0x00ff33)
            embed1.set_image(url="https://media.giphy.com/media/iFOVMvOHlCCKEQ8PBq/giphy.gif")

            await ctx.send(embed=embed1, delete_after=5.0)
 
            await asyncio.sleep(5)

            embed2 = discord.Embed(title="<:bilgi:830857146702888961> Hackleme İşlemi Başarılı", description=f"{ctx.author.display_name}, {user.name} Adlı Kullanıcıyı Başarıyla Hackledi!", color=0x0008ff)
            embed2.set_image(url="https://i.imgur.com/fTrYkeK.jpg")

            await ctx.send(embed=embed2)


@hack.error
async def hack_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen hacklemek istediğiniz kullanıcyı komut sonrasında etiketleyerek belirtiniz.')
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.')          


@bot.command(aliases=['botudavetet', 'botdavet', 'botdavetlinki'])
async def davet(ctx, user: discord.Member):
    description = str(ctx.guild.description)
    if user.bot:
       embed = discord.Embed(title="Botun Davet Linkleri ", description=f"> <:kral:830058307351478282> Yönetici Yetkileriyle ➠ [Tıkla](https://discord.com/oauth2/authorize?client_id={user.id}&permissions=8&scope=bot) \n > <:kral:830058307351478282> Bütün Yetkileriyle ➠ [Tıkla](https://discord.com/api/oauth2/authorize?client_id={user.id}&permissions=4294967287&scope=bot) \n > <:robo:833610842410450964> Yetkisiz Şekilde ➠ [Tıkla](https://discord.com/api/oauth2/authorize?client_id={user.id}&permissions=0&scope=bot)", color=0x14ffd8)
       await ctx.send(embed=embed)
    else:
       await ctx.send('Belirttiğiniz kullanıcı bir bot olmadığı için söz konusu davet bağlantıları gösterilemiyor.')

@davet.error
async def davet_error(ctx, error): 
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen davet bağlantısını almak istediğiniz botu komut sonrasında etiketleyerek belirtiniz.') 


@bot.command()
async def sarıl(ctx, user: discord.Member):
    description = str(ctx.guild.description)
    embed1 = discord.Embed(title="🤗 Kullanıcıyı Sarılma İşlemi Başlıyor", description=f"🤗 {ctx.author.display_name}, {user.name} Adlı Kullanıcıya Başarıyla Sarıldı", color=0x00ff33)
    embed1.set_image(url="https://media.giphy.com/media/IM59IWadUTtMAsYOhV/giphy.gif")

    await ctx.send(embed=embed1)


@sarıl.error
async def sarıl_error(ctx, error): 
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen sarılmak istediğiniz kullanıcyı komut sonrasında etiketleyerek belirtiniz.')         

@bot.command()
async def ateşet(ctx, user: discord.Member):
    description = str(ctx.guild.description)
    if user.id == 470599096487510016:
        await ctx.send(f"Özür dilerim {ctx.author.display_name}, yapımcımın canının acımasına gönlüm el vermiyor. :frowning:  ")
    else:
        if user.id == 819743355663548447:
            await ctx.send(f"Özür dilerim {ctx.author.display_name}, kendime ateş etmek istemiyorum. Ya yaralanırsam? :frowning:  ") 
        else:  
            embed1 = discord.Embed(title="<:silah:832581337520537640> Kullanıcıya Ateş Ediliyor", description=f"<:silah:832581337520537640> {ctx.author.display_name}, {user.name} Adlı Kullanıcıya Başarıyla Ateş Etti", color=0xffa200)
            embed1.set_image(url="https://media.giphy.com/media/FtjLBJSBtfYgBcOuFl/giphy.gif")

            await ctx.send(embed=embed1)


@ateşet.error
async def ateşet_error(ctx, error): 
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen ateş etmek istediğiniz kullanıcyı komut sonrasında etiketleyerek belirtiniz.') 


@bot.command()
async def öldür(ctx, user: discord.Member):
    description = str(ctx.guild.description)
    if user.id == 470599096487510016:
        await ctx.send(f"Özür dilerim {ctx.author.display_name}, yapımcımın öldürülmesine izin veremem. Yapımcım ölürse bana kim bakıcak? :frowning:  ")
    else:
        if user.id == 819743355663548447:
            await ctx.send(f"Özür dilerim {ctx.author.display_name}, kendimi öldürmek istemiyorum. Ben ölürsem bu güzel komutları hangi bot gerçekleştirecek. :frowning:  ") 
        else:  
            embed1 = discord.Embed(title="☠️ Kullanıcıyı Öldürme İşlemi Başlıyor", description=f"☠️ {ctx.author.display_name}, {user.name} Adlı Kullanıcıyı Başarıyla Öldürdü", color=0xff0000)
            embed1.set_image(url="https://media3.giphy.com/media/wqvu848mFma3yLEWEn/giphy.gif")

            await ctx.send(embed=embed1)
 


@öldür.error
async def öldür_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen öldürmek istediğiniz kullanıcyı komut sonrasında etiketleyerek belirtiniz.')       
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.')   



@bot.command(aliases=['yumruk'])
async def yumrukla(ctx, user: discord.Member):
    description = str(ctx.guild.description)

    if user.id == 470599096487510016:
        await ctx.send(f"Özür dilerim {ctx.author.display_name}, yapımcımın canının acımasına gönlüm el vermiyor. :frowning: ")
    else:
        if user.id == 819743355663548447:
            await ctx.send(f"Özür dilerim {ctx.author.display_name}, kendimi yumruklamak istemiyorum. :sunglasses:  ") 
        else:  
            embed1 = discord.Embed(title="<a:yumruk:833991281880858705> Kullanıcıyı Yumruklama İşlemi Başlıyor", description=f"<a:yumruk:833991281880858705> {ctx.author.display_name}, {user.name} Adlı Kullanıcıya Başarıyla Yumruk Attı", color=0xffa200)
            embed1.set_image(url="https://media.giphy.com/media/wPdeBWtyXbmT2CkCsK/giphy.gif")

            await ctx.send(embed=embed1)


@yumrukla.error
async def yumrukla_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen yumruklamak istediğiniz kullanıcyı komut sonrasında etiketleyerek belirtiniz.')       
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.')  


@bot.command(aliases=['tokat'])
async def tokatla(ctx, user: discord.Member):
    description = str(ctx.guild.description)
    if user.id == 470599096487510016:
        await ctx.send(f"Özür dilerim {ctx.author.display_name}, yapımcımın canının acımasına gönlüm el vermiyor. :frowning:  ")
    else:
        if user.id == 819743355663548447:
            await ctx.send(f"Özür dilerim {ctx.author.display_name}, kendimi tokatlamak istemiyorum. :sunglasses:  ") 
        else:  
            embed1 = discord.Embed(title="<a:slap:834101938341412897> Kullanıcıyı Tokatlama İşlemi Başlıyor", description=f"<a:slap:834101938341412897> {ctx.author.display_name}, {user.name} Adlı Kullanıcıyı Başarıyla Tokatladı", color=0xffa200)
            embed1.set_image(url="https://media1.tenor.com/images/c724e1c1ddef332e3c95165c09e5b7e2/tenor.gif")

            await ctx.send(embed=embed1)
 

@tokatla.error
async def tokatla_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen tokatlamak istediğiniz kullanıcyı komut sonrasında etiketleyerek belirtiniz.')       
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.')  


@bot.command()
async def yalvar(ctx, user: discord.Member):
    description = str(ctx.guild.description)
    embed1 = discord.Embed(title="🥺 Kullanıcıya Yalvarma İşlemi Başlıyor", description=f"🥺 {ctx.author.display_name}, {user.name} Adlı Kullanıcıya Başarıyla Yalvardı", color=0xffa200)
    embed1.set_image(url="https://media.giphy.com/media/NWi2D6hAqseUpu0pLN/giphy.gif")

    await ctx.send(embed=embed1)
 
@yalvar.error
async def yalvar_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen yalvarmak istediğiniz kullanıcyı komut sonrasında etiketleyerek belirtiniz.')       
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.')  


@bot.command(aliases=['tahminet', 'tahmin-et'])
@commands.cooldown(1, 15, commands.BucketType.user)
async def guess(ctx):
    emoji = "Hata"

    await ctx.send('**<a:party:845931188924186634> 1 ile 10 arasında bir sayı tahmin et. Tahmininin doğru olup olmadığı sana tahmininden sonra söylenecek. Tahminini belirtmediğin takdirde işlem on saniye içerisinde iptal edilecektir.** ')

    def is_correct(m):
        return m.author == ctx.author and m.content.isdigit()

    answer = random.randint(1, 10)

    if answer == 1:
        emoji = "<a:sayi1:859382873660719105>"
    if answer == 2:
        emoji = "<a:sayi2:859383616991133746> "
    if answer == 3:
        emoji = "<a:sayi3:859383618647490571> "
    if answer == 4:
        emoji = "<a:sayi4:859383619558965278> "
    if answer == 5:
        emoji = "<a:sayi5:859383619666837584>"
    if answer == 6:
        emoji = "<a:sayi6:859383620891049994> "
    if answer == 7:
        emoji = "<a:sayi7:859383619843653642>  "
    if answer == 8:
        emoji = "<a:sayi8:859383619872751646> "
    if answer == 9:
        emoji = "<a:sayi9:859383619998056478>"
    if answer == 10:
        emoji = "<a:sayi1:859382873660719105><a:sayi0:859383607768383508>"        
        
    try:
        guess = await bot.wait_for('message', check=is_correct, timeout=10.0)
    except asyncio.TimeoutError:
        return await ctx.send(f'**<:normalcarpi:852958720328466474> Tahminini belirtmen çok uzun sürdü. Doğru sayı: {emoji}**')

    if int(guess.content) == answer:
        await ctx.send(f'**<:normaltik:852958457740394506> Tahminin doğru çıktı. Doğru sayı: {emoji}**')
    else:
        await ctx.send(f'**<:normalcarpi:852958720328466474> Tahminin yanlış çıktı. Doğru sayı: {emoji}**')

@guess.error
async def guess_error(ctx, error): 
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'<:saat:867471142800457748> **Bu komutu kullanabilmek için {round(error.retry_after, 2)} saniye daha beklmelisin.**')


@bot.command(aliases=['not', 'bot_not', 'bot_notu'])
async def note(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    icon = str(ctx.guild.icon_url)
    
    embed = discord.Embed(
        title="📜 │ Bot Hakkında Önemli Notlar",
        description="Bu bot hakkında önemli sayılabilecek notlar ve dikkat edilmesi gereken hususlara belirtir.",
        color=discord.Color.blue()
    )
    embed.add_field(name="📜 │ Bot Yetkileri", value="Botun yetkilerini olabildiğince yüksek yapmanız önerilir. Bunun nedeni bottaki komutların botun yetkisi olmaması haricinde işe yaramamasıdır.", inline=False)
    embed.add_field(name="📜 │Botun Rol Sırası", value="Botun rol sayılarını olabildiğince yükseğe koymanız önerilir. Bunun nedeni ise botun kendinden yüksek rollere müdahele edememesidir.", inline=False)
    embed.add_field(name="📜 │Genel Not", value="Yukarıdaki hususlarla uyulmaması takdirde bot düzgün çalışmayabilir, bilginize.", inline=False)   
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    
    await ctx.send(embed=embed)


@bot.command(pass_context=True , aliases=['sil', 'temizle', 'mesajlarısil', 'mesajları_sil' , 'mesajsil', 'mesaj_sil'])   
async def clear(ctx, amount = 100): 
    authorperms = ctx.author.permissions_in(ctx.channel)
    if authorperms.manage_messages:
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'```css\n🗑 {amount} Mesaj Silindi 🗑```', delete_after=4.0)
    else:
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")


@commands.has_permissions(manage_channels=True)
@bot.command(aliases=['kanalitemizle', 'kanalıtemizle', 'kanalı-temizle', 'kanali-temizle', 'kanalıkopyala', 'kanalikopyala'])
async def nuke(ctx, channel: discord.TextChannel = None):
    if not channel:
        channel = ctx.channel 

        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)
        new_channel = await nuke_channel.clone(reason=f"Bu Kanal {str(ctx.author)} Tarafından Temizlendi")
        await nuke_channel.delete()
        
        embed2 = discord.Embed(title="Bu Kanal Başarıyla Temizlendi", description=f"**`{new_channel.name}`** Adlı Kanal Başarıyla Temizlendi", color=0xffa200)
        embed2.set_image(url="https://media.giphy.com/media/2I9cAAfZfyfcsrwIpB/giphy.gif")
        embed2.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

        await new_channel.send(embed=embed2)

    else:
        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

        embed1 = discord.Embed(title="<a:yesiltik:845932913806934036>  Kanal Başarıyla Temizlendi", description=f"**`{channel.name}`** Adlı Kanal Başarıyla Temizlendi", color=62150)
        embed1.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

        new_channel = await nuke_channel.clone(reason=f"Bu Kanal {str(ctx.author)} Tarafından Temizlendi")
        await nuke_channel.delete()

        embed2 = discord.Embed(title="Bu Kanal Başarıyla Temizlendi", description=f"​​**`{new_channel.name}`** Adlı Kanal Başarıyla Temizlendi", color=0xffa200)
        embed2.set_image(url="https://media.giphy.com/media/2I9cAAfZfyfcsrwIpB/giphy.gif")
        embed2.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

        await new_channel.send(embed=embed2)

        await ctx.send(embed=embed1)
  


@nuke.error
async def nuke_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")  
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Kanal Temizleme Komutu 🔐  ]▬▬▬▬▬▬",
            description="> **<:maviok:837983169579712532> Görünüşe bakılırsa bu komutu yanlış kullanmısınız.** \n > _ _ \n > **<:maviok:837983169579712532> İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:**",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> <:yesilok:771731154159796241> **w!nuke** <kanal>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> <:yesilok:771731154159796241> **w!nuke** Sohbet \n > _ _ \n > <:yesilok:771731154159796241> **w!nuke** Görsel \n > _ _ \n > <:yesilok:771731154159796241> **w!nuke** Video \n > _ _ \n > <:yesilok:771731154159796241> **w!nuke** Gif ", inline=False)

        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
               
        await ctx.send(embed=embed)
      

@commands.has_permissions(manage_channels=True)
@bot.command()
async def lock(ctx, channel: discord.TextChannel = None):
    if not channel:
        channel = ctx.channel 

    await channel.set_permissions(ctx.guild.self_role, send_messages=True)
    await channel.set_permissions(ctx.guild.default_role, send_messages=False)

    embed1 = discord.Embed(title="<a:yesiltik:845932913806934036>  Kanal Başarıyla Kilitlendi", description=f"**`{channel.name}`** Adlı Kanal Başarıyla Kilitlendi", color=62150)
    embed1.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed1) 


@lock.error
async def lock_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")  
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Kanal Kilitleme Komutu 🔐  ]▬▬▬▬▬▬",
            description="> **<:maviok:837983169579712532> Görünüşe bakılırsa bu komutu yanlış kullanmısınız.** \n > _ _  \n  **<:maviok:837983169579712532> İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:**",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> <:yesilok:771731154159796241> **w!lock** <kanal>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> <:yesilok:771731154159796241> **w!lock** Sohbet \n > _ _ \n > <:yesilok:771731154159796241> **w!lock** Görsel \n > _ _ \n > <:yesilok:771731154159796241> **w!lock** Video \n > _ _ \n > <:yesilok:771731154159796241> **w!lock** Gif ", inline=False)

        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **📁 Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > **📁 Botun Yazıldığı Dil:** **`Python`**", inline=False)
               
        await ctx.send(embed=embed)      


@commands.has_permissions(manage_channels=True)
@bot.command()
async def hide(ctx, channel: discord.TextChannel = None):
    if not channel:
        channel = ctx.channel 

    await channel.set_permissions(ctx.guild.self_role, read_messages=True, send_messages=True)
    await channel.set_permissions(ctx.guild.default_role, read_messages=False)

    embed1 = discord.Embed(title="<a:yesiltik:845932913806934036>  Kanal Başarıyla Gizlendi", description=f"**`{channel.name}`** Adlı Kanal Başarıyla Gizlendi", color=62150)
    embed1.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed1)         


@hide.error
async def hide_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")  
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Kanal Gizleme Komutu 🔐  ]▬▬▬▬▬▬",
            description="> **<:maviok:837983169579712532> Görünüşe bakılırsa bu komutu yanlış kullanmısınız.** \n > _ _ \n > <:maviok:837983169579712532> **İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:**",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> <:yesilok:771731154159796241> **w!hide** <kanal>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> <:yesilok:771731154159796241> **w!hide** Sohbet \n > _ _ \n > <:yesilok:771731154159796241> **w!hide** Görsel \n > _ _ \n > <:yesilok:771731154159796241> **w!hide** Video \n > _ _ \n > <:yesilok:771731154159796241> **w!hide** Gif ", inline=False)

        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
                
        await ctx.send(embed=embed) 


@commands.has_permissions(kick_members=True)
@bot.command(pass_context=True , aliases=['at', 'kov', 'kullanıcıyı_at', 'kullanıcıyıat'])
async def kick(ctx, user: discord.Member, *, reason="Neden kullanıcı tarafından belirtilmedi."):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f":boom: {user.name} Sunucudan Kovuldu", description=f"**Nedeni:** {reason}\n", color=0xff0000 )
        await ctx.channel.send(embed=kick)

@kick.error
async def test_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")
    if isinstance(error, commands.MissingRequiredArgument):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Kullanıcıyı Atma Komutu 🔐  ]▬▬▬▬▬▬",
            description="> **<:maviok:837983169579712532> Görünüşe bakılırsa bu komutu yanlış kullanmısınız.** \n > _ _ \n > <:maviok:837983169579712532> **İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:**",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> <:yesilok:771731154159796241> **w!kick** <kullanıcı> <nedeniniz>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> <:yesilok:771731154159796241> **w!kick** {ctx.author.mention} Spam \n > _ _ \n > <:yesilok:771731154159796241> **w!kick** {ctx.author.mention} Argo \n > _ _ \n > <:yesilok:771731154159796241> **w!kick** {ctx.author.mention} Hakaret \n > _ _ \n > <:yesilok:771731154159796241> **w!kick** {ctx.author.mention} Saygısızlık \n ", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
         
        await ctx.send(embed=embed)   

    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.')         


@commands.has_permissions(manage_roles=True)
@bot.command(pass_context=True , aliases=['sustur', 'kullanıcıyı_sustur', 'kullanıcıyısustur'])
async def mute(ctx, member: discord.Member, *, reason='Neden kullanıcı tarafından belirtilmedi.'):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, send_messages=False, read_message_history=True)
    embed = discord.Embed(title=f":boom: Kullanıcı Yazı Kanallarından Susturuldu", description=f"**Nedeni:** {reason}\n", color=0xff0000 )
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")
    if isinstance(error, commands.MissingRequiredArgument):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Kullanıcıyı Susturma Komutu 🔐  ]▬▬▬▬▬▬",
            description="> **<:maviok:837983169579712532>  Görünüşe bakılırsa bu komutu yanlış kullanmışınız.** \n > _ _ \n > **<:maviok:837983169579712532> İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:**",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> <:yesilok:771731154159796241> **w!mute** <kullanıcı> <nedeniniz>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> <:yesilok:771731154159796241> **w!mute** {ctx.author.mention} Spam \n > _ _ \n > <:yesilok:771731154159796241> **w!mute** {ctx.author.mention} Argo \n > _ _ \n > <:yesilok:771731154159796241> **w!mute** {ctx.author.mention} Hakaret \n > _ _ \n > <:yesilok:771731154159796241> **w!mute** {ctx.author.mention} Saygısızlık \n ", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
         
        await ctx.send(embed=embed)   

    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 



@commands.has_guild_permissions(mute_members=True)
@bot.command(pass_context=True , aliases=['sessustur', 'sestesustur', 'kullanıcıyısestesustur'])
async def voicemute(ctx, member: discord.Member, *, reason='Neden kullanıcı tarafından belirtilmedi.'):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Voice Mute")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Voice Mute")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False)
    embed = discord.Embed(title=f"<:muted:851537009394974750> Kullanıcı Ses Kanallarından Susturuldu", description=f"**Nedeni:** {reason}\n", color=0xff0000 )
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)


@voicemute.error
async def voicemute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")  
    if isinstance(error, commands.MissingRequiredArgument):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Kullanıcıyı Susturma Komutu 🔐  ]▬▬▬▬▬▬",
            description="> **<:maviok:837983169579712532> Görünüşe bakılırsa bu komutu yanlış kullanmısınız.** \n > _ _ \n > **<:maviok:837983169579712532> İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:**",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> <:yesilok:771731154159796241> **w!voicemute** <kullanıcı> <nedeniniz>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> <:yesilok:771731154159796241> **w!voicemute** {ctx.author.mention} Mikrofonu Yedi \n > _ _ \n > <:yesilok:771731154159796241> **w!voicemute** {ctx.author.mention} Argo Kullandı \n > _ _ \n > <:yesilok:771731154159796241> **w!voicemute** {ctx.author.mention} Hakaret Etti \n > _ _ \n > <:yesilok:771731154159796241> **w!voicemute** {ctx.author.mention} Saygısızlık Yaptı  ", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
         
        await ctx.send(embed=embed)   

    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 



@commands.has_permissions(manage_roles=True)
@bot.command(pass_context=True , aliases=['susturmayıkaldır', 'susturmayı_kaldır', 'un_mute'])
async def unmute(ctx, member: discord.Member, *, reason='Neden kullanıcı tarafından belirtilmedi.'):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   embed = discord.Embed(title=f"<a:yesiltik:845932913806934036>  Kullanıcının Yazı Kanallarından Susturulması Kaldırıldı", description=f"**Nedeni:** {reason}\n", color=62150)
   await ctx.send(embed=embed)


@unmute.error
async def test_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")  
    if isinstance(error, commands.MissingRequiredArgument):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Susturmasını Kaldırma Komutu 🔐  ]▬▬▬▬▬▬",
            description="> :dizzy: Görünüşe bakılırsa bu komutu yanlış kullanmısınız. İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> :dizzy: **w!unmute** <kullanıcı> <nedeniniz>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> :dizzy: **w!unmute** {ctx.author.mention} Spam Yapmayı Bıraktı \n > :dizzy: **w!unmute** {ctx.author.mention} Argo Yapmayı Bıraktı \n  > :dizzy: **w!unmute** {ctx.author.mention} Hakaret  Etmeyi Bıraktı \n > :dizzy: **w!unmute** {ctx.author.mention} Saygısızlık Yapmayı Bıraktı \n ", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
         
        await ctx.send(embed=embed)   

    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 

@commands.has_guild_permissions(mute_members=True)
@bot.command(pass_context=True, aliases=['sessusturmayıkaldır', 'sestesusturmayıkaldır'])
async def unvoicemute(ctx, member: discord.Member, *, reason='Neden kullanıcı tarafından belirtilmedi.'):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Voice Mute")

   await member.remove_roles(mutedRole)
   embed = discord.Embed(title=f"<:unmuted:851537111870210079> Kullanıcının Ses Kanallarından Susturulması Kaldırıldı", description=f"**Nedeni:** {reason}\n", color=0xff0000)
   await ctx.send(embed=embed)


@unvoicemute.error
async def unvoicemute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")  
    if isinstance(error, commands.MissingRequiredArgument):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Susturmasını Kaldırma Komutu 🔐  ]▬▬▬▬▬▬",
            description="> :dizzy: Görünüşe bakılırsa bu komutu yanlış kullanmısınız. İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> :dizzy: **w!unvoicemute** <kullanıcı> <nedeniniz>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> :dizzy: **w!unvoicemute** {ctx.author.mention} Mikrofonu Yemeyi Bıraktı \n > :dizzy: **w!unvoicemute** {ctx.author.mention} Bağırmayı Bıraktı \n  > :dizzy: **w!unvoicemute** {ctx.author.mention} Hakaret  Etmeyi Bıraktı \n > :dizzy: **w!unvoicemute** {ctx.author.mention} Saygısızlık Yapmayı Bıraktı \n ", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
         
        await ctx.send(embed=embed)   

    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.')   


@commands.has_permissions(ban_members=True)
@bot.command(pass_context=True , aliases=['banla', 'yasakla', 'kullanıcıyı_banla', 'kullanıcıyı_yasakla'])
async def ban(ctx, user: discord.Member, *, reason="Neden kullanıcı tarafından belirtilmedi."):
        await user.ban(reason=reason)
        ban = discord.Embed(title=f":boom: {user.name} Sunucudan Banlandı", description=f"**Nedeni**: {reason}", color=0xff0000)
        await ctx.channel.send(embed=ban)


@ban.error
async def test_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")      
    if isinstance(error, commands.MissingRequiredArgument):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Kullanıcıyı Yasaklama Komutu 🔐  ]▬▬▬▬▬▬",
            description="> :dizzy: Görünüşe bakılırsa bu komutu yanlış kullanmısınız. İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> :dizzy: **w!ban** <kullanıcı> <nedeniniz>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> :dizzy: **w!ban** {ctx.author.mention} Spam \n > :dizzy: **w!ban** {ctx.author.mention} Argo \n  > :dizzy: **w!ban** {ctx.author.mention} Hakaret \n > :dizzy: **w!ban** {ctx.author.mention} Saygısızlık \n ", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
         
        await ctx.send(embed=embed)   

    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.')  


@commands.has_permissions(ban_members=True)
@bot.command(aliases=['bankaldır', 'banı_kaldır', 'yasak_kaldır', 'yasaklamayı_kaldır'])
async def unban(ctx, *, user=None):

    try:
        user = await commands.converter.UserConverter().convert(ctx, user)
    except:
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Yasaklamasını Kaldırma Komutu 🔐  ]▬▬▬▬▬▬",
            description="> :dizzy: Görünüşe bakılırsa bu komutu yanlış kullanmısınız. İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> :dizzy: **w!unban** <kullanıcı>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> :dizzy: **w!unban** {ctx.author.mention} \n > :dizzy: **w!unban** {ctx.author.mention} \n  > :dizzy: **w!unban** {ctx.author.mention} \n > :dizzy: **w!unban** {ctx.author.mention}\n ", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
         
        await ctx.send(embed=embed)  
        return

    try:
        bans = tuple(ban_entry.user for ban_entry in await ctx.guild.bans())
        if user in bans:
            await ctx.guild.unban(user, reason=reason)
        else:
            await ctx.send("Belirttiğiniz kullanıcı yasaklı değil.")
            return

    except discord.Forbidden:
        await ctx.send("Bu komutu kullanabilmek için gerekli izinlere sahip değilim. Daha fazla bilgi için w!not komutunu kullanabilirsiniz.")
        return

    except:
        await ctx.send("Bir hata ile karşılaşıldı.")
        return

    unban = discord.Embed(title=f"<a:yesiltik:845932913806934036>  Kullanıcının Yasağı Kaldırıldı", description=f"**Yasak kaldırıldı", color=62150)
    await ctx.channel.send(embed=unban)


@unban.error
async def test_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")  
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.')  


@commands.has_permissions(manage_roles=True)
@bot.command(pass_context=True, aliases=['rolver', 'rol-ver', 'give-role'])
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    embed = discord.Embed(title="<a:yesiltik:845932913806934036>  Kullanıcıya Rol Verildi", description=f"Söz konusu kullanıcıya başarıyla belirttiğiniz rol verildi.", color=62150)

    await ctx.send(embed=embed)


@giverole.error
async def giverole_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")   
    if isinstance(error, commands.MissingRequiredArgument):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Rol Verme Komutu 🔐  ]▬▬▬▬▬▬",
            description="> :dizzy: Görünüşe bakılırsa bu komutu yanlış kullanmışınız. İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> :dizzy: **w!rol-ver** <kullanıcı> <rolünüz>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> :dizzy: **w!rol-ver** {ctx.author.mention} Admin \n > :dizzy: **w!rol-ver** {ctx.author.mention} Moderatör \n > :dizzy: **w!rol-ver** {ctx.author.mention} Denetmen \n > :dizzy: **w!rol-ver** {ctx.author.mention} VIP ", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
         
        await ctx.send(embed=embed)  
         
    if isinstance(error, commands.BadArgument):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Rol Verme Komutu 🔐  ]▬▬▬▬▬▬",
            description="> :dizzy: Görünüşe bakılırsa bu komutu yanlış kullanmısınız. İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> :dizzy: **w!rol-ver** <kullanıcı> <rolünüz>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> :dizzy: **w!rol-ver** {ctx.author.mention} Admin \n > :dizzy: **w!rol-ver** {ctx.author.mention} Moderatör \n > :dizzy: **w!rol-ver** {ctx.author.mention} Denetmen \n > :dizzy: **w!rol-ver** {ctx.author.mention} VIP ", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
         
        await ctx.send(embed=embed)  



@commands.has_permissions(manage_roles=True)
@bot.command(pass_context=True, aliases=['rolal', 'rol-al', 'take-role'])
async def takerole(ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    embed = discord.Embed(title="<a:yesiltik:845932913806934036>  Kullanıcının Rolü Kaldırıldı", description=f"Söz konusu kullanıcının belirttiğiniz rolü başarıyla kaldırıldı..", color=62150)

    await ctx.send(embed=embed)


@takerole.error
async def takerole_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")  
    if isinstance(error, commands.MissingRequiredArgument):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Rol Kaldırma Komutu 🔐  ]▬▬▬▬▬▬",
            description="> :dizzy: Görünüşe bakılırsa bu komutu yanlış kullanmışınız. İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> :dizzy: **w!rol-kaldır** <kullanıcı> <rolünüz>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> :dizzy: **w!rol-kaldır** {ctx.author.mention} Admin \n > :dizzy: **w!rol-kaldır** {ctx.author.mention} Moderatör \n > :dizzy: **w!rol-kaldır** {ctx.author.mention} Denetmen \n > :dizzy: **w!rol-kaldır** {ctx.author.mention} VIP ", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
         
        await ctx.send(embed=embed)  
         
    if isinstance(error, commands.BadArgument):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Rol Kaldırma Komutu 🔐  ]▬▬▬▬▬▬",
            description="> :dizzy: Görünüşe bakılırsa bu komutu yanlış kullanmışınız. İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> :dizzy: **w!rol-kaldır** <kullanıcı> <rolünüz>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> :dizzy: **w!rol-kaldır** {ctx.author.mention} Admin \n > :dizzy: **w!rol-kaldır** {ctx.author.mention} Moderatör \n > :dizzy: **w!rol-kaldır** {ctx.author.mention} Denetmen \n > :dizzy: **w!rol-kaldır** {ctx.author.mention} VIP ", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
         
        await ctx.send(embed=embed)  


@bot.command(aliases=['sunucu', 'sunucu_bilgi', 'sunucubilgi', 'serverinfo' , 'server_info'])
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    guild = ctx.guild

    role_count = len(ctx.guild.roles)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    total_text_channels = len(guild.text_channels)
    total_voice_channels = len(guild.voice_channels)
    total_channels = total_text_channels  + total_voice_channels

    icon = str(ctx.guild.icon_url)
    
    embed = discord.Embed(
        title="<:nametag:841951946650812426> │ Sunucu İsmi",
        description=f"{ctx.guild.name}", timestamp=ctx.message.created_at,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="📅 │ Sunucu Ne Zaman Oluşturuldu", value=ctx.guild.created_at.strftime("%d/%m/%Y"))
    embed.add_field(name="👑 │ Sunucu Sahibi", value=f"<@!{ctx.guild.owner_id}>", inline=True) 
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="🌎 │ Sunucu Bölgesi", value=region, inline=True)
    embed.add_field(name="👤 │ Sunucudaki Kişi Sayısı", value=memberCount, inline=True) 
    embed.add_field(name='🎉 │ Sunucudaki Rol Sayısı', value=str(role_count), inline=True)
    embed.add_field(name="🎉 │ Sunucudaki Kanal Sayısı", value=f"<:yazi:829082908231729172> {total_text_channels} | <:ses:829082908128051241> {total_voice_channels}", inline=True)
    embed.add_field(name="🆔 │ Sunucu ID'si", value=id, inline=False)
    embed.set_footer(text=f"{ctx.author.display_name} │ Sunucu Bilgisi")    
    
    
    await ctx.send(embed=embed) 


@bot.command(aliases=['whois', 'kullanıcı_bilgi', 'kim' , 'kullanıcı', 'kullanıcı_bilgisi', 'kullanıcıbilgisi' , 'user' ])
async def userinfo(ctx, member: discord.Member = None):
    icon = str(ctx.guild.icon_url)
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(color=0x14ffd8, timestamp=ctx.message.created_at,
                          title=f"")
    embed.set_thumbnail(url=member.avatar_url)
    

    embed.set_author(name=member.display_name, url="", icon_url=member.avatar_url)
    embed.add_field(name="👤 │Kullanıcı Adı", value=f"{str(member)}")
    embed.add_field(name="🆔 │ Kullanıcı ID'si", value=member.id)
    embed.add_field(name="<:discord:826722461943988254> │Discord'a Katıldı", value=member.created_at.strftime("%d/%m/%Y"))
    embed.add_field(name="🏛️ │ Sunucuya Katıldı ", value=member.joined_at.strftime("%d/%m/%Y"))
    if member.bot:
       embed.add_field(name=":robot: │ Bot Mu", value="Evet")
    else: 
       embed.add_field(name=":robot: │ Bot Mu", value="Hayır")   
    embed.set_footer(text=f"{member.display_name} │ Kullanıcı Bilgisi")
    
    await ctx.send(embed=embed)
    

@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.')    
    
    
@bot.command(aliases=['pp', 'Avatar', 'profilfotosu', 'profil_fotosu' , 'profilfotografi', 'profilfotografı', 'profil_fotografi' , 'profil_fotografı' ])
async def avatar(ctx, *, member: discord.Member=None): # set the member object to None
    if not member: # if member is no mentioned
        member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)


@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.')  


@bot.command(pass_context=True, aliases=['botbilgi', 'botbilgisi', 'bot_bilgi' , 'bot_bilgisi', 'bot_info'])
async def botinfo(ctx):
   icon = str(ctx.guild.icon_url)

   embed=discord.Embed(title="🤖 │ Bot Bilgisi", description="Bu bot hakkında bilgiler içerir.", color=0x00ccff)
   embed.set_author(name=f"{bot_adı}", icon_url=f"{bot_avatar}")
   embed.set_thumbnail(url=f"{bot_avatar}")
   embed.add_field(name="🤖 │ Bot ", value="Aktif", inline=False)
   embed.add_field(name="🆔 │ Bot ID'si", value=f"{bot_id}", inline=True)
   embed.add_field(name="🎓 │ Bot Yapımcısı", value=f"{bot_yapımcısı}", inline=True)
   embed.add_field(name="🌀 │ Botun Destek Sunucusu", value=f"[Tıkla]({destek_sunucusu})", inline=True)
   embed.add_field(name="🔗 │ Botun Davet Linki", value=f"[Tıkla]({önerilen_yetki_davet})", inline=True)
   embed.add_field(name="🔮 │Botun Bulunduğu Sunucu Sayısı", value=f"{len(bot.guilds)}", inline=True)
   
   await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def botistatistik(ctx):
   icon = str(ctx.guild.icon_url)

   embed=discord.Embed(title="🤖 │ Bot İstatistikleri", description="Bu bot hakkındaki istatistikleri içerir.", color=0x00ccff)
   embed.set_author(name=f"{bot_adı}", icon_url=f"{bot_avatar}")
   embed.set_thumbnail(url=f"{bot_avatar}")

   embed.add_field(name="<a:stats:832162327826268180> │ Botun Hizmet Verdiği Kişi Sayısı", value=f" {len(bot.users)}", inline=True)

   embed.add_field(name="🔮 │Botun Bulunduğu Sunucu Sayısı", value=f"{len(bot.guilds)}", inline=True)

   
   await ctx.send(embed=embed)


@bot.command()
async def öneri(ctx, *, mesaj):
    icon = str(ctx.guild.icon_url)
    channel = bot.get_channel(839404567183884299)

    embed1 = discord.Embed(title="<a:yesiltik:845932913806934036>  Öneriniz Gönderildi", description=f"Öneriniz başarıyla ilgili kişilere gönderildi. Öneriniz için teşekkürler.", color=62150)
    embed1.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed1)

    embed = discord.Embed(title="<:nametag:841951946650812426> │ Önerdiği Sunucu", description=f"{ctx.guild.name}", color=0x00ff33)
    embed.add_field(name="👤 │ Öneren Kişi", value=f"<@!{ctx.author.id}>", inline=False)
    embed.add_field(name="Önerisi", value=f"{mesaj}", inline=False)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await channel.send(embed=embed)     

@öneri.error
async def öneri_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen öneri mesajınızı, komut sonrasında belirtiniz. ')     


@bot.command(pass_context=True, aliases=['yapımcı', 'botiletişim', 'bot_iletişim', 'İletişim',])
async def iletişim(ctx):
    member = ctx.message.author

    embed=discord.Embed(title="🔗 │ İletişim Ve Linkler ", description="Bot hakkında herhangi bir sorunu bildirmek yada yardım almak için buradaki iletişim adreslerini kullanabilirsiniz.", color=0x00ccff)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=member.avatar_url)
    embed.add_field(name="🎓 │ Bot Yapımcısı", value=f"{bot_yapımcısı}", inline=False)
    embed.add_field(name="<:telegram:826727507877298187> │ Telegram", value=f"{telegram_iletişim}", inline=True)
    embed.add_field(name="<:discord:826722461943988254> │ Discord", value=f"{discord_iletişim}", inline=True)
    embed.add_field(name="🌀 │ Botun Destek Sunucusu", value=f"[Tıkla]({destek_sunucusu})", inline=True)
    embed.add_field(name="🔗 │ Botun Davet Linki", value=f"[Tıkla]({önerilen_yetki_davet}) ", inline=True)

    await ctx.send(embed=embed)


@bot.command(pass_context=True, aliases=['zarat', 'dice', 'zar_at'])
async def zar(ctx):
    variable = [
        "https://cdn.discordapp.com/emojis/828582772054294558.png?v=1",
        "https://cdn.discordapp.com/emojis/828582771647578132.png?v=1",
        "https://cdn.discordapp.com/emojis/828582772196376576.png?v=1",
        "https://cdn.discordapp.com/emojis/828582771646529547.png?v=1",
        "https://cdn.discordapp.com/emojis/828582771776684062.png?v=1",
        "https://cdn.discordapp.com/emojis/828582771504709643.png?v=1",]
    
    await ctx.send ("{}".format(random.choice(variable)))

@bot.command()
async def arabasür(ctx):
    variable = [
        "https://media.giphy.com/media/K1c6mdgK2YNaiEvrbr/giphy.gif",
        "https://media.giphy.com/media/bIdnImn9BhosUMYSMi/giphy.gif",
        "https://media.giphy.com/media/yKJ5QoghU9XVaiLoCR/giphy.gif",
        "https://media.giphy.com/media/9t6KGj9bSNv0ZTJ2wm/giphy.gif",]

    description = str(ctx.guild.description)
    embed = discord.Embed(title=":blue_car: Arabaya Biniliyor", description=f":blue_car: {ctx.author.display_name} Adlı Kullanıcı Başarıyla Araba Sürdü Ama Arabayla Nereye Gitti Bilmiyorum", color=0xffa200)
    embed.set_image(url="{}".format(random.choice(variable)))

    await ctx.send(embed=embed)

@bot.command()
async def aloadmin(ctx):
    variable = [
        "https://media.giphy.com/media/77CUNUBN6tUz2nMwLD/giphy.gif",
        "https://media.giphy.com/media/Dxyybfs3qSSkmYcDzM/giphy.gif",]

    description = str(ctx.guild.description)
    embed = discord.Embed(title="<:banned:859797760663748659> Admin Aranıyor", description=f"<:banned:859797760663748659> {ctx.author.display_name} Adlı Kullanıcı Admin'i Aradı Ama Neden Bilmiyorum", color=0xffa200)
    embed.set_image(url="{}".format(random.choice(variable)))

    await ctx.send(embed=embed)

@bot.command()
async def polisiara(ctx):
    description = str(ctx.guild.description)
    embed = discord.Embed(title="🕵️‍♂️ Polis Aranıyor", description=f"🕵️‍♂️ {ctx.author.display_name} Adlı Kullanıcı Başarıyla Polisi Aradı Ama Neden Bilmiyorum", color=0xffa200)
    embed.set_image(url="https://media.giphy.com/media/l7X7hKzUuPQbOUthqi/giphy.gif")

    await ctx.send(embed=embed)



@bot.command(aliases=['sunucu_sahibi', 'serverowner', 'server_owner', 'sunucusahibi',])
async def sahip(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    guild = ctx.guild

    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    
    embed = discord.Embed(
        title="<:kral:830058307351478282>  Sunucu Sahibi",
        description=f"<@!{ctx.guild.owner_id}>",
        color=0x14ffd8
    )

    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)  

    await ctx.send(embed=embed) 


@bot.command()
async def bothakkında(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬▬[ 🔐 Bot Hakkındaki Komutlar 🔐  ]▬▬▬▬▬▬",
        description="> <:yesilok:843149816880037899> **w!botbilgi:** Bot hakkındaki bilgileri gösterir. \n > _ _ \n > <:yesilok:843149816880037899> **w!botistatistik:** Bu bot hakkındaki istatistikleri ,çerir. \n > _ _ \n > <:yesilok:843149816880037899> **w!wersefdavet:** Botun davet linklerini gösterir. \n > _ _ \n > <:yesilok:843149816880037899> **w!iletişim:** Botun yapımcısı ile iletişim kurma yollarını gösterir. \n > _ _ \n > <:yesilok:843149816880037899> **w!öneri:** Komut sonrasında belirttiğiniz mesaj, ilgili kişilere iletilir. \n > _ _ \n > <:yesilok:843149816880037899> **w!ping:** Botun gecikme süresini yani pingini verir. \n > _ _ \n > <:yesilok:843149816880037899> **w!not:** Bot hakkındaki önemli notları size gösterir. \n > _ _ \n > <:yesilok:843149816880037899> **w!komutlarçalışmıyor:** Komutların çalışma nedeni size sunulur.",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **<:maviok:843149816401100832> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:maviok:843149816401100832> Botun Yazıldığı Dil:** **`Python`**", inline=False)

    await ctx.send(embed=embed)    



@bot.command()
async def eğlence(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬▬[ 🔐 Eğlence Komutları 🔐  ]▬▬▬▬▬▬",
        description="> <:yesilok:843149816880037899> **w!zar:** Bot bir zar atar ve sonucu size görsel olarak bildirir. \n > _ _ \n > <:yesilok:843149816880037899> **w!hack:** Komut sonrasında belirttiğiniz kiyişi hacklemenizi sağlar. \n > _ _ \n > <:yesilok:843149816880037899> **w!sarıl:** Komut sonrasında belirttiğiniz kişiye sarılmanızı sağlar. \n > _ _ \n > <:yesilok:843149816880037899> **w!yumrukla:** Komut sonrasında belirttiğiniz kişiyi yumruklamanızı sağlar. \n > _ _ \n > <:yesilok:843149816880037899> **w!tokatla:** Komut sonrasında belirttiğiniz kişiyi tokatlamınızı sağlar. \n > _ _ \n > <:yesilok:843149816880037899> **w!öldür:** Komut sonrasında belirttiğiniz kişiyi öldürmenizi sağlar. \n > _ _ \n > <:yesilok:843149816880037899> **w!ateşet:** Komut sonrasında belirttiğiniz kişiye ateş etmenizi sağlar. \n > _ _ \n > <:yesilok:843149816880037899> **w!yalvar:** Komut sonrasında belirttiğiniz kişiye yalvarmanızı sağlar. \n > _ _ \n> <:yesilok:843149816880037899> **w!arabasür:** Araba sürmenizi sağlar. \n > _ _ \n > <:yesilok:843149816880037899> **w!polisiara:** Polisi aramanız sağlanır. \n > _ _ \n > <:yesilok:843149816880037899> **w!aloadmin:** Admin'i aramanız sağlanır. \n > _ _ \n > <:yesilok:843149816880037899> **w!tahminet:** Komutu kullandıktan sonra bot, sizden 1 ile 10 arasında bir sayı tahmin etmenizi sağlar. ",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **<:maviok:843149816401100832> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:maviok:843149816401100832> Botun Yazıldığı Dil:** **`Python`**", inline=False)


    await ctx.send(embed=embed)      
    

@bot.command()
async def işeyarar(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬▬[ 🔐 İşe Yarar Komutlar 🔐  ]▬▬▬▬▬▬",
        description="> <:yesilok:843149816880037899> **w!discordnedir:** Discord hakkında bilgiler size sunulur. \n > _ _ \n > <:yesilok:843149816880037899> **w!telegramnedir:** Telegram hakkında bazı bilgileri size sunulur. \n  > _ _ \n > <:yesilok:843149816880037899> **w!instagramnedir:** İnstagram hakkında bazı bilgileri size sunulur. \n  > _ _ \n > <:yesilok:843149816880037899> **w!facebooknedir:** Facebook hakkında bazı bilgileri size sunulur. \n  > _ _ \n > <:yesilok:843149816880037899> **w!twitternedir:** Twitter hakkında bazı bilgileri size sunulur. \n  > _ _ \n > <:yesilok:843149816880037899> **w!whatsappnedir:** Whatsapp hakkında bazı bilgileri size sunulur. \n  > _ _ \n > <:yesilok:843149816880037899> **w!youtubenedir:** Youtube hakkında bazı bilgileri size sunulur. \n  > _ _ \n > <:yesilok:843149816880037899> **w!twitchnedir:** Twitch hakkında bazı bilgileri size sunulur. \n  > _ _ \n > <:yesilok:843149816880037899> **w!rozetler:** Bütün Discord rozetleri, size renkli bir şekilde sunulur. \n  > _ _ \n > <:yesilok:843149816880037899> **w!nitro:** Discord Nitro seçenekleri size sunulur. \n  > _ _ \n > <:yesilok:843149816880037899> **w!botudavetet:** Komut sonrasında belirttiğiniz botun davet linklerini size sunar. \n  > _ _ \n > <:yesilok:843149816880037899> **w!linkkısalt:** Bot, komut sonrasında belirttiğiniz linki kolay bir şekilde kısaltır. \n  > _ _ \n > <:yesilok:843149816880037899> **w!hackaraçları:** Bot, bazı yaygın hack araçlarını size sunar. (Sorumluluk kabul etmiyorum) \n  > _ _ \n > <:yesilok:843149816880037899> **w!önemligünler:** Belli başlı önemli günler size sunulur. \n > _ _ \n > <:yesilok:843149816880037899> **w!covid:** Bütün Dünya'da şuana kadarki güncel corona virüs verileri size gösterilir. n > _ _ \n > <:yesilok:843149816880037899> **w!sigarahesapla:** Girdiğiniz verilere göre, sigaradan ne kadar zarar ettiğiniz size detaylı bir rapor halinde sunulur.",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **<:maviok:843149816401100832> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:maviok:843149816401100832> Botun Yazıldığı Dil:** **`Python`**", inline=False)


    await ctx.send(embed=embed)      

@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def sigarahesapla(ctx):
    pakette_kac_sigara = "20"

    def is_correct(m):
        return m.author == ctx.author and m.content.isdigit()

    await ctx.send('**<a:sigara:854437179501182996> Kaç yıldır sigara kullanıyorsunuz?**')  
        
    try:
        kac_yil = await bot.wait_for('message', check=is_correct, timeout=10.0)
    except asyncio.TimeoutError:
        return await ctx.send(f'**<:normalcarpi:852958720328466474> Verilerini belirtmen çok uzun sürdü. Daha sonra tekrar dene.**')

    await ctx.send('**<a:sigara:854437179501182996> Bir günde kaç tane sigara içiyorsunuz?** ')  

    try:
        gunde_kac_tane = await bot.wait_for('message', check=is_correct, timeout=10.0)
    except asyncio.TimeoutError:
        return await ctx.send(f'**<:normalcarpi:852958720328466474> Verilerini belirtmen çok uzun sürdü. Daha sonra tekrar dene.**') 
        
    await ctx.send('**<a:sigara:854437179501182996> Bir paket sigaraya kaç lira harcıyorsunuz? (Eğer bu değer yıldan yıla farklılık göseriyorsa lütfen ortalama bir değer giriniz)** ')  

    try:
        paket_fiyati = await bot.wait_for('message', check=is_correct, timeout=10.0)
    except asyncio.TimeoutError:
        return await ctx.send(f'**<:normalcarpi:852958720328466474> Verilerini belirtmen çok uzun sürdü. Daha sonra tekrar dene.**')   

    embed = discord.Embed(title="<a:sigara:854437179501182996> Sigara Zarar Hesaplama Komutu", description=f"Girdiğiniz verilere göre, sigaradan ne kadar zarar ettiğiniz size detaylı bir rapor halinde sunulur.", color=62150)
    embed.add_field(name=f"<a:sigara:854437179501182996> Bir Haftada İçtiğiniz Toplam Sigara Sayısı", value=f"{int(gunde_kac_tane.content) * 7} Tane", inline=True)
    embed.add_field(name=f"<a:sigara:854437179501182996> Bir Haftada Sigaraya Harcadığınız Toplam Para", value=f"{int(gunde_kac_tane.content) / 20 * int(paket_fiyati.content) * 7}", inline=True)    
    
    embed.add_field(name=f"<a:sigara:854437179501182996> Bir Ayda İçtiğiniz Toplam Sigara Sayısı", value=f"{int(gunde_kac_tane.content) * 30} Tane", inline=True)
    embed.add_field(name=f"<a:sigara:854437179501182996> Bir Ayda Sigaraya Harcadığınız Toplam Para", value=f"{int(gunde_kac_tane.content) / 20 * int(paket_fiyati.content) * 30} TL", inline=True)   

    embed.add_field(name=f"<a:sigara:854437179501182996> Bir Yılda İçtiğiniz Toplam Sigara Sayısı", value=f"{int(gunde_kac_tane.content) * 365} Tane", inline=True)
    embed.add_field(name=f"<a:sigara:854437179501182996> Bir Yılda Sigaraya Harcadığınız Toplam Para", value=f"{int(gunde_kac_tane.content) / 20 * int(paket_fiyati.content) * 365} TL", inline=True)   

    embed.add_field(name=f"<a:sigara:854437179501182996> {kac_yil.content} Yılda İçtiğiniz Toplam Sigara Sayısı", value=f"{int(gunde_kac_tane.content) * int(kac_yil.content) * 365} Tane", inline=False)
    embed.add_field(name=f"<a:sigara:854437179501182996> {kac_yil.content} Yılda Sigaraya Harcadığınız Toplam Para", value=f"{int(gunde_kac_tane.content) / 20 * int(paket_fiyati.content) * int(kac_yil.content) * 365} TL", inline=True)       

    await ctx.send(embed=embed)

@sigarahesapla.error
async def sigarahesapla_error(ctx, error): 
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'<:saat:867471142800457748> **Bu komutu kullanabilmek için {round(error.retry_after, 2)} saniye daha beklmelisin.**')

@bot.command()
async def embeds(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬▬[ 🔐 Gömülü Mesaj Komutu 🔐  ]▬▬▬▬▬▬",
        description="> :dizzy: **Gömülü mesaj komutunun nasıl kullanılacağını belirtir.**",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> :dizzy: **w!embed** <mesajınız>", inline=False)
    embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> :dizzy: **w!embed** Merhabalar {bot_yapımcısı} \n > :dizzy: **w!embed** Nasılsınız? \n > :dizzy: **w!embed** Kod yazıyorum. \n > :dizzy: **w!embed** İyiyim, yatıyorum öyle.", inline=False)
    
    embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
             
    await ctx.send(embed=embed)   

@bot.command()
async def covid(ctx):
    covid = Covid()
    covid.get_data()

    active = covid.get_total_active_cases()
    deaths = covid.get_total_deaths()
    recovered = covid.get_total_recovered()
    confirmed = covid.get_total_confirmed_cases()

    embed = discord.Embed(title="<:corona:863514892735610890> Corona Virüsü Komutu", description=f"Bütün Dünya'da şuana kadarki güncel corona virüs verileri size gösterilir.", color=62150)
    embed.add_field(name=f":microbe: Toplam Vaka Sayısı", value=f"{confirmed}", inline=True)
    embed.add_field(name=f":mask: Aktif Vaka Sayısı", value=f"{active}", inline=True)
    embed.add_field(name=f":skull_crossbones: Hayatını Kaybeden Kişi Sayısı", value=f"{deaths}", inline=True)
    embed.add_field(name=f":syringe: İyileşen Kişi Sayısı", value=f"{recovered}", inline=True)

    await ctx.send(embed=embed)


@bot.command()
async def sunucukomutları(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬▬[ 🔐 Sunucu Komutları 🔐  ]▬▬▬▬▬▬",
        description="> <:yesilok:843149816880037899> **w!serverinfo:** Sunucu hakkındaki bilgileri size gösterir. \n > _ _ \n > <:yesilok:843149816880037899> **w!sunucusahibi:** Sunucu sahibinin kim olduğunu size gösterir. \n > _ _ \n > <:yesilok:843149816880037899> **w!sunucudavet:** Bot, komutu kullandığınız sunucunun süresiz davet linkini size verir. \n > _ _ \n > <:yesilok:843149816880037899> **w!lock:** Komut sonrasında belirttiğiniz kanalı, everyone rolü için kilitler. \n > _ _ \n > <:yesilok:843149816880037899> **w!hide:** Komut sonrasında belirttiğiniz kanalı, everyone rolü için görünmez hale getirir. \n > _ _ \n > <:yesilok:843149816880037899> **w!emojiyükle:** Komut sonrasında belirttiğiniz ad ve emoji linkiyle, yeni bir emoji oluşturulur. \n > _ _ \n > <:yesilok:843149816880037899> **w!rol-ver:** Belirttiğiniz kişiye, belirttiğiniz rolü verir. \n > _ _ \n > <:yesilok:843149816880037899> **w!rol-al:** Belirttiğiniz kişinin, belirttiğiniz rolünü alır. \n > _ _ \n > <:yesilok:843149816880037899> **w!rol-oluştur:** Komut sonrasında belirttiğiniz adla bir rol oluşturur. \n > _ _ \n > <:yesilok:843149816880037899> **w!roller:** Sunuzunuzdaki bütün roller görüntülenir. \n > _ _ \n > <:yesilok:843149816880037899> **w!sunucukur:** Sunuzunuzdaki bütün kanal ve kategorileri silip yeni bir sunucu oluşturur. \n > _ _ \n > <:yesilok:843149816880037899> **w!sunucuyutemizle:** Sunuzunuzdaki bütün kanal ve kategorileri içindeki verilerle birlikte siler.  ",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **<:maviok:843149816401100832> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:maviok:843149816401100832> Botun Yazıldığı Dil:** **`Python`**", inline=False)


    await ctx.send(embed=embed)       


@bot.command()
async def kullanıcıkomutları(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬▬[ 🔐 Kullanıcı Komutları 🔐  ]▬▬▬▬▬▬",
        description="> <:yesilok:843149816880037899> **w!kullanıcı:** Kullanıcı hakkındaki bilgileri size gösterir. \n > _ _ \n > <:yesilok:843149816880037899> **w!avatar:** Belirttiğiniz kişinin profil fotoğrafını size verir. \n > _ _ \n > <:yesilok:843149816880037899> **w!yetkileri:** Belirttiğiniz kişinin yetkileri size gösterilir. \n > _ _ \n > <:yesilok:843149816880037899> **w!mail:** Belirttiğiniz mail adresinize, belirttiğiniz içerik gönderilir.  \n > _ _ \n > <:yesilok:843149816880037899> **w!mail:** Belirttiğiniz mail adresinize, belirttiğiniz içerik gönderilir. \n > _ _ \n > <:yesilok:843149816880037899> **w!instagram:**  Bot, komut sonrasında belirttiğiniz kullanıcı adının söz konusu platformdaki profil linkini size sunar. \n > _ _ \n > <:yesilok:843149816880037899> **w!facebook:**  Bot, komut sonrasında belirttiğiniz kullanıcı adının söz konusu platformdaki profil linkini size sunar. \n > _ _ \n > <:yesilok:843149816880037899> **w!twitter:**  Bot, komut sonrasında belirttiğiniz kullanıcı adının söz konusu platformdaki profil linkini size sunar. \n > _ _ \n > <:yesilok:843149816880037899> **w!twitch:**  Bot, komut sonrasında belirttiğiniz kullanıcı adının söz konusu platformdaki profil linkini size sunar. \n > _ _ \n > <:yesilok:843149816880037899> **w!github:**  Bot, komut sonrasında belirttiğiniz kullanıcı adının söz konusu platformdaki profil linkini size sunar. \n > _ _ \n > <:yesilok:843149816880037899> **w!şifreoluştur:**  Bot, kullanabileceğiniz bazı güçlü şifreler oluşturur.  \n > _ _ \n > <:yesilok:843149816880037899> **w!embeds:** Gömülü mesaj seçeneklerini size sunar.  ",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **<:maviok:843149816401100832> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:maviok:843149816401100832> Botun Yazıldığı Dil:** **`Python`**", inline=False)


    await ctx.send(embed=embed) 


@bot.command()
async def moderasyon(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬▬[ 🔐 Moderasyon Komutları 🔐  ]▬▬▬▬▬▬",
        description="> <:yesilok:843149816880037899> **w!sil:** Belirttiğiniz miktar kadar kolayca mesaj silmenizi sağlar. \n > _ _ \n > <:yesilok:843149816880037899> **w!nuke:** Komut sonrasında belirttiğiniz kanalı kopyalamanızı ve içindeki bütün mesajları silmenizi sağlar. \n > _ _ \n > <:yesilok:843149816880037899> **w!kick:** Belirttiğiniz kişiyi sunucudan kovar. \n > _ _ \n > <:yesilok:843149816880037899> **w!mute:** Belirttiğiniz kişiyi yazı kanallarından susturur. \n > _ _ \n > <:yesilok:843149816880037899> **w!ban:** Belirttiğiniz kullanıcıyı sunucudan yasaklar. \n > _ _ \n > <:yesilok:843149816880037899> **w!unban:** Belirttiğiniz kişinin yasaklaması kaldırılır. \n > _ _ \n > <:yesilok:843149816880037899> **w!unmute:** Belirttiğiniz kişinin yazı kanallarından susturulması kaldırılır.  \n > _ _ \n > <:yesilok:843149816880037899> **w!voicemute:** Belirttiğiniz kişiyi ses kanallarından susturur. \n > _ _ \n > <:yesilok:843149816880037899> **w!unvoicemute:** Belirttiğiniz kişinin ses kanallarından susturulmasını kaldırır. \n > _ _ \n > <:yesilok:843149816880037899> **w!kullanıcıadı:** Belirttiğiniz kullanıcının adını, kullanıcıyı belirttikten sonra yazdığınız kullanıcı adı olarak değiştirir. \n > _ _ \n > <:yesilok:843149816880037899> **w!uyar:** Belirttiğiniz kişiyi, belirttiğiniz nedenle uyarmanızı sağlar. ",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **<:maviok:843149816401100832> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:maviok:843149816401100832> Botun Yazıldığı Dil:** **`Python`**", inline=False)


    await ctx.send(embed=embed) 



@bot.command(aliases=['hesap', 'hesapmakinesi', 'hesap_makinesi'])
async def hesapla(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    icon = str(ctx.guild.icon_url)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬▬[ <:hesap:828358560923516938> Hesaplama Komutları <:hesap:828358560923516938>  ]▬▬▬▬▬▬",
        description="> <:yesilok:843149816880037899> **w!topla:** Bot belirttiğiniz iki sayıyı toplamanızı sağlar. \n > _ _ \n > <:yesilok:843149816880037899> **w!çıkart:** Bot belirttiğiniz iki sayıyı çıkarmanızı sağlar. \n > _ _ \n  > <:yesilok:843149816880037899> **w!çarp:** Bot belirttiğiniz iki sayıyı çarpmanızı sağlar. \n > _ _ \n > <:yesilok:843149816880037899> **w!böl:** Bot belirttiğiniz iki sayıyı bölmenizi sağlar",
        color=discord.Color.blue()
    )
    embed.add_field(name="▬▬▬▬▬▬▬[ <:hesap:828358560923516938> Komutun Kullanılışı <:hesap:828358560923516938>  ]▬▬▬▬▬▬", value="> <:maviok:843149816401100832> **w!topla** <birinci sayı> <ikinci sayı> \n > _ _ \n > <:maviok:843149816401100832> **w!çıkart** <birinci sayı> <ikinci sayı> \n > _ _ \n  > <:maviok:843149816401100832> **w!çarp** <birinci sayı> <ikinci sayı> \n > _ _ \n  > <:maviok:843149816401100832> **w!böl** <birinci sayı> <ikinci sayı>", inline=False)
    embed.add_field(name="▬▬▬▬▬▬▬[ <:hesap:828358560923516938> Komutun Örnekleri <:hesap:828358560923516938>  ]▬▬▬▬▬▬", value="> <:pembeok:843149816724848710> **w!topla** 5 5 \n > _ _ \n  > <:pembeok:843149816724848710> **w!çıkart** 10 5 \n > _ _ \n > <:pembeok:843149816724848710> **w!çarp** 10 10 \n > _ _ \n > <:pembeok:843149816724848710> **w!böl** 80 10", inline=False)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    
    await ctx.send(embed=embed)    


@bot.command() 
async def topla(ctx,a:int,b:int): await ctx.send(a+b)

@bot.command() 
async def çıkart(ctx,a:int,b:int): await ctx.send(a-b)

@bot.command() 
async def çarp(ctx,a:int,b:int): await ctx.send(a*b)

@bot.command() 
async def böl(ctx,a:int,b:int): await ctx.send(a/b)    


@bot.command()
async def şifreoluştur(ctx):
    user = ctx.message.author

    for p in range(number):
        password1 = ''
    for c in range(lenght):
        password1 += random.choice(chars)
    for p in range(number):
        password2 = ''
    for c in range(lenght):
        password2 += random.choice(chars) 
    for p in range(number):
        password3 = ''
    for c in range(lenght):
        password3 += random.choice(chars) 
    for p in range(number):
        password4 = ''
    for c in range(lenght):
        password4 += random.choice(chars)   
    for p in range(number):
        password5 = ''
    for c in range(lenght):
        password5 += random.choice(chars)                  

    embed = discord.Embed(title="Kullanabileceğiniz Bazı Şifreler", description=f"Bot, kullanabileceğiniz bazı güçlü şifreler oluşturur.", color=0x14ffd8)
    embed.add_field(name=f"\n\u200b", value=f"> :dizzy: **{password1}**", inline=False)
    embed.add_field(name=f"\n\u200b", value=f"> :dizzy: **{password2}**", inline=False)
    embed.add_field(name=f"\n\u200b", value=f"> :dizzy: **{password3}**", inline=False)
    embed.add_field(name=f"\n\u200b", value=f"> :dizzy: **{password4}**", inline=False)
    embed.add_field(name=f"\n\u200b", value=f"> :dizzy: **{password5}**", inline=False)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    embed1 = discord.Embed(title=f"<a:yesiltik:845932913806934036>  Şifreler Gönderildi", description=f"Olası şifreler, özel mesaj yoluyla size gönderildi.", color=62150)

    await ctx.send(embed=embed1)
    await user.send(embed=embed)


@bot.command(aliases=['sunucu-davet', 'sunucudaveti', 'sunucu-daveti'])
async def sunucudavet(ctx):
    invite = await ctx.channel.create_invite()
    await ctx.send(f"{invite}")  

@bot.command(aliases=['gömülü_mesaj', 'gömülü', 'gömülümesaj'])
async def embed(ctx, *, mesaj="Kullanıcı mesaj belirtmedi."):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="<:sohbet:829082123570249739>  Mesajınız", description=f"{mesaj}", color=0x00ff33)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


@bot.command()
async def rozetler(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="Özel Discord Rozetleri", description=f"\n > <:Verified:832162327452712990> Bot geliştiricilerine verilen rozettir. \n > <:Employee:832162327017029652> Discord çalışanlarına verilen rozettir.  \n > <:Partner:832162327650238504> Discord partnerlerine verilen rozettir.", color=7506393)
    embed.add_field(name="Genel Discord Rozetleri", value="\n > <:Nitro:832162327557439498> Discord Nitro sahibi üyelere verilen rozettir. \n > <:Early_Supporter:832162327289397278> 10 Ekim 2018 tarihinden önce nitro alan üyelere verilen rozettir.", inline=False)
    embed.add_field(name="Sunucu Takviyesi Rozetleri", value="\n > <:Boosting_Level_1:832162326664708096> Birinci seviye sunucu takviyesi rozetidir.  \n > <:Boosting_Level_2:832162326723297290> İkinci seviye sunucu takviyesi rozetidir.  \n > <:Boosting_Level_3:832162326370189383> Üçüncü seviye sunucu takviyesi rozetidir.  \n > <:Boosting_Level_4:832162326332571719> Dördüncü seviye sunucu takviyesi rozetidir.  \n > <:Boosting_Level_5:832162326550675517> Beşinci seviye sunucu takviyesi rozetidir.  \n > <:Boosting_Level_6:832162326445686785> Altıncı seviye sunucu takviyesi rozetidir. \n > <:Boosting_Level_7:832162326538223667> Yedinci seviye sunucu takviyesi rozetidir.  \n > <:Boosting_Level_8:832162326714253323> Sekizinci seviye sunucu takviyesi rozetidir.  \n  > <:Boosting_Level_9:832162327033937930> Dokuzuncu seviye sunucu takviyesi rozetidir.", inline=False)
    embed.add_field(name="Hata Avcısı Rozetleri", value="> <:Bughunter_Level1:832162327046520842> Birinci seviye hata avcılarına verilen rozettir. \n > <:Bughunter_Level2:832162327221895178> İkinci seviye hata avcılarına verilen rozettir.", inline=False)
    embed.add_field(name="Hype Squad Rozetleri", value="> <:HypeSquad_Events:832162327482073089> Hype Squad etkinliklerini düzenleyen kişilere verilen rozettir. \n > <:Brilliance:832162327095803924> Hype Squad Brilliance'e üye kişilere verilen rozettir. \n > <:Bravery:832162326810853376> Hype Squad Brave'e üye kişilere verilen rozettir. \n > <:Balance:832162326681223168> Hype Squad Balance'a üye kişilere verilen rozettir.", inline=False)
    

    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AAUvwniEUaBNWbH9Pk7A1cmIBdxnYt0YYrgNKx5h8grSMA=s900-c-k-c0x00ffffff-no-rj")
    await ctx.send(embed=embed)



@bot.command()
async def discordnedir(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="<:discord:826722461943988254> │ Discord Nedir", description=f"Gün geçtikçe popülerleşen profesyonel iletişim platformlarına benzer ücretsiz bir sohbet uygulamasıdır. Özellikle oyun oynayan kesimi ilgilendiren bu uygulama oyun oynarken arkadaşlarımız ile sesli bir şekilde oyunu koordine etmemizi sağlıyor. Sadece bununla sınırlı kalmayıp; Video görüşmeleri, sesli sohbet ve yazılı iletişimi destekler, kullanıcıların istedikleri gibi bir iletişim kurmalarına olanak tanır. İnsanlar arasında ortak bir bağ kuran bu uygulama sohbet, oyun, müzik, eğlence, iş ve daha bir çok topluluk kesimini kendi içinde barındırıyor. Aynı zamanda günümüzde sosyalleşmede ön planda kendini gösteriyor.", color=7506393)
    embed.add_field(name=":date: │ Discord Ne Zaman Kullanıma Sunuldu", value="Discord ilk defa 13 Mayıs 2015 tarihinde kullanıma sunuldu ancak son zamanlarda popülerleşmeye başladı.", inline=False)
    embed.add_field(name=":mortar_board: │ Discord'un Geliştiricisi", value="Oyuni içi sesli iletişimin zorunlu olduğunu, bununla birlikte Skype ve TeamSpeak gibi servislerin ise çok fazla negatif yanı olduğunu fark eden Jason Citron,  kullanımı daha kolay ve daha modern bir iletişim aracı olan Discord'u geliştirdi.", inline=False)
    

    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AAUvwniEUaBNWbH9Pk7A1cmIBdxnYt0YYrgNKx5h8grSMA=s900-c-k-c0x00ffffff-no-rj")
    await ctx.send(embed=embed)


@bot.command()
async def telegramnedir(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="<:telegram:826727507877298187> │ Telegram Nedir", description=f"Telegram, son zamanlarda hemen hemen herkesin kullanıdığı Whatsaap'ın kullanıcıları üzecek ve söz konusu platformdan soğutacak bir politika yayınlamasından sonra popülerleşmiştir. Bununla birlikte diğer mesajlaşma uygulamalarından farklı olarak bir çok özelliği bize sunan Telegram, aynı zamanda açık kaynak kodlu oluşuyla da bir çok kullanıcının beğenesini topladağını söylemekte fayda var. Telegram'ın farklı bir özelliğine değinecek olursak ise söz konusu uygulama neredeyse bütün platformları desteklemesi. Şuanlık Telegram'ın desteklediği platformlar ise Android, iOS, Windows, Linux ve OS X şeklinde.", color=2730219)
    embed.add_field(name=":date: │ Telegram Ne Zaman Kullanıma Sunuldu", value="Telegram, 14 Ağustos 2013 tarihinde piyasaya sürülmüştür.", inline=False)
    embed.add_field(name=":mortar_board: │ Telegram'ın Geliştiricisi", value="Git gide popülerleşen mesajlaşma uygulaması Telegram, Rus programcı Pavel Durov tarafından geliştirilmiştir.", inline=False)
    embed.add_field(name="<:github:836681551215067234> │ Telegram'ın Kaynak Kodu", value="Telegram açık kaynak kodlu bir uygulama olup, kaynak kodlarından Andriod için olanlara [buradan](https://github.com/DrKLO/Telegram), İOS için olanlara ise [buradan](https://github.com/TelegramMessenger/Telegram-iOS) ulaşabilirsiniz.", inline=False)
   

    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Telegram_2019_Logo.svg/512px-Telegram_2019_Logo.svg.png")
    await ctx.send(embed=embed)


@bot.command()
async def instagramnedir(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="<:insta:836695687910916116> │ İnstagram Nedir", description=f"Hemen hemen hepimizin en az bir kere duyduğu popüler sosyal medya platformu İnstagram, daha çok fotoğraf ve video paylaşımına dayanan bir sistemle hareket etmektedir. Bununla birlikte 1 Milyar indirme sayısını aştığı belirtilen söz konusu platform, aynı zamanda bir çok ödüle sahip olmuştur. Sonradan dev teknoloj şirketi Facebook tarafından 1 Milyar Dolara satın alınan söz konusu platform, şuanlık bir çok işletim sistemini destekliyor. ", color=9321658)
    embed.add_field(name=":date: │ İnstagram Ne Zaman Kullanıma Sunuldu", value="İnstagram 6 Ekim 2010 tarihinde piyasaya sürülmüştür.", inline=False)
    embed.add_field(name=":mortar_board: │ İnstagram'ın Geliştiricisi", value="Söz konusu uygulamanın orijinal sürümü Kevin Systrom ve Mike Kriege tarafından geliştirilmiştir ancak sonradan Facebook tarafından satın alınmıştır.", inline=False)

    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/150px-Instagram_logo_2016.svg.png")
    await ctx.send(embed=embed)


@bot.command()
async def facebooknedir(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="<:facebook:837627532849184768> │ Facebook Nedir", description=f"Muhtemelen hepimizin bildiği Facebook, en büyük sosyal medya platformlarından biridir. Metin ve fotoğraf paylaşımına dayanan Facebook'ta, bunların dışında çeşitli satışlara da ev sahipliği yapmaktadır. Bununla birlikte şuanlık genç kesim tarafından pek tercih edilmeyen Facebook, aynı zamanda bir çok sosyal medya platformunu satın almış olup şuan dünyanın en büyük şirketlerinden biridir. Şuanlık Facebook'un desteklediği platformlardan bazıları ise Android, İOS ve Windows şeklinde.", color=1669107)
    embed.add_field(name=":date: │ Facebook Ne Zaman Kullanıma Sunuldu", value="Facebook 2004 yılının Şubat ayında kullanıma sunulmuştur.", inline=False)
    embed.add_field(name=":mortar_board: │ Facebook'un Geliştiricisi", value="Söz konusu uygulama Mark Zuckenberg tarafından geliştirilmiştir.", inline=False)

    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://i.imgur.com/PpXkhTK.png")
    await ctx.send(embed=embed)



@bot.command()
async def whatsappnedir(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="<:WhatsApp:837273654932275201> │ Whatsaap Nedir", description=f"Akıllı telefon sahiplerinin hemen hemen hepsinin duyduğu ve kullandığı Whatsapp, muhtemelen hepimizin bildiği gibi bir mesajlaşma uygulamasıdır. Bununla birlikte beş milyardan fazla indirilen söz konusu uygulama, yakın zamanda bir çok kullancıyı platformdan soğutacak br gizlilik politikası yayınlamış ve bir çok kullanıcısnı kaybetmişttir. Söz konusu bu politika ardından kullanıcılar ise alternatif mesajlaşma uygulaması arayıp telegam, signal gibi yeni mesajlaşma uygulamaları ile tanışmıştır. ", color=5951582)
    embed.add_field(name=":date: │ Whatsaap Ne Zaman Kullanıma Sunuldu", value="Whatsapp ilk olarak 2009 yılının Şubat ayında kullanıma sunulmuştur.", inline=False)
    embed.add_field(name=":mortar_board: │ Whatsaap'ın Geliştiricisi", value="Söz konusu uygulamanın orijinal sürümü Jan Koum tarafından geliştirilmiştir ancak sonradan Facebook tarafından satın alınmıştır.", inline=False)

    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg")
    await ctx.send(embed=embed)


@bot.command()
async def youtubenedir(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="<:youtube:837358347576541195> │ Youtube Nedir", description=f"Yine hemen hemen hepimizin duyduğu ve en az bir kere ziyaret ettiği video barındırma platformu Youtube, ilk olarak bilindiğinin aksine hiç etkileşim almamıştır. Daha sonrasında dev teknloji şirketi Google söz konusu platformu satın almıştır ve bugün milyarlarca kullanıcı tarafdan kullanılmaktadır. Bununla birlikte içerik üreticilerine bir sürü kolaylık sağlayan Youtube, aynı zamanda içerik üreticilerin para kazanmasını da sağlamaktadır.", color=16646144)
    embed.add_field(name=":date: │ Youtube Ne Zaman Kullanıma Sunuldu", value="Youtube ilk olarak 15 Şubat 2005 tarihinde kullanıma sunulmuştur ancak o dönemlerde pek fazla etkileşim alamamıştır.", inline=False)
    embed.add_field(name=":mortar_board: │ Youtube'ın Geliştiricisi", value="Söz konusu platform, üç eski paypal çalışanı olan Steve Chen, Chad Hurley ve Jawed Karim tarafından geliştirilmiştir ancak sonradan Google tarafından satın alınmıştır.", inline=False)
    embed.add_field(name=":mag_right: │ Youtube Hakkında İlginç Bir Bilgi", value="Söz konusu uygulama Google tarafından 2006 yılında 1,68 Milyar Dolara satın alınmış olup, yine söz konusu uygulamadan şuan her üç haftada bir 1,68 Milyar Dolar gelir elde ediyor. ", inline=False)


    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://i.imgur.com/jEM7YA3.png")
    await ctx.send(embed=embed)


@bot.command()
async def twitchnedir(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="<:twitch:839574790746800169> │ Twitch Nedir", description=f"Son zamanlarda popülerleşen Twitch, bazılarımızın bildiği gibi bir yayın platformudur. Bununla birlikte Twitch, en yaygın yayın platformlardan biri olmakla birlikte aynı zamanda söz konusu yayıncıların para kazanmasını da sağlamaktadır. İzleyicilerin yayıncıya bağış göndermesi olarak para elde ediilen söz konusu bu platformun günlük izleyici sayısı 15 milyon, aylık kullanıcı sayısı ise 140 milyon olarak belirlendi. ", color=5848709)
    embed.add_field(name=":date: │ Twitch Ne Zaman Kullanıma Sunuldu", value="Twitch, 2011 yılının Haziran ayında kullanıma sunulmuştur.", inline=False)
    embed.add_field(name=":mortar_board: │ Twitch'in Geliştiricisi", value="Söz konusu platform, Justin Kan ve Emmett Shear tarafından geliştirilmiştir ancak sonradan Amozon tarafından satın alınmıştır.", inline=False)
    embed.add_field(name=":mag_right: │ Twitch Hakkında İlginç Bir Bilgi", value="Twitch, 2014 yılının Şubat ayında ABD'deki internet trafiğinin en büyük dördüncü kaynağı olarak belirlenmiştir.", inline=False)


    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://i.imgur.com/lz0El0g.png")
    await ctx.send(embed=embed)


@bot.command()
async def twitternedir(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="<:twitter:837410138004389938> │ Twitter Nedir", description=f"Twitter, kullanıcıların daha çok yazı ve metin alanında paylaşım yaptığı çok yaygın platormlardan biridir. Bununla birlikte resmi makamların çeşitli duyrularını ilk olarak yayınladığı bir platorm olan Twitter, bu alanda diğer sosyal medya platformlarından bir adım öne çıkıyor. Aynı zamanda özüyle kalıp hiç bir şirkete satılmayan Twitter, 2020 yılında 339.6 Milyon kullanıcıya ulaştı. ", color=44270)
    embed.add_field(name=":date:│ Twitter Ne Zaman Kullanıma Sunuldu", value="Twitter ilk olarak 2006 yılının Temmmuz ayında kullanıma sunulmuştur.", inline=False)
    embed.add_field(name=":mortar_board: │ Twitter'ın Geliştiricisi", value="Twitter Jack Dorsey, Noah Glass, Biz Stone, ve Evan Williams tarafından geliştirilmiştir.", inline=False)

    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://i.imgur.com/v1Hl6yX.png")
    await ctx.send(embed=embed)


@bot.command(aliases=['hacktools'])
async def hackaraçları(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="<:bilgi:830857146702888961> Hack Tolları", description=f"Bot, bazı yaygın hack tool'larını size sunar.", color=9321658)
    embed.add_field(name="<:bilgisayar:837240220604825600> IP Scan Araçları", value="Angry IP Scanner ➠ [Tıkla](https://www.turkhackteam.org/web-server-guvenligi-ve-zafiyetler/1960149-angry-ip-scanner-anlatimi-kurulumu.html) \n Router Scan ➠ [Tıkla](https://www.turkhackteam.org/web-server-guvenligi-ve-zafiyetler/1957111-router-scan-ulkenizdeki-kameralari-ve-admin-panellerini-hackleyin.html) \n Nmap ➠ [Tıkla](https://nmap.org/)", inline=False)
    embed.add_field(name="<:bilgisayar:837240220604825600> Port Scan Araçları", value="Advanced Port Scanner ➠ [Tıkla](https://www.advanced-port-scanner.com/tr/) \n Nmap ➠ [Tıkla](https://nmap.org/) \n Zenmap ➠ [Tıkla](https://nmap.org/zenmap/)                                                            ", inline=False)
    embed.add_field(name="<:bilgisayar:837240220604825600> Admin Paneli Bulma Araçları", value="DW Admin Panel Bulucu ➠ [Tıkla](https://www.turkhackteam.org/web-server-guvenligi-ve-zafiyetler/1960085-dw-admin-panel-bulucu.html) \n Admin Panel Bulucu Python ➠ [Tıkla](https://www.turkhackteam.org/web-server-guvenligi-ve-zafiyetler/1960093-admin-panel-bulucu-python.html)", inline=False)
    embed.add_field(name="<:bilgisayar:837240220604825600> SQL İnjection Araçları", value="Sqlmap ➠ [Tıkla](https://www.turkhackteam.org/web-server-guvenligi-ve-zafiyetler/1601616-sqlmap-ile-sql-injection-hack-windows-cmd-uzerinden-veteran-7-a.html) \n Havij ➠ [Tıkla](https://www.turkhackteam.org/web-server-guvenligi-ve-zafiyetler/902123-havij-1-16-pro.html)", inline=False)
    embed.add_field(name="<:bilgisayar:837240220604825600> Dork Scanner Araçları", value="Katana ➠ [Tıkla](https://www.turkhackteam.org/web-server-guvenligi-ve-zafiyetler/1960946-katana-dork-scanner.html) \n T-Arayıcı ➠ [Tıkla](https://www.turkhackteam.org/web-server-guvenligi-ve-zafiyetler/1306921-t-arayici-v2-0-sql-acik-tarama-araci-dork-sql-acik-tarama.html) \n Dark-7 Tarayıcı ➠ [Tıkla](https://www.turkhackteam.org/web-server-guvenligi/1036748-dark-7-scanner-dork-sql-injection-tarayici.html)", inline=False)
    embed.add_field(name="<:bilgisayar:837240220604825600> Phishing Araçları", value="Blackeye ➠ [Tıkla](https://github.com/An0nUD4Y/blackeye) \n Hidden Eye ➠ [Tıkla](https://github.com/DarkSecDevelopers/HiddenEye-Legacy) \n Nexphisher ➠ [Tıkla](https://github.com/htr-tech/nexphisher) \n Zphisher ➠ [Tıkla](https://github.com/htr-tech/zphisher)",  inline=False)
    embed.add_field(name="<:bilgisayar:837240220604825600> SMS Bomber", value="TBomb ➠ [Tıkla](https://www.turkhackteam.org/web-server-guvenligi-ve-zafiyetler/1960954-sms-bomber-t-bomber.html) \n Impulse ➠ [Tıkla](https://www.turkhackteam.org/web-server-guvenligi-ve-zafiyetler/1960975-ozel-hack-araci-impulse.html) ",  inline=False)
    
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/830857146702888961.png?v=1")
    await ctx.send(embed=embed)



@commands.has_permissions(administrator=True)
@bot.command()
async def uyar(ctx, user: discord.Member, *, mesaj="Uyarılma nedeniniz söz konusu moderatör tarafından belitilmemiş."):
    icon = str(ctx.guild.icon_url)

    embed1 = discord.Embed(title="<a:yesiltik:845932913806934036>  Kullanıcı Uyarıldı", description=f"Belirttiğiniz kişi başarıyla uyarıldı.", color=62150)
    embed1.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed1)

    embed = discord.Embed(title=":warning: Uyarı", description=f"Merhabalar, yakın zamanda {ctx.guild.name} adlı sunucuda {ctx.author.display_name} adlı kişi tarafından uyarıldınız. Lütfen bir dahaki sefere daha dikkatli olunuz. ", color=0xff0000)
    embed.add_field(name=":warning: Nedeni", value=f"{mesaj}", inline=False)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await user.send(embed=embed)  

@uyar.error
async def uyar_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")      
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 
    


@commands.has_permissions(manage_nicknames=True)
@bot.command(aliases=['ad', 'nick', 'kullanıcıadı', 'adıdeğiştir'], pass_context=True)
async def nickname(ctx, member: discord.Member, *, nick):
    await member.edit(nick=nick)
    await ctx.send(f'{member.mention} adlı kullanıcının kullanıcı adı, belirttiğiniz ad ile değiştirildi.')

@nickname.error
async def nickname_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")           
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 
    if isinstance(error, commands.MissingRequiredArgument):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Nickname Değiştirme Komutu 🔐  ]▬▬▬▬▬▬",
            description="> :dizzy: Görünüşe bakılırsa bu komutu yanlış kullanmısınız. İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> :dizzy: **w!nickname** <kullanıcı> <yeni-ad>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> :dizzy: **w!nickname** {ctx.author.mention} Sunucu Kurucusu \n > :dizzy: **w!nickname** {ctx.author.mention} Sunucu Admin'i \n  > :dizzy: **w!nickname** {ctx.author.mention} Sunucu Moderatörü \n > :dizzy: **w!nickname** {ctx.author.mention} Cezalı Üye \n ", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
         
        await ctx.send(embed=embed)  


@bot.command()
async def yetkileri(ctx, member: discord.Member = None):
    icon = str(ctx.guild.icon_url)

    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author

    embed = discord.Embed(title="", description="", color=0x14ffd8)
    embed.set_author(name=member.display_name, url="", icon_url=member.avatar_url)

    if member.guild_permissions.administrator == True:
       embed.add_field(name="Yönetici", value="Evet", inline=False)
    else:   
       embed.add_field(name="Yönetici", value="Hayır", inline=False)  

    if member.guild_permissions.kick_members == True:
       embed.add_field(name="Üyeleri At", value="Evet", inline=False)
    else:   
       embed.add_field(name="Üyeleri At", value="Hayır", inline=False)   

    if member.guild_permissions.ban_members == True:
       embed.add_field(name="Üyeleri Yasakla", value="Evet", inline=False)
    else:   
       embed.add_field(name="Üyeleri Yasakla", value="Hayır", inline=False)  

    if member.guild_permissions.manage_channels == True:
       embed.add_field(name="Kanalları Yönet", value="Evet", inline=False)
    else:   
       embed.add_field(name="Kanalları Yönet", value="Hayır", inline=False)   

    if member.guild_permissions.manage_messages == True:
       embed.add_field(name="Mesajları Yönet", value="Evet", inline=False)
    else:   
       embed.add_field(name="Mesajları Yönet", value="Hayır", inline=False)          
       
    if member.guild_permissions.manage_roles == True:
       embed.add_field(name="Rolleri Yönet", value="Evet", inline=False)
    else:   
       embed.add_field(name="Rolleri Yönet", value="Hayır", inline=False)   

    if member.guild_permissions.view_audit_log == True:
       embed.add_field(name="Denetim Kaydını Görüntüle", value="Evet", inline=False)
    else:   
       embed.add_field(name="Denetim Kaydını Görüntüle", value="Hayır", inline=False)  

    if member.guild_permissions.manage_nicknames == True:
       embed.add_field(name="Kullanıcı Adlarını Yönet", value="Evet", inline=False)
    else:   
       embed.add_field(name="Kullanıcı Adlarını Yönet", value="Hayır", inline=False)     

    if member.guild_permissions.manage_emojis == True:
       embed.add_field(name="Emojileri Yönet", value="Evet", inline=False)
    else:   
       embed.add_field(name="Emojileri Yönet", value="Hayır", inline=False)  

    await ctx.send(embed=embed)   


@yetkileri.error
async def yetkileri_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen yetkilerini görmek istediğiniz kişiyi, komut sonrasında etiketleyerek belirtiniz. ')


@bot.command()
async def yetkilerim(ctx):
    member = ctx.message.author  

    embed = discord.Embed(title="", description="", color=0x14ffd8)
    embed.set_author(name=member.display_name, url="", icon_url=member.avatar_url)

    if member.guild_permissions.administrator == True:
       embed.add_field(name="Yönetici", value="Evet", inline=False)
    else:   
       embed.add_field(name="Yönetici", value="Hayır", inline=False)  

    if member.guild_permissions.kick_members == True:
       embed.add_field(name="Üyeleri At", value="Evet", inline=False)
    else:   
       embed.add_field(name="Üyeleri At", value="Hayır", inline=False)   

    if member.guild_permissions.ban_members == True:
       embed.add_field(name="Üyeleri Yasakla", value="Evet", inline=False)
    else:   
       embed.add_field(name="Üyeleri Yasakla", value="Hayır", inline=False)  

    if member.guild_permissions.manage_channels == True:
       embed.add_field(name="Kanalları Yönet", value="Evet", inline=False)
    else:   
       embed.add_field(name="Kanalları Yönet", value="Hayır", inline=False)   

    if member.guild_permissions.manage_messages == True:
       embed.add_field(name="Mesajları Yönet", value="Evet", inline=False)
    else:   
       embed.add_field(name="Mesajları Yönet", value="Hayır", inline=False)          
       
    if member.guild_permissions.manage_roles == True:
       embed.add_field(name="Rolleri Yönet", value="Evet", inline=False)
    else:   
       embed.add_field(name="Rolleri Yönet", value="Hayır", inline=False)   

    if member.guild_permissions.view_audit_log == True:
       embed.add_field(name="Denetim Kaydını Görüntüle", value="Evet", inline=False)
    else:   
       embed.add_field(name="Denetim Kaydını Görüntüle", value="Hayır", inline=False)  

    if member.guild_permissions.manage_nicknames == True:
       embed.add_field(name="Kullanıcı Adlarını Yönet", value="Evet", inline=False)
    else:   
       embed.add_field(name="Kullanıcı Adlarını Yönet", value="Hayır", inline=False)     

    if member.guild_permissions.manage_emojis == True:
       embed.add_field(name="Emojileri Yönet", value="Evet", inline=False)
    else:   
       embed.add_field(name="Emojileri Yönet", value="Hayır", inline=False)  

    await ctx.send(embed=embed)   


@bot.command(aliases=['mail-gönder', 'mailgönder'])
@commands.cooldown(1, 600, commands.BucketType.user)
async def mail(ctx, alici, *, içerik):
    port = 465 
    smtp_server = "smtp.gmail.com"
    sender_email = "wersefdiscordbotu@gmail.com"
    receiver_email = f"{alici}"
    password = "*/wersefyagiz1342+/"
    message = f"""\
    Wersef Discord Botu

    Konu: {str(ctx.author)} Kisisinden Wersef Discord Botuyla Size Gonderilmis Mesaj:
    
    {içerik}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


    embed = discord.Embed(title="<a:yesiltik:845932913806934036> Mail'iniz Gönderildi", description=f"Belirttiğiniz mesaj, belirttiğiniz e-mail adresine iletildi.", color=62150)
    embed.add_field(name=f"<:sohbet:829082123570249739> Mesajınızın İçeriği", value=f"{içerik}", inline=True)
    embed.add_field(name=f":e_mail: Mesaj Gönderilen Mail Adresi", value=f"{alici}", inline=True)

    await ctx.send(embed=embed)     

@mail.error
async def mail_error(ctx, error): 
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Mail Gönderme Komutu 🔐  ]▬▬▬▬▬▬",
            description="> **<:maviok:837983169579712532> Görünüşe bakılırsa bu komutu yanlış kullanmısınız.** \n > _ _ \n > **<:maviok:837983169579712532> İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:**",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> <:yesilok:771731154159796241> **w!mail** <mail adresi> <mail içeriği>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> <:yesilok:771731154159796241> **w!mail** wersefdiscordbotu@gmail.com Merhaba Wersef. \n > _ _ \n > <:yesilok:771731154159796241> **w!mail** wersefdiscordbotu@gmail.com Wersef çok iyi bir bot. \n > _ _ \n > <:yesilok:771731154159796241> **w!mail** wersefdiscordbotu@gmail.com Selam yapımcım. \n > _ _ \n > <:yesilok:771731154159796241> **w!mail** wersefdiscordbotu@gmail.com Yapımcım çok iyi biri. ", inline=False)

        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
               
        await ctx.send(embed=embed)
    
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Mail Gönderme Komutu 🔐  ]▬▬▬▬▬▬",
            description="> **<:maviok:837983169579712532> Görünüşe bakılırsa bu komutu yanlış kullanmısınız.** \n > _ _ \n > **<:maviok:837983169579712532> İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:**",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> <:yesilok:771731154159796241> **w!mail** <mail adresi> <mail içeriği>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> <:yesilok:771731154159796241> **w!mail** wersefdiscordbotu@gmail.com Merhaba Wersef. \n > _ _ \n > <:yesilok:771731154159796241> **w!mail** wersefdiscordbotu@gmail.com Wersef çok iyi bir bot. \n > _ _ \n > <:yesilok:771731154159796241> **w!mail** wersefdiscordbotu@gmail.com Selam yapımcım. \n > _ _ \n > <:yesilok:771731154159796241> **w!mail** wersefdiscordbotu@gmail.com Yapımcım çok iyi biri. ", inline=False)

        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
               
        await ctx.send(embed=embed)        

    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'<:saat:867471142800457748> **Bu komutu kullanabilmek için {round(error.retry_after, 2)} saniye daha beklmelisin.**')


@bot.command()
async def linkkısalt(ctx, url):
    user_url = f"{url}"
    header = {
        "Authorization": "Bearer bd92e32d4f8312cba7a49b128db4e326c689dc74 ",
        "Content-Type": "application/json"
    }
    params = {
        "long_url": str(user_url)
    }

    response = requests.post("https://api-ssl.bitly.com/v4/shorten", json=params, headers=header)
    kisa_url  = response.json()["link"]
    orjinal_url  = response.json()["long_url"]

    embed = discord.Embed(title="<:nametag:841951946650812426> │ Link Kısaltma", description="Bot, komut sonrasında belirttiğiniz linki kolay bir şekilde kısaltır.", color=0x14ffd8)
    embed.add_field(name=f"🔗 │ Asıl Link", value=f"{url}", inline=True)
    embed.add_field(name=f"🔗 │ Kısaltılmış Link", value=f"{kisa_url}", inline=True)

    await ctx.send(embed=embed)      

@linkkısalt.error
async def linkkısalt_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen kısaltmak istedğiniz link komut sonrasında belirtiniz. ') 

@bot.command()
async def komutlarçalışmıyor(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title=":question: │ Komutlar Çalışmıyor", description=f"Bu sorunu dile getiren genellikle her kisi bu sorunu söz konusu bota yetki vermediği için yaşıyor. Özellikle moderasyon komutlarında yaşanan bu sorunun en basit çözümü, bota gerekli yetkileri vermektir.", color=0x007bff)
    embed.add_field(name=":question: │ Komutlar Hâlâ Çalışmıyor", value="Böyle bir şey yukarıda belirttiğimiz şeyleri yaptıysanız mümkün değildir. Ancak bir diğer etken ise botun rol sırasıdır. Bot, kendinden yüksek rollere müdahele edememektedir. Bu yüzden botun rol sırasını olabildiğince yüksek yapmanız önerilir.", inline=False)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)    

@bot.command()
async def önemligünler(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="Önemli Günler", description=f":tada: ** 1 Ocak Yılbaşı** \n 🇹🇷 **8 Mart Dünya Kadınlar Günü** \n 🇹🇷 **23 Nisan Ulusal Egemenlik ve Çocuk Bayramı** \n 🇹🇷 **1 Mayıs Emek ve Dayanışma Günü** \n 🇹🇷 **9 Mayıs Dünya Anneler Günü** \n 🇹🇷 **19 Mayıs Atatürk'ü Anma Gençlik ve Spor Bayramı** \n 🇹🇷 **20 Haziran Babalar Günü**  \n 🇹🇷 **30 Ağustos Zafer Bayramı** \n 🇹🇷 **29 Ekim Cumhuriyet Bayramı** \n 🇹🇷 **10 kasım Atatürk'ü Anma Günü**", color=0xff1a1a)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)   


@commands.has_permissions(manage_roles=True)
@bot.command(pass_context=True, aliases=['rol-oluştur', 'createrole', 'create-role'])
async def rololuştur(ctx, roladı):
    description = str(ctx.guild.description)
    embed = discord.Embed(title="<a:yesiltik:845932913806934036>  Rol Oluşturuldu", description=f"Belirttiğiniz rol başarıyla oluşturuldu.", color=62150)

    await ctx.send(embed=embed)
    whatRole = await ctx.guild.create_role(name=f"{roladı}")


@rololuştur.error
async def rololuştur_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")  
    if isinstance(error, commands.MissingRequiredArgument):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Rol Oluşturma Komutu 🔐  ]▬▬▬▬▬▬",
            description="> :dizzy: Görünüşe bakılırsa bu komutu yanlış kullanmışınız. İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> :dizzy: **w!rol-oluştur** <rolünüz>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> :dizzy: **w!rol-oluştur** Admin \n > :dizzy: **w!rol-oluştur** Moderatör \n > :dizzy: **w!rol-oluştur** Denetmen \n > :dizzy: **w!rol-oluştur** VIP ", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
         
        await ctx.send(embed=embed)  
         
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.')  


@bot.command()
async def nitro(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="<:discord:826722461943988254> │ Discord Nitro Seçenekleri", description=f"Çoğumuzun bildiği kadarıyla Discord nitro sahibi kullanıcılar, diğer kullanıcılardan farklı olarak bazı ayrıcılıklara sahip oluyor. Bununla birlikte iki seçenek olarak sunulan Discord nitro seçenekleri bulunmakta.      ", color=7506393)
    embed.add_field(name="<:nitro:845932912650092545> │ Nitro Classic (5 Dolar)", value="\n \n **● Hareketli Avatar Kullanma Hakkı** \n \n **● Discord Etiketini Değiştirme Hakkı** \n \n ● **Özelleştirilmiş Emojileri Kullanma Hakkı** \n \n **● Hareketli Emojileri Kullanma Hakkı** \n \n **● 50 MB'ya Kadar Dosya Yükleyebilme Hakkı** \n \n **● Yüksek Kaliteli Ekran Paylaşabilme Hakkı**     ", inline=False)
    embed.add_field(name="<a:nitroboost:845932913840226364> │ Nitro Boost (10 Dolar)", value="\n \n **● İki Kere Sunucu Takviyesi Yapma Hakkı**  \n \n **● Hareketli Avatar Kullanma Hakkı** \n \n **● Discord Etiketini Değiştirme Hakkı** \n \n ● **Özelleştirilmiş Emojileri Kullanma Hakkı** \n \n **● Hareketli Emojileri Kullanma Hakkı** \n \n **● 100 MB'ya Kadar Dosya Yükleyebilme Hakkı** \n \n **● Yüksek Kaliteli Ekran Paylaşabilme Hakkı** \n \n **● Daha Fazla Sunucuya Katılma Hakkı** \n \n **● Daha Uzun Mesajlar Yazma Hakkı** \n \n **● Profil Afişini Düzenleme Hakkı**", inline=False)
   

    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AAUvwniEUaBNWbH9Pk7A1cmIBdxnYt0YYrgNKx5h8grSMA=s900-c-k-c0x00ffffff-no-rj")
    await ctx.send(embed=embed)



@commands.has_permissions(manage_emojis=True)
@bot.command(pass_context=True, aliases=['emoji-yükle', 'uploademoji', 'upload-emoji']) 
async def emojiyükle(ctx, name, url): 
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}') as response:
            img = await response.read()    
    await ctx.guild.create_custom_emoji(name=f'{name}', image=img)
    embed = discord.Embed(title=f"<a:yesiltik:845932913806934036>  Emoji Oluşturuldu", description=f"**`{name}`** Adlı Emoji Başarıyla Sunucuya Yüklendi", color=62150)
    embed.set_thumbnail(url=url)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    await ctx.channel.send(embed=embed)


@emojiyükle.error
async def emojiyükle_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için gerekli yetkilere sahip değilsin.")           
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 
    if isinstance(error, commands.MissingRequiredArgument):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
    
        embed = discord.Embed(
            title="▬▬▬▬▬▬▬[ 🔐 Emoji Yükleme Komutu 🔐  ]▬▬▬▬▬▬",
            description="> :dizzy: Görünüşe bakılırsa bu komutu yanlış kullanmısınız. İşte bu komutu nasıl kullanacağınız hakkında bazı bilgiler:",
            color=discord.Color.blue()
        )
        embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> :dizzy: **w!emojiyükle** <ad> <emoji-linki>", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value=f"> :dizzy: **w!emojiyükle** Emoji https://emoji.gif \n > :dizzy: **w!emojiyükle** Emoji https://emoji.png \n > :dizzy: **w!emojiyükle** Emoji https://emoji.jpg \n > :dizzy: **w!emojiyükle** Emoji https://emojil.jpeg", inline=False)
    
        embed.add_field(name="▬▬▬▬▬▬▬[ ⚙️ Genel Bilgilendirme ⚙️ ]▬▬▬▬▬▬", value="> **<:pembeok:837983496143896606> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:837983496143896606> Botun Yazıldığı Dil:** **`Python`**", inline=False)
         
        await ctx.send(embed=embed)     


@bot.command()
async def instagram(ctx, kullanıcıadı):
    description = str(ctx.guild.description)
    embed = discord.Embed(title="<:nametag:841951946650812426> │ Kullanıcı Profili", description="Bot, komut sonrasında belirttiğiniz kullanıcı adının söz konusu platformdaki profil linkini size sunar.", color=0x14ffd8)
    embed.add_field(name=f"👤 │ Kullanıcı Adı", value=kullanıcıadı, inline=True)
    embed.add_field(name=f"🔗 │ Profil Linki", value=f"[Tıkla](https://www.instagram.com/{kullanıcıadı}/)", inline=True)

    await ctx.send(embed=embed) 

@instagram.error
async def instagram_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen profilini görmek istediğiniz kişiyi komut sonrasıda kullanıcı adını yazarak belirtiniz.') 


@bot.command()
async def facebook(ctx, kullanıcıadı):
    description = str(ctx.guild.description)
    embed = discord.Embed(title="<:nametag:841951946650812426> │ Kullanıcı Profili", description="Bot, komut sonrasında belirttiğiniz kullanıcı adının söz konusu platformdaki profil linkini size sunar.", color=0x14ffd8)
    embed.add_field(name=f"👤 │ Kullanıcı Adı", value=kullanıcıadı, inline=True)
    embed.add_field(name=f"🔗 │ Profil Linki", value=f"[Tıkla](https://www.facebook.com/{kullanıcıadı}/)", inline=True)

    await ctx.send(embed=embed) 

@facebook.error
async def facebook_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen profilini görmek istediğiniz kişiyi komut sonrasıda kullanıcı adını yazarak belirtiniz.') 


@bot.command()
async def twitter(ctx, kullanıcıadı):
    description = str(ctx.guild.description)
    embed = discord.Embed(title="<:nametag:841951946650812426> │ Kullanıcı Profili", description="Bot, komut sonrasında belirttiğiniz kullanıcı adının söz konusu platformdaki profil linkini size sunar.", color=0x14ffd8)
    embed.add_field(name=f"👤 │ Kullanıcı Adı", value=kullanıcıadı, inline=True)
    embed.add_field(name=f"🔗 │ Profil Linki", value=f"[Tıkla](https://www.twitter.com/{kullanıcıadı})", inline=True)

    await ctx.send(embed=embed) 

@twitter.error
async def twitter_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen profilini görmek istediğiniz kişiyi komut sonrasıda kullanıcı adını yazarak belirtiniz.')   



@bot.command()
async def twitch(ctx, kullanıcıadı):
    description = str(ctx.guild.description)
    embed = discord.Embed(title="<:nametag:841951946650812426> │ Kullanıcı Profili", description="Bot, komut sonrasında belirttiğiniz kullanıcı adının söz konusu platformdaki profil linkini size sunar.", color=0x14ffd8)
    embed.add_field(name=f"👤 │ Kullanıcı Adı", value=kullanıcıadı, inline=True)
    embed.add_field(name=f"🔗 │ Profil Linki", value=f"[Tıkla](https://www.twitch.tv/{kullanıcıadı})", inline=True)

    await ctx.send(embed=embed) 

@twitch.error
async def twitch_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen profilini görmek istediğiniz kişiyi komut sonrasıda kullanıcı adını yazarak belirtiniz.')   


@bot.command()
async def telegram(ctx, kullanıcıadı):
    description = str(ctx.guild.description)
    embed = discord.Embed(title="<:nametag:841951946650812426> │ Kullanıcı Profili", description="Bot, komut sonrasında belirttiğiniz kullanıcı adının söz konusu platformdaki profil linkini size sunar.", color=0x14ffd8)
    embed.add_field(name=f"👤 │ Kullanıcı Adı", value=kullanıcıadı, inline=True)
    embed.add_field(name=f"🔗 │ Profil Linki", value=f"[Tıkla](https://t.me/{kullanıcıadı})", inline=True)

    await ctx.send(embed=embed) 

@telegram.error
async def telegram_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen profilini görmek istediğiniz kişiyi komut sonrasıda kullanıcı adını yazarak belirtiniz.')   


@bot.command()
async def github(ctx, kullanıcıadı):
    description = str(ctx.guild.description)
    embed = discord.Embed(title="<:nametag:841951946650812426> │ Kullanıcı Profili", description="Bot, komut sonrasında belirttiğiniz kullanıcı adının söz konusu platformdaki profil linkini size sunar.", color=0x14ffd8)
    embed.add_field(name=f"👤 │ Kullanıcı Adı", value=kullanıcıadı, inline=True)
    embed.add_field(name=f"🔗 │ Profil Linki", value=f"[Tıkla](https://www.github.com/{kullanıcıadı})", inline=True)

    await ctx.send(embed=embed) 

@github.error
async def github_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen profilini görmek istediğiniz kişiyi komut sonrasıda kullanıcı adını yazarak belirtiniz.')             

# Otamatik Cevaplar

@bot.listen('on_message')
async def hi(message):
    if message.content == '<@!819743355663548447>':

        embed = discord.Embed(
        title=f"▬▬▬▬▬▬[ :dizzy: {bot_adı} :dizzy: ]▬▬▬▬▬▬   ",
        description=f"> <:maviok:843149816401100832> **Botun Destek Sunucusu:** [Tıkla]({destek_sunucusu}) \n > _ _ \n > <:maviok:843149816401100832> **Botun Davet Bağlantısı:** [Tıkla]({önerilen_yetki_davet})",
        color=discord.Color.blue()
        ) 
        
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Wersef Prefixler 🔐  ]▬▬▬▬▬▬", value="> <:yesilok:843149816880037899> **`w!`** \n > _ _ \n > <:yesilok:843149816880037899> <@!819743355663548447> ", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **<:pembeok:843149816724848710> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:843149816724848710> Botun Yazıldığı Dil:** **`Python`**", inline=False)
        embed.set_author(name=message.author.display_name, url="", icon_url=message.author.avatar_url)       

        await message.channel.send(embed=embed)

    if message.content == 'w!':

        embed = discord.Embed(
        title=f"▬▬▬▬▬▬[ :dizzy: {bot_adı} :dizzy: ]▬▬▬▬▬▬   ",
        description=f"> <:maviok:843149816401100832> **Botun Destek Sunucusu:** [Tıkla]({destek_sunucusu}) \n > _ _ \n > <:maviok:843149816401100832> **Botun Davet Bağlantısı:** [Tıkla]({önerilen_yetki_davet})",
        color=discord.Color.blue()
        ) 
        
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Wersef Prefixler 🔐  ]▬▬▬▬▬▬", value="> <:yesilok:843149816880037899> **`w!`** \n > _ _ \n > <:yesilok:843149816880037899> <@!819743355663548447> ", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **<:pembeok:843149816724848710> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:843149816724848710> Botun Yazıldığı Dil:** **`Python`**", inline=False)
        embed.set_author(name=message.author.display_name, url="", icon_url=message.author.avatar_url)       

        await message.channel.send(embed=embed)

    if message.content == 'W!':

        embed = discord.Embed(
        title=f"▬▬▬▬▬▬[ :dizzy: {bot_adı} :dizzy: ]▬▬▬▬▬▬   ",
        description=f"> <:maviok:843149816401100832> **Botun Destek Sunucusu:** [Tıkla]({destek_sunucusu}) \n > _ _ \n > <:maviok:843149816401100832> **Botun Davet Bağlantısı:** [Tıkla]({önerilen_yetki_davet})",
        color=discord.Color.blue()
        ) 
        
        embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Wersef Prefixler 🔐  ]▬▬▬▬▬▬", value="> <:yesilok:843149816880037899> **`w!`** \n > _ _ \n > <:yesilok:843149816880037899> <@!819743355663548447> ", inline=False)
        embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **<:pembeok:843149816724848710> Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > _ _ \n > **<:pembeok:843149816724848710> Botun Yazıldığı Dil:** **`Python`**", inline=False)
        embed.set_author(name=message.author.display_name, url="", icon_url=message.author.avatar_url)       

        await message.channel.send(embed=embed)     

    if  "Wersef" in message.content:  
        if message.author.id == 819743355663548447:
            return    
        else:
            await message.channel.send("<:goz:859374017264746516>")   
    if  "wersef" in message.content:  
        if message.author.id == 819743355663548447:
            return    
        else:
            await message.channel.send("<:goz:859374017264746516>")            

# Otamatik Cevaplar Sonu     


@bot.command()
async def doviz(ctx):

    bitcoin_get = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCTRY")
    bitcoin = json.loads(bitcoin_get.text)

    ethereum_get = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETHTRY")
    ethereum = json.loads(ethereum_get.text)  

    bnb_get = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BNBTRY")
    bnb = json.loads(bnb_get.text) 

    shib_get = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=SHIBTRY")
    shib = json.loads(shib_get.text)

    sxp_get = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=SXPTRY")
    sxp = json.loads(sxp_get.text)

    avax_get = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=AVAXTRY")
    avax = json.loads(avax_get.text)    
    
    url= "https://kur.doviz.com/"

    r = requests.get(url)

    soup = BeautifulSoup(r.content, "lxml")

    altin = soup.find("span", {"data-socket-key":"gram-altin" }).text

    dolar = soup.find("span", {"data-socket-key":"USD" }).text

    euro = soup.find("span", {"data-socket-key":"EUR"}).text

    sterlin = soup.find("span", {"data-socket-key":"GBP" }).text 

    xu100 = soup.find("span", {"data-socket-key":"XU100" }).text

    coin = soup.find("span", {"data-socket-key":"bitcoin" }).text

    gumus = soup.find("span", {"data-socket-key":"gumus" }).text    

    description = str(ctx.guild.description)
    embed = discord.Embed(title="Döviz - Borsa - Kripto", description=f"Döviz, borsa ve kripto ile ilgili belli başlı değerler anlık olarak gösterilir.", color=0x00ccff)
    embed.add_field(name=f":dollar: Dolar", value=f"{dolar}", inline=True)
    embed.add_field(name=f":euro:  Euro", value=f"{euro}", inline=True)
    embed.add_field(name=f":pound: Sterlin", value=f"{sterlin}", inline=True)
    embed.add_field(name=f":coin: Gram Altın", value=f"{altin}", inline=True)
    embed.add_field(name=f"<:gumus:918898008660271124> Gümüş", value=f"{gumus}", inline=True)   
    embed.add_field(name=f"📊 XU100", value=f"{xu100}", inline=True)
    embed.add_field(name=f"<:bitcoin:918869515406811216> Bitcoin", value=int(float(bitcoin["price"])), inline=True) 
    embed.add_field(name=f"<:ethereum:918889666713903134> Ethereum", value=int(float(ethereum["price"])), inline=True)   
    embed.add_field(name=f"<:bnb:918891368665972816> Binance Coin", value=int(float(bnb["price"])), inline=True)   
    embed.add_field(name=f"<:avax:926434783452618772> Avalanche Coin", value=int(float(avax["price"])), inline=True)        
    embed.add_field(name=f"<:shib:918896052109717575> Shiba Coin", value=shib["price"], inline=True)          
    embed.add_field(name=f"<:sxp:926434783561678898> Swipe Coin", value=("{:.2f}".format(float(sxp["price"]))), inline=True)  

    await ctx.send(embed=embed)


@bot.command(aliases=['wikipedia'])
async def wikipedia_ara(ctx):
    description = str(ctx.guild.description)    
    wikipedia.set_lang("tr")

    embed = discord.Embed(title="<:nametag:841951946650812426> │ Wikipedia Araması", description="Bot, komut sonrasında belirttiğiniz arama terimini, wikipedia'da arar ve wikipedia'daki bilgileri size sunar.", color=0x14ffd8)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Wikipedia_svg_logo.svg/1200px-Wikipedia_svg_logo.svg.png")
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)    
    await ctx.send(embed=embed)

    try:
        arama = await bot.wait_for('message', timeout=10.0)
    except asyncio.TimeoutError:
        return await ctx.send(f'**<:normalcarpi:852958720328466474> Arama yapmak istediğin şeyi belirtmen çok uzun sürdü.**')

    if ctx.author.id == 819743355663548447:
        pass
    else:
        result = wikipedia.summary(f"{arama.content}", sentences = 2)
        sayfa = wikipedia.page(f"{arama.content}")

        embed1 = discord.Embed(title="<:nametag:841951946650812426> │ Wikipedia Araması", description="Bot, komut sonrasında belirttiğiniz arama terimini, wikipedia'da arar ve wikipedia'daki bilgileri size sunar.", color=0x14ffd8)
        embed1.add_field(name=f":mag_right:  │ Aramanaız", value=f"{arama.content}", inline=True)
        embed1.add_field(name=f"🔗 │ Wikipedia Linki", value=f"[Tıkla]({sayfa.url})", inline=True)
        embed1.add_field(name=f":page_facing_up: │ Arama Sonucu", value=f"{result}", inline=False)
        embed1.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Wikipedia_svg_logo.svg/1200px-Wikipedia_svg_logo.svg.png")
        embed1.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed1)

# birden fazla anlam olabilecek şeye bak sonra. mesela merhaba sözcüğü 5 tane makale falan var. Anladın? #
# error handling bir de #

bot.run(TOKEN)
