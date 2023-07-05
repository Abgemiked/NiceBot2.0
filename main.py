import json
import discord
import asyncio
from discord.ext import commands
from discord_interactions import verify_key_decorator, InteractionType
from discord import app_commands
from discord_interactions import InteractionResponseType
from commands.com_cmds.limit_cmd import handler as limit_cmd
from commands.streamer.streamer_cmd import handler as streamer_cmd
from commands.streamer.delstreamer_cmd import handler as delstreamer_cmd
from commands.team_cmds.clear_cmd import handler as clear_cmd
from commands.com_cmds.weather_cmd import handler as weather_cmd
from commands.team_cmds.settings_cmd import handler as settings_cmd
from commands.com_cmds.serverstats import handler as serverstats_cmd
from commands.help_cmd import handler as hilfe_cmd
from events.message_event import handler as message_handler
from events.logs.delete_log import on_raw_message_delete_handler
from events.logs.leave_log import on_member_remove_handler
from events.temp_channel.voice_temp import on_voice_state_update_handler
from events.statistic_channel.statistic import update_statistics
with open('./config.json', 'r', encoding= "utf-8") as f:
    cfg_json = json.load(f)
with open('wettericon.json') as config_file:
    wettericon = json.load(config_file)

TOKEN = cfg_json['TOKEN']
ALLGEMEIN_ID = cfg_json['ALLGEMEIN_ID']
OOF_ID = cfg_json['SPAM_CHANNEL_ID']
GIF_ID = cfg_json['GIF_ID']
LOG_CHANNEL_ID = cfg_json['LOG_CHANNEL_ID']
MUSIC_CHANNEL_ID = cfg_json['MUSIC_CHANNEL_ID']
PICTURE_CHANNEL_ID = cfg_json['PICTURE_CHANNEL_ID']
BOT_CHANNEL_ID = cfg_json['BOT_CHANNEL_ID']
BLOCKED_CHANNEL_IDS = cfg_json['BLOCKED_CHANNEL_IDS']
TEMP_CHANNEL_ID = cfg_json['TEMP_CHANNEL_ID']
ALLOWED_ROLE_IDS = cfg_json['ALLOWED_ROLE_IDS']
IGNORED_ROLE_ID = cfg_json['IGNORED_ROLE_ID']
GUILD_ID = cfg_json['GUILD_ID']
API_KEY = cfg_json['API_KEY']
BASE_URL = cfg_json['BASE_URL']
GEONAMES_API_USERNAME = cfg_json['GEONAMES_API_USERNAME']
weather_icons = wettericon["weather_icons"]

intents = discord.Intents(65419)
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync()
    print("Ready!")
    asyncio.create_task(update_statistics_loop())
async def update_statistics_loop():
    while True:
        guild = bot.get_guild(cfg_json['GUILD_ID'])
        print(f"Guild: {guild}")
        if guild:
            asyncio.create_task(update_statistics(cfg_json, guild))
        await asyncio.sleep(300)
@tree.command(description="Frag nach Hilfe")
async def hilfe(interaction: discord.Interaction):
    await hilfe_cmd(interaction)

@tree.command(description="Kategorie für Streamer erstellen")
async def streamer(interaction: discord.Interaction, streamer_name: discord.Member):
    await streamer_cmd(cfg_json, interaction, streamer_name)

@tree.command(description="Lösche Kategorie, Kanäle und Rollen für einen Streamer")
async def streamer_löschen(interaction: discord.Interaction, streamer: discord.Member):
    await delstreamer_cmd(cfg_json, interaction, streamer)

@tree.command(description="Nutzerlimit für den aktuellen Talk ändern")
async def limit(interaction: discord.Interaction, limit: int):
    await limit_cmd(cfg_json, interaction, limit)

@tree.command(description="Löscht eine angegebene Anzahl an Nachrichten im Channel")
async def löschen(interaction: discord.Interaction, amount: int):
    await clear_cmd(cfg_json, interaction, amount)

@tree.command(description="Hier kannst du das Wetter für deine Ortschaft abfragen")
async def wetter(interaction: discord.Interaction, ort: str):
    await weather_cmd(cfg_json, interaction, ort)

@tree.command(description="Servereinrichtung anpassen")
async def einstellungen(interaction: discord.Interaction, allgemein_channel: discord.TextChannel=None, spam_channel: discord.TextChannel=None, keyword: str=None, gif_channel: discord.TextChannel=None, log_channel: discord.TextChannel=None, musiccommand_channel: discord.TextChannel=None, temp_template_channel: discord.VoiceChannel=None, botcommand_channel: discord.TextChannel=None, adminrole: discord.Role=None, botrole: discord.Role=None, picture_channel: discord.TextChannel=None, api_key_weather: str=None,base_url: str=None, geonames_username: str=None):
    await settings_cmd(interaction, allgemein_channel, spam_channel, keyword, gif_channel, log_channel, musiccommand_channel, temp_template_channel, botcommand_channel, adminrole, botrole, picture_channel, api_key_weather, base_url, geonames_username)

@tree.command(description="Zeigt die aktuellen Nutzer ohne Bots an")
async def serverstats(interaction: discord.Interaction):
    await serverstats_cmd(interaction)

@bot.event
async def on_message(message):
    await message_handler(cfg_json, message)

@bot.event
async def on_raw_message_delete(payload):
    await on_raw_message_delete_handler(payload, bot, LOG_CHANNEL_ID, MUSIC_CHANNEL_ID, ALLOWED_ROLE_IDS)

@bot.event
async def on_member_remove(member):
    await on_member_remove_handler(member, bot, LOG_CHANNEL_ID)

@bot.event
async def on_voice_state_update(member, before, after):
    await on_voice_state_update_handler(member, before, after)

bot.run(cfg_json["TOKEN"])
