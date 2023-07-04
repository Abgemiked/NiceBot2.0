import discord
import json

async def handler(message):
    with open('./config.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
    oof_channel_id = data['OOF_ID']
    if message.channel.id == oof_channel_id:
        if message.content != "oof":
            await message.delete()
            try:
                await message.author.send(f"**Deine Nachricht aus <#{oof_channel_id}> wurde gelöscht, bitte sende dort keine Nachrichten. Der Channel ist nur für das Wort 'oof' gedacht**.")
            except discord.Forbidden:
                print("Fehler beim Senden der DM-Nachricht.")
            return True
    return False