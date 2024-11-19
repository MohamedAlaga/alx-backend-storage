select
    band_name,
    (COALESCE(split, 2022) - formed) as lifspan
from
    metal_bands
where
    style like '%Glam rock%'
order by
    lifspan desc;
