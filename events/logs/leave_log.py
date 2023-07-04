import discord

async def handle_member_remove(member, bot, LOG_CHANNEL_ID):
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    await log_channel.send(f'{member.display_name} hat den Server verlassen.')


async def on_member_remove_handler(member, bot, LOG_CHANNEL_ID):
    await handle_member_remove(member, bot, LOG_CHANNEL_ID)
