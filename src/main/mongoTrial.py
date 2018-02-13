import pymongo
uri = "mongodb://127.0.0.1:27017"

client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

students = [student['marks'] for student in collection.find({}) if student['marks'] > 95]

print(students)
for student in students:
    print(student)