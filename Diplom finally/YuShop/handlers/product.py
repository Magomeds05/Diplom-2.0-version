from keyboards import *
from texts import textproduct


async def buy_Jordan_low(call):
    with open('files/3product.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Jordanlow, reply_markup=buy_key)
    await call.answer()
async def buy_Jordan_high(call):
    with open('files/Air-Jordan-1-Mid-Chicago-Black-Toe-554724-069-Release-Date-Price-2-1.jpg.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Jordanhigh, reply_markup=buy_key)
    await call.answer()

async def buy_Jordan_Travis(call):
    with open('files/1_5f.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Travis, reply_markup=buy_key)
    await call.answer()

async def buy_Jordan_Force(call):
    with open('files/9xwx48wdn6dg4x67y4cap1ne5l08adzi.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Force, reply_markup=buy_key)
    await call.answer()

async def buy_Nike_Dunk(call):
    with open('files/AURORA_FQ.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Dunk, reply_markup=buy_key)
    await call.answer()

async def buy_Max95(call):
    with open('files/jd_720074_a.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Max95, reply_markup=buy_key)
    await call.answer()

async def buy_Max97(call):
    with open('files/2vzj47l4yxsewshjflkxg8p0yvf4wtng.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Max97, reply_markup=buy_key)
    await call.answer()

async def buy_Yeezy350(call):
    with open('files/IMG_20200627_021400.jpg.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Yeezy350, reply_markup=buy_key)
    await call.answer()

async def buy_Yeezy700(call):
    with open('files/main-square_db919406-f9a5-41e3-97bd-088b16d10731.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Yeezy700, reply_markup=buy_key)
    await call.answer()

async def buy_Raf(call):
    with open('files/d440e516e889471cba66074dda282874.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Raf, reply_markup=buy_key)
    await call.answer()

async def buy_Off_White(call):
    with open('files/off-white-out-of-office-white-grey-trainers-side.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Off_White, reply_markup=buy_key)
    await call.answer()

async def buy_Off_White_Odsy(call):
    with open('files/e6kwxxs85oy4aw499qfyr0q0vzm6p4m5.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Off_White_Odsy, reply_markup=buy_key)
    await call.answer()

async def buy_Balen(call):
    with open('files/826217_01.jpg.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Balen, reply_markup=buy_key)
    await call.answer()

async def buy_LouisSkate(call):
    with open('files/imglouis.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.LouisSkate, reply_markup=buy_key)
    await call.answer()

async def buy_LouisTrain(call):
    with open('files/louis-vuitton-lv-skate-monogram-trainer-green-sneaker-nvprod4640020v-side.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.LouisTrain, reply_markup=buy_key)
    await call.answer()

async def buy_MM(call):
    with open('files/MM6MaisonMargiela.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.MM, reply_markup=buy_key)
    await call.answer()

async def buy_MMFut(call):
    with open('files/s-l1200.jpg', "rb") as img:
        await call.message.answer_photo(img, textproduct.MMFut, reply_markup=buy_key)
    await call.answer()

async def buy_Lanvin(call):
    with open('files/nm_4837489_100296_m.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Lanvin, reply_markup=buy_key)
    await call.answer()

async def buy_Rick(call):
    with open('files/Untitled-33_22dba556-beaa-4fd2-8fe5-5d829b73a1a2.webp', "rb") as img:
        await call.message.answer_photo(img, textproduct.Rick, reply_markup=buy_key)
    await call.answer()
