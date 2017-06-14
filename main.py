import discord
import asyncio

client = discord.Client()

def yourID="" #Get this id by using \@yourname and copying only the numbers
def NikeyID="" #Get this id by using \@Nikey and copying the whole message, including the <, @, >

@client.event
async def on_message (message):
	if message.author.id == YourID:
		print(message.content)
		msg=message.content

		if "@Nikey" in message.content:
			await client.delete_message(message)
			await client.send_message(message.channel, msg.replace("@Nikey", NikeyID))
			
		elif "@nikey" in message.content:	
			await client.delete_message(message)
			await client.send_message(message.channel, msg.replace("@nikey", NikeyID))

client.run('token', bot=False) #To get your token, press ctrl/cmd + shift + I, press on the little arrow, and in the Application tab, pick Local Storage, the link below it, and scroll down to see token