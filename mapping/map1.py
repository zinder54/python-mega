import folium

maps = folium.Map(location=[44.6917992,-121.8010025], zoom_start=6, tiles= "stamen terrain")


maps.save("map.html")
