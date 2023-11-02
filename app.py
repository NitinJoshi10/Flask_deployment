from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello"

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/Post")
def somecode():
    return "Do your job"

if __name__ == "__main__":
    app.run(debug = True)
