from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello();
    return 'hello world '

if __name__== "__main":
	app.run(host = '0.0.0.0', port = 8080)