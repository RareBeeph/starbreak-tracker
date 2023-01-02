from peewee import SqliteDatabase

# TODO: pull path from environment
conn = SqliteDatabase("/code/data.db")
