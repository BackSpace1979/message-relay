from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running!"

# Keep your other routes below...
