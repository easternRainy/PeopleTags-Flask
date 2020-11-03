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
	id INTEGER CHECK(id > 0),
	my_username VARCHAR(15) DEFAULT NULL,
	password VARCHAR(50) DEFAULT NULL,
	salt VARCHAR(15) DEFAULT NULL,

	PRIMARY KEY (id),
	UNIQUE (my_username)
);

CREATE TABLE person (
	id INTEGER CHECK(id > 0),
	first_name VARCHAR(15) DEFAULT NULL,
	last_name VARCHAR(15) DEFAULT NULL,
	age INTEGER DEFAULT NULL,
	job_title VARCHAR(15) DEFAULT NULL,
	description VARCHAR(50) DEFAULT NULL,
	email VARCHAR(20) DEFAULT NULL,

	created_by INTEGER,
	image_url VARCHAR(50) DEFAULT NULL,

	PRIMARY KEY (id),
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE

);

CREATE TABLE class (
	id INTEGER CHECK(id > 0),
	name VARCHAR(15) DEFAULT NULL,
	description VARCHAR(50) DEFAULT NULL,

	created_by INTEGER,
	image_url VARCHAR(50) DEFAULT NULL,

	PRIMARY KEY (id),
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE

);

CREATE TABLE social_media (

	id INTEGER CHECK(id > 0),
	name VARCHAR(15) DEFAULT NULL,	
	url VARCHAR(50) DEFAULT NULL,

	created_by INTEGER,

	PRIMARY KEY (id),
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE post (
	id INTEGER CHECK(id > 0),
	created_by INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE
	
);

CREATE TABLE person_class_assoc (
	id INTEGER CHECK(id > 0),
	person INTEGER CHECK(person > 0) NOT NULL,
	class INTEGER CHECK(class > 0) NOT NULL,

	created_by INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY (person) references person (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (class) references class (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE

);

CREATE TABLE person_social_media_assoc (
	id INTEGER CHECK(id > 0),
	person INTEGER CHECK(person > 0) NOT NULL,
	social_media INTEGER CHECK(social_media > 0) NOT NULL,

	created_by INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY (person) references person (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (social_media) references social_media (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE

);

CREATE TABLE person_post_assoc (
	id INTEGER CHECK(id > 0),
	person INTEGER CHECK(person > 0) NOT NULL,
	post INTEGER CHECK(post > 0) NOT NULL,

	created_by INTEGER,
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY (id),
	FOREIGN KEY (person) references person (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (post) references post (id) ON UPDATE CASCADE ON DELETE CASCADE

);

CREATE TABLE class_post_assoc (
	id INTEGER CHECK(id > 0),
	class INTEGER CHECK(class > 0) NOT NULL,
	post INTEGER CHECK(post > 0) NOT NULL,

	created_by INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY (class) references class (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (post) references post (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(created_by) references my_user (id) ON UPDATE CASCADE ON DELETE CASCADE

);
