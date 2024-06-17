import rethinkdb as r

try:
    conn = r.connect('localhost', 28015)
    print("RethinkDB connection established.")
except Exception as e:
    print(f"Failed to connect to RethinkDB: {e}")
