'''
In flask_restful, the main building block is a resource. Each resource can have several methods associated with it such as GET, POST, PUT, DELETE, etc. for example, there could be a resource that calculates the square of a number whenever a get request is sent to it. Each resource is a class that inherits from the Resource class of flask_restful. Once the resource is created and defined, we can add our custom resource to the api and specify a URL path for that corresponding resource.
'''

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Createing Student resource by inheriting from resource class of flask_restful
class Student(Resource):
    def get(self, name):
        return {'student': name}

# Adding custom resource to api
api.add_resource(Student, '/student/<string:name>') # https://127.0.0.1/student/Rolf

app.run(port=8080)