import discord
async def handler(interaction: discord.Interaction):
    await interaction.response.defer()
    await interaction.edit_original_response(content= 'Hilfe ist untwegs')