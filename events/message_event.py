
from events.filters.gif_flt import handler as gif_flt
from events.filters.oof_flt import handler as oof_flt
from events.filters.picture_flt import handler as picture_flt
from events.filters.bot_flt import handler as bot_flt

async def handler(cfg_json, message):
    #Chatfilter
    if await gif_flt(message):
        return
    if await oof_flt(message):
        return
    if await picture_flt(message):
        return
    if await bot_flt(message):
        return