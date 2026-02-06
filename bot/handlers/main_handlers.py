from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.utils.deep_linking import create_start_link, decode_payload
from aiogram.filters import CommandStart, Command, CommandObject, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

from config_reader import config

import states as states
import keyboards as keyboards
import database.requests as requests
import texts as t

ADMIN_CHAT_ID = config.admin_chat_id


main_router = Router()


@main_router.message(CommandStart(deep_link=True), StateFilter("*"))
async def start_handler_with_link(
    message: Message, command: CommandObject, state: FSMContext
):
    """Обработка /start с параметром (глубокой ссылкой)."""
    await state.clear()

    try:
        payload = int(decode_payload(command.args))
    except (TypeError, ValueError):
        await message.answer(t.INVALID_LINK_OR_USER)
        return

    current_user_id = message.from_user.id

    if current_user_id == payload:
        await message.answer(t.SELF_MESSAGE_FORBIDDEN)
        return

    if not await requests.check_user_exists(payload):
        await message.answer(t.INVALID_LINK_OR_USER)
        return

    if await requests.check_if_user_blocked(
        owner_user_id=payload, blocked_user_id=current_user_id
    ):
        await message.answer(t.USER_BLOCKED_YOU)
        return

    await message.answer(t.PROMPT_ANON_MESSAGE)
    await state.set_state(states.Send_message.receive_message)
    await state.update_data(receive_message=payload)


@main_router.message(states.Send_message.receive_message)
async def send_anonymous_message(message: Message, state: FSMContext, bot: Bot):
    """Отправка анонимного сообщения пользователю."""
    data = await state.get_data()
    receiver_tg_id = data["receive_message"]

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    if message.text:
        await bot.send_message(
            chat_id=receiver_tg_id,
            text=t.incoming_text(message.text),
            reply_markup=answer_button,
        )
        await message.answer(t.SENT_OK)
        await state.clear()
        return

    if message.photo:
        caption = message.caption or ""
        photo = message.photo[-1]
        await bot.send_photo(
            chat_id=receiver_tg_id,
            photo=photo.file_id,
            caption=t.incoming_photo(caption),
            reply_markup=answer_button,
            has_spoiler=True,
        )
        await message.answer(t.SENT_OK)
        await state.clear()
        return

    if message.video:
        caption = message.caption or ""
        await bot.send_video(
            chat_id=receiver_tg_id,
            video=message.video.file_id,
            caption=t.incoming_video(caption),
            reply_markup=answer_button,
            has_spoiler=True,
        )
        await message.answer(t.SENT_OK)
        await state.clear()
        return

    if message.animation:
        caption = message.caption or ""
        await bot.send_animation(
            chat_id=receiver_tg_id,
            animation=message.animation.file_id,
            caption=t.incoming_animation(caption),
            reply_markup=answer_button,
            has_spoiler=True,
        )
        await message.answer(t.SENT_OK)
        await state.clear()
        return

    if message.document:
        caption = message.caption or ""
        await bot.send_document(
            chat_id=receiver_tg_id,
            document=message.document.file_id,
            caption=t.incoming_document(caption),
            reply_markup=answer_button,
        )
        await message.answer(t.SENT_OK)
        await state.clear()
        return

    if message.voice:
        caption = message.caption or ""
        await bot.send_voice(
            chat_id=receiver_tg_id,
            voice=message.voice.file_id,
            caption=t.incoming_voice(caption),
            reply_markup=answer_button,
        )
        await message.answer(t.SENT_OK)
        await state.clear()
        return

    if message.video_note:
        await bot.send_video_note(
            chat_id=receiver_tg_id,
            video_note=message.video_note.file_id,
            reply_markup=answer_button,
        )
        await bot.send_message(chat_id=receiver_tg_id, text=t.incoming_video_note())
        await message.answer(t.SENT_OK)
        await state.clear()
        return

    if message.sticker:
        await bot.send_sticker(
            chat_id=receiver_tg_id,
            sticker=message.sticker.file_id,
            reply_markup=answer_button,
        )
        await bot.send_message(chat_id=receiver_tg_id, text=t.incoming_sticker())
        await message.answer(t.SENT_OK)
        await state.clear()
        return

    caption = message.caption or ""
    await message.copy_to(
        chat_id=receiver_tg_id,
        caption=t.incoming_text(caption),
        reply_markup=answer_button,
    )
    await message.answer(t.SENT_OK)
    await state.clear()


