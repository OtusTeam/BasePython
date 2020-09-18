import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

from config import TOKEN

# webhook settings
WEBHOOK_HOST = "https://3129659b4512.ngrok.io"
WEBHOOK_PATH = f"/webhook/{TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = "localhost"
WEBAPP_PORT = 3000

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler()
async def echo(message: types.Message):
    # Regular request
    # await bot.send_message(message.chat.id, message.text)

    # or reply INTO webhook
    return SendMessage(message.chat.id, message.text * 2)


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=False,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )