# Databricks notebook source
# MAGIC %run ./install_packages

# COMMAND ----------

from mosaic import enable_mosaic
enable_mosaic(spark, dbutils)

# COMMAND ----------

url = ("jdbc:postgresql://<postgress server>.postgres.database.azure.com:5432/postgres"+ 
    "?tcpKeepAlive=true&prepareThreshold=-1&binaryTransfer=true&defaultRowFetchSize=10000")

sqlText = """(SELECT *,ST_AsText(point_geom) as point_g,ST_AsText(line_geom) as line_g,ST_AsText(ST_LineMerge(line_geom)) as merged_line FROM tbl_line_vs_shooting_point where st_name='ADAM CLAYTON POWELL JR' ) as tbl_line_vs_shooting_point"""

df = spark.read.format("jdbc").option("url", url).option("dbtable",sqlText).option("user", "<username>").option("password", "pgis_password").load()
df.createOrReplaceTempView("df")


# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*),st_name from df group by st_name

# COMMAND ----------

# Convert Spark DataFrame to Pandas DataFrame
pandas_df = df.toPandas()

# COMMAND ----------

pandas_df.head()

# COMMAND ----------

import folium
from IPython.display import display
import geopandas as gpd
from shapely import wkt

# COMMAND ----------

nyc_coords = (40.7128, -74.0060)
m = folium.Map(location=nyc_coords, zoom_start=12)

# COMMAND ----------

# Add LineStrings to the map
for _, row in pandas_df.iterrows():
    line_coords = row["merged_line"]
    wkt_line=wkt.loads(line_coords)
    line_coords=list(wkt_line.coords)
    reversed_coordinates = [(lat, lon) for lon, lat in line_coords]
    folium.PolyLine(locations=reversed_coordinates, color='red', weight=5).add_to(m)

# COMMAND ----------

# Add Points to the map
for _, row in pandas_df.iterrows():
    point_coords = row["point_g"]
    wkt_point=wkt.loads(point_coords)
    point_s=wkt_point.coords
    reversed_coordinates = tuple([(lat, lon) for lon, lat in point_s][0])
    #print(reversed_coordinates)
    folium.Marker(location=reversed_coordinates, popup=f"Point ID: {row['incident_key']}").add_to(m)

# COMMAND ----------

# MAGIC %fs 
# MAGIC
# MAGIC ls /mnt

# COMMAND ----------

m.save('/dbfs/mnt/map_with_st_ADAM_CLAYTON_POWELL_JR.html')

# COMMAND ----------

m.save('abfss://external-datalake@westukunitystorage.dfs.core.windows.net/map_with_geometries.html')

# COMMAND ----------

display(m)