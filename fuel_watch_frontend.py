import datetime as dt

import fuel_watch_backend as fwb
import fuel_watch_filters as filters


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
    <link rel="icon" type="image/png" href="static/media/favicon-16x16.png" />
    <link rel="stylesheet" href="static/main.css">
    <title>
        Marks Fuel Watch Project
    </title>

</head>
    '''
    return head


# def html_style():
#     """Returns a webpage styling'
#     """
#     style = '''
# <style>
#     .footer {
#         position: fixed;
#         left: 0;
#         bottom: 0;
#         width: 100%;
#         background-color: white;
#         color: black;
#         text-align: center;
#         font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
#         font-size: 12px;
#     }

#     h1 {
#          background: black;
#          color: white;
#          font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
#     }

#     h2 {
#          background: #b1cdcd;
#          border-radius: 10px;
#          color: black;
#          font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
#          font-size: 13px;
#          padding: 10px;
#          text-align: centre;

#     }

#     input {
#          background: white;
#          color: black;
#          font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
#          padding: 5px;
#          text-align: left;

#     }

#     input.select {
#          border-radius: 10px;
#          background-color: #FCF3CF;
#          color: black;
#          font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
#          padding: 5px;
#          text-align: left;

#     }

#     label {
#          background: white;
#          color: black;
#          font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
#          padding: 5px;
#          text-align: left;

#     }

#     label.tomorrow {
#         background-color: #F2D7D5;
#         border-radius: 10px;
#         font-size: 16px;
#         padding: 5px;
#     }


#     nav {
#          background-color: #FCF3CF;
#          border-radius: 10px;
#          padding: 10px;
#          font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
#     }

#     p {
#          background: white;
#          color: black;
#          font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
#          padding: 10px;
#          text-align: left;

#     p.l {
#          background: white;
#          color: black;
#          font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
#          padding: 10px;
#          text-align: left;

#     }

#     p.c {
#          background: white;
#          color: black;
#          font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
#          padding: 10px;
#          text-align: left;

#     }
#     p.r {
#          background: white;
#          color: black;
#          font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
#          padding: 5px;
#          text-align: left;

#     }

#     p.tomorrow {
#         font-size: 12px;
#         background-color: #F2D7D5;
#     }

#     select {
#          background: white;
#          color: black;
#          font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
#          padding: 5px;
#          text-align: left;

#     }

#     table {
#         border-collapse: collapse;
#         border: 1px solid black;
#         border-radius: 10px;
#         font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
#         padding: 2px;
#     }

#     th, td {
#         border: 1px solid black;
#         padding: 15px;
#         border-bottom: 1px solid #ddd;
#     }

#     th {
#         background-color: #FCF3CF;
#         color: black;
#         text-align: centre;
#         padding: 15px;
#     }

#     tr.today {
#         font-size: 12px;
#         background-color: #F2F3F4;

#     }

#     tr.tomorrow {
#         font-size: 12px;
#         background-color: #F2D7D5;
#     }

#     /*tr:nth-child(even) {background-color: #f5f5f5 ;}*/

#     tr:hover {background-color: #E8F8F5;}

#     /* unvisited link */
#     a:link {
#         color: #273746;
#     }

#     /* visited link */
#     a:visited {
#         color: #1D8348;
#     }

#     /* mouse over link */
#     a:hover {
#         color: hotpink;
#     }

#     /* selected link */
#     a:active {
#         color: blue;
#     }

#     ul.nav {
#           list-style-type: none;
#           margin: 0;
#           padding: 0;
#           overflow: hidden;
#           background-color: #333;
#     }

#     li.nav {
#       float: left;
#     }

#     li.nav a {
#       display: block;
#       color: white;
#       text-align: center;
#       padding: 14px 16px;
#       text-decoration: none;
#     }

#     /* Change the link color to #111 (black) on hover */
#     li.nav a:hover {
#       background-color: #111;
#     }

# </style>
#     '''
#     return style


def html_home_navbar():
    """Returns a webpage navbar.
    """
    navbar = '''
        <div>
            <nav>
                <span style="float:right;">
                <img class="pull-right" src="https://www.fuelwatch.wa.gov.au/fuelwatch/art/fuelwatch-logo.gif?
                 pfdrid_c=true" alt="../static/media/fuel_watch_logo.PNG"
                 height="75" width="105">
                </span>
                <h3 class="logo">Marks Fuel Watch Project</h3>
                <a href="/about" color:"#27AE60">About Project</a>
                &nbsp;&nbsp;&nbsp;&nbsp;
                <a href="https://www.fuelwatch.wa.gov.au" target="_blank">Fuel Watch Website</a>
            </nav>
        </div>
    '''
    return navbar


