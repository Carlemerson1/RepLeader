from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
@app.route('/')

def home():
    return "Hello"

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)

