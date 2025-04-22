from mallard.database import Database


DATABASE_FILE = "data/database.db"

database = Database()
database.create_table("customers", ["id", "name", "phone", "email", "orders"])
database.create_table("orders", ["id", "items"])
