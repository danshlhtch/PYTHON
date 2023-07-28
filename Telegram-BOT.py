from aiogram import Bot, Dispatcher, executor, types

# bot init
bot = Bot(token="6317860976:AAECbQ7ZxU4Ow9JGRWjePYW-1sZwYoQymtY")
dp = Dispatcher(bot)

# echo
@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)


# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)