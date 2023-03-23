from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.fsm.context import FSMContext

from core.keyboards.inline import button_keyboard_contacts
from core.utils.dbconnect import Request, get_usernames
from core.utils.states import Stepscontacts

router = Router()

async def get_contacts(callback: CallbackQuery):
    rows = await get_usernames()
    users = []
    for i in rows:
        user = i
        username = user['username']
        get_users = f'{username}'
        users.append(get_users)
    await callback.message.answer(
        f"Список контактов бота: {str(users)}", # изменить функционал, чтобы контакты были в строку
        reply_markup=button_keyboard_contacts()
    )


async def add_username(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "Введите имя пользователя, который будет добавлен"
        "в список контактов бота. Имя в формате '@testuser' "
        )
    await state.set_state(Stepscontacts.username)


async def username(message: Message, request: Request, state: FSMContext):
    await request.add_username(message.text)
    await state.clear()
    await message.answer(f'Пользователь {message.text} успешно добавлен.')


async def delete_username(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "Введите имя пользователя, которого хотите удалить из списка контактов."
        )
    await state.set_state(Stepscontacts.cancel_contact)


async def cancel_contact(message: Message, request: Request, state: FSMContext):
    await request.delete_username(message.text)
    await state.clear()
    await message.answer(f'Пользователь {message.text} удален.')
