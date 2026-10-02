select
    {{ dbt_utils.generate_surrogate_key(['row_id']) }} as order_line_key,

    order_id,

    {{ dbt_utils.generate_surrogate_key(['customer_id']) }} as customer_key,

    {{ dbt_utils.generate_surrogate_key([
    'product_id',
    'product_name',
    'category',
    'sub_category'
]) }} as product_key,

    {{ dbt_utils.generate_surrogate_key([
        'country',
        'city',
        'state',
        'postal_code',
        'region'
    ]) }} as location_key,

    {{ dbt_utils.generate_surrogate_key(['order_date']) }} as order_date_key,

    {{ dbt_utils.generate_surrogate_key(['ship_date']) }} as ship_date_key,

    {{ dbt_utils.generate_surrogate_key(['ship_mode']) }} as ship_mode_key,

    {{ dbt_utils.generate_surrogate_key(['segment']) }} as segment_key,

    sales,
    quantity,
    discount,
    profit

from {{ ref('stg_orders') }}