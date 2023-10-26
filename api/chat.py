from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
import requests 

from model.chats import *


chat_api = Blueprint('chat_api', __name__, url_prefix='/api/chats')
api = Api(chat_api)

chat_data = []
class ChatAPI:
    class _Create(Resource):
        def post(self):
            data = request.json
            chat_data.append(data)
            return jsonify({"message": "Data stored successfully!"})

    class _Read(Resource):
        def get(self):
            return jsonify(chat_data)

api.add_resource(ChatAPI._Create, '/create')
api.add_resource(ChatAPI._Read, '/read')

if __name__ == "__main__":
    server = 'https://chat.nighthawkcodingsociety.com'  # Update with your server URL
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
