import discord
intents = discord.Intents.default()
intents.messages= True 
client = discord.Client(intents=intents)
bottoken=open("C:/Users/ivobe/Desktop/Ma/Bewijzenmap/periode1.1/flex/extraphyton/04-discord/Geheim/Discordbot.txt", "r").readline()

@client.event
async def on_ready():
    guild = client.guilds[0]
    print(guild.name, "is the name of the server")
    print(client.user, "has connected to the client")

client.run(bottoken)
