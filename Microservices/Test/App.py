
from flask import Flask, json, render_template, make_response, jsonify, request

app = Flask(__name__)

PORT = 3300
HOST = "0.0.0.0"

INFO = {
    "personal": {
        "first_name": "Dineshkumar",
        "middle_name": "Babu",
        "last_name": "Kolimi"
    },
    "languages":{
       "mother_tongue": "Telugu",
        "national": "Hindi",
        "second": "English",
        "partial": "Kannada"
    },
    "Countries":{
        "home": "India",
        "immigrant": "Canada"
    }
}

#GET
@app.route("/")
def home():
    return "<h1 style='color:blue'> Welcome to Microservices! </h1>"

@app.route("/temp")
def template():
   return render_template("index.html")

@app.route("/qstr")
def query_string():
    if request.args:
        resp = {}
        req = request.args
        for key,val in req.items():
            resp[key] = val
        resp = make_response(jsonify(resp), 200)
    else:
        resp = make_response(jsonify({"Error":"No query string in arguments"}, 200))

    return resp

@app.route("/info")
def get_info():
    return make_response(jsonify(INFO),200)

@app.route("/info/<collection>/<member>")
def get_details(collection, member):
    if(collection in INFO):
        memb = INFO[collection].get(member)
        if memb:
            resp = make_response(jsonify({"resp":memb}), 200)
        else:
            resp = make_response(jsonify({"Error": "Member Not Found!"}), 400)
    else:
        resp = make_response(jsonify({"Error": "Collection not Found!"}), 400)
    return resp

#POST
@app.route("/info/<collection>", methods=["POST"])
def create_collection(collection):
    req = request.get_json()
    print(req)
    if collection in INFO:
        resp = make_response(jsonify({"Error": "Collection is already present!"}),400)
    else:
        INFO.update({collection: req})
        resp = make_response(jsonify({"Message": "Collection Updated!"}), 201)
    return resp

#PUT
@app.route("/info/<collection>/<member>", methods=["PUT"])
def update_collection(collection, member):
    req = request.get_json()
    if collection in INFO:
        if member in INFO[collection].keys():
            INFO[collection][member] = req["new"]
            resp = make_response(jsonify({"resp": INFO[collection]}), 202)
        else:
            resp = make_response(
                jsonify({"Error": "Member is not found!"}), 400)
        
    else:
        resp = make_response(jsonify({"Error": "Collection is not found!"}), 400)
    return resp

app.route("/info/delete/<collection>", methods=["DELETE"])
def delete_collection(collection):
    if collection in INFO:
        del INFO[collection]
        resp = make_response(jsonify(INFO), 201)
    else:
        resp = make_response(jsonify({"Error": "Collection is not found!"}), 400)
    return resp



if __name__ == "__main__":
    print("Sever running in port %s"%(PORT))
    app.run(host=HOST, port=PORT)

