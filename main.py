import discord
import asyncio
import re

client = discord.Client()

token = "" #To get your token, press ctrl/cmd + shift + I, press on the little arrow, and in the Application tab, pick Local Storage, the link below it, and scroll down to see token

YourID = "" #Get this id by using \@yourname and copying only the numbers
NikeyID = "" #Get this id by using \@Nikey and copying the whole message, includinga the <, @, >
#OtherPersonID = "" #Same as NikeyID, but for any person you want
#OtherPersonTag = "" #Whatever you want to tag so the bot will change it to the other person

@client.event
async def on_message (message):
	if message.author.id == YourID:
		msg = message.content
		lmsg = message.content.lower()

		if "@nikey" in lmsg:
			await client.delete_message(message)
			smsg = re.sub("(?i)@nikey","<@" + NikeyID + ">", msg)
			await client.send_message(message.channel, smsg)

		#elif "@" + OtherPersonTag in message.content:
		#	await client.delete_message(message)
		#	await client.send_message(message.channel, msg.replace("@:)", "<@" + OtherPersonID + ">"))

client.run(token, bot=False)