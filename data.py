from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("❣️ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ ❣️", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text=" 🥀 ʙᴀᴄᴋ 🥀 ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ ᴅᴇᴠᴇʟᴏᴘᴇʀ  ✨", url="https://t.me/an_unic_or_n47")],
        [
            InlineKeyboardButton(" ❔ ʜᴇʟᴘ ❔", callback_data="help"),
            InlineKeyboardButton("🎪 ᴀʙᴏᴜᴛ 🎪", callback_data="about")
        ],
        
    ]

    START = """
Hᴏɪ {}

Tʜɪs ɪs {}

A sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.
ғᴏʀ ɢᴇɴᴇʀᴀᴛɪɴɢ ᴛʜᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴs

ᴏᴡᴏ ʙʏ : [Λnanya](https://an_unic_or_n47)
    """

    HELP = """
✨ **Aᴠᴀɪʟᴀʙʟᴇ Cᴏᴍᴍᴀɴᴅs** ✨

/about - Aʙᴏᴜᴛ Tʜᴇ Bᴏᴛ
/help - Tʜɪs Mᴇssᴀɢᴇ
/start - Sᴛᴀʀᴛ ᴛʜᴇ Bᴏᴛ
/generate - Gᴇɴᴇʀᴀᴛᴇ Sᴇssɪᴏɴ
/cancel - Cᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
/restart - Cᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
"""

    ABOUT = """
**Aʙᴏᴜᴛ Tʜɪs Bᴏᴛ** 
  
  Tᴇʟᴇɢʀᴀᴍ Bᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ Pʏʀᴏɢʀᴀᴍ ᴀɴᴅ Tᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ
  
  
  Fʀᴀᴍᴇᴡᴏʀᴋ : [Pʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org)
  
  Lᴀɴɢᴜᴀɢᴇ : [Pʏᴛʜᴏɴ](https://www.python.org)
  
  Dᴇᴠᴇʟᴏᴘᴇʀ : [Λnanya](https://t.me/an_unic_or_n47)
      """
