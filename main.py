import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord import Member
from discord.ext.commands import MissingPermissions
import datetime
import asyncio
from urllib import parse, request
import re
import random


bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), description="Normal Bot")
bot.remove_command("help")

@bot.event
async def on_ready():
    print('Logged in as Wersef')
    print(f'Discord Versiyonu {discord.__version__}')
    game = discord.Game("!yardım")
    await bot.change_presence(activity=game)
    
@bot.command(aliases=['yardım'])
async def help(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬[ :dizzy: Wersef :dizzy: ]▬▬▬▬▬▬   ",
        description="> :link: **Prefix:** ! \n > :link: **Botun Destek Sunucusu:** [Tıkla](https://discord.gg/ewGpWsx454) \n > :link: **Botun Davet Bağlantısı:** [Tıkla](https://discord.com/oauth2/authorize?client_id=819743355663548447&permissions=469820598&scope=bot)",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Yardım Komutları 🔐  ]▬▬▬▬▬▬", value="> :dizzy: **!moderasyon:** Moderason komutlarını gösterir. \n > :dizzy: **!kullanıcıkomutları:** Kullanıcı komutlarını size gösterir. \n > :dizzy: **!sunucukomutları:** Sunucu ile ilgili komutları size sunar. \n > :dizzy: **!hesapla:** Bot hesaplama komutlarını size sunar. \n > :dizzy: **!eğlence:** Bot eğlence komutlarını sunar. \n > :dizzy: **!işeyarar:** Bot, işe yarar komutları size sunar. \n > :dizzy: **!bothakkında:** Bot hakkındaki komutları gösterir. (Bakmanız Önerilir) ", inline=False)
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **:open_file_folder: Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > **:open_file_folder: Botun Yazıldığı Dil:** Python", inline=False)


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

    embed = discord.Embed(title="Botun Davet Linkleri", description=f"<:kral:830058307351478282> **Gerekli İzinlerle (Önerilen):** ➠ [Tıkla](https://discord.com/oauth2/authorize?client_id=819743355663548447&permissions=469820598&scope=bot) \n <:kral:830058307351478282> **Bütün İzinlerle (Önerilen):** ➠ [Tıkla](https://discord.com/api/oauth2/authorize?client_id=819743355663548447&permissions=4294967287&scope=bot) \n <:kral:830058307351478282> **Yönetici İzinleriyle (Bazı Komutlar Çalışmayabilir):** ➠ [Tıkla](https://discord.com/oauth2/authorize?client_id=819743355663548447&permissions=8&scope=bot) \n <:robo:833610842410450964> **Yetkisiz Şekilde (Önerilmez):** ➠ [Tıkla](https://discord.com/oauth2/authorize?client_id=819743355663548447&permissions=0&scope=bot) ", color=0x14ffd8)
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
async def sunucukur(ctx):
    guild = ctx.guild

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
 
    category8 = await guild.create_category('☞VİP Kategorisi ☜')    
    await category8.create_text_channel('🔐│vip-sohbet')  
    await category8.create_text_channel('🔐│vip-bot-komut')    
    await category8.create_voice_channel('🔐│VİP Odası¹') 
    await category8.create_voice_channel('🔐│VİP Odası²')
    await category8.create_voice_channel('🔐│VİP Odası³')

    await category8.set_permissions(role, read_messages=True, send_messages=True, connect=True, speak=True)
    await category8.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False, connect=False)
    await category8.set_permissions(ctx.guild.self_role, read_messages=True, send_messages=True)

@sunucukur.error
async def sunucukur_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için Yönetici adlı yetkiye sahip olman gerekli.")      


@commands.has_permissions(administrator=True)
@bot.command()
async def sunucuyutemizle(ctx):
    guild = ctx.guild
    for c in ctx.guild.channels:
        await c.delete()
    for category in ctx.guild.categories:
        await category.delete()

