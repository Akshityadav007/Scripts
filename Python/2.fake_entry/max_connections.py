#  this program is used to get how many parallel connections are allowed on a database
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()
connStr = os.getenv("postgresql_URL")

conn = psycopg2.connect(connStr)
cur = conn.cursor()
print("[INFO] Connected successfully!")

# 🔍 Check max connections
cur.execute("SHOW max_connections;")
max_conn = cur.fetchone()[0]
print(f"[INFO] Max connections allowed: {max_conn}")
