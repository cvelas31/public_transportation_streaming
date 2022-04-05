-- If you cannot connect to the Database run the following
-- sqlplus '/as sysdba' and 
STARTUP MOUNT;

CONN sys/Oradoc_db1@ORCLCDB as SYSDBA;

ALTER DATABASE ARCHIVELOG;
ALTER DATABASE OPEN;

SELECT LOG_MODE FROM V$DATABASE;