@sunucuyutemizle.error
async def sunucuyutemizle_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için Yönetici adlı yetkiye sahip olman gerekli.")          


@bot.command()
async def hack(ctx, user: discord.Member):
    description = str(ctx.guild.description)
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
       embed = discord.Embed(title="Botun Davet Linki ", description=f"> <:kral:830058307351478282> Yönetici Yetkileriyle ➠ [Tıkla](https://discord.com/oauth2/authorize?client_id={user.id}&permissions=8&scope=bot) \n > <:kral:830058307351478282> Bütün Yetkileriyle ➠ [Tıkla](https://discord.com/api/oauth2/authorize?client_id={user.id}&permissions=4294967287&scope=bot) \n > <:robo:833610842410450964> Yetkisiz Şekilde ➠ [Tıkla](https://discord.com/api/oauth2/authorize?client_id={user.id}&permissions=0&scope=bot)", color=0x14ffd8)
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
        await ctx.send("Bu komutu kullanabilmek için Mesajları Yönet adlı yetkiye sahip olman gerekli.")



@commands.has_permissions(kick_members=True)
@bot.command(pass_context=True , aliases=['at', 'kov', 'kullanıcıyı_at', 'kullanıcıyıat'])
async def kick(ctx, user: discord.Member, *, reason="Neden kullanıcı tarafından belirtilmedi."):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f":boom: {user.name} Sunucudan Kovuldu", description=f"**Nedeni:** {reason}\n", color=0xff0000 )
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)

@kick.error
async def test_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için Üyeleri At adlı yetkiye sahip olman gerekli.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen atmak istediğiniz kullanıcyı komut sonrasında etiketleyerek belirtiniz.')  
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
async def test_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için Rolleri Yönet adlı yetkiye sahip olman gerekli.")  
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen susturmak istediğiniz kullanıcyı komut sonrasında etiketleyerek belirtiniz.')   
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
            await channel.set_permissions(mutedRole, speak=False, send_messages=True, read_message_history=True)
    embed = discord.Embed(title=f":boom: Kullanıcı Ses Kanallarından Susturuldu", description=f"**Nedeni:** {reason}\n", color=0xff0000 )
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)


@voicemute.error
async def voicemute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için Üyeleri Sustur adlı yetkiye sahip olman gerekli.")  
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen ses kanallarında susturmak istediğiniz kullanıcyı komut sonrasında etiketleyerek belirtiniz.')   
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 


@commands.has_permissions(manage_roles=True)
@bot.command(pass_context=True , aliases=['susturmayıkaldır', 'susturmayı_kaldır', 'un_mute'])
async def unmute(ctx, member: discord.Member, *, reason='Neden kullanıcı tarafından belirtilmedi.'):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   embed = discord.Embed(title=f"✅ Kullanıcının Yazı Kanallarından Susturulması Kaldırıldı", description=f"**Nedeni:** {reason}\n", color=0x2bff00)
   await ctx.send(embed=embed)


@unmute.error
async def test_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için Rolleri Yönet adlı yetkiye sahip olman gerekli.")  
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen susturulmasını kaldırmak istediğiniz kullanıcyı komut sonrasında etiketleyerek belirtiniz.')     
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 


@commands.has_guild_permissions(mute_members=True)
@bot.command(pass_context=True, aliases=['sessusturmayıkaldır', 'sestesusturmayıkaldır'])
async def unvoicemute(ctx, member: discord.Member, *, reason='Neden kullanıcı tarafından belirtilmedi.'):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Voice Mute")

   await member.remove_roles(mutedRole)
   embed = discord.Embed(title=f"✅ Kullanıcının Ses Kanallarından Susturulması Kaldırıldı", description=f"**Nedeni:** {reason}\n", color=0x2bff00)
   await ctx.send(embed=embed)


@unvoicemute.error
async def unvoicemute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için Üyeleri Sustur  adlı yetkiye sahip olman gerekli.")  
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen ses kanallarından susturulmasını kaldırmak istediğiniz kullanıcyı komut sonrasında etiketleyerek belirtiniz.')     
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 


