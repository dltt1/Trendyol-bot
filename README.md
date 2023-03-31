# Проект чат-бота парсера продуктов Trendyol
Этот проект представляет собой чат-бот, который парсит информацию о продуктах с сайта Trendyol. Проект написан на Python и использует библиотеки для парсинга и работы с Telegram API.

# Стак:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
- Beautiful Soup

## Установка и запуск
Для установки проекта необходимо склонировать репозиторий и установить необходимые библиотеки:

```
git clone git@github.com:dltt1/Trendyol-bot.git
cd Trendyol-bot
pip install -r requirements.txt
```

## Далее необходимо настроить файл .env со следующими параметрами:

```
TELEGRAM_TOKEN=<ваш токен для Telegram API>
```

## Запустите проект:

```
cd bot
python bot.py
```

## Использование
После запуска проекта можно использовать чат-бота для парсинга продуктов с сайта Trendyol. Просто откройте чат с ботом в Telegram и отправьте ему команду /start, а затем напишите в чат бот название товара.

Чат-бот будет парсить информацию о продукте и отправлять ее в чат. Пользователи могут использовать эту информацию для сравнения цен на разных сайтах и принятия решения о покупке.
