import discord
import os
from search_results import find_google_results
from db_operations import db_write_user_search,db_write_user_ping,db_read_user_history

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    print(f'{message.content} -> {message.author.id}|{message.author.name}')
    if message.content.lower() == 'hi':
        try:
            db_write_user_ping(message.author.id)
            msg = 'Hey !'
            await message.channel.send(msg)
            return
        except:
            raise Exception("Failed to reply back for Hi")

    if message.content.startswith('!google'):
        try:
            print(f'Finding Seach Results from Google for {message.content}')
            search_query = message.content.replace('!google ','')
            db_write_user_search(message.author.id,search_query)
            search_results = find_google_results(search_query)
            await message.channel.send(search_results)
            return
        except:
            await message.channel.send("Failed to fetch search results, contact admin!")

    if message.content.startswith('!recent'):
        try:
            print(f'Traversting Search History for {message.author.id} | {message.content}')
            search_query = message.content.replace('!recent ','')
            search_results = db_read_user_history(message.author.id,search_query)
            await message.channel.send(search_results)
            return
        except:
            await message.channel.send("Failed to fetch results, contact admin!")

@client.event
async def on_ready():
    print(f'Connected to discord : BOT NAME : {client.user.name} - {client.user.id} \nBot is listening :')

if __name__ == '__main__':
    print('Fetching Discord Bot Token')
    TOKEN = os.environ.get('discordapp_TOKEN')
    print(TOKEN)
    print('Conncting ...')
    client.run(TOKEN)
