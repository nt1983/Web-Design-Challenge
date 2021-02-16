import pandas as pd

html_nav="""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Web Visualization Dashboard (Latitude)</title>
  <link rel="stylesheet" href="reset.css">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
        <div class="navbar-header">
            <a class="navbar-brand" href="index.html">
                <span style="font-size:25px">Latitude</span>
            </a>
        </div>
        <div class="navbar-toggler" type="button" data-toggle="collapse" data-target="#mainNavBar">
            <span class="navbar-toggler-icon"></span>
        </div>
        <div class="collapse navbar-collapse" id="mainNavBar">
            <ul class="nav navbar-nav ml-auto">                        
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                    Plots
                    </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                        <a class="dropdown-item" href="max-temp.html">Max Temperature</a>
                        <a class="dropdown-item" href="humidity.html">Humidity</a>
                        <a class="dropdown-item" href="cloudiness.html">Cloudiness</a>
                        <a class="dropdown-item" href="windspeed.html">Wind Speed</a>
                    </div>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="comparison.html">Comparison</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="data.html">Data</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
<div class="table-responsive">
  <div class="col-sm-12 col-md-12" >
      <h2 class="text-left">Data</h2>
              <hr>
              <h4>The following table includes all of the data used for plotting during this project.</h4>
              """
html_end="""
</div>
</div>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</body>
</html>"""
city=pd.read_csv("Resources\cities.csv")
city=city.set_index('City_ID',drop=True)
print(city.head())
city_html=city.to_html(classes='table')
text_file = open("data.html", "w") 
text_file.write(html_nav) 
text_file.write(city_html) 
text_file.write(html_end)
text_file.close() 
