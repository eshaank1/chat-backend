# chat_model.py
class ChatModel:
    chat_data = []  # Data storage (You can replace this with a proper database)

    @classmethod
    def create_chat(cls, data):
        cls.chat_data.append(data)
        return {"message": "Data stored successfully!"}

    @classmethod
    def read_chat(cls):
        return cls.chat_data

