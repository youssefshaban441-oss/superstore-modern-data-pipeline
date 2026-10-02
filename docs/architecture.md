# Architecture

```mermaid
flowchart TD
    A[Superstore CSV] --> B[Python Loader]
    B --> C[DuckDB ODS]
    C --> D[dbt Staging]
    D --> E[dbt Marts]
    E --> F[6 Dimensions]
    E --> G[Fact Order Line]
    F --> H[Star Schema]
    G --> H
    H --> I[dbt Tests]

    J[Apache Airflow] -. orchestrates .-> B
    J -. orchestrates .-> D
    J -. orchestrates .-> E
    J -. orchestrates .-> I