with dates as (

    select order_date as date_value
    from {{ ref('stg_orders') }}

    union

    select ship_date as date_value
    from {{ ref('stg_orders') }}

)

select
    {{ dbt_utils.generate_surrogate_key(['date_value']) }} as date_key,
    date_value as date,
    year(date_value) as year,
    quarter(date_value) as quarter,
    month(date_value) as month,
    monthname(date_value) as month_name,
    day(date_value) as day

from dates

where date_value is not null
