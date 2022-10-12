from mongoengine import *

from datetime import datetime
import os
import json

connect(db = "mongo-dev-db")

# Defining Documents

class User(Document):
    username = StringField(unique = True, required = True)
    email = EmailField(unique = True)
    password = BinaryField(unique = True) 
    age = IntField()
    bio = StringField(max_length = 100)
    categories = ListField()
    admin = BooleanField(default = False)
    registered = BooleanField(default = False)
    date_created = DateTimeField(default = datetime.utcnow)

    def json(self):
        user_dict = {

            "username": self.username,
            "email": self.email,
            "age": self.age,
            "bio": self.bio,
            "categories": self.categories,
            "admin": self.admin,
            "registered": self.registered,
        }
        return json.dumps(user_dict)

    meta = {
        "indexes": ["username","email"],
        "ordering": ["-date_created"]
    }

# Dynamic Documents

class BlogPost(DynamicDocument):
    title = StringField()
    content = StringField()
    author = ReferenceField(User)
    date_created = DateTimeField(default = datetime.utcnow)

    meta = {
        "indexes": ["title"],
        "ordering": ["-date_created"]
    }

# Save a document

# user = User(
#     username = "Tsaar",
#     email = "hehe@gmail.com",
#     password = os.urandom(16),
#     age = 32,
#     bio = "Hello World!",
#     admin = True
# ).save()

# BlogPost(
#     title = "My first blog post!",
#     content = "MongoDB and Python!!!!",
#     author = user,
#     tags = ["Python", "MongoDB", "MongoEngine"],
#     category = "MongoDB"
# ).save()

user = User(
    username = "Hehe",
    email = "hihi@gmail.com",
    password = os.urandom(16),
    age = 32,
    bio = "Hello hehe!",
)

user.admin = True
user.registered = True

# try:
#     user.save()
# except NotUniqueError:
#     print("Username or email is not unique")

# users = User.objects()

# for user in users:
#     print(user.username, user.email, user.bio)

# Filtering

# admin_users = User.objects(admin=True)

# for a in admin_users:
#     print(a.username)

# try:
#     hehe = User.objects(username="Haha").get()
# except DoesNotExist:
#     print("User not found")


# hehe = User.objects(username="Tsaar").get()

# posts = BlogPost.objects(author = hehe)

# for post in posts:
#     print(post.author.username)

# Query operators

# Less than and greater than

# young_users = User.objects(age__lt=30)

# for user in young_users:
#     print(user.username, user.age)

# old_users = User.objects(age__gte=30)

# for user in old_users:
#     print(user.username, user.age)

# Query a list

# posts_tagged_python = BlogPost.objects(tags="MongoDB")

# for post in posts_tagged_python:
#     print(post.content)

# String queries

# python_posts = BlogPost.objects(title__icontains="First")

# for post in python_posts:
#     print(post.title)

# Limiting and skipping results

# Get the first

# first = BlogPost.objects().first()

# print(first.title)

# Get the first 2 documents

# first_2 = BlogPost.objects()[:2]

# for post in first_2:
#     print(post.title)

# Get all but the first 2

# all_but = BlogPost.objects()[2:]

# for post in all_but:
#     print(post.title)

# sliced = BlogPost.objects()[2:4]

# for post in sliced:
#     print(post.title)

# Counting

# user_count = User.objects().count()

# print(user_count)

# Aggregation

# average = BlogPost.objects.average("rating")
# print(average)

# total_rating = BlogPost.objects.sum("rating")
# print(total_rating)

tsaar = User.objects(username = "Tsaar").get()

print(tsaar.json())