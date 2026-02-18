from time import time

from ..helper.ext_utils.bot_utils import new_task
from ..helper.telegram_helper.button_build import ButtonMaker
from ..helper.telegram_helper.message_utils import send_message, edit_message, send_file
from ..helper.telegram_helper.filters import CustomFilters
from ..helper.telegram_helper.bot_commands import BotCommands


@new_task
async def start(_, message):
    buttons = ButtonMaker()
    buttons.url_button(
        "Наш канал ->", "https://t.me/+q2PQ1K33xm0xOTE0"
    )
    buttons.url_button("Помощь —", "https://t.me/ksi_fbot")
    reply_markup = buttons.build_menu(2)
    if await CustomFilters.authorized(_, message):
        start_string = f"""
Спасибо за подписку! ❤️\n Бот готов к работе.\nДанный бот умеет скачивать торренты/прямые линки, умеет скачивать с YouTube/VK/OK и многих-многих других ресурсов.\nПропишите /help чтобы получить список всех доступных команд. 
Type /{BotCommands.HelpCommand} to get a list of available commands
"""
        await send_message(message, start_string, reply_markup)
    else:
        await send_message(
            message,
            "Данный бот умеет скачивать торренты/прямые линки, умеет скачивать с YouTube/VK/OK и многих-многих других ресурсов.\n\n⚠️ ⚠️ Если хотите получить доступ к боту — оформите, пожалуйста, подписку.\n Подписка: https://t.me/tribute/app?startapp=sMms",
            reply_markup,
        )
    buttons = ButtonMaker()
    buttons.url_button(
        "Подписка ->", "https://t.me/tribute/app?startapp=sMms"
    )
    buttons.url_button("Помощь —", "https://t.me/ksi_fbot")
    reply_markup = buttons.build_menu(2)


@new_task
async def ping(_, message):
    start_time = int(round(time() * 1000))
    reply = await send_message(message, "Starting Ping")
    end_time = int(round(time() * 1000))
    await edit_message(reply, f"{end_time - start_time} ms")


@new_task
async def log(_, message):
    await send_file(message, "log.txt")
