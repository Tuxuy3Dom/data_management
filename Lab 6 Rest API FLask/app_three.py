from flask import Flask, request
from flask_restful import Resource, Api 
# pip install Flask-JWT
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required
import jwt

try:
    # 👇️ using Python 3.10+
    from collections.abc import Mapping
except ImportError:
    # 👇️ using Python 3.10-
    from collections import Mapping



app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_pass'
api = Api(app)

jwt = JWT(app, authenticate, identity)

# We should call to the database!
# However, rigth now its just a list of dictionaries
# student = [{'name': 'Andrusiv'},{name: 'Cyran'}]
# Kepp in mind, its in memory, it clears with every restart!
students = []

class StudentNames(Resource):
    def get(self, name):
        # Show list students in console(terminal)
        print(students)
        
        # Cyrcle through list for students
        for item in students:
            if item['name'] == name:
                return item
        
        # If it`s request of a student not yet in the student list
        return {name: None}, 404

    def post(self, name):
        # add the dictionary to list
        stud = {'name': name}
        students.append(stud)
        
        # Then return it back
        print(students)
        return stud
    
    def delete(self, name):
        # Cycle through list for student
        for ind, item in enumerate(students):
            if item['name'] == name:
                # don`t really need to save this
                deleted_stud = students.pop(ind)
                return {'note': 'delete successful'}
            
        
class AllNames(Resource):
    @jwt_required()
    def get(self):
        # return all students
        return {'students': students}

api.add_resource(StudentNames, '/student/<string:name>')
api.add_resource(AllNames, '/students/')

if __name__ == '__main__':
    # 👇️ <class 'collections.abc.Mapping'>
    print(Mapping)
    app.run(debug=True)

    


