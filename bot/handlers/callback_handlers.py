from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

import states as states
import database.requests as requests
import texts as t
from callback_factory import RespondCallback, BlockCallback

callback_router = Router()


@callback_router.callback_query(RespondCallback.filter())
async def handle_respond(
    callback: CallbackQuery, callback_data: RespondCallback, state: FSMContext
):
    """Обработка нажатия кнопки 'Ответить'."""
    receiver_tg_id = callback_data.user_id
    message_id = callback_data.message_id

    if await requests.check_if_user_blocked(
        owner_user_id=receiver_tg_id, blocked_user_id=callback.from_user.id
    ):
        await callback.message.answer(t.USER_BLOCKED_YOU)
        return

    await callback.message.answer(t.PROMPT_REPLY_MESSAGE)
    await state.set_state(states.Answer_message.receive_answer_message)
    await state.update_data(
        {"receive_answer_message": receiver_tg_id, "message_id": message_id}
    )


@callback_router.callback_query(BlockCallback.filter())
async def handle_block(
    callback: CallbackQuery, callback_data: BlockCallback, state: FSMContext
):
    """Обработка нажатия кнопки 'Заблокировать'."""
    receiver_tg_id = callback_data.user_id
    await requests.block_user(callback.from_user.id, receiver_tg_id)
    await callback.message.answer(t.USER_BLOCKED_OK)
