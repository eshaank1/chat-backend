from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_chat_data', methods=['POST'])
def receive_chat_data():
    try:
        data = request.get_json()
        chat_data = data.get("chat_data")
        
        # Process chat_data as needed, e.g., store it in a database

        return jsonify({"message": "Data received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(port=897)
