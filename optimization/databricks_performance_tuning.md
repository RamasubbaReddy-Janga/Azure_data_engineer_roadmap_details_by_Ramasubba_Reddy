# Azure Databricks & Delta Lake Performance Optimization Guide

## 1. Storage Optimization (Z-Ordering & Vacuum)
* **OPTIMIZE**: Compacts small files into optimal 1GB files to avoid the "small file problem" and reduce metadata overhead.
  ```sql
  OPTIMIZE delta.`abfss://silver@staccount.dfs.core.windows.net/clean_sales/`
  ZORDER BY (customer_id, transaction_date);
