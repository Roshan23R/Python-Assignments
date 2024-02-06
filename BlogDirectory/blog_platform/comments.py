# blog_platform/comments.py

class Comment:
    def __init__(self, comment_id, post_id, author, content):
        self.comment_id = comment_id
        self.post_id = post_id
        self.author = author
        self.content = content

    def __str__(self):
        return f"Comment by {self.user.username}: {self.text}"

def add_comment(post_id, author, content):
    # Generate a unique comment ID (for simplicity, using a counter)
    comment_id = len(comments_list) + 1
    comment = Comment(comment_id, post_id, author, content)
    comments_list.append(comment)
    return comment

def get_comments(post_id):
    return [c for c in comments_list if c.post_id == post_id]

comments_list = []
