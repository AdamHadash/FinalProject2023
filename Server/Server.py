from flask import Flask, render_template

app = Flask(__name__)

@app.route("/test")
def testServer():
    return "Healthy"

@app.route("/", methods=["GET"])
def index():
    return render_template("/home/newman311/PycharmProjects/FinalProject2023/templates/index.html")

if __name__ == "__main__":
    app.run(debug=True)
