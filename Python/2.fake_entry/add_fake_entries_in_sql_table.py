import psycopg2
import random
from faker import Faker
from dotenv import load_dotenv
import os
import time
from tqdm import tqdm  # ✅ progress bar

load_dotenv()  # Load environment variables

# Fetch DB credentials
connStr = os.getenv("postgresql_URL")

fake = Faker()

print("[INFO] Connecting to the database...")
conn = psycopg2.connect(connStr)
cur = conn.cursor()
print("[INFO] Connected successfully!")

# 👤 Insert 10,000 users
print("[INFO] Inserting 10,000 users...")

start_time = time.time()
user_ids = []
unique_emails = set()

# progress bar with name "Users"
for _ in tqdm(range(10000), desc="Users"):
    while True:
        email = fake.email()
        if email not in unique_emails:
            unique_emails.add(email)
            break
    password = fake.password()
    cur.execute("INSERT INTO users (email, password) VALUES (%s, %s) RETURNING id", (email, password))
    user_id = cur.fetchone()[0]
    user_ids.append(user_id)
conn.commit()
print(f"[SUCCESS] Users inserted in {time.time() - start_time:.2f} seconds.")

# ✅ Insert 1 million todos
print("[INFO] Inserting 1,000,000 todos...")
batch_size = 1000
todos = []
start_time = time.time()

# progress bar with name "Todos"
for i in tqdm(range(1_000_000), desc="Todos"):
    user_id = random.choice(user_ids)
    title = fake.sentence(nb_words=6)
    desc = fake.text()
    done = random.choice([True, False])
    todos.append((title, desc, user_id, done))

    if len(todos) >= batch_size:
        args_str = ','.join(cur.mogrify("(%s,%s,%s,%s)", x).decode('utf-8') for x in todos)
        cur.execute("INSERT INTO todos (title, description, user_id, done) VALUES " + args_str)
        conn.commit()
        todos = []

# Insert remaining todos
if todos:
    args_str = ','.join(cur.mogrify("(%s,%s,%s,%s)", x).decode('utf-8') for x in todos)
    cur.execute("INSERT INTO todos (title, description, user_id, done) VALUES " + args_str)
    conn.commit()
    print(f"[INFO] Inserted final {len(todos)} todos.")

print(f"[SUCCESS] Todos inserted in {time.time() - start_time:.2f} seconds.")


# Clean up
cur.close()
conn.close()
print("[INFO] Database connection closed.")