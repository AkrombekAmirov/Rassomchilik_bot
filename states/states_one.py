from aiogram.dispatcher.filters.state import State, StatesGroup


class Person(StatesGroup):
    number = State()
    name = State()
    set_number = State()
    image_number = State()
    school_number = State()
    age = State()


class Admin(StatesGroup):
    start = State()
    end = State()
