# MongoDB Install Using Docker Container
```sh
sudo docker pull mongo:4.4
```
```sh
sudo docker run -d -p 27017:27017 --name mongodb_4.4 mongo:4.4
```
#### Run the Python script
This script connects to MongoDB, creates a database and collections, inserts sample data, and performs basic CRUD operations
```sh
python3 blog_example.py
```
Let's query the data we've inserted
```sh
python3 read_data.py
```
To delete a post and its comments
```sh
python3 delete_data.py
```
### MongoDB Shell
```sh
sudo docker exec -it mongodb_4.4 mongo
```
# Running MongoDB Commands Directly in the Container
## Example MongoDB Shell Commands
List Databases

```sh
show dbs
```
Switch to a Database

```sh
use blog_database
```
List Collections

```sh
show collections
```
Find Documents

```sh
db.users.find().pretty()
```
# Using Redis
```sh
sudo docker pull redis:latest
```
```sh
sudo docker run -d -p 6379:6379 --name redis_db redis:latest
```
#### Install the redis-py library if not already installed
```sh
pip install redis
```
#### Run the Python Script
Ensure the Redis container is running and execute the script
```sh
python blog_example_redis.py
```
#### Verify Redis Data
To verify the data stored in Redis, you can use the Redis CLI tool inside the Docker container.
1. Access the Redis container
```sh
sudo docker exec -it redis redis-cli
```
2. Check stored data
```sh
KEYS *
HGETALL user:1
HGETALL post:1
LRANGE user:1:posts 0 -1
```
# Python script example for Cassandra
#### 1. Pull the latest Cassandra Docker image
```sh
sudo docker pull cassandra:latest
```
#### 2. Run the Cassandra container
```sh
sudo docker run -d --name cassandra -p 9042:9042 cassandra:latest
```
#### Run the Python Program
```sh
python blog_example_cassandra.py
```
#### Access the Cassandra Docker Container
```sh
sudo docker exec -it cassandra bash
```
#### Once inside the container, launch cqlsh
```sh
cqlsh
```
### Verify Data
#### 1. Select Keyspace:
```sh
USE blog;
```
#### 2. Verify Tables:
List all tables in the keyspace
```sh
DESCRIBE TABLES;
```
#### 3. Verify Data in Users Table
```sh
SELECT * FROM users;
```
#### 4. Verify Data in Posts Table
```sh
SELECT * FROM posts;
```
### Change Data
#### 1. Update Data
Update a user’s email
```sh
UPDATE users SET email = 'new_email@example.com' WHERE user_id = <user_id>;
```
Update a post’s content
```sh
UPDATE posts SET content = 'Updated content' WHERE post_id = <post_id>;
```
#### 2. Insert New Data:
Insert a new user
```sh
INSERT INTO users (user_id, username, email) VALUES (uuid(), 'new_user', 'new_user@example.com');
```
Insert a new post
```sh
INSERT INTO posts (post_id, user_id, title, content, created_at) VALUES (uuid(), <user_id>, 'New Post', 'This is a new post', toTimestamp(now()));
```
#### 3. Delete Data
Delete a user
```sh
DELETE FROM users WHERE user_id = <user_id>;
```
Delete a post
```sh
DELETE FROM posts WHERE post_id = <post_id>;
```
### Verify Changes
```sh
SELECT * FROM users;
SELECT * FROM posts;
```
# Using RethinkDB
```sh
sudo docker run -d -p 28015:28015 -p 29015:29015 -p 8080:8080 --name rethinkdb rethinkdb
```
#### Install the RethinkDB Python driver
```sh
pip3 install rethinkdb
```
#### Run the Python program
```sh
python3 blog_example_rethinkdb.py
```
### Verifying RethinkDB Setup
You can verify that RethinkDB is running correctly by accessing the RethinkDB web interface:
- Open your browser and go to `http://localhost:8080`.

This interface allows you to interact with your RethinkDB databases, tables, and documents.
### 1. Inserted Data:

- A user document was inserted into the users collection.
- A post document was inserted into the posts collection.
- A comment document was inserted into the comments collection.

### Read Data:

2. Successfully retrieved and printed the data from users, posts, and comments collections.
