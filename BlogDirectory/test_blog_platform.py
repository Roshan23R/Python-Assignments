# test_blog_platform.py
import unittest
from blog_platform import users, posts, comments

class TestBlogPlatform(unittest.TestCase):
    def test_user_management(self):
        user1 = users.create_user("test_user", "test@example.com")
        self.assertEqual(len(users.users_list), 1)

        message = users.delete_user(user1.user_id)
        self.assertEqual(message, f"User with ID {user1.user_id} deleted successfully.")

    def test_blog_posts(self):
        post1 = posts.create_post("Test Post", "This is a test post.", None)
        self.assertEqual(len(posts.posts_list), 1)

        retrieved_post = posts.get_post(post1.post_id)
        self.assertEqual(retrieved_post, post1)

    def test_comments(self):
        post1 = posts.create_post("Test Post", "This is a test post.", None)
        comment1 = comments.add_comment(post1.post_id, None, "Test comment.")
        self.assertEqual(len(comments.comments_list), 1)

        post_comments = comments.get_comments(post1.post_id)
        self.assertEqual(post_comments, [comment1])

if __name__ == '__main__':
    unittest.main()
