import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])

<<<<<<< HEAD
maps = folium.Map(location=[48.1118011,-121.1110001], zoom_start=15, tiles= "stamen terrain")
fg=folium.FeatureGroup(name="my map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup= "yo i am a marker!", icon=folium.Icon(colour="green")))

=======
maps = folium.Map(location=[36.1699, -115.1398], zoom_start=5, tiles= "stamen terrain")
fg=folium.FeatureGroup(name="my map")

for lt, ln, n in zip(lat, lon, name):
    fg.add_child(folium.Marker(location=[lt, ln], popup= "hi i am a marker!", icon=folium.Icon(colour="green"), tooltip=n))
>>>>>>> f7b6a724681c5c3f80dbcd85b20a3a556f27347c

maps.add_child(fg)

maps.save("map1.html")
