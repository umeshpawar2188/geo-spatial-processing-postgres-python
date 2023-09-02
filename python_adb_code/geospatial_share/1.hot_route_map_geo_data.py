# Databricks notebook source
import subprocess

# List of package names you want to install
package_names = ["databricks-mosaic", "folium", "geopandas"]

# Use subprocess to run the pip install command for each package
for package_name in package_names:
    try:
        subprocess.check_call(["pip", "install", package_name])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")


# COMMAND ----------

from mosaic import enable_mosaic
enable_mosaic(spark, dbutils)
import folium
from IPython.display import display
import geopandas as gpd
from shapely import wkt
from branca.colormap import linear
import numpy as np

# COMMAND ----------

url = ("jdbc:postgresql://metpoliceflexserver.postgres.database.azure.com:5432/postgres"+ 
    "?tcpKeepAlive=true&prepareThreshold=-1&binaryTransfer=true&defaultRowFetchSize=10000")

sqlText = """(SELECT *,ST_AsText(point_geom) as point_g,ST_AsText(line_geom) as line_g,ST_AsText(ST_LineMerge(line_geom)) as merged_line FROM tbl_line_vs_shooting_point ) as tbl_line_vs_shooting_point"""

sqlText_2 = """(SELECT *,ST_AsText(point_geom) as point_g,ST_AsText(line_geom) as line_g,ST_AsText(ST_LineMerge(line_geom)) as merged_line FROM tbl_line_vs_shooting_point where st_name='ADAM CLAYTON POWELL JR' ) as tbl_line_vs_shooting_point"""

df = spark.read.format("jdbc").option("url", url).option("dbtable",sqlText).option("user", "admin_user").option("password", "Qwerty123").load()
df.createOrReplaceTempView("df")


# COMMAND ----------

# Convert Spark DataFrame to Pandas DataFrame and see sample data
pandas_df = df.toPandas()
pandas_df.head(5)

# COMMAND ----------

# count number of crime incidents per street or line geometry
counts_by_seg = pandas_df.groupby(['merged_line','incident_key']).size().reset_index(name='count')
counts_by_seg

# COMMAND ----------

# select records where number of incidents is more than 1
counts_by_seg2 = counts_by_seg[counts_by_seg['count'] > 1]
counts_by_seg2

# COMMAND ----------

# summary/ distribution of data
summary_stats = counts_by_seg2['count'].describe()
print(summary_stats)

# COMMAND ----------

# Create a color palette
color_palette = linear.Reds_03.scale(0, 9)
color_palette.caption = 'crime_incidents'

# COMMAND ----------

# Create a map using the CartoDB.DarkMatter tiles 40.7128, -74.0060
m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

# COMMAND ----------

# Add LineStrings to the map
for _, row in counts_by_seg2.iterrows():
    line_coords = row["merged_line"]
    wkt_line=wkt.loads(line_coords)
    line_coords=list(wkt_line.coords)
    reversed_coordinates = [(lat, lon) for lon, lat in line_coords]
    folium.PolyLine(locations=reversed_coordinates, color=color_palette(row['count']),opacity=1, weight=5).add_to(m)

# COMMAND ----------

display(m)

# COMMAND ----------

m.save('/dbfs/mnt/map_with_st_ADAM_CLAYTON_POWELL_JR.html')
