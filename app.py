import discord
import os

client = discord.Client()

@client.event
async def on_message(message):
    print(str(message.content) + ' -> ' + str(message.author.id))
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.lower() == 'hi':
        msg = 'Hey !'
        await message.channel.send(msg)
        return

    if message.content.startswith('!google'):
        search_results = find_google_results(message.content.replace('!google ',''))
        await message.channel.send(search_results)
        return

@client.event
async def on_ready():
    print(f'Connected to discord : BOT NAME : {client.user.name} - {client.user.id} \nBot is listening :')

if __name__ == '__main__':
    print('Fetching Discord Bot Token')
    TOKEN = os.environ.get('discordapp_TOKEN')
    print('Conncting ...')
    client.run(TOKEN)
