from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Udacity! My name is tamvn, welcome to my Udacity Capstone project'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)