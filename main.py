# This example requires the 'message_content' intent. UPDATE: Does it?

import discord

intents = discord.Intents.default()
#intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '<' == message.content:
      await message.channel.send(f"{message.author.mention} is looking for love")
    if '<<' == message.content:
      await message.channel.send(f"{message.author.mention} cannot find any friends")
    if '<--' == message.content:
      await message.channel.send(f"{message.author.mention} is on comms!")
    if '<---' == message.content:
      await message.channel.send(f"{message.author.mention} is on comms!")
    if 'blinger' in message.content:
      await message.channel.send('BLINGERS PILINGERS ASSEMBLE!!')
    if 'puto' in message.content:
      await message.channel.send(f"puto tu {message.author.mention}")
    if 'madre' in message.content:
      await message.channel.send(f"la tuya {message.author.mention}")
    if 'shit' in message.content:
      await message.channel.send(f"A que hora pasas por el pan {message.author.mention}")
    if 'verga' in message.content:
      await message.channel.send(f"{message.author.mention} tiene hambre")
    if 'tibia' in message.content:
      await message.channel.send(f"sucks")
    if 'nabbot' in message.content:
      await message.channel.send(f"SUCKS BALLS!")
    if 'golf' in message.content:
      await message.channel.send(f"culean")
    if 'help' == message.content:
      await message.channel.send('pelas')
    if 'share' in message.content:
      await message.channel.send('comparte esta')
    if 'soo' in message.content:
      await message.channel.send('.........')

client.event
async def on_message_delete(message):
    await message.channel.send(f"{message.author.mention}, why would you delete the message '{message}'?")

client.run('MTAzOTMxNzg2NTA0NTY4ODM4MQ.GlsEI7.ZjB9dMY3c30GQE4m9uQz8wfDNkBi7br5FTmFuA')
