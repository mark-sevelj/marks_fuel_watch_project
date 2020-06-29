from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About Hello World'

@app.route('/fuel_watch')
def fuel_watch():
    return 'Fuel Watch Page'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
