from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage (clears if server restarts)
messages = []

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    if not data or 'from' not in data or 'text' not in data:
        return jsonify({"error": "Invalid data"}), 400
    messages.append(data)
    return jsonify({"status": "Message stored"}), 200

@app.route('/receive', methods=['GET'])
def receive_messages():
    return jsonify(messages), 200

@app.route('/clear', methods=['POST'])
def clear_messages():
    messages.clear()
    return jsonify({"status": "Messages cleared"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
