# Databricks notebook source
# MAGIC %pip install databricks-mosaic

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

from pyspark.sql.functions import *
from mosaic import enable_mosaic
enable_mosaic(spark, dbutils)

# COMMAND ----------

from mosaic import st_point

lons = [-80., -80., -70., -70., -80.]
lats = [ 35.,  45.,  45.,  35.,  35.]

# COMMAND ----------

bounds_df = (
  spark
  .createDataFrame({"lon": lon, "lat": lat} for lon, lat in zip(lons, lats))
  .coalesce(1)
  .withColumn("point_geom", st_point("lon", "lat"))
)
bounds_df.show()

# COMMAND ----------

display(bounds_df)

# COMMAND ----------

query="SELECT * FROM public.borough_boundaries_geojson"

sqlText = """(SELECT ST_AsText(geometry),* FROM borough_boundaries_geojson ) as borough_boundaries_geojson"""

# COMMAND ----------

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://pgis_server_detail.postgres.database.azure.com:5432/postgres") \
    .option("dbtable", sqlText) \
    .option("user", "admin_user") \
    .option("password", "pgis_password") \
    .option("driver", "org.postgresql.Driver") \
    .load()

# COMMAND ----------

df.createOrReplaceTempView("df")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from df

# COMMAND ----------

