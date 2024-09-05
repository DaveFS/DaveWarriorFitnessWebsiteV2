from flask import Flask #import class

app = Flask(__name__) #create object which is app, must have name

@app.route("/") #create route - impacts URL
def hello_world():
    return "<p>Hello, Rave!<p>"

@app.route("/dave")
def deeper():
    return "<p>Eat me<p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)