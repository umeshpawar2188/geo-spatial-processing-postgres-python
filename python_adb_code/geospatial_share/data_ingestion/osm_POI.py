# Databricks notebook source
from operator import index
import geopandas
from sqlalchemy import create_engine


# COMMAND ----------

# Set up database connection engine
engine = create_engine('postgresql://admin_user:pgis_password@pgis_server_detail.postgres.database.azure.com:5432/postgres')


# COMMAND ----------

data_root_path="C:\\Users\\home_directory\\OneDrive - Microsoft\\Documents\\MSFT\\Customer\Met_Police\\data"

# COMMAND ----------

# Load data into GeoDataFrame, e.g. from geo json files
gis_osm_pois_shape = geopandas.read_file(data_root_path+"\\new-york-latest-free.shp\\gis_osm_pois_a_free_1.shp")

# COMMAND ----------

gis_osm_pois_shape.head()

# COMMAND ----------

# GeoDataFrame to PostGIS
gis_osm_pois_shape.to_postgis(
    con=engine,
    name="gis_osm_pois_shape",
    if_exists="replace",
    index=True
)

# COMMAND ----------

# Close database connection
engine.dispose()

# COMMAND ----------

