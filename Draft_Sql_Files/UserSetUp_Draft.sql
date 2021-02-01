USE test_schema;

DROP USER IF EXISTS 'ios_and_admin'@'localhost';
DROP USER IF EXISTS 'export'@'localhost';
DROP USER IF EXISTS 'touchscreen'@'localhost';
DROP USER IF EXISTS 'display'@'localhost';
DROP USER IF EXISTS 'adminMa'@'localhost';
DROP USER IF EXISTS 'adminHuang'@'localhost';

CREATE USER 'ios_and_admin'@'localhost' IDENTIFIED BY 'm0bi13!';
CREATE USER 'export'@'localhost' IDENTIFIED BY 'inp+0u+P+';
CREATE USER 'touchscreen'@'localhost' IDENTIFIED BY 'w!Nd0wW03';
CREATE USER 'display'@'localhost' IDENTIFIED BY 'sh0WM24t';
CREATE USER 'adminMa'@'localhost' IDENTIFIED BY 'atm0nchu1';
CREATE USER 'adminHuang'@'localhost' IDENTIFIED BY 'm1ll!n02';

GRANT SELECT ON test_schema.users TO 'ios_and_admin'@'localhost';

GRANT SELECT ON test_schema.* TO 'adminMa'@'localhost';
GRANT UPDATE ON test_schema.* TO 'adminMa'@'localhost';
GRANT DELETE ON test_schema.* TO 'adminMa'@'localhost';
GRANT GRANT OPTION ON test_schema.* TO 'adminMa'@'localhost';
GRANT INSERT ON test_schema.* TO 'adminMa'@'localhost';

GRANT SELECT ON test_schema.* TO 'adminHuang'@'localhost';
GRANT UPDATE ON test_schema.* TO 'adminHuang'@'localhost';
GRANT DELETE ON test_schema.* TO 'adminHuang'@'localhost';
GRANT GRANT OPTION ON test_schema.* TO 'adminHuang'@'localhost';
GRANT INSERT ON test_schema.* TO 'adminHuang'@'localhost';

FLUSH PRIVILEGES;