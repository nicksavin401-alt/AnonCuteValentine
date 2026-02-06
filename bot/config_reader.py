from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    """Чтение конфигурационных настроек из .env файла."""

    bot_token: SecretStr
    redis_ip: SecretStr
    admin_chat_id: int

    model_config = SettingsConfigDict(env_file="bot/.env", env_file_encoding="utf-8")


config = Settings()
