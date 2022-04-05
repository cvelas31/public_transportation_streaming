FROM store/oracle/database-enterprise:12.2.0.1

COPY ./01-shutdown_db.sql ./01-shutdown_db.sql
COPY ./02-enable_archive_log.sql ./02-enable_archive_log.sql
COPY ./03-load_data.sql ./03-load_data.sql
COPY ./data/sample_data.csv ./tmp/sample_data.csv
COPY ./init_script.sh ./init_script.sh

#configuration
#COPY mysql.cnf /etc/mysql/conf.d/
#COPY init_sql.sql /docker-entrypoint-initdb.d/