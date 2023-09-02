# Databricks notebook source
from operator import index
import pandas as pd
from sqlalchemy import create_engine


# COMMAND ----------

# Set up database connection engine
engine = create_engine('postgresql://admin_user:pgis_password@pgis_server_detail.postgres.database.azure.com:5432/postgres')


# COMMAND ----------

data_root_path="C:\\Users\\home_directory\\OneDrive - Microsoft\\Documents\\MSFT\\Customer\Met_Police\\data"

# COMMAND ----------

df_call_service_data = pd.read_csv(data_root_path+"\\NYPD_Calls_for_Service__Year_to_Date_ (1).csv")


# COMMAND ----------

df_call_service_data.head()

# COMMAND ----------

# GeoDataFrame to PostGIS
df_call_service_data.to_sql(
    con=engine,
    name="df_call_service_data",
    if_exists="replace",
    index=True
)


# COMMAND ----------

# GeoDataFrame to PostGIS
df_call_service_data.to_sql(
    con=engine,
    name="df_call_service_data_dtypes",
    if_exists="append",
    index=True
)

# COMMAND ----------

# Close database connection
engine.dispose()

# COMMAND ----------

