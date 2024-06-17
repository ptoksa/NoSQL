from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.blog_database

# Read users
users_collection = db.users
users = users_collection.find()
print("Users:")
for user in users:
    print(user)

# Read posts
posts_collection = db.posts
posts = posts_collection.find()
print("\nPosts:")
for post in posts:
    print(post)

# Read comments
comments_collection = db.comments
comments = comments_collection.find()
print("\nComments:")
for comment in comments:
    print(comment)
