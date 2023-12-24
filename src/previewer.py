from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    result = subprocess.check_output(['php','./src/previewer/index.php'])
    return result

if __name__ == "__main__":
    app.run()
