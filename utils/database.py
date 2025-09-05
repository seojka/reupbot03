import csv
import os
from datetime import datetime
from config import ORDERS_FILE

def init_csv_file():
    """Инициализация CSV файла с заголовками"""
    if not os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                'Дата', 'ID пользователя', 'Имя пользователя', 
                'Категория', 'Данные заказа', 'Контактная информация'
            ])

def save_order(user_id: int, username: str, category: str, details: str, contact_info: str):
    """Сохранение заказа в CSV файл"""
    try:
        with open(ORDERS_FILE, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                user_id,
                username,
                category,
                details,
                contact_info
            ])
        return True
    except Exception as e:
        print(f"Ошибка сохранения в CSV: {e}")
        return False