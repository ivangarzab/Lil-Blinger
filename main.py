import discord
import random
import env

DEFAULT_CHANNEL_BLINGERS = 485714188073697296

intents = discord.Intents.default()

client = discord.Client(intents=intents)

greetings = ["Hallo", "suuup", "buenas"]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return # Avoid the bot responding to itself
    
    author = message.author.mention
    msgFormat = message.content.lower()
    allowed_mentions = discord.AllowedMentions(everyone = True)

    shouts = [f"{author} is looking for love", f"{author} cannot find any friends", f"{author} is on comms!"]
    if '<' == message.content:
      await message.channel.send(shouts[random.randint(0, 2)])
    if '<<' == message.content:
      await message.channel.send(shouts[random.randint(0, 2)])
    if '<--' == message.content:
      await message.channel.send(shouts[random.randint(0, 2)])
    if '<---' == message.content:
      await message.channel.send(shouts[random.randint(0, 2)])
    if '...' == message.content:
        await message.channel.send(f"te falta algo {author}?")
    
    if 'blingers' in msgFormat:
      await message.channel.send('BLINGERS PILINGERS ASSEMBLE:bangbang:')
    if 'lil blinger' in msgFormat:
        await message.channel.send(greetings[random.randint(0,2)])
    if 'hola' in msgFormat:
      await message.channel.send(greetings[random.randint(0,2)])
    if 'GAME' in message.content:
      await message.channel.send(f"echele! @everyone")
    if 'game' in message.content:
      await message.channel.send(f"echele!")
    if 'sup' in msgFormat:
      await message.channel.send(f"sup")
    if 'date' in msgFormat:
      await message.channel.send(f"lego")
    if 'marco' in msgFormat:
      await message.channel.send(f"POLO!")
    if 'arre' in msgFormat:
      await message.channel.send(f"arre vaquero!")
    
    if 'puto' in msgFormat:
      await message.channel.send(f"puto tu {author}")
    if 'madre' in msgFormat:
      await message.channel.send(f"la tuya {author}")
    if 'shit' in msgFormat:
      await message.channel.send(f"A que hora pasas por el pan {author}")
    if 'verga' in msgFormat:
      await message.channel.send(f"{author} tiene hambre")
    if 'tibia' in msgFormat:
      await message.channel.send(f"sucks")
    if 'nabbot' in msgFormat:
      await message.channel.send(f"el NabBot mlp :smiling_imp:")
    if 'golf' in msgFormat:
      await message.channel.send(f"te culeas")
    if 'help' == msgFormat:
      await message.channel.send(f"nadie te va a ayudar {author}!")
    if 'share' in msgFormat:
      await message.channel.send('comparte esta')
    if 'soo' in msgFormat:
      await message.channel.send('.........')
    if 'culean' in msgFormat:
      await message.channel.send('aqui nadie culea! :metal:')
    if 'culeas' in msgFormat:
      await message.channel.send(f"tu culeas {author}")
    if 'traen nada' in msgFormat:
      await message.channel.send(f"tu no traes nada! {author}")
    if 'voy' in msgFormat:
      await message.channel.send(f"que se vea")
    if 'pelas' in msgFormat:
      await message.channel.send(f"tu me la pelas {author}!")
    if 'pelan' in msgFormat:
      await message.channel.send(f"todos se la pelan al {client.user.mention}")

@client.event
async def on_message_delete(message):
    await message.channel.send(f"{message.author.mention}, why would you delete that message?")
    
@client.event
async def on_member_join(member):
    println(f"{member} joined")
    channel = client.get_channel(DEFAULT_CHANNEL_BLINGERS)
    if not channel:
        return
    await channel.send(f"Welcome {member}!")

client.run(env.TOKEN)