@main_router.message(states.Answer_message.receive_answer_message)
async def send_reply_message(message: Message, state: FSMContext, bot: Bot):
    """Отправка ответа на анонимное сообщение."""
    data = await state.get_data()
    receiver_tg_id = data["receive_answer_message"]
    reply_to_message_id = int(data["message_id"])

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    if message.text:
        await bot.send_message(
            chat_id=receiver_tg_id,
            text=t.reply_text(message.text),
            reply_to_message_id=reply_to_message_id,
            reply_markup=answer_button,
        )
        await message.answer(t.REPLY_SENT_OK)
        await state.clear()
        return

    if message.photo:
        caption = message.caption or ""
        photo = message.photo[-1]
        await bot.send_photo(
            chat_id=receiver_tg_id,
            photo=photo.file_id,
            caption=t.reply_photo(caption),
            reply_to_message_id=reply_to_message_id,
            reply_markup=answer_button,
            has_spoiler=True,
        )
        await message.answer(t.REPLY_SENT_OK)
        await state.clear()
        return

    if message.video:
        caption = message.caption or ""
        await bot.send_video(
            chat_id=receiver_tg_id,
            video=message.video.file_id,
            caption=t.reply_video(caption),
            reply_to_message_id=reply_to_message_id,
            reply_markup=answer_button,
            has_spoiler=True,
        )
        await message.answer(t.REPLY_SENT_OK)
        await state.clear()
        return

    if message.animation:
        caption = message.caption or ""
        await bot.send_animation(
            chat_id=receiver_tg_id,
            animation=message.animation.file_id,
            caption=t.reply_animation(caption),
            reply_to_message_id=reply_to_message_id,
            reply_markup=answer_button,
            has_spoiler=True,
        )
        await message.answer(t.REPLY_SENT_OK)
        await state.clear()
        return

    if message.document:
        caption = message.caption or ""
        await bot.send_document(
            chat_id=receiver_tg_id,
            document=message.document.file_id,
            caption=t.reply_document(caption),
            reply_to_message_id=reply_to_message_id,
            reply_markup=answer_button,
        )
        await message.answer(t.REPLY_SENT_OK)
        await state.clear()
        return

    if message.voice:
        caption = message.caption or ""
        await bot.send_voice(
            chat_id=receiver_tg_id,
            voice=message.voice.file_id,
            caption=t.reply_voice(caption),
            reply_to_message_id=reply_to_message_id,
            reply_markup=answer_button,
        )
        await message.answer(t.REPLY_SENT_OK)
        await state.clear()
        return

    if message.video_note:
        await bot.send_video_note(
            chat_id=receiver_tg_id,
            video_note=message.video_note.file_id,
            reply_to_message_id=reply_to_message_id,
            reply_markup=answer_button,
        )
        await bot.send_message(chat_id=receiver_tg_id, text=t.reply_video_note())
        await message.answer(t.REPLY_SENT_OK)
        await state.clear()
        return

    if message.sticker:
        await bot.send_sticker(
            chat_id=receiver_tg_id,
            sticker=message.sticker.file_id,
            reply_to_message_id=reply_to_message_id,
            reply_markup=answer_button,
        )
        await bot.send_message(
            chat_id=receiver_tg_id,
            text=t.reply_sticker(),
        )
        await message.answer(t.REPLY_SENT_OK)
        await state.clear()
        return

    caption = message.caption or ""
    await message.copy_to(
        chat_id=receiver_tg_id,
        caption=t.reply_text(caption),
        reply_markup=answer_button,
        reply_to_message_id=reply_to_message_id,
    )
    await message.answer(t.REPLY_SENT_OK)
    await state.clear()


@main_router.message(Command("clean_blacklist"))
async def clean_blacklist(message: Message, state: FSMContext):
    """Очистка черного списка пользователя."""
    if await requests.clean_blacklist(message.from_user.id):
        await message.answer(t.BLACKLIST_CLEANED)
    else:
        await message.answer(t.BLACKLIST_EMPTY)


@main_router.message(Command("feedback"))
async def feedback_handler(message: Message, state: FSMContext):
    """Начало процесса отправки отзыва."""
    if await requests.check_if_user_blocked(
        owner_user_id=8582132507, blocked_user_id=message.from_user.id
    ):
        await message.answer(t.ADMIN_BLOCKED_YOU)
        return

    await state.set_state(states.Feedback_message.receive_feedback_message)
    await message.answer(t.FEEDBACK_MESSAGE)
    await state.update_data(receive_message=message.from_user.id)


@main_router.message(states.Feedback_message.receive_feedback_message)
async def receive_feedback(message: Message, state: FSMContext, bot: Bot):
    """Получение и отправка отзыва администратору."""
    if not message.text:
        await message.answer(t.FEEDBACK_MESSAGE_INVALID)
        return

    user = message.from_user

    answer_button = await keyboards.create_answer_button(
        message.from_user.id, message.message_id
    )

    try:
        chat_info = await bot.get_chat(user.id)

        if not chat_info.has_private_forwards:
            await message.forward(chat_id=8582132507)
            await bot.send_message(
                chat_id=8582132507,
                text=t.feedback_text_select_action(
                    firstname=user.first_name, id=user.id
                ),
                reply_markup=answer_button,
            )
        else:
            await bot.send_message(
                chat_id=8582132507,
                text=t.feedback_text(
                    firstname=user.first_name,
                    id=user.id,
                    username=user.username,
                    text=message.text,
                ),
                reply_markup=answer_button,
            )

    except TelegramBadRequest:
        await message.copy_to(chat_id=8582132507)

    await message.answer(t.FEEDBACK_RECEIVED)
    await state.clear()


@main_router.message(CommandStart(deep_link=False))
@main_router.message()
async def start_handler(message: Message, bot: Bot, state: FSMContext):
    """Обработка обычного /start или любого другого сообщения."""

    await state.clear()
    user_id = message.from_user.id

    link = await create_start_link(bot, f"{user_id}", encode=True)

    if await requests.check_user_exists(user_id):
        await message.answer(t.my_link_full(link))
    else:
        await requests.create_user_profile(user_id)
        await message.answer(t.my_link_full_new(link))
