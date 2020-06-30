from flask import Flask
from fuel_watch_frontend import generate_fuel_watch_html_string

app = Flask(__name__)


@app.route('/')
def fuel_watch():
    #return generate_fuel_watch_html_string(filtered=True, **kwargs)
    return "fuel watch"


@app.route('/about')
def about():
    return 'About Hello World'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
