from flask import Flask, request
from flask_restful import Resource, Api 

app = Flask(__name__)
api = Api(app)

students = []

class StudentNames(Resource):
    def get(self, name):
        # Show list students in console(terminal)
        print(students)
        
        # Loop for searching students in the list
        for stud in students:
            if stud['name'] == name:
                return stud
        
        
        return {name: None}, 404

    def post(self, name):
        stud = {'name': name}
        students.append(stud)
        
        return stud
    
class AllNames(Resource):
    def get():
        return {'students': students}

api.add_resource(StudentNames, '/students/<string:name>')
api.add_resource(AllNames, '/students/')

if __name__ == '__main__':
    app.run(debug=True)
    


