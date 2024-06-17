import redis

# Connect to Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Function to add a user
def add_user(user_id, name, email):
    r.hset(f"user:{user_id}", mapping={"name": name, "email": email})

# Function to add a blog post
def add_post(post_id, title, content, user_id):
    r.hset(f"post:{post_id}", mapping={"title": title, "content": content, "user_id": user_id})
    r.rpush(f"user:{user_id}:posts", post_id)

# Function to get a user
def get_user(user_id):
    return r.hgetall(f"user:{user_id}")

# Function to get a blog post
def get_post(post_id):
    return r.hgetall(f"post:{post_id}")

# Function to get all posts for a user
def get_user_posts(user_id):
    post_ids = r.lrange(f"user:{user_id}:posts", 0, -1)
    posts = [r.hgetall(f"post:{post_id.decode('utf-8')}") for post_id in post_ids]
    return posts

# Example usage
add_user("1", "John Doe", "john.doe@example.com")
add_post("1", "My First Post", "This is the content of my very first post", "1")

print(get_user("1"))
print(get_post("1"))
print(get_user_posts("1"))
