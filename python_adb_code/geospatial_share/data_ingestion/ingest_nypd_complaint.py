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
geodata_nypd_complaint_shape = geopandas.read_file(data_root_path+"\\NYPD Complaint Data Current (Year To Date)\\geo_export_191937a4-897f-458c-8f0e-cceea154f421.shp")

# COMMAND ----------

geodata_nypd_complaint_shape.head()

# COMMAND ----------

# GeoDataFrame to PostGIS
geodata_nypd_complaint_shape.to_postgis(
    con=engine,
    name="geodata_nypd_complaint_shape",
    if_exists="replace",
    index=True
)

# COMMAND ----------

# Close database connection
engine.dispose()

# COMMAND ----------

