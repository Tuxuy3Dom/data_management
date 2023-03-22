# Import the pandas library
import pandas as pd
# Import the folium library
import folium
# Import the json library
import json
 
# Import information
# https://www.python-graph-gallery.com/312-add-markers-on-folium-map

# open .json file
with open('world.json', encoding='utf-8') as world:
    world = json.load(world)

# Read .txt file
data = pd.read_csv('Volcanoes.txt')

my_location = [50.05, 21.95]

# Show location open street map
map = folium.Map(location = my_location, tiles="OpenStreetMap", zoom_start = 4)

# Change type in list
lat = list(data["LAT"])
lot = list(data["LON"])
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

# Function show map points in Marker
def map_show_marker(lt, ln, el, nm):
    map.add_child(folium.Marker(location = [lt, ln], tooltip = nm, popup = popup, 
                                icon = folium.Icon(color = set_color(el))))

# Function show map points in Circle Marker
def map_show_circleMarker(lt, ln, el, nm):
    map.add_child(folium.CircleMarker(location = [lt, ln], radius = 10, tooltip = nm, popup = popup, fill_color = set_color(el), fill_opacity=0.7,
                                icon = folium.Icon(color = set_color(el))))

# Loop in create points locations on the Steet Open Map and change HTML text in map
for lt, ln, el, nm in zip(lat, lot, elev, name):
    html=f"""
        <h2> Imię wulkanu: "{nm}"<h2>
        <p> Informacja dodatkowa: {el} m. </p>
        """
    iframe = folium.IFrame(html=html, width=200, height=200)
    popup = folium.Popup(iframe, max_width=2650)
    map_show_marker(lt, ln, el, nm)
    # map_show_circleMarker(lt, ln, el, nm)

# Save google open street map in format .html
map.save("labTwo.html")
map
