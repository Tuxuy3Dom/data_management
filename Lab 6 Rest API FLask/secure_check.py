# secure_check.py

# In the real world/solution this should be a database table!
from user import User

users = [User(1, 'Ihor', 'my_pass'),
         User(2, 'Dawid', 'your_pass')]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = userid_table.get(username, None)
    if user and password == user.password:
        return user
    
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

