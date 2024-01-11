import telebot
from keyboard import phone_number, products_menu, payment, back
from parsing_laptops import data_laptop
from parsing_office_technique import data_Base
from monitor_parsing import monitor_Base
from program_parsing import program_Base
from accessory_parsing import accessory_Base
from complects_parsing import complects_Base
from laptops_DATA_BASE import laptop_data_base
from monitor_DATA_BASE import monitor_data_base
from complects_DATA_BASE import complects_data_base
from program_DATA_BASE import program_data_base
from accessory_DATA_BASE import accessory_data_base
from office_technique_DATA_BASE import office_technique_data_base

token = "6766087680:AAF4ZnogYOe7hJCVlQsWJ6zLBtzfSJVrhuI"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_id = message.from_user.id
    username = message.from_user.username
    bot.send_message(chat_id, f"Hello {first_name} {last_name}"
        f"\nYour id: {user_id}\nUsername: {username}", reply_markup=phone_number())
    bot.register_next_step_handler(message, get_phone_number)

def get_phone_number(message):
    chat_id = message.chat.id
    phone_number = message.contact.phone_number
    bot.send_message(chat_id, f"Your number: {phone_number}\n"
                              f"Choose one of them!", reply_markup=products_menu())
    bot.register_next_step_handler(message, product_menu)


def product_menu(message):
    chat_id = message.chat.id
    if message.text == "Notebook":
        for parsed_notebooks in data_laptop:
            product_name = parsed_notebooks["Product_name"]
            product_price = parsed_notebooks["Product_price"]
            product_image = parsed_notebooks["Product_image"]
            bot.send_photo(chat_id, product_image, caption=f"Name: {product_name}\nPrice: {product_price}",
            reply_markup=payment("https://ultrashop.uz/ru/store/noutbuki"))

    elif message.text == "Techniques":
        for technique in data_Base:
            technique_name = technique["Technique_name"]
            technique_price = technique["Technique_price"]
            technique_image = technique["Technique_image"]
            bot.send_photo(chat_id, technique_image, caption=f"Name: {technique_name}\nPrice: {technique_price}",
                   reply_markup=payment("https://ultrashop.uz/ru/store/pechatnaya-tehnika"))


    elif message.text == "Monitors":
        for monitor in monitor_Base:
            product_name = monitor["Monitor_name"]
            product_price = monitor["Monitor_price"]
            product_image = monitor["Monitor_image"]
            bot.send_photo(chat_id, product_image, caption=f"Name: {product_name}\nPrice: {product_price}",
                   reply_markup=payment("https://ultrashop.uz/ru/store/monitory"))


    elif message.text == "Programs":
        for program in program_Base:
            product_name = program["Program_name"]
            product_price = program["Program_price"]
            product_image = program["Program_image"]
            bot.send_photo(chat_id, product_image, caption=f"Name: {product_name}\nPrice: {product_price}",
                           reply_markup=payment("https://ultrashop.uz/ru/store/programmy"))


    elif message.text == "Accessories":
        for program in accessory_Base:
            product_name = program["Accessory_name"]
            product_price = program["Accessory_price"]
            product_image = program["Accessory_image"]
            bot.send_photo(chat_id, product_image, caption=f"Name: {product_name}\nPrice: {product_price}",
                           reply_markup=payment("https://ultrashop.uz/ru/store/aksessuary"))



    elif message.text == "Complects":
        for program in complects_Base:
            product_name = program["Complects_name"]
            product_price = program["Complects_price"]
            product_image = program["Complects_image"]
            bot.send_photo(chat_id, product_image, caption=f"Name: {product_name}\nPrice: {product_price}",
                           reply_markup=payment("https://ultrashop.uz/ru/store/komplektuyushie"))

    bot.send_message(chat_id, "Choose one of them!", reply_markup=back())
    bot.register_next_step_handler(message, back_to_menu)



def back_to_menu(message):
    chat_id = message.chat.id
    if message.text == "Back":
        bot.send_message(chat_id, "Choose one of them!", reply_markup=products_menu())
        bot.register_next_step_handler(message, product_menu)


bot.polling(none_stop=True)