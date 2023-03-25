# Import the pandas library
import pandas as pd
# Import the folium library
import folium

# Import information
# https://www.python-graph-gallery.com/312-add-markers-on-folium-map

# Read .txt file
data = pd.read_csv('Volcanoes.txt')

# load .json file
geojson_data = open('world.json').read()

my_location = [50.05, 21.95]
mapa = folium.Map(location = my_location, tiles="Stamen Terrain", zoom_start = 4)

# Change type in list
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

# Function change color in points for heigth volcans
def set_color(elev):
    if elev < 2000:
        return "green"
    elif elev < 3000:
        return "orange"
    else: 
        return "red"

marker_layer = folium.FeatureGroup(name='Markers')
# Function show map points in Marker
def map_show_marker(lt, ln, el, nm):
    folium.Marker(location = [lt, ln], tooltip = nm, popup = popup, 
                                icon = folium.Icon(color = set_color(el))).add_to(marker_layer)

circle_marker_layer = folium.FeatureGroup(name='Circle Markers')
# Function show map points in Circle Marker
def map_show_circleMarker(lt, ln, el, nm):
    folium.CircleMarker(location = [lt, ln], radius = 10, tooltip = nm, popup = popup, fill_color = set_color(el), fill_opacity=0.7,
                                icon = folium.Icon(color = set_color(el))).add_to(circle_marker_layer)
    
# Loop in create circleMarker points on Map and change HTML text in Map
for lt, ln, el, nm in zip(lat, lon, elev, name):
    html=f"""
        <h2> Imię wulkanu: "{nm}"<h2>
        <p> Informacja dodatkowa: {el} m. </p>
        """
    iframe = folium.IFrame(html=html, width=200, height=200)
    popup = folium.Popup(iframe, max_width=2650)
    map_show_circleMarker(lt, ln, el, nm) 
circle_marker_layer.add_to(mapa)

# Loop in create marker points on Map and change HTML text in Map
for lt, ln, el, nm in zip(lat, lon, elev, name):
    html=f"""
        <h2> Imię wulkanu: "{nm}"<h2>
        <p> Informacja dodatkowa: {el} m. </p>
        """
    iframe = folium.IFrame(html=html, width=200, height=200)
    popup = folium.Popup(iframe, max_width=2650)
    map_show_marker(lt, ln, el, nm)
marker_layer.add_to(mapa)   

# create object LayerControl
layer_control = folium.LayerControl()

# Function style fill_color in maps
def style_function(feature):
    pop = feature['properties']['POP2005']
    if pop < 10000000:
        return {'fillColor': 'green'}
    elif pop < 20000000:
        return {'fillColor': 'yellow'}
    else:
        return {'fillColor': 'red'}

# create object FeatureGroup
polygon_layer = folium.FeatureGroup(name='Polygons')
geojson_layer = folium.FeatureGroup(name='geojson')

# add data to GeoJSON a layer
folium.GeoJson(data = geojson_data, style_function = style_function).add_to(polygon_layer)

# create a map and add a layer GeoJSON
polygon_layer.add_to(mapa)

folium.LayerControl(collapsed=False).add_to(mapa)

# Save google open street map in format .html
mapa.save("maps.html")
mapa





