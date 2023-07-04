import discord

async def handler(cfg_json, interaction, streamer):
    streamer_category = streamer.name.capitalize()
    category_name = f'📺 {streamer_category}'
    category = discord.utils.get(interaction.guild.categories, name=category_name)
    
    if not category:
        await interaction.response.send_message(content=f"Die Kategorie für **{streamer_category}** existiert nicht.")
        return
    
    await interaction.response.defer()
    
    for channel in category.channels:
        await channel.delete()
    
    role_names = [f'👨‍💻 {streamer_category}', f'👨‍💻 {streamer_category}-Mod', f'👨‍💻 {streamer_category}-Zuschauer']
    
    for role_name in role_names:
        role = discord.utils.get(interaction.guild.roles, name=role_name)
        if role:
            await role.delete()
    
    await category.delete()
    
    await interaction.edit_original_response(content=f"Die Kategorie von **{streamer_category}** wurde gelöscht.")
