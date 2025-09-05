from telegram import Update
from telegram.ext import CallbackContext
from utils.keyboards import get_main_menu
from config import WEBSITE_URL, TELEGRAM_CHANNEL, PHONE_NUMBER, EMAIL, YOUR_TELEGRAM_USERNAME

async def price(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /price"""
    price_text = f"""
💰 Каталог наших услуг:

🏠 Подъём домов - от 1500 руб/м²
🔨 Замена венцов - от 2000 руб/п.м.
🚚 Перемещение домов - от 50000 руб
🏡 Строительство каркасных домов - от 25000 руб/м²

📊 Подробные цены и расчет сметы на нашем сайте:
{WEBSITE_URL}

💬 Для точного расчета стоимости вашего проекта нажмите /order
    """
    await update.message.reply_text(
        price_text,
        reply_markup=get_main_menu()
    )

async def portfolio(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /portfolio"""
    portfolio_text = f"""
📸 Наше портфолио:

🏠 Подъём дома 6×8м на 1.2 метра
Фото: [Фото до] [Фото после]
Описание: Полный подъем с заменой фундамента

🔨 Замена венцов в бревенчатом доме
Фото: [Фото повреждений] [Фото после ремонта]  
Описание: Замена 25 п.м. нижних венцов

🚚 Перемещение дома 5×6м на 50 метров
Фото: [Фото старого места] [Фото нового места]
Описание: Перемещение на подготовленный фундамент

🏡 Каркасный дом 8×10м с отделкой
Фото: [Фото стройки] [Фото готового дома]
Описание: Полный цикл "под ключ"

📢 Больше наших работ в телеграм канале:
{TELEGRAM_CHANNEL}
    """
    
    await update.message.reply_text(
        portfolio_text,
        reply_markup=get_main_menu()
    )

async def about(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /about"""
    about_text = """
🏢 О нашей компании:

Мы специализируемся на ремонте, реконструкции и строительстве домов в Иркутске и области.

✅ 10+ лет опыта
✅ Гарантия на все работы
✅ Современное оборудование
✅ Квалифицированные специалисты
✅ Работаем по договору

Наша миссия - делать качественный ремонт доступным для каждого!
    """
    await update.message.reply_text(
        about_text,
        reply_markup=get_main_menu()
    )

async def contacts(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /contacts"""
    contacts_text = f"""
📞 Контактная информация:

📍 Адрес: Иркутск, ул. Строителей, 15
📞 Телефон: {PHONE_NUMBER}
📧 Email: {EMAIL}
🌐 Сайт: {WEBSITE_URL}

🕒 Режим работы:
Пн-Пт: 9:00-18:00
Сб: 10:00-16:00  
Вс: выходной

💬 Напишите мне в Telegram: [Написать сообщение](https://t.me/{YOUR_TELEGRAM_USERNAME})

Пишите нам в любое время - перезвоним в рабочее время!
    """
    await update.message.reply_text(
        contacts_text,
        parse_mode='Markdown',
        disable_web_page_preview=True,
        reply_markup=get_main_menu()
    )

async def handle_message(update: Update, context: CallbackContext) -> None:
    """Обработка обычных сообщений с показом главного меню"""
    await update.message.reply_text(
        "Выберите команду из меню:",
        reply_markup=get_main_menu()
    )