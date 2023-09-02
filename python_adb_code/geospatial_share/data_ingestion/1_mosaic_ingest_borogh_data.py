# Databricks notebook source
# MAGIC %md ## Package installation

# COMMAND ----------

# MAGIC %run ../install_packages

# COMMAND ----------

# MAGIC %md ## Required imports

# COMMAND ----------

from mosaic import enable_mosaic
enable_mosaic(spark, dbutils)
from pyspark.sql.functions import explode, col,to_json
import mosaic as mos

# COMMAND ----------

# MAGIC %md ## Postgress engine server details

# COMMAND ----------

# Set up database connection engine
postgress_url='postgresql://admin_user:pgis_password@pgis_server_detail.postgres.database.azure.com:5432/postgres'


# COMMAND ----------

# MAGIC %md ##data path

# COMMAND ----------

borough_path="abfss://geo-spatial@westukunitystorage.dfs.core.windows.net/raw/data/Borough Boundaries.geojson"

# COMMAND ----------

borogh_df = (
  spark.read
    .option("multiline", "true")
    .format("json")
    .load(borough_path)
    .select("type", explode(col("features")).alias("feature"))
    .select("type", col("feature.properties").alias("properties"), to_json(col("feature.geometry")).alias("json_geometry"))
    .withColumn("geometry", mos.st_aswkt(mos.st_geomfromgeojson("json_geometry")))
    .select(
    "*",
    col("properties.boro_code").alias("boro_code"),
    col("properties.boro_name").alias("boro_name"),
    col("properties.shape_area").alias("shape_area"),
    col("properties.shape_leng").alias("shape_leng")
).drop (col("properties"))
)

# COMMAND ----------

# MAGIC %md ## PostGIS details

# COMMAND ----------

table_name="borogh_json_spark"

# COMMAND ----------

borogh_df.write.option('driver', 'org.postgresql.Driver').jdbc(postgress_url, table, mode, properties)

# COMMAND ----------

jdbc_url = "jdbc:postgresql://pgis_server_detail.postgres.database.azure.com:5432/postgres"
connection_properties = {
    "user": "admin_user",
    "password": "pgis_password",
    "driver": "org.postgresql.Driver"
}

# COMMAND ----------

borogh_df.write.jdbc(url=jdbc_url, table="target_table", mode="overwrite", properties=connection_properties)


# COMMAND ----------

mos.