from aiogram.filters.callback_data import CallbackData


class RespondCallback(CallbackData, prefix="respond"):
    """СallbackData для кнопки 'Ответить'."""

    user_id: int
    message_id: int


class BlockCallback(CallbackData, prefix="block"):
    """CallbackData для кнопки 'Заблокировать'."""

    user_id: int
