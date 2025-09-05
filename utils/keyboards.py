from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

# Категории услуг с кнопкой отмены
CATEGORIES = [
    ["Подъём дома"],
    ["Замена венцов"], 
    ["Перемещение дома"],
    ["Строительство каркасных домов"],
    ["❌ Отмена заказа"]
]

# Главное меню
MAIN_MENU = [
    ["/price", "/portfolio"],
    ["/order", "/contacts"],
    ["/about", "/start"]
]

def get_main_menu():
    """Возвращает клавиатуру главного меню"""
    return ReplyKeyboardMarkup(
        MAIN_MENU,
        resize_keyboard=True,
        input_field_placeholder="Выберите команду..."
    )

def get_categories_keyboard():
    """Возвращает клавиатуру категорий"""
    return ReplyKeyboardMarkup(
        CATEGORIES,
        one_time_keyboard=True,
        resize_keyboard=True,
        input_field_placeholder="Выберите услугу или отмените заказ..."
    )

def remove_keyboard():
    """Убирает клавиатуру"""
    return ReplyKeyboardRemove()