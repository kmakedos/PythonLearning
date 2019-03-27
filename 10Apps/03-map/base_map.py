#!/usr/bin/env python3
import folium
import pandas
beaches = pandas.read_csv('thasos.beaches.txt')
map = folium.Map(location=[40.6, 24.5], zoom_start=9)
beaches.set_index('Title')
beach_titles = list(beaches['Title'])
beach_lon = list(beaches['Long'])
beach_lat = list(beaches['Lat'])

fg = folium.FeatureGroup('Thasos Beaches')
for title,lon,lat in zip(beach_titles, beach_lon, beach_lat):
    fg.add_child(folium.Marker(location=[lon,lat], popup=title,icon=folium.Icon(icon='bicycle')))
fg.add_child(folium.CircleMarker(location=[40.6, 24.5], radius = 20))



map.add_child(fg)
map.add_child(folium.ClickForMarker())
map.save("BaseMap.html")
