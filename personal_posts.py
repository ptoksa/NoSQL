from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.blog_database

# Find all posts tagged with 'personal'
posts_collection = db.posts
personal_posts = posts_collection.find({'tags': 'personal'})

print("Personal posts:")
for post in personal_posts:
    print(post)
