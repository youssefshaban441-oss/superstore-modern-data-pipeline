select distinct
    {{ dbt_utils.generate_surrogate_key([
        'country',
        'city',
        'state',
        'postal_code',
        'region'
    ]) }} as location_key,

    country,
    city,
    state,
    postal_code,
    region

from {{ ref('stg_orders') }}