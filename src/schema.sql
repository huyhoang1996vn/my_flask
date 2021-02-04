DROP TABLE IF EXISTS user_flask;
DROP TABLE IF EXISTS post;

DROP SEQUENCE IF EXISTS user_flask_seq CASCADE;
CREATE SEQUENCE user_flask_seq;
DROP TABLE IF EXISTS user_flask CASCADE;
CREATE TABLE user_flask(
	id varchar(20) NOT NULL PRIMARY KEY
		CHECK (id ~ '^U[0-9]+$' )
		DEFAULT 'U' || lpad(nextval('user_flask_seq'::regclass)::text, 9, '0'),
	username varchar(20) NOT NULL,
	password varchar(20) NOT NULL
);



DROP SEQUENCE IF EXISTS post_seq CASCADE;
CREATE SEQUENCE post_seq;
DROP TABLE IF EXISTS post CASCADE;
CREATE TABLE post(
	id varchar(20) NOT NULL PRIMARY KEY
		CHECK (id ~ '^B[0-9]+$' )
		DEFAULT 'B' || lpad(nextval('post_seq'::regclass)::text, 9, '0'),
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	author_id varchar(20) references "user_flask"(id),
	title varchar(20) NOT NULL,
	body varchar(200) NOT NULL
);


