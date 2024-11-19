select
    band_name,
    (COALESCE(split, 2022) - formed) as lifespan
from
    metal_bands
where
    style like '%Glam rock%'
order by
    lifespan desc;
