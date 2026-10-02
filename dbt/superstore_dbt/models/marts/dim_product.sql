select distinct

    {{ dbt_utils.generate_surrogate_key([
        'product_id',
        'product_name',
        'category',
        'sub_category'
    ]) }} as product_key,

    product_id,
    product_name,
    category,
    sub_category

from {{ ref('stg_orders') }}