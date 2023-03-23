from aiogram import Router, types
from aiogram.types import CallbackQuery

from core.keyboards.inline import button_keyboard_start
from core.utils.dbconnect import Request

router = Router()

@router.message(commands=['start'])
async def cmd_start(message: types.Message, request: Request):
    text = (
        f'Данный бот предназначен для рассылки сообщений и рекламы\n'
        'пользователям напрямую, а так же в группы и чаты.'
    )
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await request.add_databases()
    await message.answer(
        f"Welcome to Hell, <b>{message.from_user.first_name}</b>.\n{text}",
        reply_markup=button_keyboard_start(),
        parse_mode="HTML"
    )

@router.callback_query_handler(lambda c: c.data == 'help')
async def cmd_help(callback: CallbackQuery):
    await callback.message.answer(
        f"Инструкция по использованию бота:\n"
        f"1. Редактировать список контактов(добавить/удалить)\n"
        f"2. Сформировать сообщение для рассылки\n"
        f"3. После нажатия на кнопку рассылка задать количество сообщений и интервал отправки\n"
        "4. Нажать кнопку 'Отправить'"
        )

@router.callback_query_handler(lambda c: c.data == 'back')
async def cmd_back(callback: CallbackQuery):
    await callback.message.answer(
        f"Welcome to Hell, <b>{callback.from_user.first_name}</b>.",
        reply_markup=button_keyboard_start(),
        parse_mode="HTML"
    )
