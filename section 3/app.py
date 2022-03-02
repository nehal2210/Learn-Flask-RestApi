
from flask import Flask, jsonify,request,render_template


app = Flask(__name__)

stores = [
    {
        "name":"wonderfull store",
        "items":[{
            "name":"item 1",
            "price":"255"
        }

        ]
    }
]


@app.route("/")
def home():
    return render_template("index.html")




@app.route("/store")
def get_stores():
    return jsonify({"stores":stores})


@app.route("/store/<string:name>")
def get_store(name):
    for s in stores:
        if s.get("name") == name:
            return jsonify(s)
    
    return jsonify({"message":"Note found"})




@app.route("/store/<string:name>/item")
def get_item(name):
    for s in stores:
        if s.get("name") == name:
            return jsonify(s["items"])
    
    return jsonify({"message":"Note found"})




@app.route("/store",methods=['POST'])
def create_store():
    rq_data = request.get_json()
    new_store = {
        "name": rq_data["name"],
        "items":[]
    }

    stores.append(new_store)

    return jsonify(new_store)






@app.route("/store/<string:name>/item",methods=['POST'])
def create_item(name):
    rq_data = request.get_json()
    for s in stores:
        if s["name"] == name:
            s["items"].append(rq_data)
            return jsonify(stores)

    return jsonify({"message":"not found~"})

app.run(port=5000)
