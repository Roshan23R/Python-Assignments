# blog_platform/categories.py

class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

    def __str__(self):
        return f"Category: {self.name}"

def create_category(name):
    # Generate a unique category ID (for simplicity, using a counter)
    category_id = len(categories_list) + 1
    category = Category(category_id, name)
    categories_list.append(category)
    return category

def get_categories():
    return categories_list

categories_list = []
