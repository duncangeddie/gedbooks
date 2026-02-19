USE user_data;

CREATE TABLE IF NOT EXISTS chart_of_accounts (
    user_id INT NOT NULL,
    ref INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    status BOOLEAN,
    created DATE
);
