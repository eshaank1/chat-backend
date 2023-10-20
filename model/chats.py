import random

chat_data = []

# Initialize chat messages
def initChat():
    # You can add initial chat messages here if needed.
    pass

# Add a new chat message
def addChatMessage(message):
    chat_data.append({"message": message})

# Get all chat messages
def getChatMessages():
    return chat_data

# Test Chat Model
if __name__ == "__main__": 
    initChat()  # initialize chat data

    # Add a sample chat message
    addChatMessage("Hello, this is a test message!")

    # Retrieve chat messages
    chat_messages = getChatMessages()
    for message in chat_messages:
        print(message)
