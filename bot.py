import discord
from discord.ext import commands
import config
import json

#pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]

bot = commands.Bot(command_prefix=config.prefix)

@bot.listen('on_ready')
async def on_ready():
    print('Bot Hazır')
    print(bot.user)
    members = list(bot.get_all_members())
    print(f'Kullanıcı Sayısı : { len(members) }')
    durum = discord.Streaming(name='Mutlu Çalılıklar',url='')
    await bot.change_presence(activity=durum)

@bot.listen('on_message')
async def on_message(message: discord.Message):
    if not message.content.lower().startswith(config.prefix):
        return
    komutlar = KomutlariGetir()
    komut = message.content.lower()[len(config.prefix):]
    for k in komutlar:
        if k['ad'].lower() == komut:
            await message.channel.send(k['deger'])
            
def KomutlariGetir():
    try:
        with open(config.commands_path, 'r', encoding='utf-8') as f:
            return json.load(f) or []
    except:
        return []
    
komutlar = KomutlariGetir()
    
bot.run(config.token)