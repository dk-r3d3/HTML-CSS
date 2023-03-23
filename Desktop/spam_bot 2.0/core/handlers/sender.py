import time
from config_reader import app
from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.fsm.context import FSMContext

from core.keyboards.inline import button_keyboard_start_two, button_keyboard_send_3
from core.utils.dbconnect import get_usernames
from core.utils.states import Stepssender
from core.handlers.message import text_mes

count = 0
interval = 0

async def send_one(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        (
        f"Если вы еще не сформировали сообщение, то сформируйте его. \n"
        f"Если сообщение уже есть, задайте желаемое количество сообщений, которое хотите отправить."),
        reply_markup=button_keyboard_start_two()
    )
    await state.set_state(Stepssender.get_count)


async def get_count(message: Message, state: FSMContext):
    global count
    count = int(message.text)
    await message.answer(f"Заданное вами сообщение будет отправлено {count} раз.")
    await message.answer(f"Задайте интервал отправки (в секундах).")
    await state.set_state(Stepssender.get_time)


async def get_time(message: Message, state: FSMContext):
    global count
    global interval
    interval = int(message.text)
    await message.answer(f"Заданное вами сообщение будет отправлено {count} раз с интервалом в {interval} секунд.")
    await message.answer(f"Если все готово, нажмите 'Отправить' ", reply_markup=button_keyboard_send_3())
    await state.set_state(Stepssender.get_time)


async def send_mes(message: Message, bot: Bot):
    global count
    global interval
    rows = await get_usernames()
    for i in rows:
        username = i['username']
        for j in range(int(count)):
            time.sleep(int(interval))
            try:
                await app.send_message(username, text_mes[0])
                await message.answer(f"Сообщение отправлено.")
            except Exception as e:
                await bot.send_message(
                    chat_id=message.from_user.id,
                    text=(
                    f"Ошибка - {e} \n\r\n\r"
                    "Если не знаете, как решить эту ошибку - пишите админу"
                    )
                )
    text_mes.clear()


async def send_stic(message: Message, bot: Bot):
    global count
    global interval
    rows = await get_usernames()
    for i in rows:
        username = i['username']
        for j in range(int(count)):
            time.sleep(int(interval))
            try:
                await app.send_sticker(username, text_mes[0])
                await message.answer(f"Стикер отправлен.")
            except Exception as e:
                await bot.send_message(
                    chat_id=message.from_user.id,
                    text=(
                    f"Ошибка - {e} \n\r\n\r"
                    "Если не знаете, как решить эту ошибку - пишите админу"
                    )
                )
