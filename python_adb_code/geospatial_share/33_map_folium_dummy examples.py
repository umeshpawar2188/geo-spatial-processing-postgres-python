# Databricks notebook source
# MAGIC %pip install folium

# COMMAND ----------

import folium
from IPython.display import display

# Create a folium map centered at New York City
nyc_coords = (40.7128, -74.0060)
m = folium.Map(location=nyc_coords, zoom_start=10)

# Add markers for points
folium.Marker(location=(40.759011, -73.984472), popup="Times Square").add_to(m)
folium.Marker(location=(40.697403, -73.979681), popup="Brooklyn Bridge").add_to(m)

# Add a line
line_coords = [(40.759011, -73.984472), (40.697403, -73.979681)]
folium.PolyLine(locations=line_coords, color='blue', weight=5).add_to(m)

# Define coordinates for a polygon
polygon_coords = [[
    (40.748817, -73.985428),
    (40.48817, -73.81428),
    (40.75817, -73.981428),
    (40.745817, -73.85428)
],
                  [
    (30.748817, -83.985428),
    (30.48817, -83.81428),
    (30.75817, -83.981428),
    (30.745817, -83.85428)
]
                  ]

# Add a polygon
#folium.Polygon(locations=polygon_coords, color='green', fill=True, fill_color='green').add_to(m)
# Add markers for each point
for polygon_coords in polygon_coords:
    folium.Polygon(locations=polygon_coords, color='red', fill=True, fill_color='red').add_to(m)


# Display the map
display(m)


# COMMAND ----------

import folium
from shapely.wkt import loads

# Define the MULTILINESTRING geometry in WKT format
multiline_wkt = "MULTILINESTRING ((-74.01428922948978 40.70454907535256, -74.01437031212745 40.70455803784475, -74.01451712300867 40.704605675392386, -74.01466709872304 40.70464721296995, -74.01478059501136 40.704674113029824, -74.01489542085365 40.70469751835281, -74.014961252156 40.70475979724394))"

# Convert the WKT to a Shapely geometry
multiline = loads(multiline_wkt)

linestring=ST_LineMerge(multiline_wkt:geometry)

print(linestring)

# COMMAND ----------

import folium
from shapely.wkt import loads

# Define the MULTILINESTRING geometry in WKT format
multiline_wkt = "MULTILINESTRING ((-74.01428922948978 40.70454907535256, -74.01437031212745 40.70455803784475, -74.01451712300867 40.704605675392386, -74.01466709872304 40.70464721296995, -74.01478059501136 40.704674113029824, -74.01489542085365 40.70469751835281, -74.014961252156 40.70475979724394))"

# Convert the WKT to a Shapely geometry
multiline = loads(multiline_wkt)

linestring=ST_LineMerge(multiline_wkt::geometry)

print(linestring)
# Create a Folium map centered at a specific location
m = folium.Map(location=[40.70454907535256, -74.01428922948978], zoom_start=15)

# Iterate through the LineStrings within the MULTILINESTRING
#for line in multiline:
    # Extract coordinates from the LineString
coordinates = list(multiline.coords)
print(coordinates)    
    # Create a PolyLine on the Folium map
folium.PolyLine(locations=coordinates, color='blue', weight=5).add_to(m)

# Display the map
m.save("multiline_map.html")


# COMMAND ----------




# Create a map centered at a specific location
m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

# Iterate through geometry texts and add lines to the map
for geometry_text in geometry_texts:
    geometry = wkt.loads(geometry_text[0])  # Convert WKT text to Shapely geometry object
    coordinates = list(geometry.coords)
    
    # Create a polyline and add it to the map
    folium.PolyLine(locations=coordinates, color='blue').add_to(m)

# Save the map to an HTML file
m.save('geometry_lines_map.html')


# COMMAND ----------

geometry_text = "0105000020E610000001000000010200000007000000FE555F1DEA8052C07C8802AA2E5A4440BA277571EB8052C0AC5631F52E5A444079233AD9ED8052C07231CE84305A4440EE55454EF08052C035763FE1315A44401C0C4F2AF28052C084E6E6C2325A44404D5BEC0BF48052C0E7723D87335A4440E72D0A20F58052C06259AC91355A4440"


# COMMAND ----------

# Create a map centered at a specific location
m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)


# COMMAND ----------

geometry = wkt.loads(geometry_text)  # Convert WKT text to Shapely geometry object
coordinates = list(geometry.coords)

# COMMAND ----------

wkt_text = "LINESTRING (0 0, 1 1, 2 2, 3 3)"

# Convert WKT text to Shapely geometry object
geometry = wkt.loads(wkt_text)

# COMMAND ----------

wkt_text = "MULTILINESTRING ((-74.01428922948978 40.70454907535256, -74.01437031212745 40.70455803784475, -74.01451712300867 40.704605675392386, -74.01466709872304 40.70464721296995, -74.01478059501136 40.704674113029824, -74.01489542085365 40.70469751835281, -74.014961252156 40.70475979724394))"

# COMMAND ----------

geometry = wkt.loads(wkt_text)  # Convert WKT text to Shapely geometry object
coordinates = list(geometry.coords)

# COMMAND ----------

coordinates = list(geometry.coords)

# COMMAND ----------

folium.PolyLine(locations=coordinates, color='green').add_to(m)

# COMMAND ----------

display(m)