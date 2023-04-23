from flask import Flask
app = Flask(__name__)

@app.route("/test")
def testServer():
    return "Healthy"

@app.route("/", methods=["GET"])
def index():
    return "HW"

if __name__ == "__main__":
    app.run(debug=True)
