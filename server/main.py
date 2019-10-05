import math
from flask import Flask, jsonify

App = Flask(__name__)

@App.route("/")
def Index():
	return jsonify({"about":"good"})



if __name__ == "__main__":
	App.run(debug=True)

