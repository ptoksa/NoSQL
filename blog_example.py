from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client.blog_database

users_collection = db.users
posts_collection = db.posts
comments_collection = db.comments

# Clear collections to avoid duplicate entries
users_collection.delete_many({})
posts_collection.delete_many({})
comments_collection.delete_many({})

# Insert a user
user = {
    'username': 'johndoe',
    'email': 'john.doe@newdomain.com',
    'password': 'hashedpassword',
    'created_at': datetime.now()
}
user_id = users_collection.insert_one(user).inserted_id

# Insert a post
post = {
    'title': 'My First Blog Post',
    'content': 'This is the content of my first blog post.',
    'author_id': user_id,
    'tags': ['introduction', 'personal'],
    'created_at': datetime.now()
}
post_id = posts_collection.insert_one(post).inserted_id

# Insert a comment
comment = {
    'post_id': post_id,
    'author_id': user_id,
    'content': 'This is a comment on the first blog post.',
    'created_at': datetime.now()
}
comment_id = comments_collection.insert_one(comment).inserted_id

print("Data insertion complete.")
