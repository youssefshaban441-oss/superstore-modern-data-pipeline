select distinct
    {{ dbt_utils.generate_surrogate_key(['segment']) }} as segment_key,
    segment
from {{ ref('stg_orders') }}
