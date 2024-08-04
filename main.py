import logging
import asyncio
from utils.commands import set_default_commands
from database.data import db
from create_bot import bot,dp,CHAT

from handlers.client import cl_route
from handlers.admin import ad_route

dp.include_routers(cl_route,ad_route)


async def main():
    logging.basicConfig(filename='logfile.log',
                        filemode='a',
                        format='%(asctime)s, %(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    logging.info("Бот вышел в онлайн!!!!")
    print('Бот вышел в онлайн !!!!!!!!!')
    await db.create_db()
    # await bot.send_message(chat_id=CHAT,
    #                        text='Бот вышел в онлайн!!!')
    await dp.start_polling(bot, skip_updates=True)
    await set_default_commands(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')