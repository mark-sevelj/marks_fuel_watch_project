from flask import Flask
from fuel_watch_frontend import generate_fuel_watch_html_string

app = Flask(__name__)

kwargs = {"Region": '',
          "Suburb": '',
          "Product": 'Unleaded Petrol',
          "Day": '',
          "Surrounding": 'yes',
          "Brand": '',
          "Sort_on": 'price',
          "keys_of_interest": [
              'updated',
              'price',
              'trading-name',
              'brand',
              'address',
              'location',
              ],
          }


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/about')
def about():
    return 'About Hello World'


@app.route('/fuel_watch')
def fuel_watch():
    return generate_fuel_watch_html_string(filtered=True, **kwargs)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
