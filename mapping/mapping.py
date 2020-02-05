import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])

maps = folium.Map(location=[36.1699, -115.1398], zoom_start=5, tiles= "stamen terrain")
fg=folium.FeatureGroup(name="my map")

for lt, ln, n in zip(lat, lon, name):
    fg.add_child(folium.Marker(location=[lt, ln], popup= "hi i am a marker!", icon=folium.Icon(colour="green"), tooltip=n))

maps.add_child(fg)

maps.save("mapping.html")
