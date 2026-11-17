# Modern Azure Data Engineering Roadmap & Architecture Hub

Welcome to the centralized, deduplicated, and modernized Azure Data Engineering repository. This repository consolidates industry-standard best practices from top data engineering handbooks, roadmaps, and real-world project portfolios, strictly filtering out deprecated technologies (ADF v1, ADLS Gen1, HDInsight) in favor of the modern cloud-scale stack.

## 🚀 Core Technology Stack
* **Storage & Compute**: Azure Data Lake Storage Gen2 (ADLS Gen2), Microsoft Fabric OneLake, Delta Lake.
* **Orchestration**: Azure Data Factory (ADF v2), Databricks Workflows.
* **Processing & Analytics**: Azure Databricks (Spark, Unity Catalog, Delta Live Tables), Azure Synapse Analytics / Fabric Warehouse.
* **Data Modeling & Transformation**: dbt (data build tool), PySpark, T-SQL.

---

## 📂 Directory Overview
* [`/concepts`](./concepts): Architectural blueprints, medallion architecture (Bronze, Silver, Gold), and governance standards.
* [`/pipelines`](./pipelines): Reusable ADF orchestration templates and PySpark / Delta Live Table ETL scripts.
* [`/optimization`](./optimization): Performance tuning guides, Z-ordering, VACUUM strategies, and cluster sizing for cost efficiency.

