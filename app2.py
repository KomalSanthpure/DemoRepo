
from flask import Flask
app = Flask(__name__)

@app.route('/app/<name>')
def hello_name(name):
    return 'Hello hello %s!' % name

if __name__ == '__main__':
    app.run()
