from dataclasses import dataclass

from infra.postgres.db import Database

@dataclass
class UserRepository:
    database: Database

    async def create_user_if_not_exists(self, user_id: int, is_waiter: bool = False) -> None:
        async with self.database.connection() as conn:
            await conn.execute("insert into users values ($1, $2) on conflict do nothing", user_id, is_waiter)