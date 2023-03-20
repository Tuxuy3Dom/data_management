# Import the pandas library
import pandas as pd
# Import the folium library
import folium
 
# Przydatna informacja
# https://www.python-graph-gallery.com/312-add-markers-on-folium-map

data = pd.read_csv('Volcanoes.txt')

map = folium.Map(location = [50.05, 21.95],tiles="OpenStreetMap", zoom_start = 4)

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

for lt, ln, el, nm in zip(lat, lot, elev, name):
    html=f"""
        <h2> Imię wulkanu: "{nm}"<h2>
        <p> Informacja dodatkowa: {el} m. </p>
        """
    iframe = folium.IFrame(html=html, width=200, height=200)
    popup = folium.Popup(iframe, max_width=2650)
    map.add_child(folium.Marker(location = [lt, ln], tooltip = nm, popup = popup, 
                                icon = folium.Icon(color = set_color(el))))

map.save("labTwo.html")
map
