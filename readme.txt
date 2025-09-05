Установка и запуск:

    Создайте виртуальное окружение:

bash

python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

    Установите зависимости:

bash

pip install -r requirements.txt

    Создайте файл .env и настройте его:

bash

cp .env.example .env
# отредактируйте .env файл

    Запустите бота:

bash

python main.py
