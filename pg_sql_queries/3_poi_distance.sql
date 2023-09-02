-- ==(a) for each POI, calculate the distance to the nearest shooting incident 
-- (b) summarise/aggregate for each type of POI (i.e., banks, atms etc) statistics showing the min/max/mean/median distance to a shooting incident; 
-- and the total number of shootings that are within 100m, 200m, 300m of the POI group 
-- (then access table data in PowerBI)



--with index distance cross join-
-- time taken: 
create table pois_with_shooting_distance as (
select * from (
select  pois.osm_id as osm_id, 
        shooting_points.incident_key as incident_key,
        st_distance((pois.geometry::geography), (shooting_points.geometry::geography)) as distance
        --st_shortestline((pois.geometry::geography), (shooting_points.geometry::geography)) as geom
				,shooting_points.geometry as hooting_geom
		,pois.geometry as shooting_geom
,name
,shooting_points.boro
from public.gis_osm_pois_shape pois 
cross join public.geodata_nypd_shooting_json shooting_points
where st_distance((pois.geometry::geography), (shooting_points.geometry::geography)) <=500) a)

-- median/max/min/avg and grouping as per distance
select poi_type,count(*) as total_incidents,min(distance),max(distance),AVG(distance),
PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER BY distance) as median,
SUM(CASE WHEN distance <= 100 THEN 1 ELSE 0 END) AS within_100m,
SUM(CASE WHEN distance <=200 THEN 1 ELSE 0 END) AS within_200m,
SUM(CASE WHEN distance <=300 THEN 1 ELSE 0 END) AS within_300m
from pois_with_shooting_distance
group by poi_type













---

select incident_key,latitude,longitude,ST_AsText(geometry),* from geodata_nypd_shooting_json where incident_key='57342204' limit 100

select incident_key,latitude,longitude,ST_AsText(geometry),* from geodata_nypd_shooting_json limit 100
select  fclass, osm_id,ST_AsText(geometry) from gis_osm_pois_shape where fclass='library' limit 100

select * from geodata_nypd_shooting_json limit 100 --27312
select count(*) from gis_osm_pois_shape --135860

SELECT ST_Distance(
           ST_MakePoint(-73.73083868899994 40.662964620000025)::geography ,  -- First point (x1, y1)
           ST_MakePoint(-73.7627949 42.6482684)::geography    -- Second point (x2, y2)
       ) AS euclidean_distance;

select ST_Distance(ST_MakePoint(51.51668, -0.17674)::geography, geometry::geography) from gis_osm_pois_shape limit 100


select poi_type,
SUM(CASE WHEN distance <= 100 THEN 1 ELSE 0 END) AS within_100m,
SUM(CASE WHEN distance <=200 THEN 1 ELSE 0 END) AS within_200m,
SUM(CASE WHEN distance <=300 THEN 1 ELSE 0 END) AS within_300m
from pois_with_shooting_distance
where poi_type='bookshop'
group by poi_type


ALTER TABLE pois_with_shooting_distance
ADD COLUMN poi_type text;


UPDATE pois_with_shooting_distance
SET poi_type = gis_osm_pois_shape.fclass
FROM gis_osm_pois_shape
WHERE pois_with_shooting_distance.osm_id = gis_osm_pois_shape.osm_id;

select * from gis_osm_pois_shape
--sample
select  pnt.id as pointid, 
        poly.id as polyid,
        st_distance(pnt.geom, poly.geom) as distance, 
        st_shortestline(pnt.geom, poly.geom) as geom
from public.pointtable pnt
cross join public.polygontable poly
