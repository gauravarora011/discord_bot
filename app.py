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

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

if __name__ == '__main__':
    TOKEN = os.environ.get('discodrapp_TOKEN')
    client.run(TOKEN)
