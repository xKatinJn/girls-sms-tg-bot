from localization import buttons_loc

from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


remove_keyboard = ReplyKeyboardRemove(
    remove_keyboard=True
)

keyboard_spin_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=buttons_loc['spin']),
         KeyboardButton(text=buttons_loc['back_ru'])]
    ]
)

keyboard_main_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=buttons_loc['main_menu_play_ru'])] # ,KeyboardButton(text=buttons_loc['main_menu_thanks_ru'])
    ]
)

keyboard_main_menu_admin_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=buttons_loc['main_menu_play_ru'])], # ,KeyboardButton(text=buttons_loc['main_menu_thanks_ru'])
        [KeyboardButton(text=buttons_loc['main_menu_admin_ru'])]
    ]
)

keyboard_author_thank_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=buttons_loc['author_thank_girl_ru']),
         KeyboardButton(text=buttons_loc['author_thank_feature_ru'])],
        [KeyboardButton(text=buttons_loc['author_thank_thanks_ru']),
         KeyboardButton(text=buttons_loc['author_thank_other_ru'])],
        [KeyboardButton(text=buttons_loc['back_ru'])]
    ]
)

keyboard_phrase_editing_admin_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=buttons_loc['phrase_editing_add_ru']),
         KeyboardButton(text=buttons_loc['phrase_editing_delete_ru'])],
        [KeyboardButton(text=buttons_loc['back_ru'])]
    ]
)
