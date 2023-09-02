-- Table: public.df_call_service_data_dtypes

-- DROP TABLE IF EXISTS public.df_call_service_data_dtypes;

CREATE TABLE IF NOT EXISTS public.df_call_service_data_dtypes
(
    index bigint,
    "CAD_EVNT_ID" bigint,
    "CREATE_DATE" timestamp without time zone,
    "INCIDENT_DATE" timestamp without time zone,
    "INCIDENT_TIME" text COLLATE pg_catalog."default",
    "NYPD_PCT_CD" double precision,
    "BORO_NM" text COLLATE pg_catalog."default",
    "PATRL_BORO_NM" text COLLATE pg_catalog."default",
    "GEO_CD_X" bigint,
    "GEO_CD_Y" bigint,
    "RADIO_CODE" text COLLATE pg_catalog."default",
    "TYP_DESC" text COLLATE pg_catalog."default",
    "CIP_JOBS" text COLLATE pg_catalog."default",
    "ADD_TS" timestamp without time zone,
    "DISP_TS" timestamp without time zone,
    "ARRIVD_TS" timestamp without time zone,
    "CLOSNG_TS" timestamp without time zone,
    "Latitude" double precision,
    "Longitude" double precision
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.df_call_service_data_dtypes
    OWNER to admin_user;
-- Index: ix_df_call_service_data_dtypes_index

-- DROP INDEX IF EXISTS public.ix_df_call_service_data_dtypes_index;

CREATE INDEX IF NOT EXISTS ix_df_call_service_data_dtypes_index
    ON public.df_call_service_data_dtypes USING btree
    (index ASC NULLS LAST)
    TABLESPACE pg_default;