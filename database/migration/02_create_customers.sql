USE user_data;

CREATE TABLE IF NOT EXISTS customers (
    user_id INT NOT NULL,
    name VARCHAR(255),
    email_address VARCHAR(255),
    tax_number BIGINT,
    phone_number BIGINT,
    address TEXT,
    status BOOLEAN,
    created DATE
);
