import discord
import os
from search_results import find_google_results

client = discord.Client()

@client.event
async def on_message(message):
    print(f'{message.content} -> {message.author.id}|{message.author.name}')
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.lower() == 'hi':
        msg = 'Hey !'
        await message.channel.send(msg)
        return

    if message.content.startswith('!google'):
        try:
            print(f'Finding Seach Results for {message.content}'    )
            search_results = find_google_results(message.content.replace('!google ',''))
            await message.channel.send(search_results)
            return
        except:
            await message.channel.send("Failed to fetch search results, contact admin!")

@client.event
async def on_ready():
    print(f'Connected to discord : BOT NAME : {client.user.name} - {client.user.id} \nBot is listening :')

if __name__ == '__main__':
    print('Fetching Discord Bot Token')
    TOKEN = os.environ.get('discordapp_TOKEN')
    print('Conncting ...')
    client.run(TOKEN)
