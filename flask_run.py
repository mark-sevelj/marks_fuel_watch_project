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
    return '<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="icon" type="image/png" href="../static/media/favicon-16x16.png" />
    <title>
        Fuel Watch
    </title>
    <img src="https://www.fuelwatch.wa.gov.au/fuelwatch/art/fuelwatch-logo.gif?
    pfdrid_c=true" alt="../static/media/fuel_watch_logo.PNG"
     height="50" width="70">

</head>'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
