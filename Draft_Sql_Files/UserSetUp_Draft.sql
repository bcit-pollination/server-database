USE test_schema;

DROP USER IF EXISTS 'server'@'localhost';
DROP USER IF EXISTS 'adminMa'@'localhost';
DROP USER IF EXISTS 'adminHuang'@'localhost';

CREATE USER 'server'@'localhost' IDENTIFIED BY 'm0bi13!';
CREATE USER 'adminMa'@'localhost' IDENTIFIED BY 'atm0nchu1';
CREATE USER 'adminHuang'@'localhost' IDENTIFIED BY 'm1ll!n02';

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