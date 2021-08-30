from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu_keyboards():
    keyboard = [
        [
            InlineKeyboardButton("Online Market 🛒", callback_data='market'),
            InlineKeyboardButton("Xizmatlar ⌨", callback_data='services'),
        ],
        [
            InlineKeyboardButton("Biz haqimizda 👤", callback_data='about'),
            InlineKeyboardButton("Bot Qanday Ishlaydi 🤖", callback_data='about_bot'),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
