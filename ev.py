import discord
import requests

token = 'OTgxNjg0MDgxNTE3NTI3MDUx.GKn7AS.MSrKV2mkr1XDiiCDBmGsyX3_7XgyoZiKK2SYBQ'

client = discord.Client()

@client.event
async def on_message(message):
    # !views number_of_views link
    if message.author == client.user:
        return

    if '!views' in message.content:
        number_of_views = message.content.split(' ')[1]
        link = message.content.split(' ')[2]

        response = f'Adding {number_of_views} views...'
        await message.channel.send(response)

        for i in range(int(number_of_views)):
            requests.get(link)

        response = f'Added {number_of_views} views.'
        await message.channel.send(response)

client.run(token)