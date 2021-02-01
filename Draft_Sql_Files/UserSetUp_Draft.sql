USE test_schema;

DROP USER IF EXISTS 'ios_and_admin'@'localhost';
DROP USER IF EXISTS 'export'@'localhost';
DROP USER IF EXISTS 'touchscreen'@'localhost';
DROP USER IF EXISTS 'display'@'localhost';

CREATE USER 'ios_and_admin'@'localhost' IDENTIFIED BY 'm0bi13!';
CREATE USER 'export'@'localhost' IDENTIFIED BY 'inp+0u+P+';
CREATE USER 'touchscreen'@'localhost' IDENTIFIED BY 'w!Nd0wW03';
CREATE USER 'display'@'localhost' IDENTIFIED BY 'sh0WM24t';

