from aiogram import types, executor, Dispatcher, Bot
from bs4 import BeautifulSoup as b
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TOKEN')

bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(bot)


#start
@dp.message_handler(commands=['start'])
async def start(message: types.message):
    await bot.send_message(message.chat.id, """
    Привет я бот для поиска товаров на сайте <b><a href="https://www.trendyol.com/">Trendyol.</a></b>
Для поиска, введи название товара в сообщении.
<i>Для более точного и полноценного поиска нужно вводить полные названия продуктов, которые хотите найти.
Такие запросы как одиночные буквы, цифры не работают.</i>""",
    parse_mode="html", disable_web_page_preview=1)



#parser
@dp.message_handler(content_types=['text'])
async def parser(message: types.message):
    url = 'https://www.trendyol.com/sr?q=' + message.text
    r = requests.get(url)
    soup = b(r.text, "html.parser").find('div', class_='prdct-cntnr-wrppr')
    all_links = soup.find_all('a', href=True)
    for link in all_links:
        url = 'https://www.trendyol.com' + link['href']
        r = requests.get(url)
        soup = b(r.text, "html.parser")
        name = soup.find('h1', class_='pr-new-br')
        name = name.text
        price = soup.find('div', class_='product-price-container').find('span', class_='prc-dsc')
        price = price.text
        
        await bot.send_message(
            message.chat.id,
            '<b>' + name + '</b>\n<i>' + price + f"</i>\n<a href='{url}'>Ссылка на сайт</a>",
            parse_mode='html'
        )

        if all_links.index(link) == 9:
            break


executor.start_polling(dp)
