import logging

from telegram.ext import Application as PTBApplication, ApplicationBuilder

from app.handlers import HANDLERS
from app.core.users.repositories import UserRepository
from app.core.users.services import UserService
from app.infra.postgres.db import Database
from app.infra.postgres.base import Base
from settings.config import AppSettings

class Application(PTBApplication):
    def __init__(self, app_settings: AppSettings, **kwargs):
        super().__init__(**kwargs)
        self._settings = app_settings
        self._register_handlers()
        self.database = Database(app_settings.POSTGRES_DSN, declarative_base=Base)
        user_repository = UserRepository(database=self.database)
        self.user_service = UserService(repository=user_repository)


    def run(self) -> None:
        self.run_polling()


    def _register_handlers(self):
        for handler in HANDLERS:
            self.add_handler(handler)

    @staticmethod
    async def initialize_dependencies(application: "Application") -> None:
        await application.database.create_tables()

    @staticmethod
    async def shutdown_dependencies(application: "Application") -> None:
        await application.database.shutdown()




def configure_logging():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)

def create_app(app_settings: AppSettings) -> Application:
    application = (ApplicationBuilder()
                   .application_class(Application,kwargs={"app_settings": app_settings})
                   .post_init(Application.initialize_dependencies) # type: ignore[arg-type]
                   .post_shutdown(Application.shutdown_dependencies) # type: ignore[arg-type]
                   .token(app_settings.TELEGRAM_API_KEY.get_secret_value())
                   .build())
    return application # type: ignore[return-value]


if __name__ == "__main__":
    configure_logging()
    settings = AppSettings()
    app = create_app(settings)
    app.run()
