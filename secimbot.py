import discord
import datetime
import pytz

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot {0.user} is online!'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!secimekalan'):
        election_date = datetime.datetime(2023, 5, 14, 0, 0, 0, 0, pytz.UTC)
        now = datetime.datetime.now(pytz.UTC)
        remaining_time = election_date - now

        total_seconds = remaining_time.total_seconds()
        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        await message.channel.send(f'14 Mayıs seçimlerine {int(days)} gün, {int(hours)} saat, {int(minutes)} dakika ve {int(seconds)} saniye kaldı.')

client.run('TOKEN') # buraya token giriniz

