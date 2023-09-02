--Join the Census Block codes to a point dataset, summarise and aggregate for each census block and crime type the number of crimes per year-month and/or per iso-week as new table (long data)

CREATE TABLE cesnsus_vs_complaint as(
SELECT
    cb2000, shape_area, ct2000, bctcb2000, shape_leng, boro_name, boro_code, po.geometry as census_geom,

    p.cmplnt_num,p.geometry as complaint_geom,date_cmpln,juris_desc,law_cat_cd,prem_typ_d,ofns_desc,pd_desc
	FROM
    geodata_nypd_complaint_shape p
JOIN
    geodata_census_json po
ON
    ST_Within(ST_SetSRID(p.geometry,4326), po.geometry))
	

-- aggregation over above table

WITH date_summary AS (
    SELECT
        bctcb2000,
        law_cat_cd,
        TO_CHAR(date_cmpln::DATE, 'YYYY-MM') AS year_month,
        TO_CHAR(date_cmpln::DATE, 'IYYY-IW') AS iso_week
        
    FROM
        cesnsus_vs_complaint
  
)
SELECT
   bctcb2000,
        law_cat_cd,
        year_month,
        iso_week,
COUNT(*) OVER (PARTITION BY bctcb2000,law_cat_cd,year_month) AS crime_per_month,
COUNT(*) OVER (PARTITION BY bctcb2000,law_cat_cd,iso_week) AS crime_per_week

FROM
    date_summary where year_month='2023-02'
