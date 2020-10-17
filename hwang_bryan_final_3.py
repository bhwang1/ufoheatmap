file = open('hwang_bryan_latlon.txt', 'r')

map = open('hwang_bryan.html', 'w')
map.write("""
<html>
  <head>
    <script src="https://api.mqcdn.com/sdk/mapquest-js/v1.3.2/mapquest.js"></script>
    <link type="text/css" rel="stylesheet" href="https://api.mqcdn.com/sdk/mapquest-js/v1.3.2/mapquest.css"/>
    <script src="https://leaflet.github.io/Leaflet.heat/dist/leaflet-heat.js"></script>
    <script src="hwang_bryan.js"></script>
    <script type="text/javascript">
      window.onload = function() {
        L.mapquest.key = 'x5yDN0jlWSLU43Ggm9Yj2YHAuQbAfCTb';
        var baseLayer = L.mapquest.tileLayer('map');
        var map = L.mapquest.map('map', {
          center: [39.83, -98.58],
          layers: baseLayer,
          zoom: 4
        });
        addressPoints = addressPoints.map(function (addressPoint) { return [addressPoint[0], addressPoint[1]]; });
        L.heatLayer(addressPoints).addTo(map);
      }
    </script>
  </head>
  <body style="border: 0; margin: 0;">
    <div id="map" style="width: 100%; height: 530px;"></div>
  </body>
</html>""")


addressPoints = []
for x in file:
	line = file.readline()
	new = line.split("\t")
	coords = new[0]
	loc = coords.split(",")
	lat = float(loc[0])
	lon = float(loc[1])
	tally = new[1].replace("\n", "")
	listy = [lat, lon, tally]
	addressPoints.append(listy)

data = open('hwang_bryan.js', 'w')
data.write("")
data.close
data = open('hwang_bryan.js', 'a')
data.write("var addressPoints = [")
for x in addressPoints:
	data.write("[%f,%f,%s]" % (x[0], x[1], x[2]))
	data.write(",")
data.write("];")
data.close()
map.close()
file.close()

