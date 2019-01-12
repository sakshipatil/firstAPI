from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Sakshi Subodh Dubey, Welcome to API World!"


if __name__=='__main__':
    app.run(debug=True,port=5050,host="0.0.0.0")