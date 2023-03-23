import logging
import asyncpg
import asyncio

from aiogram import Bot, Dispatcher

from config_reader import config
from core.utils.commands import set_commands
from core.handlers import basic, contacts, message, sender
from core.middlewares.dbmiddleware import DbSession
from core.utils.states import Stepscontacts, Stepsmessages, Stepssender
from config_reader import app

logging.basicConfig(level=logging.INFO)

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(1622135457, text='Бот запущен!')

async def stop_bot(bot: Bot):
    await bot.send_message(1622135457, text='Бот остановлен!')

async def create_pool():
    """Создание пулла соединения с БД"""
    return await asyncpg.create_pool(
        user='postgres',
        password='D97794422d69',
        database='spambot_database',
        host='127.0.0.1',
        port=5432,
        command_timeout=60
    )

async def main():
    
    bot = Bot(token=config.bot_token.get_secret_value())
    pool_connect = await create_pool()
    dp = Dispatcher()
    await app.start()

    dp.update.middleware.register(DbSession(pool_connect))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    
    dp.include_router(basic.router)

    dp.callback_query.register(contacts.get_contacts, lambda c: c.data == 'contacts')
    dp.callback_query.register(contacts.add_username, lambda c: c.data == 'add_contact')
    dp.callback_query.register(contacts.delete_username, lambda c: c.data == 'cancel_contact')
    dp.message.register(contacts.username, Stepscontacts.username)
    dp.message.register(contacts.cancel_contact, Stepscontacts.cancel_contact)

    dp.callback_query.register(message.get_message, lambda c: c.data == 'create_message')
    # dp.callback_query.register(message.get_message_image, lambda c: c.data == 'add_image')
    dp.message.register(message.get_text, Stepsmessages.get_text)
    # dp.message.register(message.get_image, Stepsmessages.get_image)

    dp.callback_query.register(sender.send_one, lambda c: c.data == 'send')
    dp.message.register(sender.get_count, Stepssender.get_count)
    dp.message.register(sender.get_time, Stepssender.get_time)
    dp.callback_query.register(sender.send_mes, lambda c: c.data == 'send_message')
    dp.callback_query.register(sender.send_stic, lambda c: c.data == 'send_sticker')

    try:
        await dp.start_polling(bot)
    finally:
        await app.stop()
        await dp.session.close()

if __name__ == "__main__":
    asyncio.run(main())
