USE user_data;

ALTER TABLE customers
MODIFY created DATE DEFAULT (CURRENT_DATE);
