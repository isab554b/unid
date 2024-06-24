-- SQLite


-- ##############################
-- USERS
CREATE TABLE IF NOT EXISTS users (
    user_id	            	INTEGER NOT NULL UNIQUE,
	user_role_id			INTEGER,	
	first_name	        	TEXT NOT NULL,
	last_name	        	TEXT NOT NULL,
	email	            	TEXT NOT NULL,
	phone					INTEGER NOT NULL UNIQUE,
	username				TEXT NOT NULL UNIQUE,
	password	        	TEXT NOT NULL,
	is_active	        	INTEGER NOT NULL CHECK (is_active IN (0, 1)),
	created_at	        	TEXT NOT NULL,
	updated_at	        	TEXT,
	deleted_at	        	TEXT,
	PRIMARY KEY(user_id),
	FOREIGN KEY(user_role_id) REFERENCES user_roles(user_role_id)
) WITHOUT ROWID;


-- ##############################
-- CLIPCARDS AND CARDTYPES
CREATE TABLE IF NOT EXISTS clipcards (
	clipcard_id	        INTEGER NOT NULL UNIQUE,
	clipcard_type_id	INTEGER NOT NULL,
	time_used			INTEGER NOT NULL,
	remaining_time	    INTEGER NOT NULL,
	created_at	        TEXT NOT NULL,
	updated_at	        TEXT NOT NULL,
	deleted_at			TEXT,
	is_active			INTEGER NOT NULL CHECK (is_active IN (0, 1)),
	PRIMARY KEY(clipcard_id),
	FOREIGN KEY(clipcard_type_id) REFERENCES card_types(clipcard_type_id)
) WITHOUT ROWID;

CREATE TABLE IF NOT EXISTS card_types (
	clipcard_type_id	INTEGER NOT NULL UNIQUE,
	clipcard_type_title	TEXT NOT NULL,
	clipcard_type_time	INTEGER NOT NULL,
	clipcard_price		INTEGER NOT NULL,
	PRIMARY KEY(clipcard_type_id)
) WITHOUT ROWID;

INSERT INTO card_types (clipcard_type_id, clipcard_type_title, clipcard_type_time, clipcard_price) VALUES
(1, '10 timer', 600, 7000),
(2, '20 timer', 1200, 14000),
(3, '30 timer', 1800, 19500);


-- ##############################
-- TASKS
CREATE TABLE IF NOT EXISTS tasks (
	task_id	            INTEGER NOT NULL UNIQUE,
	clipcard_id	        INTEGER NOT NULL,
	customer_id			INTEGER NOT NULL,
	task_title			TEXT NOT NULL,
	task_description	TEXT NOT NULL,
	created_at	        TEXT,
	time_spent	        INTEGER NOT NULL,
	PRIMARY KEY(task_id),
	FOREIGN KEY(clipcard_id) REFERENCES clipcards(clipcard_id),
	FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
) WITHOUT ROWID;


-- ##############################
-- PAYMENTS
CREATE TABLE IF NOT EXISTS payments (
	payment_id	        INTEGER NOT NULL UNIQUE,
	user_id				INTEGER NOT NULL,
	clipcard_id	        INTEGER NOT NULL UNIQUE,
	amount_paid	        INTEGER NOT NULL,
	created_at	        TEXT NOT NULL,
	PRIMARY KEY(payment_id),
	FOREIGN KEY(user_id) REFERENCES users(user_id),
	FOREIGN KEY(clipcard_id) REFERENCES clipcards(clipcard_id)
) WITHOUT ROWID;


-- ##############################
-- USER ROLES AND RIGHTS
CREATE TABLE IF NOT EXISTS user_roles (
	user_role_id		INTEGER NOT NULL,
	user_role_title		TEXT NOT NULL,
	PRIMARY KEY(user_role_id)
) WITHOUT ROWID;

INSERT INTO user_roles (user_role_id, user_role_title) VALUES
(1, 'customer'),
(2, 'staff');

CREATE TABLE IF NOT EXISTS customers (
	customer_id			INTEGER NOT NULL UNIQUE,
	user_role_id		INTEGER NOT NULL,
	website_name		TEXT NOT NULL,
	website_url			TEXT NOT NULL,
	PRIMARY KEY(customer_id),
	FOREIGN KEY(user_role_id) REFERENCES user_roles(user_role_id)
) WITHOUT ROWID;

CREATE TABLE IF NOT EXISTS staff (
	staff_id			INTEGER NOT NULL UNIQUE,
	user_role_id		INTEGER NOT NULL,
	PRIMARY KEY(staff_id),
	FOREIGN KEY(user_role_id) REFERENCES user_roles(user_role_id)
) WITHOUT ROWID;


-- ##############################
-- MESSAGES
CREATE TABLE IF NOT EXISTS messages (
	message_id			INTEGER NOT NULL UNIQUE,
	user_id				INTEGER NOT NULL,
	message_subject		TEXT NOT NULL,
	message_text		TEXT NOT NULL,
	message_file		TEXT,
	created_at			TEXT NOT NULL,
	deleted_at			TEXT,
	PRIMARY KEY(message_id),
	FOREIGN KEY(user_id) REFERENCES users(user_id)
) WITHOUT ROWID;


-- ##############################
-- VIEWS
CREATE VIEW active_clipcards AS
SELECT cc.clipcard_id, cc.remaining_time, cc.time_used, cc.created_at,
       u.user_id, u.first_name, u.last_name, u.username, u.email, u.phone,
       cust.website_name, cust.website_url, ct.clipcard_type_title
FROM clipcards cc
JOIN payments p ON cc.clipcard_id = p.clipcard_id
JOIN users u ON p.user_id = u.user_id
JOIN customers cust ON u.user_id = cust.customer_id
JOIN card_types ct ON cc.clipcard_type_id = ct.clipcard_type_id
WHERE cc.is_active = 1;

-- HOW TO USE THE VIEW IN THE CODE
SELECT * FROM active_clipcards;


-- ##############################
-- TRIGGERS
CREATE TRIGGER update_clipcard_data
AFTER INSERT ON tasks
FOR EACH ROW
BEGIN
    UPDATE clipcards
    SET time_used = time_used + NEW.time_spent,
        remaining_time = remaining_time - NEW.time_spent
    WHERE clipcard_id = NEW.clipcard_id;
END;
