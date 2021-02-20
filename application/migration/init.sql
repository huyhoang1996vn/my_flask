DROP SEQUENCE IF EXISTS integration_id_seq CASCADE;
CREATE SEQUENCE integration_id_seq;
DROP TABLE IF EXISTS integration CASCADE;
CREATE TABLE integration
(
    id integer NOT NULL DEFAULT nextval('integration_id_seq'::regclass),
    created_date timestamp with time zone NOT NULL,
    modified_date timestamp with time zone NOT NULL,
    uid character varying(50) COLLATE pg_catalog."default" NOT NULL,
    source character varying(50) COLLATE pg_catalog."default" NOT NULL,
    provider character varying(50) COLLATE pg_catalog."default",
    extra_data jsonb,
    user_id integer,
    content_type_id integer,
    created_by_id integer,
    modified_by_id integer,
    CONSTRAINT integration_integration_pkey PRIMARY KEY (id),
    CONSTRAINT integration_integration_uid_provider_a4ba5e6d_uniq UNIQUE (uid, provider)
);

DROP TABLE IF EXISTS integration_auth CASCADE;
CREATE TABLE integration_auth
(
    id integer NOT NULL PRIMARY KEY,
    created_date timestamp with time zone NOT NULL,
    modified_date timestamp with time zone NOT NULL,
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    token character varying(250) COLLATE pg_catalog."default" NOT NULL,
    created_by_id integer,
    modified_by_id integer
);

DROP TABLE IF EXISTS organization_integration CASCADE;
CREATE TABLE organization_integration
(
    id integer NOT NULL NOT NULL PRIMARY KEY,
    created_date timestamp with time zone NOT NULL,
    modified_date timestamp with time zone NOT NULL,
    school_name character varying(255) COLLATE pg_catalog."default",
    group_school character varying(255) COLLATE pg_catalog."default" NOT NULL,
    partner character varying(255) COLLATE pg_catalog."default" NOT NULL,
    auth_id integer NOT NULL references "integration_auth"(id)
);



