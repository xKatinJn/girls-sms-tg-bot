import os
import logging
import random

from database import User, Phrases
from chatting import *
from keyboards import *

from telegram import Update, Bot
from telegram.ext import Updater, CallbackContext, Filters, MessageHandler


admin_id = int(os.getenv('admin_id'))
bot = Bot(
    token=os.getenv('token')
)


def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    user_id = update.message.from_user.id

    if user_id not in User.get_all_users_ids():
        current_user = User(user_id=user_id, user_step=1)
        current_user.save()
    else:
        current_user = User.get(User.user_id == user_id)

    print(current_user.user_id == admin_id)

    if current_user.user_step == 1:
        if text == buttons_loc['main_menu_play_ru']:
            User.update(user_step=2).where(User.user_id == current_user.user_id).execute()
            return start_spin_menu(update, context, reply_markup=keyboard_spin_ru)
        elif text == buttons_loc['main_menu_thanks_ru']:
            User.update(user_step=3).where(User.user_id == current_user.user_id).execute()
            return start_author_thank_menu(update, context, reply_markup=keyboard_author_thank_ru)
        elif text == buttons_loc['main_menu_admin_ru'] and current_user.user_id == admin_id:
            User.update(user_step=8).where(User.user_id == current_user.user_id).execute()

            phrases = Phrases.format_all_phrases(Phrases.get_all_phrases())
            if not phrases:
                phrases = 'Список фраз пуст.\n\n'

            return start_phrase_editing(update, context, phrases, reply_markup=keyboard_phrase_editing_admin_ru)

        if current_user.user_id == admin_id:
            return start_main_menu(update, context, reply_markup=keyboard_main_menu_admin_ru)
        else:
            return start_main_menu(update, context, reply_markup=keyboard_main_menu_ru)

    elif current_user.user_step == 2:
        if text == buttons_loc['spin']:
            phrase = random.choice(Phrases.get_all_phrases(True))
            return send_message(update, context, text=f'Девочка прочитает: *"{phrase}"*')
        elif text == buttons_loc['back_ru']:
            User.update(user_step=1).where(User.user_id == current_user.user_id).execute()
            if current_user.user_id == admin_id:
                return start_main_menu(update, context, reply_markup=keyboard_main_menu_admin_ru)
            else:
                return start_main_menu(update, context, reply_markup=keyboard_main_menu_ru)

        return start_spin_menu(update, context, reply_markup=keyboard_spin_ru)

    elif current_user.user_step == 3:
        if text == buttons_loc['author_thank_girl_ru']:
            User.update(user_step=4).where(User.user_id == current_user.user_id).execute()
            return send_message(update, context, text=texts_loc['author_thank_girl_ru'],
                                reply_markup=remove_keyboard)
        elif text == buttons_loc['author_thank_feature_ru']:
            User.update(user_step=5).where(User.user_id == current_user.user_id).execute()
            return send_message(update, context, text=texts_loc['author_thank_default_ru'],
                                reply_markup=remove_keyboard)
        elif text == buttons_loc['author_thank_thanks_ru']:
            User.update(user_step=6).where(User.user_id == current_user.user_id).execute()
            return send_message(update, context, text=texts_loc['author_thank_default_ru'],
                                reply_markup=remove_keyboard)
        elif text == buttons_loc['author_thank_other_ru']:
            User.update(user_step=7).where(User.user_id == current_user.user_id).execute()
            return send_message(update, context, text=texts_loc['author_thank_default_ru'],
                                reply_markup=remove_keyboard)
        elif text == buttons_loc['back_ru']:
            User.update(user_step=1).where(User.user_id == current_user.user_id).execute()
            if current_user.user_id == admin_id:
                return start_main_menu(update, context, reply_markup=keyboard_main_menu_admin_ru)
            else:
                return start_main_menu(update, context, reply_markup=keyboard_main_menu_ru)

    elif current_user.user_step == 4:
        User.update(user_step=1).where(User.user_id == current_user.user_id).execute()
        send_message_to_id(bot, f'Благодарность: 💝 Подогнать девочку\n'
                                f'Пользователь: {update.message.from_user.name}\n'
                                f'Сообщение: {text}',
                           admin_id)
        if current_user.user_id == admin_id:
            return start_main_menu(update, context, reply_markup=keyboard_main_menu_admin_ru)
        else:
            return start_main_menu(update, context, reply_markup=keyboard_main_menu_ru)

    elif current_user.user_step == 5:
        User.update(user_step=1).where(User.user_id == current_user.user_id).execute()
        send_message_to_id(bot, f'Благодарность: 🧐 Поделиться фишкой\n'
                                f'Пользователь: {update.message.from_user.name}\n'
                                f'Сообщение: {text}',
                           admin_id)
        if current_user.user_id == admin_id:
            return start_main_menu(update, context, reply_markup=keyboard_main_menu_admin_ru)
        else:
            return start_main_menu(update, context, reply_markup=keyboard_main_menu_ru)

    elif current_user.user_step == 6:
        User.update(user_step=1).where(User.user_id == current_user.user_id).execute()
        send_message_to_id(bot, f'Благодарность: 💬 Сказать спасибо\n'
                                f'Пользователь: {update.message.from_user.name}\n'
                                f'Сообщение: {text}',
                           admin_id)
        if current_user.user_id == admin_id:
            return start_main_menu(update, context, reply_markup=keyboard_main_menu_admin_ru)
        else:
            return start_main_menu(update, context, reply_markup=keyboard_main_menu_ru)

    elif current_user.user_step == 7:
        User.update(user_step=1).where(User.user_id == current_user.user_id).execute()
        send_message_to_id(bot, f'Благодарность: 🎁 Другое\n'
                                f'Пользователь: {update.message.from_user.name}\n'
                                f'Сообщение: {text}',
                           admin_id)
        if current_user.user_id == admin_id:
            return start_main_menu(update, context, reply_markup=keyboard_main_menu_admin_ru)
        else:
            return start_main_menu(update, context, reply_markup=keyboard_main_menu_ru)

    elif current_user.user_step == 8:
        if text == buttons_loc['phrase_editing_add_ru']:
            User.update(user_step=9).where(User.user_id == current_user.user_id).execute()
            return send_message(update, context, text=texts_loc['phrases_editing_add_ru'],
                                reply_markup=remove_keyboard)
        elif text == buttons_loc['phrase_editing_delete_ru']:
            User.update(user_step=10).where(User.user_id == current_user.user_id).execute()
            return send_message(update, context, text=texts_loc['phrases_editing_delete_ru'],
                                reply_markup=remove_keyboard)
        elif text == buttons_loc['back_ru']:
            User.update(user_step=1).where(User.user_id == current_user.user_id).execute()
            if current_user.user_id == admin_id:
                return start_main_menu(update, context, reply_markup=keyboard_main_menu_admin_ru)
            else:
                return start_main_menu(update, context, reply_markup=keyboard_main_menu_ru)

        phrases = Phrases.format_all_phrases(Phrases.get_all_phrases())

        if not phrases:
            phrases = 'Список фраз пуст.\n\n'

        return start_phrase_editing(update, context, phrases, keyboard_phrase_editing_admin_ru)

    elif current_user.user_step == 9:
        User.update(user_step=8).where(User.user_id == current_user.user_id).execute()
        Phrases(phrase=text).save()

        phrases = Phrases.format_all_phrases(Phrases.get_all_phrases())

        if not phrases:
            phrases = 'Список фраз пуст.\n\n'

        return start_phrase_editing(update, context, phrases, keyboard_phrase_editing_admin_ru)

    elif current_user.user_step == 10:
        User.update(user_step=8).where(User.user_id == current_user.user_id).execute()
        Phrases.delete_by_id(int(text))

        phrases = Phrases.format_all_phrases(Phrases.get_all_phrases())

        if not phrases:
            phrases = 'Список фраз пуст.\n\n'

        return start_phrase_editing(update, context, phrases, keyboard_phrase_editing_admin_ru)


def start() -> None:
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    updater = Updater(
        token=os.getenv('token'),
        use_context=True
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    start()
