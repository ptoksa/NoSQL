from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.blog_database

# Delete a specific post
posts_collection = db.posts
posts_collection.delete_one({'title': 'My First Blog Post'})

print("Post deleted.")
