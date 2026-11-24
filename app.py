import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.get("/ping")
def ping():
    host = request.args.get("host", "")
    output = subprocess.check_output("ping -c 1 " + host, shell=True)
    return output

@app.get("/")
def index():
    return "LR10 demo app"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
