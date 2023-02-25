import env
import logging
__import__("os").system("pip install -U -r requirements.txt")
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Client(
    "bot",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="StringSessionBot"),
)


if __name__ == "__main__":
    print("Starting the bot")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("ʏᴏᴜʀ ᴀᴘɪ_ɪᴅ/ᴀᴘɪ_ʜᴀsʜ ɪs ɴᴏᴛ ᴠᴀʟɪᴅ.")
    except AccessTokenInvalid:
        raise Exception("ʏᴏᴜʀ ʙᴏᴛ_ᴛᴏᴋᴇɴ ɪs ɴᴏᴛ ᴠᴀʟɪᴅ.")
    uname = app.get_me().username
    print(f"@{uname} is now running!")
    idle()
    app.stop()
    print("ʙᴏᴛ sᴛᴏᴘᴘᴇᴅ. ᴀʟᴠɪᴅᴀ!")
