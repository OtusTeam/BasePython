import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentTypes
from aiogram.dispatcher.filters import Text

from aiogram.utils import markdown

import config

# Configure logging
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)


def filter_hellos(message: types.Message):
    text = message.text.lower()
    return "привет" in text or "hello" in text


# @dp.message_handler(Text(contains="привет", ignore_case=True))
# @dp.message_handler(Text(contains="hello", ignore_case=True))
@dp.message_handler(filter_hellos)
async def greet_user(message: types.Message):
    await message.answer("И тебе привет!")


@dp.message_handler()
async def echo_message(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    text_to_send = markdown.text("You sent:", repr(message.text), sep=" ")
    logging.info("sending text %r", text_to_send)
    sent_msg: types.Message = await message.answer(text_to_send)
    logging.info("Sent message: %s", sent_msg)


@dp.message_handler(content_types=ContentTypes.STICKER)
async def echo_sticker(message: types.Message):
    await message.answer_sticker(message.sticker.file_id)


@dp.message_handler(content_types=ContentTypes.DICE)
async def handle_dice(message: types.Message):
    text = markdown.text(
        markdown.hbold("You sent"),
        repr(message.dice.emoji),
        "with value",
        message.dice.value,
        sep=" ",
    )
    await message.answer(text, parse_mode=types.ParseMode.HTML)


if __name__ == '__main__':
    executor.start_polling(dp)
