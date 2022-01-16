'''
In flask_restful, the main building block is a resource. Each resource can have several methods associated with it such as GET, POST, PUT, DELETE, etc. for example, there could be a resource that calculates the square of a number whenever a get request is sent to it. Each resource is a class that inherits from the Resource class of flask_restful. Once the resource is created and defined, we can add our custom resource to the api and specify a URL path for that corresponding resource.
'''

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

# Createing Item resource by inheriting from resource class of flask_restful
class Item(Resource):
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item is not None else 404 # 404 ==> Not found

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {"message":f"AN item with name {name} already exists."}, 400 # 400 ==> Bad request
            
        request_data  =  request.get_json()
        item ={'name': name, 'price': request_data["price"]}
        items.append(item)
        return item, 201 # 201 ==> Created

class ItemList(Resource):
    def get(self):
        return {'items': items}

# Adding custom resource to api
api.add_resource(Item, '/item/<string:name>') # https://127.0.0.1/item/chair
api.add_resource(ItemList, '/items')

app.run(port=8080, debug=True)