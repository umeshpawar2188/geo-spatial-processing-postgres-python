SELECT index, boro_code, boro_name, shape_area, shape_leng, ST_Area(geometry),ST_Length(geometry::geography) AS length_in_meters
	FROM public."Bborough_boundaries_geojson";
	
SELECT boro_code, boro_name, shape_area, shape_leng, ST_Area(geometry),ST_Length(geometry::geography) AS length_in_meters
	FROM public."borough_boundaries_shape";
	
-- Views

CREATE OR REPLACE VIEW public.vw_borough_boundries
 AS
 SELECT boro_code, boro_name, shape_area, shape_leng, ST_Area(geometry),ST_Length(geometry::geography) AS length_in_meters
	FROM public."borough_boundaries_shape";

select * from public.vw_borough_boundries;

-- Working with Times/Dates/Parsing Timestamps into D/M/Y/Hour columns

select * from df_call_service_data limit 100;

select  "ARRIVD_TS", 
extract(hour from  to_timestamp("ARRIVD_TS", 'MM/DD/YYYY HH24:MI:SS')) as hours,
to_timestamp("ARRIVD_TS", 'MM/DD/YYYY HH24') date_time,
extract(hour from timestamp '2001-02-16 20:38:40')  
from df_call_service_data limit 100;

select "ARRIVD_TS",extract(hour from  "ARRIVD_TS") as hours from  df_call_service_data_dtypes limit 100;

-- Coordinate/Spatial Reference ID (transforming geom between projected and lat long)

SELECT ST_AsText(geometry) FROM public."borough_boundaries_geojson";

SELECT ST_MakePoint(-70.233231321, 40.12324213)

--===Measurements (calculating length, area, perimeter and specifying units - i.e. feet, metres, miles)
SELECT shape_area,
	ST_Area(ST_Transform(geometry, 2249)) As sqm,
	ST_Area(ST_Transform(geometry, 2249))/ 0.3048 ^ 2 sqft,
	ST_Length(ST_Transform(geometry, 2249)) AS length_in_meters
FROM public."borough_boundaries_geojson";

-- more examples- https://postgis.net/docs/en/ST_Area.html

--Distance:

select ST_Perimeter(geometry) from  geodata_census_json limit 100

--distance in meters (eucliean)
SELECT ST_Distance(
           ST_SetSRID(ST_MakePoint(51.51668, -0.17674), 4326)::geography ,  -- First point (x1, y1)
           ST_SetSRID(ST_MakePoint(51.50111, -0.19332), 4326)::geography    -- Second point (x2, y2)
       ) AS euclidean_distance;

--distance in meters

SELECT ST_Distance(
           ST_MakePoint(51.51668, -0.17674)::geography ,  -- First point (x1, y1)
           ST_MakePoint(51.50111, -0.19332)::geography    -- Second point (x2, y2)
       ) AS euclidean_distance;
	


---- == You can cross join all points to all polygons to measure distances and create shortest lines: 
--https://gis.stackexchange.com/questions/449104/calculate-the-distance-between-a-single-point-and-multiple-polygons-using-postgi#:~:text=You%20can%20cross%20join%20all%20points%20to%20all,geom%20from%20public.pointtable%20pnt%20cross%20join%20public.polygontable%20poly

select  pnt.id as pointid, 
        poly.id as polyid,
        st_distance(pnt.geom, poly.geom) as distance, 
        st_shortestline(pnt.geom, poly.geom) as geom
from public.pointtable pnt
cross join public.polygontable poly
--There's a line from each point to all polygons, 2581*65=167765 lines.



SELECT ST_Distance(
           ST_MakePoint(-73.73083868899994, 40.662964620000025)::geography ,  -- First point (x1, y1)
           ST_MakePoint(-73.7627949, 42.6482684)::geography    -- Second point (x2, y2)
       ) AS euclidean_distance;
