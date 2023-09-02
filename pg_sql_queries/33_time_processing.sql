--=== Time processing
	
SELECT *,
ROUND(EXTRACT(EPOCH FROM ("ARRIVD_TS" - "DISP_TS")) / 60,4) AS arrived_disp_min,
ROUND(EXTRACT(EPOCH FROM ("CLOSNG_TS" - "ARRIVD_TS")) / 60,4) AS close_arrived_min,
ROUND(EXTRACT(EPOCH FROM ("CLOSNG_TS" - "DISP_TS")) / 60,4) AS close_disp_min,
CASE
	WHEN "DISP_TS" is null THEN 'no resource despatched'
	WHEN ROUND(EXTRACT(EPOCH FROM ("CLOSNG_TS" - "DISP_TS")) / 60,4) < 20.0 THEN 'less than 20 minutes'
	WHEN ROUND(EXTRACT(EPOCH FROM ("CLOSNG_TS" - "DISP_TS")) / 60,4) < 30.0 THEN 'less than 30 minutes'
	WHEN ROUND(EXTRACT(EPOCH FROM ("CLOSNG_TS" - "DISP_TS")) / 60,4) < 60.0 THEN 'less than 60 minutes'
	ELSE 'more than 60 minutes'
END AS duration_label
	FROM public.df_call_service_data_dtypes limit 100