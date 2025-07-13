import asyncio
import aiosqlite

dbpath = "E:/ALX ProDev Back-End/alx-backend-python/python-decorators-0x01/users.db"

async def async_fetch_users():
    print("Fetching all users...")
    async with aiosqlite.connect(dbpath) as db:
        cursor = await db.execute("SELECT * FROM users")
        users = await cursor.fetchall()
        await cursor.close()
        return users

async def async_fetch_older_users():
    print("Fetching users older than 40...")
    async with aiosqlite.connect(dbpath) as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        old_users = await cursor.fetchall()
        await cursor.close()
        return old_users

async def fetch_concurrently():
    users, old_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print("All Users:")
    for users in users:
        print(users)
    print("All users older than 40:")
    for old_users in old_users:
        print(old_users)

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
