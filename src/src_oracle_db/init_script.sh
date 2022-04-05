#!/bin/bash

echo "Init script..."

source /home/oracle/.bashrc;

sqlplus -S sys/Oradoc_db1@ORCLCDB as sysdba @01-shutdown_db.sql

sqlplus '/as sysdba' @02-enable_archive_log.sql

sqlplus sys/Oradoc_db1@ORCLCDB as sysdba @03-load_data.sql