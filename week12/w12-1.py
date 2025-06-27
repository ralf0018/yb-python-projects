from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<p>Hello, Flask!</p>"

@app.route("/bye")
def bye():
    return "<p>Goodbye, Flask!</p>"

@app.route("/greet/<name>")
def greet(name):
    return f"<p>Hello, {name} is learning Flask!</p>"

if __name__ == "__main__":
    app.run(debug=True)