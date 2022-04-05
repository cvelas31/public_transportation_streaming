CREATE TABLE stations (
  stop_id INTEGER PRIMARY KEY,
  direction_id VARCHAR(1) NOT NULL,
  stop_name VARCHAR(70) NOT NULL,
  station_name VARCHAR(70) NOT NULL,
  station_descriptive_name VARCHAR(200) NOT NULL,
  station_id INTEGER NOT NULL,
  "order" INTEGER,
  red VARCHAR(10) NOT NULL,
  blue VARCHAR(10) NOT NULL,
  green VARCHAR(10) NOT NULL
);

CREATE TABLE cars (
  car_id INTEGER PRIMARY KEY,
  brand VARCHAR(200) NOT NULL,
  model VARCHAR(200) NOT NULL,
  ts_created timestamp NOT NULL
);
INSERT INTO cars (car_id, brand, model, ts_created) VALUES ( 1, 'ford', 'mustang', CURRENT_TIMESTAMP);
INSERT INTO cars (car_id, brand, model, ts_created) VALUES ( 2, 'mercedes', 'a200', CURRENT_TIMESTAMP);
-- SELECT car_id, brand FROM cars;

-- Look for tables and schemas (owner, table_name, TABLESPACE_NAME WHERE owner LIKE 'cars')
-- SELECT DISTINCT table_name FROM all_tables WHERE rownum <= 100;
-- SELECT table_name FROM user_tables