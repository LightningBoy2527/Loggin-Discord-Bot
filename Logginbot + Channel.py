import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user: #If message author is the bot, do not record message (infinite loop)
        return
    if message.channel.id == LoggingChannel: #Checks if channel is the same as the logging channel, if it is, then it does not record that message (infinite loop)
        return
    channel = client.get_channel(LoggingChannel) #Tells bot which channel to send it to
    await channel.send(f"#{message.channel}: {message.author}: {message.content}") #Sends message with the channel, author, and content of the message

client.run('BotToken') #Bot token to connect to the bot