CREATE TABLE stations (
  stop_id INTEGER PRIMARY KEY,
  direction_id VARCHAR(1) NOT NULL,
  stop_name VARCHAR(70) NOT NULL,
  station_name VARCHAR(70) NOT NULL,
  station_descriptive_name VARCHAR(200) NOT NULL,
  station_id INTEGER NOT NULL,
  "order" INTEGER,
  red BOOLEAN NOT NULL,
  blue BOOLEAN NOT NULL,
  green BOOLEAN NOT NULL
);

INSERT INTO stations(stop_id, direction_id, stop_name, station_name, station_descriptive_name, station_id, "order", red, blue, green) 
    VALUES (999999, 'N', 'Ayura (Jumbo)', 'Ayura', 'Estacion Ayura', 111111, 9, 'true', 'false', 'false');