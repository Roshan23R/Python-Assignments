# blog_platform/users.py

class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def __str__(self):
        return f"User: {self.username} ({self.email})"

def create_user(username, email):
    # Generate a unique user ID (for simplicity, using a counter)
    user_id = len(users_list) + 1
    user = User(user_id, username, email)
    users_list.append(user)
    return user

def delete_user(user_id):
    user = next((u for u in users_list if u.user_id == user_id), None)
    if user:
        users_list.remove(user)
        return f"User with ID {user_id} deleted successfully."
    else:
        return f"User with ID {user_id} not found."

users_list = []
