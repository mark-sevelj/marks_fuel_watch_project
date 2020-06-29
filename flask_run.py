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
    return '''
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

<nav>
    <h3 class="logo">Marks Fuel Watch Project</h3>
    <a href="/about" color:"#27AE60" target="_blank">About Project</a>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://www.fuelwatch.wa.gov.au" target="_blank">Fuel Watch Website</a>
</nav>

<br>
<hr>
<br>
<div style="overflow-x:auto;">
<table border="1" width="100%">
<thead>
<tr>
    <th>Updated</th><th>Price</th><th>Trading-name</th><th>Brand</th><th>Address</th><th>Location</th>
</tr>
</thead>
</div>
<tbody>
<tr class='today'><td>2020-04-14</td><td>101.9</td><td>Caltex StarMart North Wanneroo</td><td>Caltex</td><td>2624 Wanneroo Rd</td><td>NOWERGUP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>103</td><td>Mundijong Store & Deli</td><td>Independent</td><td>20 Paterson St</td><td>MUNDIJONG</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>103.7</td><td>Better Choice Roleystone</td><td>Better Choice</td><td>770 Brookton Hwy</td><td>ROLEYSTONE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>104.4</td><td>Shell Fresh Trading Co Welshpool</td><td>Shell</td><td>36 Welshpool Rd</td><td>WELSHPOOL</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>105.9</td><td>Herne Hill General Store</td><td>Puma</td><td>777 Great Northern Hwy</td><td>HERNE HILL</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>106</td><td>Chidlow Growers Mart Liquor Store</td><td>Independent</td><td>570 Rosedale Rd</td><td>CHIDLOW</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>107.9</td><td>Shell Gidgegannup</td><td>Shell</td><td>2095 Toodyay Rd</td><td>GIDGEGANNUP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>107.9</td><td>Liberty Gosnells</td><td>Liberty</td><td>2341 Albany Hwy</td><td>GOSNELLS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>107.9</td><td>Shell Jarrahdale</td><td>Shell</td><td>2 Jarrahdale Rd (Cnr South Western Hwy)</td><td>JARRAHDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>108.9</td><td>United Roleystone</td><td>United</td><td>11 Wygonda Rd</td><td>ROLEYSTONE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>109.9</td><td>BP Baskerville</td><td>BP</td><td>1084 Great Northern Hwy</td><td>BASKERVILLE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>111.9</td><td>United Swanbourne</td><td>United</td><td>2 Servetus St</td><td>SWANBOURNE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>115</td><td>Wesco North Perth</td><td>Wesco</td><td>41 Angove St</td><td>NORTH PERTH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.4</td><td>Shell Fresh Trading Co Ascot</td><td>Shell</td><td>472-480 Great Eastern Hwy</td><td>ASCOT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.4</td><td>Liberty Perth</td><td>Liberty</td><td>17 Brisbane St (Cnr Pier St)</td><td>PERTH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.8</td><td>Glen Forrest Fuel</td><td>Independent</td><td>20 Great Eastern Hwy</td><td>GLEN FORREST</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Banksia Grove</td><td>Coles Express</td><td>1001 Joondalup Dr</td><td>BANKSIA GROVE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Beeliar</td><td>Coles Express</td><td>8 Durnin Ave</td><td>BEELIAR</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Bentley</td><td>Coles Express</td><td>1128 Albany Hwy</td><td>BENTLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Bicton</td><td>Coles Express</td><td>394 Canning Hwy</td><td>BICTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Butler</td><td>Coles Express</td><td>41 Butler Bvd</td><td>BUTLER</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>BP Canning Vale OPT</td><td>BP</td><td>13 Bannister Rd</td><td>CANNING VALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Clarkson</td><td>Coles Express</td><td>Cnr Marmion Ave & Pensacola Tce</td><td>CLARKSON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Cloverdale</td><td>Coles Express</td><td>223 Belmont Ave (Cnr Wright St)</td><td>CLOVERDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Dianella</td><td>Coles Express</td><td>67 Walter Rd West (Cnr Grand Prom)</td><td>DIANELLA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Ellenbrook</td><td>Coles Express</td><td>3 Goodwood Cres</td><td>ELLENBROOK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Forrestfield</td><td>Coles Express</td><td>2 Strelitzia Ave (Cnr Hale Rd)</td><td>FORRESTFIELD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Girrawheen</td><td>Coles Express</td><td>60 Marangaroo Dr</td><td>GIRRAWHEEN</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Karawara</td><td>Coles Express</td><td>222 Manning Rd</td><td>KARAWARA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Kardinya</td><td>Coles Express</td><td>200 North Lake Rd</td><td>KARDINYA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Kingsley</td><td>Coles Express</td><td>Cnr Moolanda Bvd & Hepburn Ave</td><td>KINGSLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Langford</td><td>Coles Express</td><td>70 Nicholson Rd (Cnr Spencer Rd)</td><td>LANGFORD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Leeming</td><td>Coles Express</td><td>51 Farrington St (Cnr Findlay St)</td><td>LEEMING</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Malaga</td><td>Coles Express</td><td>492 Alexander Dr (Cnr Truganina Rd)</td><td>MALAGA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Highgate</td><td>Coles Express</td><td>1-5 Guildford Rd</td><td>MT LAWLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Mount Pleasant</td><td>Coles Express</td><td>1 The Esplanade (Cnr Canning Hwy)</td><td>MT PLEASANT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Myaree</td><td>Coles Express</td><td>69 North Lake Rd (Cnr Marmion St)</td><td>MYAREE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Perth</td><td>Coles Express</td><td>480 William St</td><td>PERTH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Upper Swan Roadhouse</td><td>Coles Express</td><td>1333 Great Northern Hwy</td><td>UPPER SWAN</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>119.9</td><td>Coles Express Warwick (WA)</td><td>Coles Express</td><td>274 Erindale Rd</td><td>WARWICK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>121.9</td><td>Caltex Rous Head</td><td>Caltex</td><td>Cnr North Mole Dr & Rous Head Rd</td><td>NORTH FREMANTLE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>121.9</td><td>Caltex Welshpool</td><td>Caltex</td><td>119 Kurnall Rd</td><td>WELSHPOOL</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>124.9</td><td>Caltex Bibra Lake</td><td>Caltex</td><td>5 Cocos Dr</td><td>BIBRA LAKE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>78.7</td><td>Costco Perth Airport</td><td>Costco</td><td>142 Dunreath Dr</td><td>PERTH AIRPORT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>82.9</td><td>BP Redcliffe</td><td>BP</td><td>419 Great Eastern Hwy</td><td>REDCLIFFE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.7</td><td>Puma Byford</td><td>Puma</td><td>8 Kardan Bvd (Cnr Thomas Rd)</td><td>BYFORD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.7</td><td>Puma Como</td><td>Puma</td><td>393 Canning Hwy</td><td>COMO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.7</td><td>Puma Gnangara</td><td>Puma</td><td>220 Gnangara Rd</td><td>GNANGARA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.7</td><td>Puma Joondalup</td><td>Puma</td><td>49 Candlewood Bvd</td><td>JOONDALUP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.7</td><td>Puma Maddington</td><td>Puma</td><td>137 Kelvin Rd</td><td>MADDINGTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.7</td><td>Puma Midvale</td><td>Puma</td><td>232-234 Morrison Rd</td><td>MIDVALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.7</td><td>Puma Gingers</td><td>Puma</td><td>1383 Great Northern Hwy</td><td>UPPER SWAN</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.7</td><td>Puma Warnbro</td><td>Puma</td><td>649-651 Safety Bay Rd</td><td>WARNBRO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.9</td><td>BP 2go Bellevue</td><td>BP</td><td>59 Great Eastern Hwy</td><td>BELLEVUE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.9</td><td>BP Bull Creek</td><td>BP</td><td>83 Wheatley Dr (Cnr Parry Ave)</td><td>BULL CREEK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.9</td><td>BP Forrestfield</td><td>BP</td><td>155 Hale Rd</td><td>FORRESTFIELD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.9</td><td>FastFuel 24/7</td><td>FastFuel 24/7</td><td>54 Cumberland Rd</td><td>FORRESTFIELD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.9</td><td>BP Crystal Brook (Lesmurdie)</td><td>BP</td><td>7 Welshpool Rd East</td><td>LESMURDIE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.9</td><td>BP Manning</td><td>BP</td><td>73 Manning Rd</td><td>MANNING</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>84.9</td><td>BP 2go Morrison Road</td><td>BP</td><td>226 Morrison Rd</td><td>MIDVALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.3</td><td>Vibe Armadale</td><td>Vibe</td><td>126 Forrest Rd</td><td>ARMADALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.3</td><td>Vibe Hamilton Hill</td><td>Vibe</td><td>114 Rockingham Rd</td><td>HAMILTON HILL</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.3</td><td>Vibe Kwinana</td><td>Vibe</td><td>4 Ocean St (Cnr Patterson Rd)</td><td>KWINANA BEACH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.3</td><td>Vibe Nollamara</td><td>Vibe</td><td>66 Sylvia St</td><td>NOLLAMARA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.3</td><td>Vibe Charles St</td><td>Vibe</td><td>427 Charles St</td><td>NORTH PERTH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.3</td><td>Vibe Port Kennedy</td><td>Vibe</td><td>35 Blackburn Dr (Cnr Port Kennedy Dr)</td><td>PORT KENNEDY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.3</td><td>Vibe Spearwood</td><td>Vibe</td><td>333 Rockingham Rd</td><td>SPEARWOOD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.5</td><td>Vibe Ascot IGA Xpress</td><td>Vibe</td><td>268 Great Eastern Hwy</td><td>ASCOT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.5</td><td>Vibe Subiaco</td><td>Vibe</td><td>123 Thomas St</td><td>SUBIACO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.5</td><td>Vibe Upper Swan IGA Xpress</td><td>Vibe</td><td>1447 Great Northern Hwy</td><td>UPPER SWAN</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.5</td><td>Vibe Welshpool</td><td>Vibe</td><td>124 Welshpool Rd</td><td>WELSHPOOL</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Alexander Heights</td><td>Puma</td><td>200 Mirrabooka Ave</td><td>ALEXANDER HEIGHTS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Armadale Central</td><td>Puma</td><td>Cnr Neerigan St & Third Rd</td><td>ARMADALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Balcatta</td><td>Puma</td><td>229 Balcatta Rd</td><td>BALCATTA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Baldivis</td><td>Puma</td><td>67 Ridge Bvd</td><td>BALDIVIS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Bayswater</td><td>Puma</td><td>502 Guildford Rd</td><td>BAYSWATER</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Yule-Du Roadhouse</td><td>Puma</td><td>681 Albany Hwy</td><td>BEDFORDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Bellevue</td><td>Puma</td><td>18 Clayton St</td><td>BELLEVUE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Belmont</td><td>Puma</td><td>33 Belvidere St (Cnr Keymer St)</td><td>BELMONT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Burswood</td><td>Puma</td><td>265 Gt Eastern Hwy</td><td>BURSWOOD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Vibe Byford</td><td>Vibe</td><td>868 South Western Hwy</td><td>BYFORD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Dayton</td><td>Puma</td><td>8 Repton St</td><td>DAYTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Dianella</td><td>Puma</td><td>61 Walter Rd</td><td>DIANELLA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Ranford</td><td>Puma</td><td>4 Remisko Dr</td><td>FORRESTDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Glen Forrest</td><td>Puma</td><td>1/1400 Great Eastern Hwy</td><td>GLEN FORREST</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Guildford</td><td>Puma</td><td>16 Johnson St</td><td>GUILDFORD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Gwelup</td><td>Puma</td><td>1 Wishart St (Cnr North Beach Rd)</td><td>GWELUP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Phoenix</td><td>Puma</td><td>216 Rockingham Rd (Cnr Phoenix Rd)</td><td>HAMILTON HILL</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Hamilton Hill</td><td>Puma</td><td>224 Clontarf Rd</td><td>HAMILTON HILL</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Kalamunda</td><td>Puma</td><td>26 Kalamunda Rd</td><td>KALAMUNDA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Kewdale</td><td>Puma</td><td>23 Kewdale Rd</td><td>KEWDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Kiara</td><td>Puma</td><td>157 Morley Dr</td><td>KIARA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Parmelia</td><td>Puma</td><td>60 Meares Ave (Cnr Challenger Ave)</td><td>KWINANA TOWN CENTRE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Lesmurdie</td><td>Puma</td><td>194 Canning Rd</td><td>LESMURDIE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Lynwood</td><td>Puma</td><td>2 Lynwood Ave (Cnr Metcalfe Rd)</td><td>LYNWOOD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Landsdale</td><td>Puma</td><td>182 Wanneroo Rd</td><td>MADELEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Malaga</td><td>Puma</td><td>1896 Beach Rd (Cnr Crocker Dr)</td><td>MALAGA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Merriwa</td><td>Puma</td><td>4 Hughie Edwards Dr (Cnr Marmion Ave)</td><td>MERRIWA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Mindarie</td><td>Puma</td><td>22 Anchorage Dr</td><td>MINDARIE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma First Avenue Mt Lawley</td><td>Puma</td><td>81 Guildford Rd</td><td>MT LAWLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Mundaring</td><td>Puma</td><td>7060 Great Eastern Hwy</td><td>MUNDARING</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Munster</td><td>Puma</td><td>512 Rockingham Rd</td><td>MUNSTER</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma North Perth</td><td>Puma</td><td>311 Fitzgerald St</td><td>NORTH PERTH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Osborne Park</td><td>Puma</td><td>8 Main St</td><td>OSBORNE PARK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Pearsall</td><td>Puma</td><td>204 Shiraz Bvd (Cnr Cabernet Loop)</td><td>PEARSALL</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Sawyers Valley</td><td>Puma</td><td>96 Great Eastern Hwy</td><td>SAWYERS VALLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Causeway</td><td>Puma</td><td>170 Albany Hwy (Causeway)</td><td>VICTORIA PARK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Wangara</td><td>Puma</td><td>1 Brady St (Cnr Ocean Reef Rd)</td><td>WANGARA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Wanneroo</td><td>Puma</td><td>951 Wanneroo Rd</td><td>WANNEROO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Wattle Grove</td><td>Puma</td><td>604 Welshpool Rd East</td><td>WATTLE GROVE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Yanchep</td><td>Puma</td><td>1 Ikara Lane (Cnr Kakadu Rd)</td><td>YANCHEP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.7</td><td>Puma Yokine</td><td>Puma</td><td>86 Flinders St (Cnr Hector St)</td><td>YOKINE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Alkimos</td><td>Caltex Woolworths</td><td>11 Shorehaven Bvd (Cnr Pacific Prom)</td><td>ALKIMOS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Applecross</td><td>BP</td><td>848 Canning Hwy</td><td>APPLECROSS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Connect Ascot (WA)</td><td>BP</td><td>210 Great Eastern Hwy (Cnr Resolution Dr)</td><td>ASCOT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Aveley</td><td>Caltex Woolworths</td><td>317 Millhouse Rd</td><td>AVELEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Ballajura (Glenview)</td><td>Caltex Woolworths</td><td>5 Hamelin Dr (Cnr Bellefin Dr)</td><td>BALLAJURA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>NightOwl Shell Bellevue</td><td>Shell</td><td>49 Great Eastern Hwy</td><td>BELLEVUE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex StarMart Byford</td><td>Caltex</td><td>Lot 22 South Western Hwy (Cnr Nettleton Rd)</td><td>BYFORD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Canning Vale</td><td>Caltex Woolworths</td><td>15 Sarah Cl (Cnr Nicholson Rd)</td><td>CANNING VALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Cannington</td><td>Caltex Woolworths</td><td>25 Cecil Ave</td><td>CANNINGTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Clarkson</td><td>BP</td><td>28K Caloundra Rd</td><td>CLARKSON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Currambine Marketplace</td><td>Caltex Woolworths</td><td>1244 Marmion Ave (Cnr Shenton Ave)</td><td>CURRAMBINE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Connect Currambine</td><td>BP</td><td>2 Sunlander Dr (Cnr Burns Beach Rd)</td><td>CURRAMBINE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Dianella</td><td>Caltex Woolworths</td><td>372 Grand Prom</td><td>DIANELLA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex StarMart Doubleview</td><td>Caltex</td><td>365 Scarborough Beach Rd</td><td>DOUBLEVIEW</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Ellenbrook</td><td>Caltex Woolworths</td><td>11 Main St (Cnr The Promenade)</td><td>ELLENBROOK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Floreat</td><td>Caltex Woolworths</td><td>5 Howtree Pl</td><td>FLOREAT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Forrestfield</td><td>Caltex Woolworths</td><td>78C Hale Rd</td><td>FORRESTFIELD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Westgate</td><td>BP</td><td>85 Queen Victoria St</td><td>FREMANTLE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Greenwood</td><td>Caltex Woolworths</td><td>37 Canham Way (Cnr Wanneroo Rd)</td><td>GREENWOOD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex StarMart High Wycombe</td><td>Caltex</td><td>967 Abernethy Rd (Cnr Grogan Rd)</td><td>HIGH WYCOMBE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Shell High Wycombe</td><td>Shell</td><td>1100 Abernethy Rd</td><td>HIGH WYCOMBE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Whitfords</td><td>Caltex Woolworths</td><td>470 Whitfords Ave</td><td>HILLARYS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Jindalee</td><td>BP</td><td>2 Abello Bvd (Cnr Marmion Ave)</td><td>JINDALEE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Joondalup Winton Road</td><td>Caltex Woolworths</td><td>189 Winton Rd</td><td>JOONDALUP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Kewdale</td><td>BP</td><td>549 Abernethy Rd</td><td>KEWDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Welshpool</td><td>BP</td><td>1 Ballantyne Rd</td><td>KEWDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Kwinana</td><td>Caltex Woolworths</td><td>6 Chisham Ave</td><td>KWINANA TOWN CENTRE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Maddington Centro Shopping Centre</td><td>Caltex Woolworths</td><td>77 Attfield St</td><td>MADDINGTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>NightOwl Shell Maddington</td><td>Shell</td><td>1 Davison St</td><td>MADDINGTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Maddington West</td><td>Caltex Woolworths</td><td>207 Burslem Dr</td><td>MADDINGTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Kingsway</td><td>Caltex Woolworths</td><td>168 Wanneroo Rd (opp Giralt Rd)</td><td>MADELEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Maida Vale</td><td>BP</td><td>269 Kalamunda Rd</td><td>MAIDA VALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Mirrabooka</td><td>Caltex Woolworths</td><td>53 Yirrigan Dr</td><td>MIRRABOOKA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Morley Galleria</td><td>Caltex Woolworths</td><td>60 Russell St (Cnr Walter Rd West)</td><td>MORLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Connect Wellington Rd</td><td>BP</td><td>257 Walter Rd (Cnr Wellington Rd)</td><td>MORLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Connect Myaree</td><td>BP</td><td>246 Leach Hwy</td><td>MYAREE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Rosegarden</td><td>BP</td><td>129 Stirling Hwy</td><td>NEDLANDS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Connect North Perth</td><td>BP</td><td>349 Charles St (Cnr Scarborough Beach Rd)</td><td>NORTH PERTH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Connect Beaumauris</td><td>BP</td><td>2 Prendiville Ave (Cnr Marmion Ave)</td><td>OCEAN REEF</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Osborne Park</td><td>Caltex Woolworths</td><td>401 Scarborough Beach Rd</td><td>OSBORNE PARK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Connect Padbury</td><td>BP</td><td>2 Warburton Ave (Cnr Marmion Ave)</td><td>PADBURY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Port Kennedy</td><td>Caltex Woolworths</td><td>12 Saltaire Way</td><td>PORT KENNEDY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>NightOwl Shell Redcliffe</td><td>Shell</td><td>443 Great Eastern Hwy</td><td>REDCLIFFE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Connect Riverton</td><td>BP</td><td>339 High Rd</td><td>RIVERTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Connect Rockingham Park</td><td>BP</td><td>2 Chalgrove Ave (Cnr Read St)</td><td>ROCKINGHAM</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Connect West Coast</td><td>BP</td><td>11 Scarborough Beach Rd (Cnr West Coast Hwy)</td><td>SCARBOROUGH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Sorrento</td><td>BP</td><td>128 West Coast Dr</td><td>SORRENTO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths South Fremantle</td><td>Caltex Woolworths</td><td>219 Hampton Rd</td><td>SOUTH FREMANTLE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths South Lake</td><td>Caltex Woolworths</td><td>752 North Lake Rd (Cnr Berrigan Dr)</td><td>SOUTH LAKE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Connect South Perth</td><td>BP</td><td>9 Mends St</td><td>SOUTH PERTH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Southern River</td><td>Caltex Woolworths</td><td>466 Warton Rd (Cnr Furley Rd)</td><td>SOUTHERN RIVER</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Connect Thomsons Lake</td><td>BP</td><td>810 Beeliar Dr (Cnr Midgegooroo Ave)</td><td>SUCCESS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>Caltex Woolworths Warnbro Fair</td><td>Caltex Woolworths</td><td>202 Warnbro Sound Ave</td><td>WARNBRO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Kenwick</td><td>BP</td><td>40 Courtney Pl</td><td>WATTLE GROVE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP Connect Wembley</td><td>BP</td><td>240 Cambridge St</td><td>WEMBLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP 2go Collins Road</td><td>BP</td><td>121 Collins Rd (Cnr Willeri Dr)</td><td>WILLETTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>85.9</td><td>BP 2go Burrendah</td><td>BP</td><td>69 Pinetree Gully Rd (Cnr Burrendah Bvd)</td><td>WILLETTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex The Foodary Melville</td><td>Caltex</td><td>585 Canning Hwy (Cnr North Lake Rd)</td><td>ALFRED COVE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Applecross</td><td>Caltex</td><td>918 Canning Hwy (Cnr Kintail Rd)</td><td>APPLECROSS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP 2go Armadale</td><td>BP</td><td>3249 Albany Hwy</td><td>ARMADALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex The Foodary Ascot</td><td>Caltex</td><td>204 Great Eastern Hwy</td><td>ASCOT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex The Foodary Ashby</td><td>Caltex</td><td>2 Hollosy Way (Cnr Pinjar Rd)</td><td>ASHBY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Northlands</td><td>Caltex</td><td>391 Wanneroo Rd</td><td>BALCATTA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex The Foodary Baldivis</td><td>Caltex</td><td>614 Baldivis Rd (Cnr Safety Bay Rd)</td><td>BALDIVIS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP Baldivis Northbound Travel Centre</td><td>BP</td><td>Lot 191 Paparone Rd</td><td>BALDIVIS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP Baldivis Southbound Travel Centre</td><td>BP</td><td>Lot 192 Leary Rd</td><td>BALDIVIS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarShop Beechboro</td><td>Caltex</td><td>495 Beechboro Rd North</td><td>BEECHBORO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Altone Road</td><td>Caltex</td><td>159 Altone Rd (Cnr Hull Way)</td><td>BEECHBORO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Better Choice Bellevue</td><td>Better Choice</td><td>177-179 Great Eastern Hwy</td><td>BELLEVUE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex The Foodary Belmont</td><td>Caltex</td><td>303 Great Eastern Hwy</td><td>BELMONT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarShop Bentley</td><td>Caltex</td><td>91-93 Manning Rd (Cnr Wyong Rd)</td><td>BENTLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Butler</td><td>Caltex</td><td>11 Headingly Cr (Cnr Connolly Dr)</td><td>BUTLER</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarShop Livingston</td><td>Caltex</td><td>110 Ranford Rd</td><td>CANNING VALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarShop Bannister Road</td><td>Caltex</td><td>60 Bannister Rd</td><td>CANNING VALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Canning Vale</td><td>Caltex</td><td>1 Wilfred Rd (Cnr Ranford Rd)</td><td>CANNING VALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP 2go Cannington</td><td>BP</td><td>1443 Albany Hwy</td><td>CANNINGTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Cannington</td><td>Caltex</td><td>1346 Albany Hwy</td><td>CANNINGTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Carine</td><td>Caltex</td><td>510 Beach Rd (Cnr Duffy Rd)</td><td>CARINE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP Connect Carlisle</td><td>BP</td><td>44 Archer St (Cnr Orrong Rd)</td><td>CARLISLE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Clarkson</td><td>Caltex</td><td>7 Ocean Keys Bvd (Cnr Marmion Ave)</td><td>CLARKSON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarShop Dianella</td><td>Caltex</td><td>382 Grand Prom</td><td>DIANELLA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex The Foodary East Fremantle</td><td>Caltex</td><td>176 Canning Hwy</td><td>EAST FREMANTLE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP Connect East Perth</td><td>BP</td><td>68-70 Brown St (Cnr East Pde)</td><td>EAST PERTH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP Embleton</td><td>BP</td><td>484 Walter Rd East</td><td>EMBLETON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Forrestdale</td><td>Caltex</td><td>63 Alex Wood Dr (Cnr Armadale Rd)</td><td>FORRESTDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Glendalough</td><td>Caltex</td><td>2 Jon Sanders Dr (Cnr Harborne St)</td><td>GLENDALOUGH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Gosnells</td><td>Caltex</td><td>158 Corfield St</td><td>GOSNELLS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarShop Gosnells North</td><td>Caltex</td><td>2100 Albany Hwy (Cnr Mills St)</td><td>GOSNELLS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex The Foodary Karrinyup</td><td>Caltex</td><td>490 Karrinyup Rd</td><td>GWELUP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP Huntingdale</td><td>BP</td><td>68 Warton Rd (Cnr Matilda Rd)</td><td>HUNTINGDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex The Foodary Cockburn Central</td><td>Caltex</td><td>1/5 Armadale Rd</td><td>JANDAKOT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Joondalup</td><td>Caltex</td><td>Lakeside Joondalup Shopping Centre</td><td>JOONDALUP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP Connect Karrinyup</td><td>BP</td><td>190 Karrinyup Rd (Cnr Burroughs Rd)</td><td>KARRINYUP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Kelmscott</td><td>Caltex</td><td>2877 Albany Hwy</td><td>KELMSCOTT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Kewdale</td><td>Caltex</td><td>2 Fenton St (Cnr Kewdale Rd)</td><td>KEWDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Kingsley Drive</td><td>Caltex</td><td>86 Kingsley Dr</td><td>KINGSLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex Kwinana</td><td>Caltex</td><td>Lot 500 Mandurah Rd (Cnr Wellard Rd)</td><td>KWINANA BEACH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP Connect Kwinana Hub</td><td>BP</td><td>4 Chisham Ave (Cnr Gilmore Ave)</td><td>KWINANA TOWN CENTRE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Leederville</td><td>Caltex</td><td>319 Vincent St</td><td>LEEDERVILLE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex Malaga Drive</td><td>Caltex</td><td>76 Malaga Dr (Cnr Truganina Rd)</td><td>MALAGA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex The Foodary Malaga</td><td>Caltex</td><td>1 Capital Rd (Cnr Alexander Dr)</td><td>MALAGA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Midvale</td><td>Caltex</td><td>375 Great Eastern Hwy</td><td>MIDVALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Morley</td><td>Caltex</td><td>296 Benara Rd (Cnr Beechboro Rd North)</td><td>MORLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Mosman Park</td><td>Caltex</td><td>676 Stirling Hwy</td><td>MOSMAN PARK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarShop Mt Lawley</td><td>Caltex</td><td>810 Beaufort St</td><td>MT LAWLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Mundaring</td><td>Caltex</td><td>5895 Great Eastern Hwy</td><td>MUNDARING</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Murdoch</td><td>Caltex</td><td>10 Robson Way (Cnr South St)</td><td>MURDOCH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP Naval Base</td><td>BP</td><td>1351 Rockingham Rd</td><td>NAVAL BASE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Nedlands</td><td>Caltex</td><td>1 Broadway (Cnr Stirling Hwy)</td><td>NEDLANDS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP 2go Noranda</td><td>BP</td><td>40 Benara Rd</td><td>NORANDA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart O'Connor</td><td>Caltex</td><td>309 Stock Rd (Cnr Sainsbury Rd)</td><td>O'CONNOR</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP Connect Main Street</td><td>BP</td><td>218 Main St (Cnr Royal St)</td><td>OSBORNE PARK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Highgate</td><td>Caltex</td><td>342 Beaufort St (Cnr Bulwer St)</td><td>PERTH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart East Perth</td><td>Caltex</td><td>157 Lord St</td><td>PERTH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP Connect Merriwa</td><td>BP</td><td>2 Ridgewood Bvd (Cnr Hester Ave)</td><td>RIDGEWOOD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Riverton</td><td>Caltex</td><td>270 High Rd</td><td>RIVERTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Rivervale</td><td>Caltex</td><td>111 Great Eastern Hwy</td><td>RIVERVALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Rockingham</td><td>Caltex</td><td>29 Dixon Rd</td><td>ROCKINGHAM</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Scarborough</td><td>Caltex</td><td>74 Scarborough Beach Rd</td><td>SCARBOROUGH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Secret Harbour</td><td>Caltex</td><td>420 Secret Harbour Boulevard</td><td>SECRET HARBOUR</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarShop Seville Grove</td><td>Caltex</td><td>537 Lake Rd</td><td>SEVILLE GROVE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarShop South Lake</td><td>Caltex</td><td>2 Omeo St (Cnr North Lake Rd)</td><td>SOUTH LAKE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP Connect Phoenix</td><td>BP</td><td>Cnr Rockingham Rd & Phoenix Rd</td><td>SPEARWOOD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex The Foodary Stratton</td><td>Caltex</td><td>240 Toodyay Rd (Cnr Lewis Jones Crss)</td><td>STRATTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Subiaco</td><td>Caltex</td><td>194 Rokeby Rd</td><td>SUBIACO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarShop Swan View</td><td>Caltex</td><td>309 Morrison Rd</td><td>SWAN VIEW</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP The Lakes Roadhouse</td><td>BP</td><td>Cnr Great Eastern Hwy & Great Southern Hwy</td><td>THE LAKES</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Thornlie Square</td><td>Caltex</td><td>316 Spencer Rd</td><td>THORNLIE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Thornlie</td><td>Caltex</td><td>219 Yale Rd</td><td>THORNLIE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarShop Wangara</td><td>Caltex</td><td>79 Buckingham Dr (Cnr Hartman Dr)</td><td>WANGARA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Warnbro</td><td>Caltex</td><td>2 Bristol St (Cnr Warnbro Sound Ave)</td><td>WARNBRO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP Connect Palm Springs</td><td>BP</td><td>214 Warnbro Sound Ave (Cnr Halliburton Ave)</td><td>WARNBRO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarShop West Swan</td><td>Caltex</td><td>6639 West Swan Rd</td><td>WEST SWAN</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarShop Balga</td><td>Caltex</td><td>436 Wanneroo Rd</td><td>WESTMINSTER</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex StarMart Willetton</td><td>Caltex</td><td>169 High Rd</td><td>WILLETTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>BP 2go Woodvale</td><td>BP</td><td>941 Whitfords Ave (Cnr Trappers Dr)</td><td>WOODVALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex The Foodary Yanchep</td><td>Caltex</td><td>1 Morwell St</td><td>YANCHEP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>86.9</td><td>Caltex The Foodary Yangebup</td><td>Caltex</td><td>289 Beeliar Dr</td><td>YANGEBUP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.3</td><td>Vibe Yangebup</td><td>Vibe</td><td>109 Barrington St (Cnr Stock Rd)</td><td>YANGEBUP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>7-Eleven Balga</td><td>7-Eleven</td><td>102 Princess Rd</td><td>BALGA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>7-Eleven Banksia Grove</td><td>7-Eleven</td><td>81 Ghost Gum Bvd</td><td>BANKSIA GROVE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Casuarina (WA)</td><td>Coles Express</td><td>1 Johnson Rd (Cnr Thomas Rd)</td><td>BERTRAM</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Brentwood</td><td>Coles Express</td><td>71 Cranford Ave</td><td>BRENTWOOD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Bull Creek</td><td>Coles Express</td><td>44 Benningfield Rd (Cnr Leichhardt St)</td><td>BULL CREEK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>7-Eleven Butler</td><td>7-Eleven</td><td>270 Butler Bvd</td><td>BUTLER</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Canning Vale</td><td>Coles Express</td><td>280 Bannister Rd</td><td>CANNING VALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Claremont</td><td>Coles Express</td><td>269 Stirling Hwy</td><td>CLAREMONT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Duncraig</td><td>Coles Express</td><td>193 Warwick Rd (Cnr Glengarry Dr)</td><td>DUNCRAIG</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Victoria Park</td><td>Coles Express</td><td>66 Kent St (Cnr Berwick St)</td><td>EAST VICTORIA PARK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Edgewater</td><td>Coles Express</td><td>57 Joondalup Dr</td><td>EDGEWATER</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Fremantle</td><td>Coles Express</td><td>101 Hampton Rd</td><td>FREMANTLE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Jolimont</td><td>Coles Express</td><td>6 Jersey St (Cnr Hay St)</td><td>JOLIMONT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>NightOwl Shell Kalamunda</td><td>Shell</td><td>7 Mead St</td><td>KALAMUNDA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>7-Eleven Kelmscott</td><td>7-Eleven</td><td>105 Champion Dr</td><td>KELMSCOTT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Kewdale</td><td>Coles Express</td><td>518 Abernethy Rd (Cnr Kewdale Rd)</td><td>KEWDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Kwinana Beach</td><td>Coles Express</td><td>4 Beach St</td><td>KWINANA BEACH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>7-Eleven Maddington South</td><td>7-Eleven</td><td>1969 Albany Hwy</td><td>MADDINGTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Maddington</td><td>Coles Express</td><td>117 Burslem Dr</td><td>MADDINGTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Better Choice Malaga</td><td>Better Choice</td><td>3 Carson Rd (Cnr Alexander Dr)</td><td>MALAGA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>7-Eleven Middle Swan</td><td>7-Eleven</td><td>40-42 Great Northern Hwy</td><td>MIDDLE SWAN</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Better Choice Naval Base</td><td>Better Choice</td><td>Cnr Rockingham Rd & Lee Rd</td><td>NAVAL BASE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Mount Lawley</td><td>Coles Express</td><td>253 Walcott St (Cnr Fitzgerald St)</td><td>NORTH PERTH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Ocean Reef</td><td>Coles Express</td><td>6 Marina Bvd (Cnr Marmion Ave)</td><td>OCEAN REEF</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Palmyra</td><td>Coles Express</td><td>80 Carrington St (Cnr Marmion St)</td><td>PALMYRA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Scarborough</td><td>Coles Express</td><td>205 West Coast Hwy</td><td>SCARBOROUGH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Westfield</td><td>Coles Express</td><td>88 Champion Dr (Cnr Seville Dr)</td><td>SEVILLE GROVE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Singleton</td><td>Coles Express</td><td>492 Mandurah Rd</td><td>SINGLETON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express South Perth</td><td>Coles Express</td><td>3 Canning Hwy (Cnr Mill Point Rd)</td><td>SOUTH PERTH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Southern River</td><td>Coles Express</td><td>216 Lakey St (Cnr Ranford Rd)</td><td>SOUTHERN RIVER</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>7-Eleven Southern River</td><td>7-Eleven</td><td>481 Balfour St</td><td>SOUTHERN RIVER</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Better Choice Tuart Hill</td><td>Better Choice</td><td>150 Wanneroo Rd</td><td>TUART HILL</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Waikiki</td><td>Coles Express</td><td>1-9 Gnangara Dr (Cnr Read St)</td><td>WAIKIKI</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Wangara</td><td>Coles Express</td><td>1 Niche Pde</td><td>WANGARA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express Wanneroo Pearsall</td><td>Coles Express</td><td>621 Wanneroo Rd</td><td>WANNEROO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>87.9</td><td>Coles Express West Perth</td><td>Coles Express</td><td>30 Thomas St (Cnr Wellington St)</td><td>WEST PERTH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>88.8</td><td>Better Choice Stratton</td><td>Better Choice</td><td>117 O'Connor Rd (Cnr Farrall Rd)</td><td>STRATTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>88.9</td><td>7-Eleven Ascot</td><td>7-Eleven</td><td>194 Great Eastern Hwy</td><td>ASCOT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>88.9</td><td>Coles Express Middle Swan</td><td>Coles Express</td><td>Lot 46 Great Northern Hwy (Cnr Toodyay Rd)</td><td>MIDDLE SWAN</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>88.9</td><td>Coles Express Mosman Park</td><td>Coles Express</td><td>582 Stirling Hwy (Cnr Willis St)</td><td>MOSMAN PARK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>88.9</td><td>Coles Express Wembley</td><td>Coles Express</td><td>337 Cambridge St</td><td>WEMBLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>88.9</td><td>Coles Express Willetton</td><td>Coles Express</td><td>239 High Rd (Cnr Vahland Ave)</td><td>WILLETTON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Armadale</td><td>United</td><td>178 South Western Hwy</td><td>ARMADALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>7-Eleven Bassendean</td><td>7-Eleven</td><td>302-318 Collier Rd</td><td>BASSENDEAN</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Bassendean</td><td>United</td><td>335 Collier Rd (Cnr Fairford St)</td><td>BASSENDEAN</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Bibra Lake</td><td>United</td><td>13 Whyalla Ct</td><td>BIBRA LAKE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Byford</td><td>United</td><td>801-803 South Western Highway</td><td>BYFORD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United East Victoria Park</td><td>United</td><td>916 Albany Hwy</td><td>EAST VICTORIA PARK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Ellenbrook</td><td>United</td><td>3 Locke Lane</td><td>ELLENBROOK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>7-Eleven Forrestdale</td><td>7-Eleven</td><td>2 Haydock St</td><td>FORRESTDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Hamilton Hill</td><td>United</td><td>9 Winterfold Rd</td><td>HAMILTON HILL</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Kewdale</td><td>United</td><td>410-412 Orrong Rd</td><td>KEWDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Leda</td><td>United</td><td>2 Feilman Dr (Cnr Gilmore Ave)</td><td>LEDA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Lexia</td><td>United</td><td>779 Gnangara Rd</td><td>LEXIA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Mt Lawley</td><td>United</td><td>791 Beaufort St</td><td>MT LAWLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Myaree</td><td>United</td><td>182 Leach Hwy</td><td>MYAREE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Neerabup</td><td>United</td><td>2038 Wanneroo Rd</td><td>NEERABUP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Northbridge</td><td>United</td><td>31 Fitzgerald St</td><td>NORTHBRIDGE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Osborne Park</td><td>United</td><td>479 Scarborough Beach Rd</td><td>OSBORNE PARK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Hepburn Heights</td><td>United</td><td>4 Walter Padbury Bvd (Cnr Hepburn Ave)</td><td>PADBURY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Quinns Rocks</td><td>United</td><td>121 Quinns Rd (Cnr Tapping Way)</td><td>QUINNS ROCKS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United South Lake</td><td>United</td><td>49 Berrigan Dr (Cnr South Lake Dr)</td><td>SOUTH LAKE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.3</td><td>United Southern River</td><td>United</td><td>Lot 101 Terrier Pl (Cnr Ranford Rd)</td><td>SOUTHERN RIVER</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.5</td><td>Vibe Mt Helena IGA Xpress</td><td>Vibe</td><td>9 McVicar Pl</td><td>MT HELENA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>Shell Alkimos</td><td>Shell</td><td>Cnr Marmion Av & Santorini Dr</td><td>ALKIMOS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Haynes</td><td>7-Eleven</td><td>1256 Armadale Rd</td><td>ARMADALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Balcatta</td><td>7-Eleven</td><td>174 Balcatta Rd</td><td>BALCATTA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Bibra Lake</td><td>7-Eleven</td><td>35 Port Kembla Dr</td><td>BIBRA LAKE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Byford South</td><td>7-Eleven</td><td>25 Abernethy Rd</td><td>BYFORD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Canning Vale</td><td>7-Eleven</td><td>215 Campbell Rd</td><td>CANNING VALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Carlisle</td><td>7-Eleven</td><td>232 Orrong Rd</td><td>CARLISLE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Caversham</td><td>7-Eleven</td><td>2131 West Swan Rd</td><td>CAVERSHAM</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Cockburn Central</td><td>7-Eleven</td><td>814 North Lake Rd</td><td>COCKBURN CENTRAL</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>Better Choice Como</td><td>Better Choice</td><td>25 Preston St (Cnr Labouchere Rd)</td><td>COMO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Rockingham</td><td>7-Eleven</td><td>129 Dixon Rd</td><td>EAST ROCKINGHAM</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>Better Choice Edgewater</td><td>Better Choice</td><td>21 Edgewater Dr</td><td>EDGEWATER</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Malvern Springs</td><td>7-Eleven</td><td>324 The Broadway</td><td>ELLENBROOK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Gosnells</td><td>7-Eleven</td><td>303 Corfield St</td><td>GOSNELLS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Harrisdale</td><td>7-Eleven</td><td>120 Yellowwood Ave</td><td>HARRISDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Joondalup</td><td>7-Eleven</td><td>8 Buick Way</td><td>JOONDALUP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Kelmscott Central</td><td>7-Eleven</td><td>4 Church St</td><td>KELMSCOTT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>Lori's Fuel Supply</td><td>Independent</td><td>259 Railway Ave</td><td>KELMSCOTT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Landsdale</td><td>7-Eleven</td><td>8 Mullingar Way</td><td>LANDSDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Malaga</td><td>7-Eleven</td><td>750 Marshall Rd (Cnr Guadalupe Rd)</td><td>MALAGA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Midvale</td><td>7-Eleven</td><td>231 Morrison Rd</td><td>MIDVALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Morley</td><td>7-Eleven</td><td>162 Russell St</td><td>MORLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>Puma Neerabup</td><td>Puma</td><td>2056 Wanneroo Rd</td><td>NEERABUP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Queens Park</td><td>7-Eleven</td><td>235 Welshpool Rd</td><td>QUEENS PARK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Success</td><td>7-Eleven</td><td>660 Beeliar Dr</td><td>SUCCESS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Thornlie</td><td>7-Eleven</td><td>125 Murdoch Rd</td><td>THORNLIE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Wangara</td><td>7-Eleven</td><td>79 Gnangara Rd</td><td>WANGARA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Wanneroo</td><td>7-Eleven</td><td>990 Wanneroo Rd</td><td>WANNEROO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Wanneroo South</td><td>7-Eleven</td><td>929-931 Wanneroo Rd</td><td>WANNEROO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.7</td><td>7-Eleven Wattle Grove</td><td>7-Eleven</td><td>332 Hale Rd</td><td>WATTLE GROVE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.9</td><td>BP Kelmscott</td><td>BP</td><td>2907 Albany Hwy</td><td>KELMSCOTT</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.9</td><td>BP Langford</td><td>BP</td><td>230-234 Nicholson Rd</td><td>LANGFORD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>89.9</td><td>BP Dog Swamp</td><td>BP</td><td>4 Wanneroo Rd</td><td>YOKINE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>91.7</td><td>BP Caversham</td><td>BP</td><td>40 Bennett St</td><td>CAVERSHAM</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>91.7</td><td>BP Forrestdale</td><td>BP</td><td>2 Alex Wood Dr</td><td>FORRESTDALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>91.7</td><td>BP Sawyers Valley</td><td>BP</td><td>10895 Great Eastern Hwy</td><td>SAWYERS VALLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>91.7</td><td>BP Woodbridge</td><td>BP</td><td>380 Great Eastern Hwy</td><td>WOODBRIDGE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>91.9</td><td>BP Port Kennedy</td><td>BP</td><td>46 Bakewell Dr</td><td>PORT KENNEDY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>92.7</td><td>BP Ballajura</td><td>BP</td><td>2 Illawarra Cres North (Cnr Alexander Dr)</td><td>BALLAJURA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>92.9</td><td>BP Bibra Lake</td><td>BP</td><td>2 Wellard St</td><td>BIBRA LAKE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>92.9</td><td>BP Koondoola</td><td>BP</td><td>28 Koondoola Ave (Cnr Burbridge Ave)</td><td>KOONDOOLA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>93.7</td><td>Gull Rockingham</td><td>Gull</td><td>40 Kent St</td><td>ROCKINGHAM</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>93.9</td><td>BP Balcatta</td><td>BP</td><td>53 Erindale Rd</td><td>BALCATTA</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>93.9</td><td>BP Beldon</td><td>BP</td><td>261 Eddystone Ave</td><td>BELDON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>93.9</td><td>BP Beeliar</td><td>BP</td><td>701 Beeliar Dr</td><td>COCKBURN CENTRAL</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>93.9</td><td>Vibe Toodyay Rd IGA XPress</td><td>Vibe</td><td>2086 Toodyay Rd</td><td>GIDGEGANNUP</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>93.9</td><td>BP Greenwood</td><td>BP</td><td>19 Coolibah Dr</td><td>GREENWOOD</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>93.9</td><td>BP Henley Brook</td><td>BP</td><td>1520 Gnangara Rd</td><td>HENLEY BROOK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>93.9</td><td>BP Mindarie</td><td>BP</td><td>360 Anchorage Dr N (Cnr Marmion Ave)</td><td>MINDARIE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>93.9</td><td>BP Mullaloo</td><td>BP</td><td>101 Dampier Av</td><td>MULLALOO</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>94.9</td><td>BP Attadale</td><td>BP</td><td>530 Canning Hwy (Cnr Hislop St)</td><td>ATTADALE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>94.9</td><td>BP Morley</td><td>BP</td><td>335 Walter Rd (Cnr Crimea St)</td><td>MORLEY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>94.9</td><td>BP Waikiki</td><td>BP</td><td>430 Safety Bay Rd (Cnr Malibu Rd)</td><td>SAFETY BAY</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>95</td><td>Shell Bullsbrook</td><td>Shell</td><td>2539 Great Northern Hwy</td><td>BULLSBROOK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>95.9</td><td>Kwikfuel Osborne Park</td><td>Kwikfuel</td><td>7 Hutton St</td><td>OSBORNE PARK</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>97.9</td><td>Serpentine Falls Roadhouse</td><td>Independent</td><td>2 Falls Rd (Cnr South Western Hwy)</td><td>SERPENTINE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>99.7</td><td>Puma Henderson OPT</td><td>Puma</td><td>81 Quill Way</td><td>HENDERSON</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>99.7</td><td>Puma High Wycombe</td><td>Puma</td><td>494 Kalamunda Rd</td><td>HIGH WYCOMBE</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>99.7</td><td>Puma Karragullen Motors</td><td>Puma</td><td>164 Brookton Hwy</td><td>KARRAGULLEN</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>99.7</td><td>Puma Kwinana OPT</td><td>Puma</td><td>Cnr Mandurah Rd & Beach St</td><td>KWINANA BEACH</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>99.8</td><td>BP Baldivis West</td><td>BP</td><td>1/909 Mandurah Rd</td><td>BALDIVIS</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>99.9</td><td>Hills Emporio</td><td>Independent</td><td>1615 Canning Rd</td><td>KARRAGULLEN</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>99.9</td><td>Tomeo's Service Station</td><td>BP</td><td>1287 Brookton Hwy</td><td>KARRAGULLEN</td>
</tr>
<tr class='today'><td>2020-04-14</td><td>99.9</td><td>Caltex StarMart Maddington</td><td>Caltex</td><td>18 Orchard Rd (Cnr Kelvin Rd)</td><td>MADDINGTON</td>
</tr>
</tbody>
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
'''



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
