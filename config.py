# Конфигурационные параметры бота
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Данные бота
BOT_TOKEN = os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN')
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID', 'ВАШ_CHAT_ID')

# Данные компании
WEBSITE_URL = "https://ваш-сайт.ru"
TELEGRAM_CHANNEL = "https://t.me/ваш_канал"
PHONE_NUMBER = "+7 (XXX) XXX-XX-XX"
EMAIL = "your-email@example.com"
YOUR_TELEGRAM_USERNAME = "ваш_username"

# Настройки файлов
ORDERS_FILE = "data/orders.csv"

# Создаем папку data если ее нет
os.makedirs('data', exist_ok=True)