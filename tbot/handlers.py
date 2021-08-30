from tbot.keyboards import get_menu_keyboards


def start(update, context):
    user = update.effective_user
    text = 'Assalomu Alaykum ! Asosiy menyuga xush kelibsiz !'
    update.message.reply_text(text=text, reply_markup=get_menu_keyboards())


def echo(update, context):
    update.message.reply_text(update.message.text)
