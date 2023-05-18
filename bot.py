from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types.message import ContentType

from PIL import Image

from config import TOKEN
import keyboard as kb
from classs import WI

from os import listdir, remove


def Name(path = 'imgs/downloads/', name = 'img'):
    Name = name.split('.')[0] + '.png'
    j = 0
    while Name in listdir(path):
        Name = name.split('.')[0] + str(j) + '.png'
        j += 1
    return path + '/' + Name

def Last_Name(path = 'imgs/result', name = 'img'):
    out, num = listdir(path)[0], 0
    for file in listdir(path)[1:]:
        if file.startswith(name):
            if file.split('.')[0][-1] in '0123456789':
                if int(file.split('.')[0][-1]) >= num:
                    out = file
    return path + '/' + out

def clear(*paths):
    for path in paths:
        for file in listdir(path):
            remove(f'{path}/{file}')


bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Hello!\nsend me photo!', reply_markup=kb.kb_help)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply('Send me any photo\nand I\'ll send you telegram-sticker-format image!\n\n!note: Please don\'t allow group items to better experiance\nAlso don\'t send more than 10 files at once')

@dp.message_handler(content_types=['photo'])
async def photo_handler(msg: types.Document):
    file_id = ''
    count = 0
    for i in range(len(msg.photo)):
        file_id1 = msg.photo[-1]['file_unique_id'] + msg.photo[-1]['file_id']
        if file_id != file_id1:
            name = Name()
            await msg.photo[-1].download(name)
            WI(name).Save(True, path='imgs/result/', exst='png')
            await msg.reply_document(open(Last_Name(), 'rb'))
        file_id = file_id1
        count += 1

@dp.message_handler(commands=['clear', 'clear cache', 'cache', 'clear history', 'history'])
async def process_clear_command(message: types.Message):
    clear('imgs/downloads', 'imgs/result')
    await message.reply('Cache has been cleared')

@dp.message_handler(content_types=ContentType.ANY)
async def echo_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Use /help!', reply_markup=kb.kb_help)

executor.start_polling(dp)
