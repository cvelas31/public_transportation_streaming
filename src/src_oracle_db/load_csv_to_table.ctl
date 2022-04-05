load data
infile '/tmp/sample_data.csv'
into table stations
fields terminated by ','  lines terminated by '\n' 
(
stop_id INTEGER ,
direction_id VARCHAR(1),
stop_name VARCHAR(70),
station_name VARCHAR(70),
station_descriptive_name VARCHAR(200),
station_id INTEGER ,
"order" INTEGER,
red VARCHAR(10),
blue VARCHAR(10),
green VARCHAR(10)
)