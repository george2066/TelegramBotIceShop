from telegram.ext import ContextTypes

async def sync_roles(context: ContextTypes.DEFAULT_TYPE) -> None:
    context.application.setup_roles() # type: ignore[attr-defined]
