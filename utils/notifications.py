from telegram import Update
from telegram.ext import CallbackContext
from config import ADMIN_CHAT_ID, YOUR_TELEGRAM_USERNAME

async def send_notification(context: CallbackContext, message: str):
    """Отправка уведомления администратору"""
    try:
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID, 
            text=message,
            parse_mode='HTML'
        )
        return True
    except Exception as e:
        print(f"Ошибка отправки уведомления: {e}")
        return False

async def send_direct_message_link(context: CallbackContext, user_id: int, user_first_name: str):
    """Отправить пользователю ссылку для прямого сообщения"""
    try:
        message_text = f"""
👋 Привет, {user_first_name}!

Я заметил, что у вас не установлен username в Telegram.

Чтобы я мог легко с вами связаться, вы можете:
1. Установить username в настройках Telegram
2. Или написать мне напрямую: [Написать сообщение](https://t.me/{YOUR_TELEGRAM_USERNAME})

Так мы сможем оперативно обсудить детали вашего заказа! 📞
        """
        
        await context.bot.send_message(
            chat_id=user_id,
            text=message_text,
            parse_mode='Markdown',
            disable_web_page_preview=True
        )
        return True
    except Exception as e:
        print(f"Ошибка отправки ссылки пользователю: {e}")
        return False