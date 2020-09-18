import logging
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import Message, ContentTypes
from aiogram.utils import executor

from config import TOKEN

BOT_DIR = Path(__file__).resolve().parent

STICKERS_DIR: Path = BOT_DIR / "stickers"
STICKERS_DIR.mkdir(exist_ok=True)

logging.basicConfig(level=logging.DEBUG)

bot = Bot(TOKEN)
dp = Dispatcher(bot)

logging_middleware = LoggingMiddleware()
dp.middleware.setup(logging_middleware)


@dp.message_handler()
async def echo_message(message: Message):
    return await message.answer(message.text)
    # await bot.send_message()


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def echo_photo(message: Message):
    return await message.answer_photo(
        message.photo[-1].file_id,
        caption=f"You wrote: {message.caption!r}",
    )


@dp.message_handler(content_types=ContentTypes.STICKER | ContentTypes.ANIMATION)
async def forward_any_sticker(message: Message):
    file_id = message.sticker.file_id
    await bot.download_file_by_id(
        file_id=file_id,
        destination=STICKERS_DIR / f"sticker_{file_id}.{'TGS' if message.sticker.is_animated else 'webp'}",
    )
    return await message.forward(message.chat.id)


if __name__ == "__main__":
    executor.start_polling(dp)
