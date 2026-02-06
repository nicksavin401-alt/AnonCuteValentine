from aiogram import Router, Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import states as states
import texts as t

donate_router = Router()


@donate_router.message(Command("donate"))
async def cmd_donate(message: Message, state: FSMContext):
    """Обработка команды /donate и запрос суммы для доната."""
    await message.answer(t.DONATE_PROMPT_AMOUNT)
    await state.set_state(states.Donate.amount)


@donate_router.message(states.Donate.amount)
async def donate(message: Message, state: FSMContext):
    """Обработка ввода суммы для доната и отправка счёта."""
    if message.text and message.text.isdigit() and 0 < int(message.text) < 100001:
        prices = [LabeledPrice(label="XTR", amount=int(message.text))]
        await message.answer_invoice(
            title=t.INVOICE_TITLE,
            description=t.INVOICE_DESCRIPTION,
            prices=prices,
            provider_token="",
            payload=t.INVOICE_PAYLOAD,
            currency="XTR",
        )
        await state.clear()
        return

    await message.answer(t.DONATE_BAD_AMOUNT)


@donate_router.pre_checkout_query()
async def on_pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    """Обработка предварительной проверки оплаты."""
    await pre_checkout_query.answer(ok=True, error_message=t.PRECHECKOUT_ERROR)
    await bot.send_message(
        chat_id=pre_checkout_query.from_user.id, text=t.DONATE_THANKS
    )
