# Общие
SELF_MESSAGE_FORBIDDEN = "Ой 😅 <b>Себе валентинку</b> отправить нельзя."
INVALID_LINK_OR_USER = (
    "Упс 😔 <b>Получатель не найден</b> или ссылка <i>недействительна</i>."
)
USER_BLOCKED_YOU = (
    "Не получится 😕 <b>Получатель</b> добавил вас в <i>чёрный список</i>."
)
ADMIN_BLOCKED_YOU = "К сожалению 😔 <b>Администратор</b> ограничил вам доступ."

PROMPT_ANON_MESSAGE = (
    "💌 <b>Напиши валентинку</b>, которую хочешь отправить <i>анонимно</i>:"
)
PROMPT_REPLY_MESSAGE = "💞 <b>Напиши ответ</b> на валентинку:"
FEEDBACK_MESSAGE = "📝 <b>Оставь отзыв</b> о боте (только текстом):"

SENT_OK = "💘 <b>Готово!</b> Валентинка отправлена."
REPLY_SENT_OK = "💖 <b>Готово!</b> Ответ отправлен."

BLACKLIST_CLEANED = "🧹 <b>Чёрный список очищен!</b>"
BLACKLIST_EMPTY = "📭 <i>Чёрный список пуст.</i>"

USER_BLOCKED_OK = (
    "🚫 <b>Пользователь заблокирован.</b>\n🔓 Разблокировать: /clean_blacklist"
)

FEEDBACK_RECEIVED = "Спасибо за отзыв! ❤️ <i>Мы обязательно посмотрим.</i>"
FEEDBACK_MESSAGE_INVALID = "Пожалуйста, отправь отзыв <b>текстом</b> 📝"


# Ссылки (HTML)
def my_link_full(link: str) -> str:
    return (
        "💌 <b>Твоя ссылка для валентинок</b>\n"
        "━━━━━━━━━━━━━━\n\n"
        f"<code>{link}</code>\n\n"
        "📌 Скопируй её в профиль/сторис и получай <i>анонимные валентинки</i> 💖"
    )


def my_link_full_new(link: str) -> str:
    return (
        "Привет! 👋 <b>Добро пожаловать в валентинки</b> 💘\n\n"
        "💌 <b>Твоя ссылка для валентинок</b>\n"
        "━━━━━━━━━━━━━━\n\n"
        f"<code>{link}</code>\n\n"
        "📌 Скопируй её в профиль/сторис и получай <i>анонимные валентинки</i> 💖"
    )


def my_link_short(link: str) -> str:
    return f"💌 <b>Твоя ссылка:</b>\n<code>{link}</code>"


# Получатель: входящие сообщения
def incoming_text(text: str) -> str:
    return (
        "💝 <b>Тебе пришла валентинка</b>\n"
        "━━━━━━━━━━━━━━\n\n"
        f"{text}"
    )


def incoming_photo(caption: str = "") -> str:
    caption = (caption or "").strip()
    if caption:
        return (
            "📸 <b>Тебе прислали валентинку-картинку</b>\n"
            "━━━━━━━━━━━━━━\n\n"
            f"<i>{caption}</i>"
        )
    return "📸 <b>Тебе прислали валентинку-картинку</b>."


def incoming_video(caption: str = "") -> str:
    caption = (caption or "").strip()
    if caption:
        return (
            "🎬 <b>Тебе прислали видео-валентинку</b>\n"
            "━━━━━━━━━━━━━━\n\n"
            f"<i>{caption}</i>"
        )
    return "🎬 <b>Тебе прислали видео-валентинку</b>."


def incoming_animation(caption: str = "") -> str:
    caption = (caption or "").strip()
    if caption:
        return (
            "🪩 <b>Тебе прислали GIF-валентинку</b>\n"
            "━━━━━━━━━━━━━━\n\n"
            f"<i>{caption}</i>"
        )
    return "🪩 <b>Тебе прислали GIF-валентинку</b>."


def incoming_document(caption: str = "") -> str:
    caption = (caption or "").strip()
    if caption:
        return (
            "📎 <b>Тебе прислали файл-валентинку</b>\n"
            "━━━━━━━━━━━━━━\n\n"
            f"<i>{caption}</i>"
        )
    return "📎 <b>Тебе прислали файл-валентинку</b>."


def incoming_voice(caption: str = "") -> str:
    caption = (caption or "").strip()
    if caption:
        return (
            "🎤 <b>Тебе прислали голосовую валентинку</b>\n"
            "━━━━━━━━━━━━━━\n\n"
            f"<i>{caption}</i>"
        )
    return "🎤 <b>Тебе прислали голосовую валентинку</b>."


