import folium 

map = folium.Map(location = [50.04901660881584, 21.98171232724226], )

map.save("task01.html")

map.add_child(
    folium.Marker(
        location = [50.05, 21.98],
        popus = "To jest nasz pierwszy marker",
        icon = 
    )
)