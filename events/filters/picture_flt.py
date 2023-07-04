import discord
import json
async def handler(message):
    with open('./config.json', 'r', encoding= "utf-8") as f:
        data = json.load(f)
    if message.channel.id == data["PICTURE_CHANNEL_ID"]:
        if not message.attachments and not message.reference:
            await message.delete()
            return False
        elif message.reference and not message.reference.resolved.attachments:
            await message.delete()
            return True
    return False