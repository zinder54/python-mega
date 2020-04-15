import folium
import pandas

data = pandas.read_csv("volcanoes.txt")#reads the txt file into a variable
lat = list(data["LAT"]) #extracts latitude column from txt file
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def colourProducer(elevation): ##creates a function to change colour of markers
    if elevation < 1000:##      in relation to the elevation of the valcanoe
        return 'blue'
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

maps = folium.Map(location=[36.1699, -115.1398], zoom_start=5, tiles= "stamen terrain")#creates the map and points to location
# adds a certain tile and how much to zoom in to said location
fgv=folium.FeatureGroup(name="valcanoes") ##creates the markers/layers on the map

for lt, ln, n, el in zip(lat, lon, name, elev): ##creates a 'for' loop for the markers and what to display
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup= str(el) + 'm',
    color=colourProducer(el), fill=True,fill_opacity=0.7, tooltip=n, ))
#^^ adds a child group to format the markers, and what they display. colour points to the function above
#tooltip makes it so when cursor hovers over the markers the information will be produced.

fgp=folium.FeatureGroup(name='population')
##^^creates a layer on top of the map to do with population

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor': 'green' if x ['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
##extracts the data from the json file then reads from pop column and corresponds
#then corresponds amount with a colour to produce over the map

maps.add_child(fgv) ##adds the child paramter to maps
maps.add_child(fgp)
maps.add_child(folium.LayerControl())##adds a button and list to turn on the certain layers from above

maps.save("mapping.html")
