from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "579f1bcf3eac1660d81ef34b09906012")
      API_ID = int(getenv("API_ID", " 23903140"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "8520776596:AAFVjlV3Vtk_1G1yuJI72lO7j7eMcXyDBLY")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1003166629808: -1003169061900").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
