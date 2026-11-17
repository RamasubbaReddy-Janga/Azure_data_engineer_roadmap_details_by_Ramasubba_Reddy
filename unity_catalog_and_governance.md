# Azure Databricks Unity Catalog & Data Governance

Unity Catalog provides centralized access control, auditing, lineage, and data discovery across Azure Databricks workspaces.

## Key Features
* **Three-Tier Namespace**: `catalog.schema.table` structure providing fine-grained access control down to row and column levels.
* **Automatic Lineage**: Captures runtime table-to-table and column-to-column lineage automatically for compliance and impact analysis.
* **External Locations**: Securely connects Databricks storage containers in ADLS Gen2 to external catalogs without exposing storage account keys directly to end-users.
