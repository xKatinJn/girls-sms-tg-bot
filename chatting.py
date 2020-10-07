from localization import buttons_loc, texts_loc

from telegram import Update, ReplyKeyboardMarkup, Bot, ParseMode
from telegram.ext import CallbackContext


def send_message(update: Update, context: CallbackContext, text: str, reply_markup: ReplyKeyboardMarkup = None) -> None:
    update.message.reply_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode='markdown'
    )


def send_message_to_id(bot: Bot, text: str, chat_id: int) -> None:
    bot.send_message(
        chat_id=chat_id,
        text=text
    )


def start_main_menu(update: Update, context: CallbackContext, reply_markup: ReplyKeyboardMarkup = None) -> None:
    update.message.reply_text(
        text=texts_loc['main_menu_ru'],
        reply_markup=reply_markup
    )


def start_spin_menu(update: Update, context: CallbackContext, reply_markup: ReplyKeyboardMarkup = None) -> None:
    update.message.reply_text(
        text=texts_loc['press_the_button_ru'],
        reply_markup=reply_markup
    )


def start_author_thank_menu(update: Update, context: CallbackContext, reply_markup: ReplyKeyboardMarkup = None) -> None:
    update.message.reply_text(
        text=texts_loc['author_thank_menu_ru'],
        reply_markup=reply_markup
    )


def start_phrase_editing(update: Update, context: CallbackContext, phrases: str, reply_markup: ReplyKeyboardMarkup = None) -> None:
    update.message.reply_text(
        text=phrases+texts_loc['phrase_editing_start_ru'],
        reply_markup=reply_markup,
        parse_mode='markdown'
    )
