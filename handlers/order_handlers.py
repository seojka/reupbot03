from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from utils.keyboards import get_categories_keyboard, remove_keyboard, get_main_menu
from utils.notifications import send_notification
from utils.database import save_order
from config import YOUR_TELEGRAM_USERNAME
from datetime import datetime
from .conversation_states import *

async def order(update: Update, context: CallbackContext) -> int:
    """Начало оформления заказа"""
    user = update.message.from_user
    
    # Если у пользователя нет username, напоминаем ему
    if not user.username:
        reminder_text = f"""
📝 <b>Внимание!</b>

У вас не установлен username в Telegram. Рекомендую его настроить для удобства связи.

А пока вы можете:
• Указать телефон в контактных данных
• Или написать мне напрямую: [Написать сообщение](https://t.me/{YOUR_TELEGRAM_USERNAME})
        """
        await update.message.reply_text(
            reminder_text,
            parse_mode='HTML',
            disable_web_page_preview=True
        )
    
    await update.message.reply_text(
        "🏠 Выберите категорию услуги:",
        reply_markup=get_categories_keyboard()
    )
    
    return CATEGORY

async def category(update: Update, context: CallbackContext) -> int:
    """Обработка выбора категории"""
    user_choice = update.message.text
    context.user_data['category'] = user_choice
    
    if user_choice == "❌ Отмена заказа":
        return await cancel(update, context)
        
    elif user_choice == "Подъём дома":
        await update.message.reply_text(
            "🏠 Подъём дома\n\nВведите данные через запятую в формате:\n"
            "Размер дома (например: 6x8м), Этажность, Высота подъема\n\n"
            "Пример: 6x8м, 1, 1.2м",
            reply_markup=remove_keyboard()
        )
        return HOUSE_LIFTING
        
    elif user_choice == "Замена венцов":
        await update.message.reply_text(
            "🔨 Замена венцов\n\nВведите данные через запятую в формате:\n"
            "Материал (брус/бревно), Сечение, Погонные метры\n\n"
            "Пример: брус, 150x150мм, 25",
            reply_markup=remove_keyboard()
        )
        return CROWN_REPLACEMENT
        
    elif user_choice == "Перемещение дома":
        await update.message.reply_text(
            "🚚 Перемещение дома\n\nВведите данные через запятую в формате:\n"
            "Размер дома, Материал стен, Расстояние, Готов ли фундамент (да/нет/в процессе)\n\n"
            "Пример: 5x6м, брус, 50м, да",
            reply_markup=remove_keyboard()
        )
        return HOUSE_MOVING
        
    elif user_choice == "Строительство каркасных домов":
        await update.message.reply_text(
            "🏡 Строительство каркасных домов\n\nВведите данные через запятую в формате:\n"
            "Размер, Этажность, Количество комнат, Отделка, Пожелания\n\n"
            "Пример: 8x10м, 1, 3, чистовая, терраса и котельная",
            reply_markup=remove_keyboard()
        )
        return FRAME_HOUSES
        
    else:
        await update.message.reply_text(
            "Пожалуйста, выберите категорию из предложенных:",
            reply_markup=get_categories_keyboard()
        )
        return CATEGORY

async def house_lifting(update: Update, context: CallbackContext) -> int:
    """Обработка данных для подъема дома"""
    if update.message.text == "❌ Отмена заказа":
        return await cancel(update, context)
        
    context.user_data['details'] = update.message.text
    await update.message.reply_text(
        "📞 Пожалуйста, оставьте ваши контактные данные (телефон или Telegram):",
        reply_markup=remove_keyboard()
    )
    return CONTACT_INFO

async def crown_replacement(update: Update, context: CallbackContext) -> int:
    """Обработка данных для замены венцов"""
    if update.message.text == "❌ Отмена заказа":
        return await cancel(update, context)
        
    context.user_data['details'] = update.message.text
    await update.message.reply_text(
        "📞 Пожалуйста, оставьте ваши контактные данные (телефон или Telegram):",
        reply_markup=remove_keyboard()
    )
    return CONTACT_INFO

async def house_moving(update: Update, context: CallbackContext) -> int:
    """Обработка данных для перемещения дома"""
    if update.message.text == "❌ Отмена заказа":
        return await cancel(update, context)
        
    context.user_data['details'] = update.message.text
    await update.message.reply_text(
        "📞 Пожалуйста, оставьте ваши контактные данные (телефон или Telegram):",
        reply_markup=remove_keyboard()
    )
    return CONTACT_INFO

async def frame_houses(update: Update, context: CallbackContext) -> int:
    """Обработка данных для строительства каркасных домов"""
    if update.message.text == "❌ Отмена заказа":
        return await cancel(update, context)
        
    context.user_data['details'] = update.message.text
    await update.message.reply_text(
        "📞 Пожалуйста, оставьте ваши контактные данные (телефон или Telegram):",
        reply_markup=remove_keyboard()
    )
    return CONTACT_INFO

async def contact_info(update: Update, context: CallbackContext) -> int:
    """Обработка контактной информации и сохранение заказа"""
    if update.message.text == "❌ Отмена заказа":
        return await cancel(update, context)
        
    contact_data = update.message.text
    user_data = context.user_data
    user = update.message.from_user
    
    # Сохраняем заказ
    save_order(
        user_id=user.id,
        username=user.username or user.first_name,
        category=user_data.get('category', ''),
        details=user_data.get('details', ''),
        contact_info=contact_data
    )
    
    # Формируем текст уведомления
    order_text = f"""
📋 <b>НОВЫЙ ЗАКАЗ!</b>

👤 <b>Пользователь:</b> {user.first_name}"""
    
    if user.username:
        order_text += f" (@{user.username})"
    
    order_text += f"""
🆔 <b>ID:</b> {user.id}
📞 <b>Контакты:</b> {contact_data}
🏠 <b>Категория:</b> {user_data.get('category', '')}
📝 <b>Детали:</b> {user_data.get('details', '')}

⏰ <b>Время заказа:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

💬 <b>Ссылка для ответа:</b> <a href="tg://user?id={user.id}">Написать пользователю</a>
    """
    
    # Отправляем уведомление администратору
    await send_notification(context, order_text)
    
    # Возвращаем главное меню после завершения заказа
    success_text = "✅ Ваш заказ принят! Мы свяжемся с вами в ближайшее время.\n\nДля нового заказа нажмите /order"
    await update.message.reply_text(
        success_text,
        reply_markup=get_main_menu()
    )
    
    # Очищаем данные пользователя
    context.user_data.clear()
    
    return ConversationHandler.END

async def cancel(update: Update, context: CallbackContext) -> int:
    """Отмена заказа"""
    user = update.message.from_user
    
    # Возвращаем главное меню после отмены
    await update.message.reply_text(
        '❌ Заказ отменен. Для нового заказа нажмите /order',
        reply_markup=get_main_menu()
    )
    
    # Уведомление об отмене
    cancel_text = f"❌ Заказ отменен пользователем {user.first_name}"
    if user.username:
        cancel_text += f" (@{user.username})"
    cancel_text += f" ({user.id})"
    
    await send_notification(context, cancel_text)
    
    context.user_data.clear()
    return ConversationHandler.END