def html_about_navbar():
    """Returns a webpage navbar.
    """
    navbar = '''
        <div>
            <nav>
                <span style="float:right;">
                <img class="pull-right" src="https://www.fuelwatch.wa.gov.au/fuelwatch/art/fuelwatch-logo.gif?
                 pfdrid_c=true" alt="../static/media/fuel_watch_logo.PNG"
                 height="75" width="105">
                </span>
                <h3 class="logo">Marks Fuel Watch Project</h3>
                <a href="/" color:"#27AE60">Home</a>
                &nbsp;&nbsp;&nbsp;&nbsp;
                <a href="https://www.fuelwatch.wa.gov.au" target="_blank">Fuel Watch Website</a>
            </nav>
        </div>
    '''
    return navbar


def html_home_body(filtered=True, **kwargs):
    """Return a HTML string containing the fuel watch data table.
    """

    product = filters.Product()
    suburb = filters.Suburb()
    data = fwb.get_fuel_data(filtered, **kwargs)

    today = str(dt.date.today())

    body = '''
<hr>
<div style="overflow-x:auto;">
<table border="1" width="100%">
<thead>
<tr>
    '''

    select_form = """
    <div>
    <form>
      <label for="product">Product:</label>
      <select name="product" id="product">
    """
    # Create the Product dropdown selector
    for key in product.keys():
        if key == 'FilterName':
            key = ''
        # Renders the returned selectors with selection made by user
        if key != kwargs['Product']:
            select_form = select_form + f'<option value={key}>{key}</option>'
        else:
            select_form = select_form + f'<option value={key} selected>{key}</option>'

    select_form = select_form + """
      </select>
      &nbsp;
      <label for="suburb">Suburb:</label>
      <select name="suburb" id="suburb">
    """
    for key in suburb.keys():
        if key == 'FilterName':
            key = ''
        # Renders the returned selectors with selection made by user
        if key != kwargs['Suburb']:
            select_form = select_form + f'<option value={key}>{key}</option>'
        else:
            select_form = select_form + f'<option value={key} selected>{key}</option>'

    select_form = select_form + """
      </select>
      &nbsp;
      &nbsp;
      <label for="surrounding">Include Surrounding:</label>
      <input type="radio" checked="True" id="yes" name="surrounding" value="yes" />
      <label for="yes">Yes</label>
      <input type="radio" id="no" name="surrounding" value="no" />
      <label for="no">No</label>
      &nbsp;
      &nbsp;
      <input class="select" type="submit" value="submit" />
      &nbsp;
      &nbsp;
      <label class='tomorrow'>Tomorrows data included after 2:30 PM</label>
    </form>
    <br>
    <hr>
    </div>
    """

    body = body + select_form

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
    """ Return a HTML string containing the About page body
    """

    about = """
    <body style="overflow-x:auto;">
        <h2>About the Fuel Watch Project</h2>
        <hr>
        <br>
        <div>
            <p class='l'>
                This project is a result of a Learn Python Course developed by
                Robin Chew.
            </p>
            <p class='l'>
               The course was run for 10 Weeks from march 2020 at the Bentley
               Technology centre in Perth Western Australia, there was several
               break due to the covid 19 pandemic.
            </p>
            <p class='l'>
               The objective of the course was to get the Perth Fuel Watch RSS
               feed, extract the data into a format that suited our
               own needs, then present the data in a html page using Flask.
            </p>
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

            All data is sourced from the Fuel Watch Website,
            produced by the Government of Western Australia.

            </em>
            </strong>
            <hr>
        </div>


    """
    return footer


def generate_home_html_string(filtered=True, **kwargs):
    """

    """

    # Put the suburb name into the correct format
    kwargs['Suburb'] = str.capitalize(kwargs['Suburb'])

    return html_head() + html_home_navbar() + html_home_body(filtered, **kwargs) + html_footer()


def generate_about_html_string():
    """
    """
    return html_head() + html_about_navbar() + html_about_body() + html_footer()

# + html_style()


if __name__ == '__main__':
    """Run the fuel watch html generator with default filters

    """
    print('Generating file')
    kwargs = {"Region": '',
              "Suburb": '',
              "Product": '',
              "Day": '',
              "Surrounding": '',
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

    generate_home_html_string(filtered=True, **kwargs)
    print('Fuel Watch.html has been generated and can be found in \html_files')
