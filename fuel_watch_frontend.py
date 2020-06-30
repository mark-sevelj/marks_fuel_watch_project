import datetime as dt

import fuel_watch_backend as fwb


def html_head():
    """Returns a webpage head.
    """
    head = '''
    <!DOCTYPE html>
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

</head>
    '''
    return head


def html_style():
    """Returns a webpage styling'
    """
    style = '''
<style>
    h1 {
         background: blue;
         color: white;
         font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
    }

    nav {
         background-color: #F9E79F;
         border-radius: 10px;
         padding: 10px;
         font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
    }

    table {
        border-collapse: collapse;
        border: 1px solid black;
        border-radius: 10px;
        font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
        padding: 2px;
    }

    th, td {
        border: 1px solid black;
        padding: 15px;
        border-bottom: 1px solid #ddd;
    }

    th {
        background-color: #FCF3CF;
        color: black;
        text-align: centre;
        padding: 15px;
    }

    tr.today {
        font-size: 12px;
        background-color: #F2F3F4;

    }

    tr.tomorrow {
        font-size: 12px;
        background-color: #F2D7D5;
    }

    /*tr:nth-child(even) {background-color: #f5f5f5 ;}*/

    tr:hover {background-color: #E8F8F5;}

    /* unvisited link */
    a:link {
        color: #273746;
    }

    /* visited link */
    a:visited {
        color: #1D8348;
    }

    /* mouse over link */
    a:hover {
        color: hotpink;
    }

    /* selected link */
    a:active {
        color: blue;
    }

    .footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: white;
    color: black;
    text-align: center;
    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
    font-size: 12px;
    }
</style>
    '''
    return style


def html_home_navbar():
    """Returns a webpage navbar.
    """
    navbar = '''
        <nav>
            <h3 class="logo">Marks Fuel Watch Project</h3>
            <a href="/about" color:"#27AE60">About Project</a>
            &nbsp;&nbsp;&nbsp;&nbsp;
            <a href="https://www.fuelwatch.wa.gov.au" target="_blank">Fuel Watch Website</a>
        </nav>
    '''
    return navbar


def html_about_navbar():
    """Returns a webpage navbar.
    """
    navbar = '''
        <nav>
            <h3 class="logo">Marks Fuel Watch Project</h3>
            <a href="/" color:"#27AE60">Home</a>
            &nbsp;&nbsp;&nbsp;&nbsp;
            <a href="https://www.fuelwatch.wa.gov.au" target="_blank">Fuel Watch Website</a>
        </nav>
    '''
    return navbar


def html_home_body(filtered=True, **kwargs):
    """Returns a webpage body.
    """

    data = fwb.get_fuel_data(filtered, **kwargs)

    today = str(dt.date.today())

    body = '''
<br>
<hr>
<br>
<div style="overflow-x:auto;">
<table border="1" width="100%">
<thead>
<tr>
    '''
    # Create the column labels from the data keys
    for key in data[0].keys():
        body = body + "<th>" + key.capitalize() + "</th>"
    # Close out the column headings
    body = body + "\n</tr>\n</thead>\n</div>"

    # Add each row of data to the table
    body = body + "\n<tbody>"
    for x in data:
        if x['updated'] == today:

            body = body + "\n<tr class='today'>"

        else:
            body = body + "\n<tr class='tomorrow'>"

        for key, value in x.items():

            body = body + "<td>" + str(value) + "</td>"

        body = body + "\n</tr>"
    body = body + "\n</tbody>"

    return body

def html_about_body():
    """
    """

    about = """
                <body>

                    <h2>About the Fuel Watch Project</h2>
                    <hr>
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
            """
    return about


def html_footer():

    footer = """
<div class="footer">
    <hr>
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


    """
    return footer


def generate_home_html_string(filtered=True, **kwargs):
    """

    """

    return html_head() + html_style() + html_home_navbar() + html_home_body(filtered, **kwargs) + html_footer()


def generate_about_html_string():
    """
    """
    return html_head() + html_style() + html_about_navbar() + html_about_body() + html_footer()


if __name__ == '__main__':
    """Run the fuel watch html generator with default filters

    """
    print('Generating file')
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

    generate_fuel_watch_html(filtered=True, **kwargs)
    print('Fuel Watch.html has been generated and can be found in \html_files')
