from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


def lessons_menu():

    keyboard = [

        [
            InlineKeyboardButton("📘 1-dars F.I.SH", callback_data="lesson1"),
            InlineKeyboardButton("📘 2-dars Jshshr Tel", callback_data="lesson2")
        ],

        [
            InlineKeyboardButton("📘 3-dars Krill Lotin", callback_data="lesson3"),
            InlineKeyboardButton("📘 4-dars Yosh chegarasi", callback_data="lesson4")
        ]

    ]

    return InlineKeyboardMarkup(keyboard)

def less_btn():
    lessons_button = KeyboardButton("📚 Darslar")
    keyboard = ReplyKeyboardMarkup([[lessons_button]], resize_keyboard=True)
    return keyboard

def check_channel(CHANNEL):
    keyboard = [
        [InlineKeyboardButton("📢 Kanalga obuna", url=f"https://t.me/{CHANNEL.replace('@', '')}")],
        [InlineKeyboardButton("✅ Tekshirish", callback_data="check")]
    ]
    return keyboard
