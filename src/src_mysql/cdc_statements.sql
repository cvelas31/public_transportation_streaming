INSERT INTO `cars` (`car_id`, `brand`, `model`, `ts_created`) VALUES ( 1, 'ford', 'mustang', '2020-07-06 15:50:47');
INSERT INTO cars (car_id, brand, model, ts_created) VALUES ( 2, 'ford', 'mondeo', '2019-07-06 15:52:47');
INSERT INTO cars (car_id, brand, model, ts_created) VALUES ( 3, 'toyota', 'camary', '2020-07-06 16:50:47');
INSERT INTO cars (car_id, brand, model) VALUES ( 4, 'bmw', 'm3');
INSERT INTO cars (car_id, brand, model) VALUES ( 5, 'ford', 'ch');
INSERT INTO cars (car_id, brand, model, ts_created) VALUES ( 6, 'ford', '33', '2020-07-06 16:50:47');
INSERT INTO cars (car_id, brand, model, ts_created) VALUES ( 7, 'ford', 'alksd', '2020-07-06 16:50:47');
INSERT INTO cars (car_id, brand, model, ts_created) VALUES ( 8, 'ford', 'kldfs', '2020-07-06 16:50:47');
INSERT INTO cars (car_id, brand, model, ts_created) VALUES ( 9, 'ford', 'ksdfs', '2020-07-06 16:50:47');
INSERT INTO cars (car_id, brand, model, ts_created) VALUES ( 10, 'tesla', 'blaa', '2020-07-06 16:50:47');


UPDATE cars set model="litro" WHERE car_id=3;
UPDATE cars set model="cool" WHERE car_id=5;
UPDATE cars set model="low" WHERE car_id=8;
UPDATE cars set model="high" WHERE car_id=10;
UPDATE cars set model="mike" WHERE car_id=7;


DELETE from cars WHERE brand='ford';



INSERT INTO cars (car_id, brand, model) VALUES ( 11, 'honda', 'crv');
INSERT INTO cars (car_id, brand, model) VALUES ( 12, 'ford', 'fusion');
INSERT INTO cars (car_id, brand, model) VALUES ( 13, 'mercedes', 'cl200');
INSERT INTO cars (car_id, brand, model) VALUES ( 14, 'suzuki', 'vitara');
UPDATE cars set model="roadster" WHERE car_id=10;
UPDATE cars set model="f150" WHERE car_id=12;

INSERT INTO cars (car_id, brand, model) VALUES ( 15, 'bmw', 'vitara');
UPDATE cars set model="m5" where brand = 'bmw';

DELETE from cars WHERE brand='bmw' or brand='tesla';