import discord
import json
async def handler(message):
    with open('./config.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
    #Chatfilter for GIFs only from tenor
    if message.channel.id != data["GIF_ID"]:
        return False
    if message.content and not message.content.startswith("https://tenor.com/"):
        await message.delete()
        return True
    if message.attachments:
        for attachment in message.attachments:
            if not attachment.url.startswith("https://tenor.com/"):
                await message.delete()
                return True
    return False
                                 