USE user_data;

CREATE TABLE IF NOT EXISTS general_ledger (
    user_id INT NOT NULL,
    transaction_date DATE,
    post_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ref VARCHAR(255),
    account_number VARCHAR(255),
    account_name VARCHAR(255),
    debit_amount DECIMAL(15,2),
    credit_amount DECIMAL(15,2),
    status BOOLEAN,
    created DATE
);
