# Databricks notebook source
# MAGIC %md ## Required imports

# COMMAND ----------

from operator import index
import geopandas
from sqlalchemy import create_engine


# COMMAND ----------

# MAGIC %md ## Postgress engine server details

# COMMAND ----------

# Set up database connection engine
engine = create_engine('postgresql://admin_user:pgis_password@pgis_server_detail.postgres.database.azure.com:5432/postgres')


# COMMAND ----------

# MAGIC %md ##data path

# COMMAND ----------

data_root_path="C:\\Users\\home_directory\\OneDrive - Microsoft\\Documents\\MSFT\\Customer\\Met_Police\\data"

# COMMAND ----------

# Load data into GeoDataFrame, e.g. from shapefile
geodata_boro_shape = geopandas.read_file(data_root_path+"\\Borough Boundaries\\geo_export_ab5fa879-26f3-467a-845a-9f4e5cba55d3.shp")


# COMMAND ----------

geodata_boro_shape.head()

# COMMAND ----------



# GeoDataFrame to PostGIS
geodata_boro_shape.to_postgis(
    con=engine,
    name="borough_boundaries_shape",
    if_exists="replace",
    index=False
)

# COMMAND ----------



# Load data into GeoDataFrame, e.g. from geo json files
geodata_boro_json = geopandas.read_file(data_root_path+"\\Borough Boundaries.geojson")

# COMMAND ----------

geodata_boro_json.head()

# COMMAND ----------



# GeoDataFrame to PostGIS
geodata_boro_json.to_postgis(
    con=engine,
    name="borough_boundaries_geojson",
    if_exists="replace",
    index=False
    
)



# COMMAND ----------


# Close database connection
engine.dispose()