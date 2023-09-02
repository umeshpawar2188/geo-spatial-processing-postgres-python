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
geodata_police_json = geopandas.read_file(data_root_path+"\\Police Precincts.geojson")

# COMMAND ----------

geodata_police_json.head()

# COMMAND ----------

# GeoDataFrame to PostGIS
geodata_police_json.to_postgis(
    con=engine,
    name="police_precinct_geojson",
    if_exists="replace",
    index=True
)


# Close database connection
engine.dispose()

# COMMAND ----------

