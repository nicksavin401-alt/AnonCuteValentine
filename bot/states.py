from aiogram.fsm.state import State, StatesGroup


class Send_message(StatesGroup):
    """Состояние для отправки анонимного сообщения."""

    receive_message = State()


class Answer_message(StatesGroup):
    """Состояние для ответа на анонимное сообщение."""

    receive_answer_message = State()


class Feedback_message(StatesGroup):
    """Состояния для отправки отзыва о боте."""

    receive_feedback_message = State()
    receive_answer_message = State()


class Donate(StatesGroup):
    """Состояние для процесса доната."""

    amount = State()
