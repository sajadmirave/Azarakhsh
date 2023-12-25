from flask import Flask,jsonify
import subprocess

import sys
import os

# get current path
current_path = os.path.abspath(__file__)

# get root directory path
root = os.path.dirname(os.path.dirname(current_path))

sys.path.append(root)

from index import DB



app = Flask(__name__)

@app.route("/")
def home():
    db = DB()
    result = db.getAll('fruit')
    db.close_connection()
    return jsonify(result)        

if __name__ == "__main__":
    app.run(debug=True)