@commands.has_permissions(ban_members=True)
@bot.command(pass_context=True , aliases=['banla', 'yasakla', 'kullanıcıyı_banla', 'kullanıcıyı_yasakla'])
async def ban(ctx, user: discord.Member, *, reason="Neden kullanıcı tarafından belirtilmedi."):
        await user.ban(reason=reason)
        ban = discord.Embed(title=f":boom: {user.name} Sunucudan Banlandı", description=f"**Nedeni**: {reason}", color=0xff0000)
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)

@ban.error
async def test_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için Üyeleri Yasakla adlı yetkiye sahip olman gerekli.")      
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen yasaklamak istediğiniz kullanıcyı komut sonrasında etiketleyerek belirtiniz.') 
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 

@commands.has_permissions(ban_members=True)
@bot.command(aliases=['bankaldır', 'banı_kaldır', 'yasak_kaldır', 'yasaklamayı_kaldır'])
async def unban(ctx, *, user=None, reason="Neden kullanıcı tarafından belirtilmedi."):

    try:
        user = await commands.converter.UserConverter().convert(ctx, user)
    except:
        await ctx.send("Lütfen yasaklamasını kaldırmak istediğiniz kullanıcyı komut sonrasında etiketleyerek belirtiniz.")
        return

    try:
        bans = tuple(ban_entry.user for ban_entry in await ctx.guild.bans())
        if user in bans:
            await ctx.guild.unban(user, reason=reason)
        else:
            await ctx.send("Belirttiğiniz kullanıcı yasaklı değil.")
            return

    except discord.Forbidden:
        await ctx.send("Bu komutu kullanabilmek için gerekli izinlere sahip değilim. Daha fazla bilgi için !not komutunu kullanabilirsiniz.")
        return

    except:
        await ctx.send("Bir hata ile karşılaşıldı.")
        return

    unban = discord.Embed(title=f"✅ Kullanıcının Yasağı Kaldırıldı", description=f"**Nedeni**: {reason}", color=0x2bff00)
    await ctx.channel.send(embed=unban)


@unban.error
async def test_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için Üyeleri Yasakla adlı yetkiye sahip olman gerekli.")  
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.')   


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
        title="Sunucu İsmi",
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
    embed.add_field(name="👤 │Kullanıcı Adı", value=member.display_name)
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
   embed.set_author(name="Wersef", icon_url="https://cdn.discordapp.com/avatars/819743355663548447/93b04f1275bc6f1b9c5fcac9dd97802f.webp?size=1024")
   embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/819743355663548447/93b04f1275bc6f1b9c5fcac9dd97802f.webp?size=1024")
   embed.add_field(name="🤖 │ Bot ", value="Aktif", inline=False)
   embed.add_field(name="🆔 │ Bot ID'si", value="819743355663548447", inline=True)
   embed.add_field(name="🎓 │ Bot Yapımcısı", value="SWORD", inline=True)
   embed.add_field(name="🌀 │ Botun Destek Sunucusu", value="https://tik.lat/K5BjK", inline=True)
   embed.add_field(name="🔗 │ Botun Davet Linki", value="https://tik.lat/0UmWl", inline=True)
   embed.add_field(name="🔮 │Botun Bulunduğu Sunucu Sayısı", value=f"{len(bot.guilds)}", inline=True)
   
   await ctx.send(embed=embed)



