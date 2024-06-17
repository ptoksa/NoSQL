from rethinkdb import RethinkDB
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

r = RethinkDB()

# Connect to RethinkDB
try:
    conn = r.connect(host='localhost', port=28015).repl()
    print("Connected to RethinkDB")
except RqlDriverError:
    print("Could not connect to RethinkDB. Ensure RethinkDB is running.")

# Create a database
try:
    r.db_create('blog').run(conn)
    print("Database 'blog' created.")
except RqlRuntimeError:
    print("Database 'blog' already exists.")

# Create tables
try:
    r.db('blog').table_create('users').run(conn)
    print("Table 'users' created.")
except RqlRuntimeError:
    print("Table 'users' already exists.")

try:
    r.db('blog').table_create('posts').run(conn)
    print("Table 'posts' created.")
except RqlRuntimeError:
    print("Table 'posts' already exists.")

# Insert a user
user = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}
result = r.db('blog').table('users').insert(user).run(conn)
print(f"User inserted with ID: {result['generated_keys'][0]}")

# Insert a post
post = {
    "title": "Hello World",
    "content": "This is my first blog post!",
    "author_id": result['generated_keys'][0]
}
result = r.db('blog').table('posts').insert(post).run(conn)
print(f"Post inserted with ID: {result['generated_keys'][0]}")

# Fetch and print all users
users = r.db('blog').table('users').run(conn)
print("Users:")
for user in users:
    print(user)

# Fetch and print all posts
posts = r.db('blog').table('posts').run(conn)
print("Posts:")
for post in posts:
    print(post)
