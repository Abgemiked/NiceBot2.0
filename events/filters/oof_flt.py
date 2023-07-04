import discord 
import json
async def handler(message):
    with open('./config.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
    #Chatfilter for the word "oof"    
    if message.channel.id != data["OOF_ID"]:
        return False
    if message.content != "oof":
        await message.delete()
        print("done")
        return True
    return False
                                 