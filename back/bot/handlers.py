"""Tg-bot handlers"""


from aiogram import Router, types
from aiogram.filters import CommandStart, Command
import aiohttp

from .config import TELEGRAM_BOT_TOKEN, API_TRANSCRIBE_URL


router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    """start start"""
    await message.answer("Hi! Send me a voice message and I'll transcribe it")


@router.message(lambda msg: msg.voice or msg.audio)
async def handle_voice(message: types.Message, bot):
    """handle voice"""
    file_id = message.voice.file_id if message.voice else message.audio.file_id

    # get file from tg-server
    file = await bot.get_file(file_id)
    file_url = f"https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{file.file_path}"

    # Download the file to a temporary buffer
    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as resp:
            if resp.status != 200:
                await message.answer("Failed to download voice message")
                return

            audio_bytes = await resp.read()

    # send audio to asr endpoint
    form = aiohttp.FormData()
    form.add_field("audio", audio_bytes, filename="voice.ogg",
                   content_type="audio/ogg")
    # form.add_field("task", "transcribe")
    # form.add_field("language", "ru")

    async with aiohttp.ClientSession() as session:
        async with session.post(API_TRANSCRIBE_URL, data=form) as resp:
            if resp.status != 200:
                await message.answer("Error in recognition")
                return

            result = await resp.json()

    await message.answer(f"{result.get('text', '')}")


@router.message(lambda msg: msg.video_note or msg.video)
async def handle_video(message: types.Message):
    """handle video"""
    await message.answer("Video is not supported")


@router.message(Command("help"))
async def cmd_battle_help(message:  types.Message):
    """handle /help"""
    await message.answer("Processing audio messages")
