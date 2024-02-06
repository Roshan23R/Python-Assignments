# blog_platform/posts.py

class Post:
    def __init__(self, post_id, title, content, author):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.author = author

    
    def __str__(self):
        return f"Post: {self.title} by {self.author.username}"

def create_post(title, content, author):
    # Generate a unique post ID (for simplicity, using a counter)
    post_id = len(posts_list) + 1
    post = Post(post_id, title, content, author)
    posts_list.append(post)
    return post

def get_post(post_id):
    return next((p for p in posts_list if p.post_id == post_id), None)

def list_posts():
    return posts_list

posts_list = []
