from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Connect to the Cassandra cluster
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()

# Create a keyspace
session.execute("""
CREATE KEYSPACE IF NOT EXISTS blog 
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
""")

# Use the keyspace
session.set_keyspace('blog')

# Create users and posts tables
session.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id UUID PRIMARY KEY,
    username text,
    email text
)
""")

session.execute("""
CREATE TABLE IF NOT EXISTS posts (
    post_id UUID PRIMARY KEY,
    user_id UUID,
    title text,
    content text,
    created_at timestamp
)
""")

# Insert data
from uuid import uuid4
import datetime

user_id = uuid4()
session.execute("""
INSERT INTO users (user_id, username, email) 
VALUES (%s, %s, %s)
""", (user_id, 'john_doe', 'john@example.com'))

post_id = uuid4()
session.execute("""
INSERT INTO posts (post_id, user_id, title, content, created_at) 
VALUES (%s, %s, %s, %s, %s)
""", (post_id, user_id, 'My First Post', 'This is the content of my first post', datetime.datetime.now()))

# Query data
rows = session.execute("SELECT * FROM users")
for row in rows:
    print(row)

rows = session.execute("SELECT * FROM posts")
for row in rows:
    print(row)

# Close the session and cluster connection
session.shutdown()
cluster.shutdown()
