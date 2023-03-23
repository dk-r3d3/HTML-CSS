from aiogram.dispatcher.fsm.state import State, StatesGroup

class Stepscontacts(StatesGroup):
    username = State()
    cancel_contact = State()

class Stepsmessages(StatesGroup):
    get_text = State()
    get_image = State()

class Stepssender(StatesGroup):
    get_count = State()
    get_time = State()
