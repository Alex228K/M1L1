import discord

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswit('Привет'):
        await message.channel.send("привет, если ты хочешь помочь своему городу перейди сюда:https://recyclemap.ru")