@bot.command(pass_context=True, aliases=['yapımcı', 'botiletişim', 'bot_iletişim', 'İletişim',])
async def iletişim(ctx):
    member = ctx.message.author


    embed=discord.Embed(title="🔗 │ İletişim Ve Linkler ", description="Bot hakkında herhangi bir sorunu bildirmek yada yardım almak için buradaki iletişim adreslerini kullanabilirsiniz.", color=0x00ccff)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=member.avatar_url)
    embed.add_field(name="🎓 │ Bot Yapımcısı", value="SWORD", inline=False)
    embed.add_field(name="<:telegram:826727507877298187> │ Telegram", value="SS_w_o_R_d", inline=True)
    embed.add_field(name="<:discord:826722461943988254> │ Discord", value="SWORD#8666", inline=True)
    embed.add_field(name="🌀 │ Botun Destek Sunucusu", value="https://tik.lat/K5BjK", inline=True)
    embed.add_field(name="🔗 │ Botun Davet Linki", value="https://tik.lat/0UmWl", inline=True)

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
        description="> :dizzy: **!botbilgi** Bot hakkındaki bilgileri gösterir. \n > :dizzy: **!wersefdavet** Botun davet linklerini gösterir. \n > :dizzy: **!iletişim:** Botun yapımcısı ile iletişim kurma yollarını gösterir. \n > :dizzy: **!ping:** Botun gecikme süresini yani pingini verir. \n > :dizzy: **!not:** Bot hakkındaki önemli notları size gösterir. \n > :dizzy: **!komutlarçalışmıyor:** Komutların çalışma nedeni size sunulur.",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **:open_file_folder: Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > **:open_file_folder: Botun Yazıldığı Dil:** Python", inline=False)


    await ctx.send(embed=embed)      



