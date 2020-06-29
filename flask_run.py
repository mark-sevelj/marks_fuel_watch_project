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
    <link rel="icon" type="image/png" href="static/media/favicon-16x16.png" />
    <title>
        Fuel Watch
    </title>
    <img src="https://www.fuelwatch.wa.gov.au/fuelwatch/art/fuelwatch-logo.gif?pfdrid_c=true" alt="Smiley face" height="50" width="70">

    <link rel="stylesheet" type="text/css" href="../css/fuel_watch.css">
</head>

<!-- <style type="text/css">

    h2 {
        font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
        padding: 2px;
        font-size: 22px;
        text-align: center;
    }

     p {
        font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
        padding: 10px;
        font-size: 18px;
        text-align: left;
    }
S
</style> -->

<body>

    <h2>About the Fuel Watch Project</h2>
    <br>
    <br>
    <br>
    <hr>
    <br>
    <br>

    <div>
        <p>
            This project is a result of a Learn Python Course developed by
            Robin Chew.
        </p>
        <p>
           The course was run for 10 Weeks from march 2020 at the Bentley
           Technology centre in Perth Western Australia
        </p>
        <p>
            The objective of the course was to get the Perth Fuel Watch RSS
            feed, extract the data into a format that suited our
            own needs, then present the data in a html page.

        </p>

    </div>
    <br>
    <br>
    <br>
    <hr>
<div class="footer">
    <strong>
    <em>
    <p>
    All data is sourced from the Fuel Watch Website,
    produced be the Government of Western Australia.
    </p>
    </em>
    </strong>
    <hr>
</div>

</body>

</html>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
