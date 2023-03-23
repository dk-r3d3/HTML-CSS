from aiogram.utils.keyboard import InlineKeyboardBuilder

def button_keyboard_start(): # основное меню
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='1. Контакты', callback_data='contacts')
    keyboard_builder.button(text='2. Рассылка', callback_data='send')
    keyboard_builder.button(text='3. Инструкция', callback_data='help')
    keyboard_builder.button(text='4. Сформировать сообщение', callback_data='create_message')
    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()

def button_keyboard_start_two(): # кнопка после нажатия "Рассылка"
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Сформировать сообщение', callback_data='create_message')
    return keyboard_builder.as_markup()

# def button_keyboard_message_1():
#     keyboard_builder = InlineKeyboardBuilder()
#     keyboard_builder.button(text='Добавить картинку', callback_data='add_image')
#     keyboard_builder.button(text='Рассылка без картинки', callback_data='send')
#     keyboard_builder.button(text='Назад', callback_data='back')
#     keyboard_builder.adjust(3)
#     return keyboard_builder.as_markup()

# def button_keyboard_message_2():
#     keyboard_builder = InlineKeyboardBuilder()
#     keyboard_builder.button(text='Добавить кнопку', callback_data='add_button')
#     keyboard_builder.button(text='Продолжить без кнопки', callback_data='no_button')
#     keyboard_builder.adjust(1)
#     return keyboard_builder.as_markup()

def button_keyboard_send():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Рассылка', callback_data='send')
    keyboard_builder.button(text='Назад', callback_data='back')
    return keyboard_builder.as_markup()

def button_keyboard_send_1():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Установить количество сообщений', callback_data='count')
    keyboard_builder.button(text='Назад', callback_data='back')
    return keyboard_builder.as_markup()

def button_keyboard_send_2():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Установить интервал отправки', callback_data='interval')
    keyboard_builder.button(text='Назад', callback_data='back')
    return keyboard_builder.as_markup()

def button_keyboard_send_3():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Отправить сообщение', callback_data='send_message')
    keyboard_builder.button(text='Отправить стикер', callback_data='send_sticker')
    keyboard_builder.button(text='Назад', callback_data='back')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()

def button_keyboard_contacts():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Добавить контакт', callback_data='add_contact')
    keyboard_builder.button(text='Удалить контакт', callback_data='cancel_contact')
    keyboard_builder.button(text='Назад', callback_data='back')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
