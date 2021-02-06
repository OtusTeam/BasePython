import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes, ContentType

import config

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize bot and dispatcher
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(content_types=ContentTypes.TEXT)
async def echo_message(message: types.Message):
    # await message.reply(message.text)
    user_sender = message.from_user
    # await bot.send_message(user_sender.id, text=f"Hi, {user_sender.full_name}!")
    # await message.bot.send_message(user_sender.id, text=f"Hi, {user_sender.full_name}!")
    return await message.answer(f"Hi, {user_sender.full_name}!")
    # return True


@dp.message_handler(content_types=ContentTypes.STICKER | ContentTypes.ANIMATION)
async def handle_sticker_or_animation(message: types.Message, state: FSMContext):
    # await state.set_state("abc")
    logging.info("current state: %s", (await state.get_state()))
    logging.info("current data: %s", (await state.get_data()))
    logging.info("Content type %s", message.content_type)
    if message.content_type == ContentType.STICKER:
        if message.sticker.is_animated:
            logging.debug("animated sticker")
        return await message.answer_sticker(message.sticker.file_id)

    return await message.answer_animation(message.animation.file_id)


if __name__ == "__main__":
    executor.start_polling(dp)
