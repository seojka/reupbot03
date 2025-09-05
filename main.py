import logging
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, filters
from handlers.conversation_states import *
from handlers.start import start
from handlers.commands import price, portfolio, about, contacts, handle_message
from handlers.order_handlers import order, category, house_lifting, crown_replacement, house_moving, frame_houses, contact_info, cancel
from utils.database import init_csv_file
from config import BOT_TOKEN

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    """Запуск бота"""
    # Инициализация бота
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Инициализация CSV файла
    init_csv_file()
    
    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("price", price))
    application.add_handler(CommandHandler("portfolio", portfolio))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("contacts", contacts))
    
    # Обработчик заказа (ConversationHandler)
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('order', order)],
        states={
            CATEGORY: [MessageHandler(filters.TEXT & ~filters.COMMAND, category)],
            HOUSE_LIFTING: [MessageHandler(filters.TEXT & ~filters.COMMAND, house_lifting)],
            CROWN_REPLACEMENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, crown_replacement)],
            HOUSE_MOVING: [MessageHandler(filters.TEXT & ~filters.COMMAND, house_moving)],
            FRAME_HOUSES: [MessageHandler(filters.TEXT & ~filters.COMMAND, frame_houses)],
            CONTACT_INFO: [MessageHandler(filters.TEXT & ~filters.COMMAND, contact_info)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    application.add_handler(conv_handler)
    
    # Обработчик обычных сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запуск бота
    print("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()