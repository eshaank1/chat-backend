from flask import Blueprint, request, jsonify  
from flask_restful import Api, Resource 
from flask_cors import CORS
import requests  
import random
import os

from model.chats import *

chat_api = Blueprint('chat_api', __name__,
            url_prefix='/api/chats')
api = Api(chat_api)

CORS(chat_api, resources={r"/api/*": {"origins": "*"}}) # uncomment this line for local testing

chat_data = []

class ChatAPI:
    class _Test(Resource):
        def get(self):
            response = jsonify({"Connection Test": "Successfully connected to backend!"})
            return response
        
    class _Create(Resource):
        def get(self):
            return jsonify({"message": "This is the GET request for _Creating"})

        def post(self):
            data = request.json
            chat_data.append(data)
            return jsonify({"message": "Data stored successfully!"})


    class _Read(Resource):
        def get(self):
            return jsonify(chat_data)


api.add_resource(ChatAPI._Create, '/create')
api.add_resource(ChatAPI._Read, '/read')
api.add_resource(ChatAPI._Test, '/test')


if __name__ == "__main__":
    # server = "http://127.0.0.1:8987" # run local
    server = 'https://chat.stu.nighthawkcodingsociety.com'  # Update with your server URL
    url = server + "/api/chats"
    responses = []

    # Simulate sending data to the chat API
    sample_data = {"message": "Hello, this is a test message!"}
    create_response = requests.post(url+"/create", json=sample_data)
    responses.append(create_response)

    # Retrieve stored data from the chat API
    read_response = requests.get(url+"/read")
    responses.append(read_response)

    # Display responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")
