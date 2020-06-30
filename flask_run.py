from flask import Flask
from fuel_watch_frontend import (generate_about_html_string,
                                 generate_home_html_string)

app = Flask(__name__)


@app.route('/')
def fuel_watch():

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
    return generate_home_html_string(filtered=True, **kwargs)


@app.route('/about')
def about():
    return generate_about_html_string()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
