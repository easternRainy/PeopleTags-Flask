DROP TABLE IF EXISTS my_user CASCADE;
DROP TABLE IF EXISTS person CASCADE;
DROP TABLE IF EXISTS class CASCADE;
DROP TABLE IF EXISTS social_media CASCADE;
DROP TABLE IF EXISTS post CASCADE;
DROP TABLE IF EXISTS person_class_assoc CASCADE;
DROP TABLE IF EXISTS person_social_media_assoc CASCADE;
DROP TABLE IF EXISTS person_post_assoc CASCADE;
DROP TABLE IF EXISTS class_post_assoc CASCADE;

CREATE TABLE my_user (
	id VARCHAR(65),
	my_username VARCHAR(65) DEFAULT NULL,
	password VARCHAR(65) DEFAULT NULL,
	salt VARCHAR(65) DEFAULT NULL,

	PRIMARY KEY (id),
	UNIQUE (my_username)
);

CREATE TABLE person (
	id VARCHAR(65),
	first_name TEXT DEFAULT NULL,
	last_name TEXT DEFAULT NULL,
	age INTEGER DEFAULT NULL,
	job_title TEXT DEFAULT NULL,
	description TEXT DEFAULT NULL,
	email TEXT DEFAULT NULL,

	created_by VARCHAR(65),
	image_url TEXT DEFAULT NULL,

	PRIMARY KEY (id),
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE

);

CREATE TABLE class (
	id VARCHAR(65),
	name VARCHAR(15) DEFAULT NULL,
	description TEXT DEFAULT NULL,

	created_by VARCHAR(65),
	image_url TEXT DEFAULT NULL,

	PRIMARY KEY (id),
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE

);

CREATE TABLE social_media (

	id VARCHAR(65),
	name TEXT DEFAULT NULL,	
	url TEXT DEFAULT NULL,

	created_by VARCHAR(65),

	PRIMARY KEY (id),
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE post (
	id VARCHAR(65),

	file_url TEXT,
	visibility TEXT,
	create_time DATE,
	created_by VARCHAR(65),
	PRIMARY KEY (id),
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE
	
);

CREATE TABLE person_class_assoc (
	id VARCHAR(65),
	person VARCHAR(65) NOT NULL,
	class VARCHAR(65) NOT NULL,

	created_by VARCHAR(65),
	PRIMARY KEY (id),
	FOREIGN KEY (person) references person (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (class) references class (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE

);

CREATE TABLE person_social_media_assoc (
	id VARCHAR(65),
	person VARCHAR(65) NOT NULL,
	social_media VARCHAR(65) NOT NULL,

	created_by VARCHAR(65),
	PRIMARY KEY (id),
	FOREIGN KEY (person) references person (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (social_media) references social_media (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE

);

CREATE TABLE person_post_assoc (
	id VARCHAR(65),
	person VARCHAR(65) NOT NULL,
	post VARCHAR(65) NOT NULL,

	created_by VARCHAR(65),
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY (id),
	FOREIGN KEY (person) references person (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (post) references post (id) ON UPDATE CASCADE ON DELETE CASCADE

);

CREATE TABLE class_post_assoc (
	id VARCHAR(65),
	class VARCHAR(65) NOT NULL,
	post VARCHAR(65) NOT NULL,

	created_by VARCHAR(65),
	PRIMARY KEY (id),
	FOREIGN KEY (class) references class (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (post) references post (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE

);
