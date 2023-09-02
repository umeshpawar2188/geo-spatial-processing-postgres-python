-- Index: idx_borough_boundaries_geojson_geometry

-- DROP INDEX IF EXISTS public.idx_borough_boundaries_geojson_geometry;

CREATE INDEX IF NOT EXISTS idx_borough_boundaries_geojson_geometry
    ON public.borough_boundaries_geojson USING gist
    (geometry)
    TABLESPACE pg_default;
