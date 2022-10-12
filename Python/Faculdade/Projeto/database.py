import datetime
from pymongo import MongoClient

cluster = "mongodb+srv://esdras:emcg88222764@cluster0.b5qbl.mongodb.net/project?retryWrites=true&w=majority"
client = MongoClient(cluster)

db = client.project

entries = db.entries

# Registration

def CreateEntry(user):
    
    entry = {
        "username": user.username,
        "password": user.password,
        "name": user.name,
        "age": user.age,
        "email": user.email,
        "phone": user.phone,
        "address": user.address,
        "date": datetime.datetime.utcnow()
    }
    
    result = entries.insert_one(entry)

def SearchEntry(username, password):

    result = entries.find_one({"username": username})
    
    if (result != None):
        for username in result:
            for password in result:
                return True
            else: return False
        else: return False

def CreateBook(book):

    entry = {
        "Book ID": book.number,
        "title": book.title,
        "author": book.author,
        "tag": book.tag,
        "stock": book.stock,
    }

    result = entries.insert_one(entry)

def SearchBook(bookID):

    result = entries.find_one({"Book ID": bookID})
    if result is None: return None
    for results in result:
        return result

def SearchMany():

    return entries.count_documents({"Book ID": {"$gt": 0}})

def TakeBook(book):

    result = entries.update_one({"Book ID": book.number}, {"$set": {"stock": book.stock - 1}})