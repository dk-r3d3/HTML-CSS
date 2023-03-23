import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_data(self, user_id, user_name): # добавление в таблицу данных о юзере
        query = f"INSERT INTO datausers (user_id, user_name) VALUES ({user_id}, '{user_name}') " \
                f"ON CONFLICT (user_id) DO UPDATE SET user_name='{user_name}';"
        await self.connector.execute(query)

    async def add_databases(self): # создание таблицы, где буду храниться имена юзеров
        query = f"CREATE TABLE IF NOT EXISTS public.database(username text,PRIMARY KEY (username));"
        await self.connector.execute(query)

    async def add_username(self, username):
        query = f"INSERT INTO database (username) VALUES ('{username}');"
        await self.connector.execute(query)

    async def create_message(self, message):
        query = f"CREATE TABLE IF NOT EXISTS message (message_text text, PRIMARY KEY (message_text));"
        await self.connector.execute(query)
        query = f"INSERT INTO message (message_text) VALUES ('{message}');"
        await self.connector.execute(query)

    async def delete_username(self, username):
        query = f"DELETE FROM database  WHERE username='{username}';"
        await self.connector.execute(query)

    async def find_username(self, username):
        query = f"SELECT username FROM database WHERE username='{username}';"
        await self.connector.execute(query)


# ПОЛУЧЕНИЕ ПЕРВОЙ СТРОКИ ИЗ БД

async def get_usernames(): # особый метод для получения списка целей
    base = await asyncpg.connect(
        user='postgres',
        password='D97794422d69',
        database='spambot_database',
        host='127.0.0.1',
        port=5432,
        command_timeout=60
    )
    rows = await base.fetch("SELECT username FROM database;")
    await base.close()
    return rows # добавить исключения позже
