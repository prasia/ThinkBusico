from flask import Flask, render_template, request, jsonify
from chat import get_response
import random
import json

app = Flask(__name__)

@app.get("/") # or @app.route("/", methods=["GET"])
def index_get():
  return render_template("base.html")

@app.route("/predict")
def predict():
  text = request.get_json().get("message")
  #TODO : check if text is valid
  response = get_response(text)
  message = {"answer": response}
  return jsonify(message)

"""
if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)
"""
if __name__ == "__main__":
  app.run(debug=True)