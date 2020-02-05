import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

maps = folium.Map(location=[48.1118011,-121.1110001], zoom_start=15, tiles= "stamen terrain")
fg=folium.FeatureGroup(name="my map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup= "yo i am a marker!", icon=folium.Icon(colour="green")))


maps.add_child(fg)

maps.save("map1.html")
