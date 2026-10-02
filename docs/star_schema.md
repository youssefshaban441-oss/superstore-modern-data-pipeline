# Star Schema

```mermaid
erDiagram

    FACT_ORDER_LINE {
        string order_line_key PK
        string order_id
        string customer_key FK
        string product_key FK
        string location_key FK
        string order_date_key FK
        string ship_date_key FK
        string ship_mode_key FK
        string segment_key FK
        double sales
        int quantity
        double discount
        double profit
    }

    DIM_CUSTOMER {
        string customer_key PK
        string customer_id
        string customer_name
    }

    DIM_PRODUCT {
        string product_key PK
        string product_id
        string product_name
        string category
        string sub_category
    }

    DIM_LOCATION {
        string location_key PK
        string country
        string city
        string state
        int postal_code
        string region
    }

    DIM_DATE {
        string date_key PK
        date date
        int year
        int quarter
        int month
        string month_name
        int day
    }

    DIM_SHIP_MODE {
        string ship_mode_key PK
        string ship_mode
    }

    DIM_SEGMENT {
        string segment_key PK
        string segment
    }

    DIM_CUSTOMER ||--o{ FACT_ORDER_LINE : customer_key
    DIM_PRODUCT ||--o{ FACT_ORDER_LINE : product_key
    DIM_LOCATION ||--o{ FACT_ORDER_LINE : location_key
    DIM_DATE ||--o{ FACT_ORDER_LINE : order_date_key
    DIM_DATE ||--o{ FACT_ORDER_LINE : ship_date_key
    DIM_SHIP_MODE ||--o{ FACT_ORDER_LINE : ship_mode_key
    DIM_SEGMENT ||--o{ FACT_ORDER_LINE : segment_key