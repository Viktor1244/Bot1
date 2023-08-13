from aiogram import *
from decouple import config
from random import randint

FILE1 = 'phrases.txt'
FILE2 = 'phrases1.txt'
FILE3 = 'phrases2.txt'
FILE4 = 'phrases3.txt'
bot = Bot(config('API_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Привет! Я бот,который может разговаривать с тобой.\nНапиши мне вопрос,и я тебе отвечу!\nМой команды:/help /start')

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply('Я могу ответить на пару твоих вопросов.\nЕще не забывей ели хочеш задать вопрос используй "?"\nВот на какие вопросы я могу ответить:привет,как дела?,какая погода?,какое у тебя настроение? ')

@dp.message_handler(content_types=['text'])
async def handle_messages(message:types.Message):
    user_text = message.text.lower()
    if 'привет' in user_text:
        try:
            with open(FILE1, "r", encoding="utf-8") as file:
                lines = file.readlines()
                second_line = lines[randint(0, len(lines) - 1)].strip()
                await message.answer(second_line)
        except:
            await message.answer(f"Произошла ошибка")
    elif 'как дела?' in user_text:
        await handle_kakdela(message)
    elif 'какая погода?' in user_text:
        await kakay_bogota(message)
    elif 'какая погода?' in user_text:
        await kakay_bogota(message)
    elif 'какое у тебя настроение?' in user_text:
        await nactroenue(message)
    else:
        await message.answer("Прости,я вас не понимаю.Попробуйте тругой вариант.")

async def handle_kakdela(message:types.Message):
    q = ['как дела?']
    a = randint(0,4)
    if str(message.text).lower() in q:
        with open(FILE2, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if len(lines) >= a:
                second_line = lines[a].strip()
                await message.answer(second_line)
    
async def kakay_bogota(message:types.Message):
    g = ['какая погода?']
    y = randint(0,4)
    if str(message.text).lower() in g:
       with open(FILE3,"r", encoding="utf-8") as file:
            lines = file.readlines()
            if len(lines) >= y:
                second_line = lines[y].strip()
                await message.answer(second_line)      
    
async def nactroenue(message:types.Message):
    h = ['какое у тебя настроение?']
    i = randint(0,4)
    if str(message.text).lower() in h:
        with open(FILE4,"r", encoding="utf-8") as file:
            lines = file.readlines()
            if len(lines) >= i:
                second_line = lines[i].strip()
                await message.answer(second_line)    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
