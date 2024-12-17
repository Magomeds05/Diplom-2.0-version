import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types

import database
from keyboards import *
from key_catalog import *
from texts import text
from classtate import UserState, UserSale
from key_size import size_key
from config import *

import handlers.Admin
import handlers.Start
import handlers.product
import handlers.taskhandler

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
disp = Dispatcher(bot, storage=MemoryStorage())

@disp.message_handler(commands=['start'])
async def start(message):
    await message.answer(text.start, reply_markup=start_key)

@disp.message_handler(text='О нас')
async def price(message):
    with open('files/vhodnaya-gruppa-magazina-scaled.jpg', "rb") as img:
        await message.answer_photo(img, text.about, reply_markup=start_key)

@disp.message_handler(text='📋Таблица размеров')
async def size(message):
    with open('files/maxresdefault.jpg', "rb") as img:
        await message.answer_photo(img, "Размерная сетка", reply_markup=start_key)

disp.message_handler(text='🏷️Получить скидку!')(handlers.taskhandler.set_sale)
disp.message_handler(state=UserSale.name)(handlers.taskhandler.set_number)
disp.message_handler(state=UserSale.number)(handlers.taskhandler.set_email)
disp.message_handler(state=UserSale.email)(handlers.taskhandler.calories)
disp.message_handler(text='🖊️Рассчитать свой размер')(handlers.taskhandler.set_name)
disp.message_handler(state=UserState.age)(handlers.taskhandler.set_growth)
disp.message_handler(state=UserState.growth)(handlers.taskhandler.send_calories)


@disp.message_handler(text='💸Стоимость')
async def info(message):
    await message.answer("Что вас интересует?", reply_markup=catalog_key)

disp.callback_query_handler(text='Jordanlow')(handlers.product.buy_Jordan_low)
disp.callback_query_handler(text='Jordanhigh')(handlers.product.buy_Jordan_high)
disp.callback_query_handler(text='Travis')(handlers.product.buy_Jordan_Travis)
disp.callback_query_handler(text='Force')(handlers.product.buy_Jordan_Force)
disp.callback_query_handler(text='Dunk')(handlers.product.buy_Nike_Dunk)
disp.callback_query_handler(text='Max95')(handlers.product.buy_Max95)
disp.callback_query_handler(text='Max97')(handlers.product.buy_Max97)
disp.callback_query_handler(text='Yeezy350')(handlers.product.buy_Yeezy350)
disp.callback_query_handler(text='Yeezy700')(handlers.product.buy_Yeezy700)
disp.callback_query_handler(text='Raf')(handlers.product.buy_Raf)
disp.callback_query_handler(text='Off_White')(handlers.product.buy_Off_White)
disp.callback_query_handler(text='Off_White_Odsy')(handlers.product.buy_Off_White_Odsy)
disp.callback_query_handler(text='Balen')(handlers.product.buy_Balen)
disp.callback_query_handler(text='LouisSkate')(handlers.product.buy_LouisSkate)
disp.callback_query_handler(text='LouisTrain')(handlers.product.buy_LouisTrain)
disp.callback_query_handler(text='MM')(handlers.product.buy_MM)
disp.callback_query_handler(text='MMFut')(handlers.product.buy_MMFut)
disp.callback_query_handler(text='Lanvin')(handlers.product.buy_Lanvin)
disp.callback_query_handler(text='Rick')(handlers.product.buy_Rick)


@disp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(text.other, reply_markup=back_key)
    await call.answer()

@disp.callback_query_handler(text='back_to_catalog')
async def back(call):
    await call.message.answer("Что вас интересует?", reply_markup=catalog_key)
    await call.answer()

@disp.callback_query_handler(text='back_to_start')
async def back_start(call):
    await call.message.answer("Что вас интересует?", reply_markup=start_key)
    await call.answer()

@disp.callback_query_handler(text='choose_size')
async def choose_size(call):
    await call.message.answer("Все размеры в наличии:", reply_markup=size_key)
    await call.answer()

@disp.callback_query_handler(text='buy_size')
async def pay(call):
    await call.message.answer(f"👌Отличный выбор, можем перейти к оплате!:", reply_markup=buy_size)
    await call.answer()

####

disp.message_handler(lambda m: database.check_block(m.from_user.id))(handlers.Start.ban_message)
disp.callback_query_handler(lambda c: database.check_block(c.from_user.id))(handlers.Start.ban_callbackquery)


disp.message_handler(commands=['admin'])(handlers.Admin.start)
disp.callback_query_handler(text="statick")(handlers.Admin.statick)
disp.callback_query_handler(text="users")(handlers.Admin.users)
disp.callback_query_handler(text="mailing")(handlers.Admin.mailing)
disp.message_handler(state=handlers.Admin.Admins.mailing_step1)(handlers.Admin.mailing1)
disp.message_handler(content_types=types.ContentTypes.PHOTO, state=handlers.Admin.Admins.mailing_step2)(handlers.Admin.mailing2)
disp.callback_query_handler(text="block")(handlers.Admin.block)
disp.message_handler(state=handlers.Admin.Admins.ban)(handlers.Admin.ban1)
disp.callback_query_handler(text="back_to_admin")(handlers.Admin.back_admin)


@disp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(disp, skip_updates=True)