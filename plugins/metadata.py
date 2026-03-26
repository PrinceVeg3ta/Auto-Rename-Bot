from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from helper.database import db
from pyromod.exceptions import ListenerTimeout
from config import Txt


ON = [[InlineKeyboardButton('Metadata On ✅', callback_data='metadata_1')],
      [InlineKeyboardButton('Set Custom Metadata', callback_data='custom_metadata')]]

OFF = [[InlineKeyboardButton('Metadata Off ❌', callback_data='metadata_0')],
       [InlineKeyboardButton('Set Custom Metadata', callback_data='custom_metadata')]]


# 🔥 DATABASE FUNCTIONS (ADD THIS)
async def get_metadata(user_id):
    data = await db.find_one({"_id": user_id})
    return data.get("metadata", False) if data else False


async def set_metadata(user_id, value):
    await db.update_one(
        {"_id": user_id},
        {"$set": {"metadata": value}},
        upsert=True
    )


async def get_metadata_code(user_id):
    data = await db.find_one({"_id": user_id})
    return data.get("metadata_code", "") if data else ""


async def set_metadata_code(user_id, code):
    await db.update_one(
        {"_id": user_id},
        {"$set": {"metadata_code": code}},
        upsert=True
    )


# 🔥 COMMAND
@Client.on_message(filters.private & filters.command('metadata'))
async def handle_metadata(bot: Client, message: Message):

    ms = await message.reply_text("Please Wait...")
    
    bool_metadata = await get_metadata(message.from_user.id)
    user_metadata = await get_metadata_code(message.from_user.id)
    
    await ms.delete()

    if bool_metadata:
        return await message.reply_text(
            f"**Your Current Metadata :-**\n\n➜ `{user_metadata}`",
            reply_markup=InlineKeyboardMarkup(ON)
        )

    return await message.reply_text(
        f"**Your Current Metadata :-**\n\n➜ `{user_metadata}`",
        reply_markup=InlineKeyboardMarkup(OFF)
    )


# 🔥 CALLBACK
@Client.on_callback_query(filters.regex('.*?(custom_metadata|metadata).*?'))
async def query_metadata(bot: Client, query: CallbackQuery):

    data = query.data

    if data.startswith('metadata_'):
        _bool = data.split('_')[1]

        user_metadata = await get_metadata_code(query.from_user.id)

        if _bool == "1":
            await set_metadata(query.from_user.id, False)
            await query.message.edit(
                f"**Your Current Metadata :-**\n\n➜ `{user_metadata}`",
                reply_markup=InlineKeyboardMarkup(OFF)
            )
        else:
            await set_metadata(query.from_user.id, True)
            await query.message.edit(
                f"**Your Current Metadata :-**\n\n➜ `{user_metadata}`",
                reply_markup=InlineKeyboardMarkup(ON)
            )

    elif data == 'custom_metadata':
        await query.message.delete()

        try:
            try:
                metadata = await bot.ask(
                    text=Txt.SEND_METADATA,
                    chat_id=query.from_user.id,
                    filters=filters.text,
                    timeout=30
                )
            except ListenerTimeout:
                return await query.message.reply_text(
                    "⚠️ Timeout!\nUse /metadata again"
                )

            ms = await query.message.reply_text("Saving...")

            await set_metadata_code(query.from_user.id, metadata.text)

            await ms.edit("✅ Metadata saved successfully!")

        except Exception as e:
            print(e)