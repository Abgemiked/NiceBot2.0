import discord

async def handler(cfg_json, interaction, streamer_name):
    streamer_names = streamer_name.name.capitalize()
    category_name = f'📺 {streamer_names}'
    text_channel_names = ['🔊-streaming', '🎥-clips']
    voice_channel_names = [f'💻 {streamer_names}-Live', f'💻 {streamer_names}-Warteraum']
    role_names = [f'👨‍💻 {streamer_names}', f'👨‍💻 {streamer_names}-Mod', f'👨‍💻 {streamer_names}-Zuschauer']
    
    # creates category
    category = await interaction.guild.create_category(category_name)
    await interaction.response.defer()
    
    # creates text channels
    for name in text_channel_names:
        await category.create_text_channel(name)
    
    # creates voice channels
    for name in voice_channel_names:
        await category.create_voice_channel(name)
    
    # creates roles
    roles = []
    for name in role_names:
        role = await interaction.guild.create_role(name=name)
        roles.append(role)
    
    # set permissions for category
    for role in roles:
        if role.name == f'👨‍💻 {streamer_names}':
            await category.set_permissions(
                role,
                view_channel=True,
                manage_channels=True,
                manage_permissions=True,
                manage_webhooks=True,
                create_instant_invite=True,
                send_messages=True,
                send_messages_in_threads=True,
                create_public_threads=True,
                create_private_threads=True,
                embed_links=True,
                attach_files=True,
                add_reactions=True,
                use_external_emojis=True,
                use_external_stickers=True,
                mention_everyone=False,
                manage_messages=True,
                manage_threads=True,
                read_message_history=True,
                send_tts_messages=True,
                use_application_commands=True,
                send_voice_messages=True,
                connect=True,
                speak=True,
                stream=True,
                use_embedded_activities=True,
                use_soundboard=True,
                use_external_sounds=True,
                use_voice_activation=True,
                mute_members=True,
                deafen_members=True,
                move_members=True,
                request_to_speak=True,
                manage_events=True
            )
        elif role.name == f'👨‍💻 {streamer_names}-Mod':
            await category.set_permissions(
                role,
                view_channel=True,
                manage_channels=False,
                manage_permissions=False,
                manage_webhooks=False,
                create_instant_invite=True,
                send_messages=True,
                send_messages_in_threads=True,
                create_public_threads=True,
                create_private_threads=True,
                embed_links=True,
                attach_files=True,
                add_reactions=True,
                use_external_emojis=True,
                use_external_stickers=True,
                mention_everyone=False,
                manage_messages=True,
                manage_threads=True,
                read_message_history=True,
                send_tts_messages=True,
                use_application_commands=True,
                send_voice_messages=True,
                connect=True,
                speak=True,
                stream=True,
                use_embedded_activities=True,
                use_soundboard=True,
                use_external_sounds=True,
                use_voice_activation=True,
                mute_members=True,
                deafen_members=True,
                move_members=True,
                request_to_speak=True,
                manage_events=False
            )
        elif role.name == f'👨‍💻 {streamer_names}-Zuschauer':
            await category.set_permissions(
                role,
                view_channel=True,
                manage_channels=False,
                manage_permissions=False,
                manage_webhooks=False,
                create_instant_invite=True,
                send_messages=True,
                send_messages_in_threads=True,
                create_public_threads=True,
                create_private_threads=True,
                embed_links=True,
                attach_files=True,
                add_reactions=True,
                use_external_emojis=True,
                use_external_stickers=True,
                mention_everyone=False,
                manage_messages=False,
                manage_threads=False,
                read_message_history=True,
                send_tts_messages=True,
                use_application_commands=True,
                send_voice_messages=True,
                connect=True,
                speak=True,
                stream=True,
                use_embedded_activities=True,
                use_soundboard=True,
                use_external_sounds=True,
                use_voice_activation=True,
                mute_members=False,
                deafen_members=False,
                move_members=False,
                request_to_speak=True,
                manage_events=False
            )
    
    await category.set_permissions(interaction.guild.default_role, read_messages=False, connect=False)

    for channel in category.channels:
        await channel.edit(sync_permissions=True)
    
    await interaction.edit_original_response(content=f"Die Kategorie, Channel & Rollen für **{streamer_names}** wurden eingerichtet & können verwendet werden.")
