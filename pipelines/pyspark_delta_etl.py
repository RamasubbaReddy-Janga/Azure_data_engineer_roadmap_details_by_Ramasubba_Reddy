# Production-Grade PySpark Delta Lake ETL Pipeline (Bronze to Silver)
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp, lit

# Initialize Spark Session with Delta support
spark = SparkSession.builder \
    .appName("BronzeToSilver_DeltaETL") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Paths
bronze_path = "abfss://bronze@staccount.dfs.core.windows.net/raw_sales/"
silver_path = "abfss://silver@staccount.dfs.core.windows.net/clean_sales/"

def process_bronze_to_silver():
    # 1. Read Raw Bronze Data
    df_bronze = spark.read.format("parquet").load(bronze_path)
    
    # 2. Cleanse and Transform
    df_cleaned = df_bronze \
        .dropDuplicates(["transaction_id"]) \
        .filter(col("amount") > 0) \
        .withColumn("processed_timestamp", current_timestamp()) \
        .withColumn("status", lit("VALID"))

    # 3. Write / Merge into Silver Delta Table
    df_cleaned.write \
        .format("delta") \
        .mode("append") \
        .option("mergeSchema", "true") \
        .save(silver_path)

    print("Bronze to Silver ETL completed successfully.")

if __name__ == "__main__":
    process_bronze_to_silver()
