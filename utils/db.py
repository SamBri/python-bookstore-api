from databases import Database

from utils.const import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME


async def connect_db():
    db = Database(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
    await db.connect()
    return db

async def disconnect_db(db):
    await db.disconnet()

