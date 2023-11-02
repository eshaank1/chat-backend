from flask import Blueprint, request, jsonify  
from flask_restful import Api, Resource 
from flask_cors import CORS
import requests  
from model.discussions import *

discussion_api = Blueprint('discussion_api', __name__,
            url_prefix='/api/discussion')
api = Api(discussion_api)

CORS(discussion_api, resources={r"/api/discussion/create": {"origins": "https://eshaank1.github.io"}})

discussion_data = []

class discussionAPI:
    class _Test(Resource):
        def get(self):
            response = jsonify({"Connection Test": "Successfully connected to backend!"})
            return response
        
    class _Create(Resource):
        def get(self):
            return jsonify({"message": "This is the GET request for _Create"})

        def post(self):
            data = request.json
            discussion_data.append(data)
            return jsonify({"message": "Data stored successfully!"})


    class _Read(Resource):
        def get(self):
            return jsonify(discussion_data)


api.add_resource(discussionAPI._Create, '/create')
api.add_resource(discussionAPI._Read, '/read')
api.add_resource(discussionAPI._Test, '/test')


if __name__ == "__main__":
    # server = "http://127.0.0.1:8987" # run local
    server = 'https://chat.stu.nighthawkcodingsociety.com'  # Update with your server URL
    url = server + "/api/discussions"
    responses = []

    # Simulate sending data to the discussion API
    sample_data = {"message": "Hello, this is a test message!"}
    create_response = requests.post(url+"/create", json=sample_data)
    responses.append(create_response)

    # Retrieve stored data from the discussion API
    read_response = requests.get(url+"/read")
    responses.append(read_response)

    # Display responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")