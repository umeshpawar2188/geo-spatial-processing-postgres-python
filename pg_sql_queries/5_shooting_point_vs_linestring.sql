

create table  tbl_line_vs_shooting_point as(
SELECT
ST_DWithin(p.geometry, l.geometry,0.0001) AS point_intersects_line,
ST_Distance(p.geometry, l.geometry) distance,
l.st_name,
p.boro,
l.geometry as line_geom,
p.geometry as point_geom,
	p.incident_key,
	l.r_blkfc_id
FROM
    geodata_nypd_shooting_json p
JOIN
    geodata_nyc_street_json l
ON
    ST_DWithin(p.geometry, l.geometry,0.0001));
	
select * from tbl_line_vs_shooting_point;


	









---
SELECT index, perp_sex, latitude, y_coord_cd, incident_key, loc_of_occur_desc, occur_time, perp_age_group, jurisdiction_code, loc_classfctn_desc, x_coord_cd, vic_sex, statistical_murder_flag, longitude, vic_race, location_desc, precinct, perp_race, boro, vic_age_group, occur_date, geometry
	FROM public.geodata_nypd_shooting_json;
	
	select ST_AsText(geometry) from geodata_nypd_shooting_json
	
	SELECT index, rw_type, l_low_hn, pre_direct, st_width, r_zip, r_low_hn, bike_lane, post_type, r_blkfc_id, bike_trafd, frm_lvl_co, post_modif, pre_type, full_stree, l_blkfc_id, shape_leng, to_lvl_co, modified, status, post_direc, r_high_hn, l_zip, segment_ty, snow_pri, borocode, trafdir, pre_modifi, st_label, physicalid, st_name, created, l_high_hn, geometry
	FROM public.geodata_nyc_street_json where st_name='BATTERY' limit 100
	
	select ST_AsText(geometry) from geodata_nyc_street_json

select ST_GeometryType(ST_LineMerge(geometry)) from geodata_nyc_street_json

SELECT distinct(ST_GeometryType(ST_AsText(ST_LineMerge(
    'MULTILINESTRING((0 0, 1 1), (1 1, 3 3))'::geometry)));

SELECT
    p.*,
    l.*,
    ST_Intersects(p.geometry, l.geometry) AS point_intersects_line
FROM
    geodata_nypd_shooting_json p
JOIN
    geodata_nyc_street_json l
ON
    ST_Intersects(p.geometry, l.geometry)
	and l.st_name='BATTERY'

select * from bettery_line