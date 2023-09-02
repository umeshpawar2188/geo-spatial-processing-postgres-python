# Databricks notebook source
# MAGIC %md ## Required imports

# COMMAND ----------

# MAGIC %run ../install_packages

# COMMAND ----------

from operator import index
import geopandas


# COMMAND ----------

from pyspark.sql.functions import *
import mosaic as mos
mos.enable_mosaic(spark, dbutils)

# COMMAND ----------

# MAGIC %md ## access gpkg

# COMMAND ----------

# MAGIC %md ##data path

# COMMAND ----------

gpkg_path="/dbfs/FileStore/geo_data/nyc_shootings_geopackageFormat.gpkg"

# COMMAND ----------

# Load data into GeoDataFrame, e.g. from shapefile
gpkg_df = geopandas.read_file(gpkg_path)


# COMMAND ----------

gpkg_df

# COMMAND ----------

# MAGIC %md ##access gdb

# COMMAND ----------

gdb_path="/dbfs/FileStore/geo_data/NYC_DoITT_Planimetric_OpenData.gdb"

# COMMAND ----------

# Load data into GeoDataFrame, e.g. from shapefile
gdb_df = geopandas.read_file(gdb_path)


# COMMAND ----------

gdb_df

# COMMAND ----------

# MAGIC %md ## Tab/mid

# COMMAND ----------

mid_tab_path="/dbfs/FileStore/geo_data/staten_island_shootings_MapInfoFormat"

# COMMAND ----------

# Load data into GeoDataFrame, e.g. from shapefile
mid_tab_df = geopandas.read_file(mid_tab_path)