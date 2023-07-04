async def handler(cfg_json, interaction, limit):
    BLOCKED_CHANNEL_IDS = cfg_json['BLOCKED_CHANNEL_IDS']

    channel_id = interaction.channel.id
    if limit >= 99 or limit < 2:
        await interaction.response.send_message(content="**Das Limit muss zwischen 2 und 99 liegen!**")
        return 
    if channel_id in BLOCKED_CHANNEL_IDS:
        await interaction.response.send_message(content="**Das ist für diesen Voicechannel nicht erwünscht!**")
        return
    if not interaction.user.voice:
        await interaction.response.send_message(content="**Du bist nicht in einem VoiceChannel!**")
        return
    if channel_id != interaction.user.voice.channel.id:
        await interaction.response.send_message(content="**Du bist nicht in dem dazugehörigen VoiceChannel!**")
    else:
        await interaction.user.voice.channel.edit(user_limit=limit)
        await interaction.response.send_message(content=f"Das Benutzerlimit für **{interaction.user.voice.channel.name}** wurde auf **{limit}** gesetzt")
