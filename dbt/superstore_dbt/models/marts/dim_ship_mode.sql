select distinct
    {{ dbt_utils.generate_surrogate_key(['ship_mode']) }} as ship_mode_key,
    ship_mode
from {{ ref('stg_orders') }}