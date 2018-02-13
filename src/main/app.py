from src.models.blog import Blog
from src.main.database import Database
__author__= "Mayur"


Database.initialize()

blog = Blog(author='Mayur Kumar',
            title='First Blog Title',
            description='This can also be left as empty.')

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(from_database.json())