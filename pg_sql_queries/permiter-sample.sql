SELECT st_length((ST_MakeLine(sp,ep)))
FROM
   -- extract the endpoints for every 2-point line segment for each linestring
   (SELECT shape_leng,
      ST_PointN(geom, generate_series(1, ST_NPoints(geom)-1)) as sp,
      ST_PointN(geom, generate_series(2, ST_NPoints(geom)  )) as ep
    FROM
       -- extract the individual linestrings
      (SELECT shape_leng, (ST_Dump(ST_Boundary(geometry))).geom
       FROM geodata_census_json
       ) AS linestrings
    ) AS segments;
