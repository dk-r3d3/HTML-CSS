from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.fsm.context import FSMContext

from core.utils.states import Stepsmessages
from core.keyboards.inline import button_keyboard_send

router = Router()

text_mes = [] # сообщение сохраняется в список

async def get_message(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        f'Создается рассылка. \r\n\r\n'
        f'Вы можете отправить либо сообещение, либо код стикера \r\n'
        f'Код стикера можно получить отправив стикер данному боту "https://t.me/idstickerbot" \r\n'
        f'Код стикера не должен содержать пробелов \r\n'
        f'Отправьте текст рассылки'
    )
    await state.set_state(Stepsmessages.get_text)

# async def get_message_image(callback: CallbackQuery, state: FSMContext):
#     await callback.message.answer(
#         f'Откправьте картинку'
#     )
#     await state.set_state(Stepsmessages.get_image)

async def get_text(message: Message, state: FSMContext):
    text_mes.append(message.text)
    await state.clear()
    await message.answer(f'Сообщение "{text_mes[0]}" сохранено.', reply_markup=button_keyboard_send())