def incoming_video_note() -> str:
    return "📼 <b>Тебе прислали валентинку-кружочек</b>."


def incoming_sticker() -> str:
    return "🧩 <b>Тебе прислали валентинку-стикер</b>."


# Получатель: ответы
def reply_text(text: str) -> str:
    return (
        "💞 <b>Тебе ответили на валентинку</b>\n"
        "━━━━━━━━━━━━━━\n\n"
        f"{text}"
    )


def reply_photo(caption: str = "") -> str:
    caption = (caption or "").strip()
    if caption:
        return (
            "💞 <b>Тебе ответили картинкой</b>\n"
            "━━━━━━━━━━━━━━\n\n"
            f"<i>{caption}</i>"
        )
    return "💞 <b>Тебе ответили картинкой</b>."


def reply_video(caption: str = "") -> str:
    caption = (caption or "").strip()
    if caption:
        return (
            "💞 <b>Тебе ответили видео</b>\n"
            "━━━━━━━━━━━━━━\n\n"
            f"<i>{caption}</i>"
        )
    return "💞 <b>Тебе ответили видео</b>."


def reply_animation(caption: str = "") -> str:
    caption = (caption or "").strip()
    if caption:
        return (
            "💞 <b>Тебе ответили GIF</b>\n"
            "━━━━━━━━━━━━━━\n\n"
            f"<i>{caption}</i>"
        )
    return "💞 <b>Тебе ответили GIF</b>."


def reply_document(caption: str = "") -> str:
    caption = (caption or "").strip()
    if caption:
        return (
            "💞 <b>Тебе ответили файлом</b>\n"
            "━━━━━━━━━━━━━━\n\n"
            f"<i>{caption}</i>"
        )
    return "💞 <b>Тебе ответили файлом</b>."


def reply_voice(caption: str = "") -> str:
    caption = (caption or "").strip()
    if caption:
        return (
            "💞 <b>Тебе ответили голосовым</b>\n"
            "━━━━━━━━━━━━━━\n\n"
            f"<i>{caption}</i>"
        )
    return "💞 <b>Тебе ответили голосовым</b>."


def reply_video_note() -> str:
    return "💞 <b>Тебе ответили кружочком</b>."


def reply_sticker() -> str:
    return "💞 <b>Тебе ответили стикером</b>."


# Обратная связь (HTML) — не меняю логику, только лёгкая тематизация
def feedback_text(firstname: str, id: int, username: str, text: str) -> str:
    username_line = (
        f"@{username}"
        if username and username != "(no username)"
        else "<i>не указан</i>"
    )
    return (
        "📝 <b>Новый отзыв о боте-валентинке</b>\n"
        "━━━━━━━━━━━━━━\n"
        f'👤 Пользователь: <a href="tg://user?id={id}"><b>{firstname}</b></a>\n'
        f"🔗 Username: {username_line}\n"
        f"🆔 ID: <code>{id}</code>\n\n"
        "💬 <b>Текст:</b>\n"
        f"{text}"
    )


def feedback_text_select_action(firstname: str, id: int) -> str:
    return (
        "🛠️ <b>Управление пользователем</b>\n"
        "━━━━━━━━━━━━━━\n"
        f"🆔 ID: <code>{id}</code>\n"
        f"👤 Пользователь: <b>{firstname}</b>\n\n"
        "<i>Выберите действие 👇</i>"
    )


# Донат (HTML)
DONATE_PROMPT_AMOUNT = (
    "⭐️ <b>Сколько звёзд</b> хочешь отправить разработчику? <i>(введи число)</i> 🥺"
)
DONATE_BAD_AMOUNT = "⚠️ Введи, пожалуйста, <b>число</b> от 1 до <code>100000</code>."

INVOICE_TITLE = "Поддержать разработчика 💛"
INVOICE_DESCRIPTION = "Спасибо! Это помогает развивать проект 🚀"
INVOICE_PAYLOAD = "donate_support"

PRECHECKOUT_ERROR = "Упс 😔 <b>Ошибка оплаты</b>. Попробуй ещё раз."
DONATE_THANKS = "Спасибо за поддержку! ❤️⭐️ <i>Это очень помогает.</i>"


# Кнопки
BTN_BLOCK = "🚫 Заблокировать"
BTN_RESPOND = "💬 Ответить"

