'''This is the main file which contains all the end points'''


from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
import enum
app = Flask(__name__)
app.secret_key = 'sdfdslfls@#1223$lskd'
api = Api(app)

jwt = JWT(app,authenticate, identity) # gives /auth end point

items: list = []







# Using enum class create enumerations
class http_status(enum.Enum):
   Ok = 200
   Created = 201
   Accepted = 202
   BadRequest = 400
   Unauthorized = 401
   NotFound = 404




class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type = float, required = True, help = 'this field cannot be left blank')

  
    @jwt_required()
    def get(self, name: str) -> dict:
        '''End Point of GET request which takes name and return the whole information about the item in json'''

        item: dict = next(filter(lambda x:x['name'] == name, items), None)
        return item, http_status.Ok if item else http_status.NotFound

    
    
    def post(self, name: str) -> dict:
        '''End point of POST request which takes name and save the information about the item'''

        if next(filter(lambda x:x['name'] == name, items), None) is not None:
            return {"message": "name {} already exist".format(name)}, http_status.BadRequest

        data: dict = Item.parser.parse_args()
        item: dict = {"name": name, "price": data["price"]} 
        items.append(item)
        return item, http_status.Created
    
    
    
    def delete(self, name: str) -> dict:
        '''End point of DELETE request which takes the name and delete the whole information about the item from memory'''
            
        for i, item in enumerate(items):
            if item["name"] == name:
                del items[i]

        return {"message": "item deleted"}, http_status.Ok

   
   
    def put(self, name: str) -> dict:
        '''End Point of PUT request which takes the name and update the information about that item'''
        
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {"name": name, "price": data["price"]}
            items.append(item)
        else:
            item.update(data)

        return item, http_status.Created



class ItemList(Resource):
    def get(self) -> dict:
        '''End point of GET which return the whole list of items'''

        return {"items": items}, http_status.Ok





def msesage_response(message: str) -> dict:
    '''Function takes message of response and return it in dictionery format'''
    return {"message": message}

api.add_resource(Item, "/items/<string:name>") 
api.add_resource(ItemList, "/items") 

app.run(port = 5000)