import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def colourProducer(elevation):
    if elevation < 1000:
        return 'blue'
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

maps = folium.Map(location=[36.1699, -115.1398], zoom_start=5, tiles= "stamen terrain")
fgv=folium.FeatureGroup(name="valcanoes")

for lt, ln, n, el in zip(lat, lon, name, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup= str(el) + 'm',
    color=colourProducer(el), fill=True,fill_opacity=0.7, tooltip=n, ))

fgp=folium.FeatureGroup(name='population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor': 'green' if x ['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

maps.add_child(fgv)
maps.add_child(fgp)
maps.add_child(folium.LayerControl())

maps.save("mapping.html")
