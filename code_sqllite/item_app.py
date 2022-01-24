'''
In flask_restful, the main building block is a resource. Each resource can have several methods associated with it such as GET, POST, PUT, DELETE, etc. for example, there could be a resource that calculates the square of a number whenever a get request is sent to it. Each resource is a class that inherits from the Resource class of flask_restful. Once the resource is created and defined, we can add our custom resource to the api and specify a URL path for that corresponding resource.
'''
'''
When we initialise the JWT object, that is going to use our authenticate and the identity functions together to allow for authentication of the users. JWT creates a new endpoint that endpoint is /auth. We send it a username and a password and the JWT extension gets that username and password and sends it over to the authenticate function, that takes a username and a password. We are then going to find the correct user object using that username and we're going to compare its password to the one that we receive through the auth endpoint. If they match we're going to return the user and that becomes sort of the identity. So what happens next is the auth endpoint returns a JWT token, Now that JWT token in itself doesn't do anything, but we can send it to the next request we make. So when we send a JW token, it calls the identity function and then it uses the JWT token to get the user ID and with that it gets the correct user for that user ID that the JWT token represents.

'''
'''
Flask-RESTful’s request parsing interface, reqparse, is modeled after the argparse interface. It’s designed to provide simple and uniform access to any variable on the flask.request object in Flask.

https://flask-restful.readthedocs.io/en/latest/reqparse.html#:~:text=Flask-RESTful%E2%80%99s%20request%20parsing%20interface%2C%20reqparse%2C%20is%20modeled%20after,the%20flask.Request.values%20dict%3A%20an%20integer%20and%20a%20string
'''

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from security import authenticate, identity
from flask_jwt import JWT, jwt_required
from user import UserRegister

app = Flask(__name__)
app.secret_key = 'xyz'

api = Api(app)
jwt = JWT(app, authenticate, identity) # /auth

items = []

# Createing Item resource by inheriting from resource class of flask_restful
class Item(Resource):

    # class attributes
    parser =  reqparse.RequestParser()
    parser.add_argument("price",
    type=float, required=True,
    help="Price can not be blank"
    )

    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item is not None else 404 # 404 ==> Not found

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {"message":"AN item with name already exists."}, 400 # 400 ==> Bad request
            
        #request_data  =  request.get_json()
        request_data = Item.parser.parse_args()
        item ={'name': name, 'price': request_data["price"]}
        items.append(item)
        return item, 201 # 201 ==> Created

    def delete(self, name):
        global items # to overcome local variable issue, otherwise items will be treated as local variable without 'global' declaration
        items = list(filter(lambda x : x['name'] != name, items))
        return {"message":"Item Deleted"}

    def put(self, name):
    
        data = Item.parser.parse_args()
        #data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}

# Adding custom resource to api
api.add_resource(Item, '/item/<string:name>') # https://127.0.0.1/item/chair
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


app.run(port=8080, debug=True)