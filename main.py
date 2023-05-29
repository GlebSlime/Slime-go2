from PIL import Image, ImageFilter, ImageOps
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "6250509799:AAE5QkGrO420LYKSXkikd-JAfCs_fYttXEA"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Отправь фото и начну работать.")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer("Чем я могу помочь?")


@dp.message_handler(content_types=['photo'])
async def handle_docs_document(message: types.Message):
    src = "/photo"
    await message.photo[-1].download(destination_file='test.jpg')
    await message.answer("Фото добавлено! Напишите команду /filter чтобы начать работу с фото!")


@dp.message_handler(commands=['filter'])
async def send_filter(message: types.Message):
    await message.answer(f"Какой фильтр нанести? \n"
                         f"-Blur - напишите bl \n"
                         f"-Smooth - напишите sm \n"
                         f"-Sharpen - напишите sh \n"
                         f"-Contour - напишите ct \n"
                         f"-GrayScale - напишите gs \n"
                         f"-DETAIL - напишите dt \n"
                         f"-EDGE_ENHANCE_MORE - напишите ede \n"
                         f"-EMBOSS - напишите em \n"
                         f"-EDGE_ENHANCE - напишите ed \n")


@dp.message_handler(content_types=['text'])
async def filter_photo(message: types.Message):
    chat_id = message.chat.id
    image = Image.open("test.jpg")
    if message.text == "bl":
        filtered_photo = image.filter(ImageFilter.BLUR)
        filtered_photo.save('test2.jpg')
    if message.text == "sm":
        filtered_photo = image.filter(ImageFilter.SMOOTH)
        filtered_photo.save('test2.jpg')
    if message.text == "sh":
        filtered_photo = image.filter(ImageFilter.SHARPEN )
        filtered_photo.save('test2.jpg')
    if message.text == "ct":
        filtered_photo = image.filter(ImageFilter.CONTOUR)
        filtered_photo.save('test2.jpg')
    if message.text == "gs":
        filtered_photo = ImageOps.grayscale(image)
        filtered_photo.save('test2.jpg')
    if message.text == "dt":
        filtered_photo = image.filter(ImageFilter.DETAIL)
        filtered_photo.save('test2.jpg')
    if message.text == "ede":
        filtered_photo = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        filtered_photo.save('test2.jpg')
    if message.text == "em":
        filtered_photo = image.filter(ImageFilter.EMBOSS)
        filtered_photo.save('test2.jpg')
    if message.text == "ed":
        filtered_photo = image.filter(ImageFilter.EDGE_ENHANCE)
        filtered_photo.save('test2.jpg')

    await message.answer_photo(open("test2.jpg", "rb"))
    await message.answer("Вот обработанное фото! Спасибо что выбрали меня!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
