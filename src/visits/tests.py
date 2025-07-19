import psycopg
import os

url = os.getenv("DATABASE_URL")
print("Connecting to:", url)

conn = psycopg.connect(url)
print("Connected!")
conn.close()
