from telebot import types



def phone_number():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    phone_number = types.KeyboardButton(text="Send your number!", request_contact=True)
    keyboard.row(phone_number)
    return keyboard


def products_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    laptops = types.KeyboardButton(text="Notebook")
    techniques = types.KeyboardButton(text="Techniques")
    monitors = types.KeyboardButton(text="Monitors")
    programs = types.KeyboardButton(text="Programs")
    accessories = types.KeyboardButton(text="Accessories")
    complects = types.KeyboardButton(text="Complects")
    keyboard.row(laptops,techniques)
    keyboard.row(monitors,programs)
    keyboard.row(accessories,complects)
    return keyboard

def techniques():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    techniques = types.KeyboardButton(text="Techniques")
    keyboard.row(techniques)
    return keyboard

def monitors():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    monitors = types.KeyboardButton(text="Monitors")
    keyboard.row(monitors)
    return keyboard

def programs():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    programs = types.KeyboardButton(text="Programs")
    keyboard.row(programs)
    return keyboard

def accessories():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    accessories = types.KeyboardButton(text="Accessories")
    keyboard.row(accessories)
    return keyboard


def complects():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    complects = types.KeyboardButton(text="Complects")
    keyboard.row(complects)
    return keyboard

def payment(url):
    keyboard = types.InlineKeyboardMarkup()
    btn_payment = types.InlineKeyboardButton(text="Payment!", url=url)
    keyboard.row(btn_payment)
    return keyboard


def back():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_btn = types.KeyboardButton(text="Orqaga")
    keyboard.row(back_btn)
    return keyboard