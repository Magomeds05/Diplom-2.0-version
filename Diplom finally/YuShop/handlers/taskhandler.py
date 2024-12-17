from classtate import UserState, UserSale
from texts import text
from keyboards import start_key

async def set_sale(message):
    with open('files/400w-LcdG9JFW3I0.webp', "rb") as img:
        await message.answer_photo(img, text.sale)
        await UserSale.name.set()
async def set_number(message, state):
    await state.update_data(name=message.text)
    await message.answer('📝Введите свой номер телефона:')
    await UserSale.number.set()
async def set_email(message, state):
    await state.update_data(age=message.text)
    await message.answer('📝Введите свой email:')
    await UserSale.email.set()
async def calories(message, state):
    await state.update_data(email=message.text)
    data = await state.get_data()
    n = data['name']
    await message.answer(f"✅Поздравляем, {n}, регистрация прошла успешно, ваша скидка - 30%", reply_markup=start_key)
    await state.finish()

async def set_name(message):
    with open('files/razmer-1.jpg', "rb") as img:
        await message.answer_photo(img, 'Измерьте и введите длину стопы в сантиметрах:')
        await UserState.age.set()
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой возраст:')
    await UserState.growth.set()
async def send_calories(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    a = data['age']
    g = data['growth']
    if g >= str(18):
        await message.answer(f"Ваш размер: {(16 + int(a))} EU", reply_markup=start_key)
    else:
        await message.answer(f"Ваш размер: {(15.5 + int(a))} EU", reply_markup=start_key)
    await state.finish()
