from flask import Blueprint, request, jsonify, make_response
import json
import traceback
from handler import CreateUser
from utility import FileReader

serv = Blueprint("serv", __name__)

config = FileReader().file_reader()


@serv.route("/createUser", methods=['POST'])
def create_user():
    create_user_obj = CreateUser()
    try:
        headers = request.headers
        bearer = headers.get('Authorization')
        token = bearer.split()[1]
        if token == config["token"]:
            if request.method == "POST":
                try:
                    input_data = json.loads(request.data)
                    if "username" in input_data:
                        user_name = input_data["username"]
                    else:
                        raise Exception("username not present!")
                    if "password" in input_data:
                        password = input_data["password"]
                    else:
                        raise Exception("password not present!")

                    if "age" in input_data:
                        age = input_data["age"]
                        try:
                            age = int(age)
                        except Exception as e:
                            raise Exception("age should be integer!")
                    else:
                        raise Exception("age not present!")

                    response = create_user_obj.create_user(user_name, password, age)
                    return response
                except Exception as e:
                    traceback.print_exc()
                    return jsonify({"status": "failed", "message": str(e)})
            else:
                return make_response("method_not_supported", 401)
        else:
            return make_response("forbidden", 401)

    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": "failed", "message": str(e)})
