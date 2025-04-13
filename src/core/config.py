from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    # Application
    app_host: str
    app_port: int
    environment: str

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