@bot.command()
async def eğlence(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬▬[ 🔐 Eğlence Komutları 🔐  ]▬▬▬▬▬▬",
        description="> :dizzy: **!zar:** Bot bir zar atar ve sonucu size görsel olarak bildirir. \n > :dizzy: **!hack:** Komut sonrasında belirttiğiniz kiyişi hacklemenizi sağlar. \n > :dizzy: **!sarıl:** Komut sonrasında belirttiğiniz kişiye sarılmanızı sağlar. \n > :dizzy: **!yumrukla:** Komut sonrasında belirttiğiniz kişiyi yumruklamanızı sağlar. \n > :dizzy: **!tokatla:** Komut sonrasında belirttiğiniz kişiyi tokatlamınızı sağlar. \n > :dizzy: **!öldür:** Komut sonrasında belirttiğiniz kişiyi öldürmenizi sağlar. \n > :dizzy: **!ateşet:** Komut sonrasında belirttiğiniz kişiye ateş etmenizi sağlar. \n > :dizzy: **!yalvar:** Komut sonrasında belirttiğiniz kişiye yalvarmanızı sağlar.",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **:open_file_folder: Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > **:open_file_folder: Botun Yazıldığı Dil:** Python", inline=False)


    await ctx.send(embed=embed)      
    

@bot.command()
async def işeyarar(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬▬[ 🔐 İşe Yarar Komutlar 🔐  ]▬▬▬▬▬▬",
        description="> :dizzy: **!discordnedir:** Discord hakkında bazı bilgileri size sunar. \n > :dizzy: **!rozetler** Bütün Discord rozetlerini renkli bir şekilde size sunar \n > :dizzy: **!botudavetet:** Komut sonrasında belirttiğiniz botun davet linklerini size sunar. ",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **:open_file_folder: Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > **:open_file_folder: Botun Yazıldığı Dil:** Python", inline=False)


    await ctx.send(embed=embed)      

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
    embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Kullanılışı 🔐 ]▬▬▬▬▬▬", value="> :dizzy: **!embed** <mesajınız>", inline=False)
    embed.add_field(name="▬▬▬▬▬▬▬[ 🔐 Komutun Örnekleri 🔐 ]▬▬▬▬▬▬", value="> :dizzy: **!embed** Merhabalar SWORD. \n > :dizzy: **!embed** Nasılsınız? \n > :dizzy: **!embed** Kod yazıyorum. \n > :dizzy: **!embed** İyiyim, yatıyorum öyle.", inline=False)
    
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **:open_file_folder: Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > **:open_file_folder: Botun Yazıldığı Dil:** Python", inline=False)


    await ctx.send(embed=embed)   


@bot.command()
async def sunucukomutları(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬▬[ 🔐 Sunucu Komutları 🔐  ]▬▬▬▬▬▬",
        description="> :dizzy: **!serverinfo:** Sunucu hakkındaki bilgileri size gösterir. \n > :dizzy: **!sunucusahibi:** Sunucu sahibinin kim olduğunu size gösterir. \n > :dizzy: **!sunucukur:** Sunuzunuzdaki bütün kanal ve kategorileri silip yeni, modern bir sunucu oluşturur. \n > :dizzy: **!sunucuyutemizle:** Sunuzunuzdaki bütün kanal ve kategorileri içindeki verilerle birlikte siler. \n > :dizzy: **!roller:** Sunuzunuzdaki bütün roller görüntülenir. ",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **:open_file_folder: Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > **:open_file_folder: Botun Yazıldığı Dil:** Python", inline=False)


    await ctx.send(embed=embed)       


@bot.command()
async def kullanıcıkomutları(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬▬[ 🔐 Kullanıcı Komutları 🔐  ]▬▬▬▬▬▬",
        description="> :dizzy: **!kullanıcı:** Kullanıcı hakkındaki bilgileri size gösterir. \n > :dizzy: **!avatar:** Belirttiğiniz kişinin profil fotoğrafını size verir. \n > :dizzy: **!yetkileri:** Belirttiğiniz kişinin yetkileri size gösterilir. \n > :dizzy: **!embeds:** Gömülü mesj seçeneklerini size sunar.  ",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **:open_file_folder: Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > **:open_file_folder: Botun Yazıldığı Dil:** Python", inline=False)


    await ctx.send(embed=embed) 


@bot.command()
async def moderasyon(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬▬[ 🔐 Moderasyon Komutları 🔐  ]▬▬▬▬▬▬",
        description="> :dizzy: **!sil:** Belirttiğiniz miktar kadar kolayca mesaj silmenizi sağlar. \n > :dizzy: **!kick:** Belirttiğiniz kişiyi sunucudan kovar. \n > :dizzy: **!mute:** Belirttiğiniz kişiyi yazı kanallarından susturur. \n > :dizzy: **!ban:** Belirttiğiniz kullanıcıyı sunucudan yasaklar. \n > :dizzy: **!unban:** Belirttiğiniz kişinin yasaklaması kaldırılır. \n > :dizzy: **!unmute:** Belirttiğiniz kişinin yazı kanallarından susturulması kaldırılır.  \n > :dizzy: **!voicemute:** Belirttiğiniz kişiyi ses kanallarından susturur. \n > :dizzy: **!unvoicemute:** Belirttiğiniz kişinin ses kanallarından susturulmasını kaldırır. \n > :dizzy: **!kullanıcıadı:** Belirttiğiniz kullanıcının adını, kullanıcıyı belirttikten sonra yazdığınız kullanıcı adı olarak değiştirir. \n > :dizzy: **!uyar:** Belirttiğiniz kişiyi, belirttiğiniz nedenle uyarmanızı sağlar. ",
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.add_field(name="▬▬▬▬▬▬▬[ :gear: Genel Bilgilendirme :gear:]▬▬▬▬▬▬", value="> **:open_file_folder: Fikirlerinizi her zaman belirtebilirsiniz.** Memnun olurum. \n > **:open_file_folder: Botun Yazıldığı Dil:** Python", inline=False)


    await ctx.send(embed=embed) 



@bot.command(aliases=['hesap', 'hesapmakinesi', 'hesap_makinesi'])
async def hesapla(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    
    icon = str(ctx.guild.icon_url)
    
    embed = discord.Embed(
        title="▬▬▬▬▬▬▬[ <:hesap:828358560923516938> Hesaplama Komutları <:hesap:828358560923516938>  ]▬▬▬▬▬▬",
        description="> :dizzy: **!topla:** Bot belirttiğiniz iki sayıyı toplamanızı sağlar. \n > :dizzy: **!çıkart:** Bot belirttiğiniz iki sayıyı çıkarmanızı sağlar. \n > :dizzy: **!çarp:** Bot belirttiğiniz iki sayıyı çarpmanızı sağlar. \n > :dizzy: **!böl:** Bot belirttiğiniz iki sayıyı bölmenizi sağlar",
        color=discord.Color.blue()
    )
    embed.add_field(name="▬▬▬▬▬▬▬[ <:hesap:828358560923516938> Komutun Kullanılışı <:hesap:828358560923516938>  ]▬▬▬▬▬▬", value="> :dizzy: **!topla** <birinci sayı> <ikinci sayı> \n > :dizzy: **!çıkart** <birinci sayı> <ikinci sayı> \n > :dizzy: **!çarp** <birinci sayı> <ikinci sayı> \n > :dizzy: **!böl** <birinci sayı> <ikinci sayı>", inline=False)
    embed.add_field(name="▬▬▬▬▬▬▬[ <:hesap:828358560923516938> Komutun Örnekleri <:hesap:828358560923516938>  ]▬▬▬▬▬▬", value="> :dizzy: **!topla** 5 5 \n > :dizzy: **!çıkart** 10 5 \n > :dizzy: **!çarp** 10 10 \n > :dizzy: **!böl** 80 10", inline=False)
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


@bot.command(aliases=['gömülü_mesaj', 'gömülü', 'gömülümesaj'])
async def embed(ctx, *, mesaj="Kullanıcı mesaj belirtmedi."):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title="<:sohbet:829082123570249739>  Mesajınız", description=f"{mesaj}", color=0x00ff33)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

@embed.error
async def embed_error(ctx, error):  
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen uyarmak istediğiniz istediğiniz kullanıcyı komut sonrasında etiketleyerek ve bunun sonrasında ise isteğe bağlı uyarılma nedenini belirtiniz. ') 


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

    embed = discord.Embed(title=":question: │ Discord Nedir", description=f"Gün geçtikçe popülerleşen profesyonel iletişim platformlarına benzer ücretsiz bir sohbet uygulamasıdır. Özellikle oyun oynayan kesimi ilgilendiren bu uygulama oyun oynarken arkadaşlarımız ile sesli bir şekilde oyunu koordine etmemizi sağlıyor. Sadece bununla sınırlı kalmayıp; Video görüşmeleri, sesli sohbet ve yazılı iletişimi destekler, kullanıcıların istedikleri gibi bir iletişim kurmalarına olanak tanır. İnsanlar arasında ortak bir bağ kuran bu uygulama sohbet, oyun, müzik, eğlence, iş ve daha bir çok topluluk kesimini kendi içinde barındırıyor. Aynı zamanda günümüzde sosyalleşmede ön planda kendini gösteriyor.", color=7506393)
    embed.add_field(name=":date: │ Discord Ne Zaman Kullanıma Sunuldu", value="Discord ilk defa 13 Mayıs 2015 tarihinde kullanıma sunuldu ancak son zamanlarda popülerleşmeye başladı.", inline=False)
    embed.add_field(name=":mortar_board: │ Discord'un Geliştiricisi", value="Oyuni içi sesli iletişimin zorunlu olduğunu, bununla birlikte Skype ve TeamSpeak gibi servislerin ise çok fazla negatif yanı olduğunu fark eden Jason Citron,  kullanımı daha kolay ve daha modern bir iletişim aracı olan Discord'u geliştirdi.", inline=False)
    

    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AAUvwniEUaBNWbH9Pk7A1cmIBdxnYt0YYrgNKx5h8grSMA=s900-c-k-c0x00ffffff-no-rj")
    await ctx.send(embed=embed)


@commands.has_permissions(administrator=True)
@bot.command()
async def uyar(ctx, user: discord.Member, *, mesaj="Uyarılma nedeniniz söz konusu moderatör tarafından belitilmemiş."):
    icon = str(ctx.guild.icon_url)

    embed1 = discord.Embed(title=":white_check_mark: Kullanıcı Uyarıldı", description=f"Belirttiğiniz kişi başarıyla uyarıldı.", color=0x00ff33)
    embed1.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed1)

    embed = discord.Embed(title=":warning: Uyarı", description=f"Merhabalar sayın {user.name}, yakın zamanda {ctx.guild.name} adlı sunucuda {ctx.author.display_name} adlı kişi tarafından uyarıldınız. ", color=0xff0000)
    embed.add_field(name=":warning: Nedeni", value=f"{mesaj}", inline=False)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await user.send(embed=embed)  

@uyar.error
async def uyar_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için Yönetici adlı yetkiye sahip olman gerekli.")      
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen uyarmak istediğiniz istediğiniz kullanıcyı komut sonrasında etiketleyerek ve bunun sonrasında ise isteğe bağlı uyarılma nedenini belirtiniz. ') 

    


@commands.has_permissions(manage_nicknames=True)
@bot.command(aliases=['ad', 'nick', 'kullanıcıadı', 'adıdeğiştir'], pass_context=True)
async def nickname(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'{member.mention} adlı kullanıcının kullanıcı adı, belirttiğiniz ad ile değiştirildi.')

@nickname.error
async def nickname_error(ctx, error): 
    if isinstance(error, MissingPermissions):
        await ctx.send("Bu komutu kullanabilmek için Kullanıcı Adlarını Yönet adlı yetkiye sahip olman gerekli.")           
    if isinstance(error, commands.BadArgument):
        await ctx.send('Belirttiğiniz kişiyi sunucuda bulamadım.') 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Lütfen adını değiştirmek istediğiniz kullanıcyı komut sonrasında etiketleyerek, bunun sonrasında ise değiştirmek istedğiniz adı belirtiniz. ') 


@bot.command(aliases=['yetkilerim'])
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


@bot.command()
async def komutlarçalışmıyor(ctx):
    description = str(ctx.guild.description)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title=":question: │ Komutlar Çalışmıyor", description=f"Bu sorunu dile getiren genellikle her kisi bu sorunu söz konusu bota yetki vermediği için yaşıyor. Özellikle moderasyon komutlarında yaşanan bu sorunun en basit çözümü, bota gerekli yetkileri vermektir.", color=0x007bff)
    embed.add_field(name=":question: │ Komutlar Hâlâ Çalışmıyor", value="Böyle bir şey yukarıda belirttiğimiz şeyleri yaptıysanız mümkün değildir. Ancak bir diğer etken ise botun rol sırasıdır. Bot, kendinden yüksek rollere müdahele edememektedir. Bu yüzden botun rol sırasını olabildiğince yüksek yapmanız önerilir.", inline=False)
    embed.set_author(name=ctx.author.display_name, url="", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


@bot.listen('on_message')
async def hi(message):
    if message.content == 'Selamlar':
        await message.channel.send('Selamlar :slight_smile:')

@bot.listen('on_message')
async def hi(message):
    if message.content == 'Tünaydınlar':
        await message.channel.send('Tünaydınlar :slight_smile:')

@bot.listen('on_message')
async def hi(message):
    if message.content == 'İyi akşamlar':
        await message.channel.send('Sanada iyi akşamlar. :sunglasses:')


@bot.listen('on_message')
async def hi(message):
    if message.content == 'Günaydın':
        await message.channel.send('Günaydınlar :slight_smile:')

@bot.listen('on_message')
async def hi(message):
    if message.content == 'İyi geceler':
        await message.channel.send('İyi geceler :sunglasses:')


bot.run('ODE5NzQzMzU1NjYzNTQ4NDQ3.YErDfg.NQJNCdgMV3JEVUcsmYXBeDg7q3A')
