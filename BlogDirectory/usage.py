# example_usage.py
from blog_platform import users, posts, comments

# example_usage.py (extended)
from blog_platform import categories

# Creating categories
category1 = categories.create_category("Technology")
category2 = categories.create_category("Travel")

# Creating users
user1 = users.create_user("john_doe", "john@example.com")
user2 = users.create_user("jane_doe", "jane@example.com")

# Creating posts
post1 = posts.create_post("First Post", "This is the content of the first post.", user1)
post2 = posts.create_post("Second Post", "This is the content of the second post.", user2)

# Adding comments
comment1 = comments.add_comment(post1.post_id, user2, "Great post!")
comment2 = comments.add_comment(post1.post_id, user1, "I agree!")

user_list = list(users.users_list)
print("Users:", user_list)
post_list = list(posts.posts_list)
print("Posts:", post_list)
post1_comments = comments.get_comments(post1.post_id)
print("Comments for Post 1:", post1_comments)
categories_list = categories.get_categories()
print("Categories:", categories_list)
