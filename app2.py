from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return "go to /hello, /goodbye, or /ok"

@app.route("/hello")
def hello_world():
    return "hi friend"

@app.route("/goodbye")
def goodbye_world():
    return "WILSOOOOOOOOOON"

@app.route("/ok")
def ok_world():
    return "ok."

if __name__ == "__main__":
    app.run()
