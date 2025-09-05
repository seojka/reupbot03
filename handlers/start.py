from telegram import Update
from telegram.ext import CallbackContext
from utils.keyboards import get_main_menu
from utils.notifications import send_notification, send_direct_message_link

async def start(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /start"""
    user = update.message.from_user
    welcome_text = f"""
🏠 Добро пожаловать, {user.first_name}!

Я бот компании по ремонту и строительству домов в Иркутске.

Доступные команды:
/start - Приветствие и список команд
/price - Каталог услуг и цены
/portfolio - Наши работы и портфолио
/order - Оформить заказ
/contacts - Контактная информация
/about - О нашей компании

Выберите нужную команду или нажмите /order чтобы оформить заказ!
    """
    await update.message.reply_text(
        welcome_text,
        reply_markup=get_main_menu()
    )
    
    # Отправляем уведомление о новом пользователе
    notification = f"👤 Новый пользователь: {user.first_name}"
    if user.username:
        notification += f" (@{user.username})"
    notification += f" ({user.id})"
    
    await send_notification(context, notification)
    
    # Если у пользователя нет username, отправляем ему ссылку
    if not user.username:
        await send_direct_message_link(context, user.id, user.first_name)