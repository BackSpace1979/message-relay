from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Message Relay is running"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Render expects this
    app.run(host="0.0.0.0", port=port)
