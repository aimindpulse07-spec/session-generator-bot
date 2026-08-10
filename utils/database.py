import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "bot.db"


def init_database() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        connection.commit()


def add_or_update_user(
    user_id: int,
    username: str | None,
    first_name: str | None,
) -> None:
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute(
            """
            INSERT INTO users (
                user_id,
                username,
                first_name
            )
            VALUES (?, ?, ?)
            ON CONFLICT(user_id)
            DO UPDATE SET
                username = excluded.username,
                first_name = excluded.first_name
            """,
            (
                user_id,
                username,
                first_name,
            ),
        )

        connection.commit()


def get_user_count() -> int:
    with sqlite3.connect(DATABASE_PATH) as connection:
        result = connection.execute(
            "SELECT COUNT(*) FROM users"
        ).fetchone()

    return int(result[0]) if result else 0
