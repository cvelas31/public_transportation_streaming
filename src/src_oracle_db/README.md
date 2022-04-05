# Docker Set Up of Oracle

# Oracle Overview
Multitenant Architecture
The multitenant architecture enables an Oracle database to be a multitenant container database (CDB).
A CDB is a single physical database that contains zero, one, or many user-created pluggable databases. A pluggable database (PDB) is a portable collection of schemas, schema objects, and nonschema objects that appears to an Oracle Net client as a non-CDB. A non-CDB is a traditional Oracle database that cannot contain PDBs.

Starting in Oracle Database 12c, you must create a database as either a CDB or non-CDB. You can plug a non-CDB into a CDB as a PDB. To move a PDB to a non-CDB, you must use Oracle Data Pump.

This image contains a default database in a multi-tenant configuration with a single pluggable database (PDB).

# Basic test
[Sample](https://dev.to/chindara/install-oracle-12c-with-docker-55h7)
```bash
docker run -d -it --name ejemplo store/oracle/database-enterprise:12.2.0.1
# SQL Access to the DB
docker exec -it ejemplo bash -c "source /home/oracle/.bashrc; sqlplus /nolog"
```

# Testing the docker
`docker build . -t test_oracle_db`
`docker run -d -it --name test_oracle_db_sample test_oracle_db`
`docker exec -it test_oracle_db_sample bash`

```bash


```

- Restart instance (Not connected) `sqlplus '/as sysdba'`
To connect from outside run:
```
$ sqlplus sys/Oradoc_db1@ORCLCDB as sysdba

exit | sqlplus -S sys/Oradoc_db1@ORCLCDB as SYSDBA @03-load_data.sql

sqlldr userid=sys/Oradoc_db1@ORCLCDB control="./load_csv_to_table.ctl" LOG="csv_load.log" BAD="bad.log" Discard="discarded.log"
```

- Healthcheck: `bash /home/oracle/setup/healthcheck.sh`


# OPTION 2: Download from Oracle Container Registry
Register and create an account to the oracle container registry
[Login with docker](https://docs.oracle.com/cd/E37670_01/E75728/html/oracle-registry-server.html) and download the image you want from [here](https://container-registry.oracle.com/ords/f?p=113:4:31919549663214:::::)



Inside the SQL plus run:
```sql
connect sys as sysdba;
alter session set "_ORACLE_SCRIPT"=true;
create user oracle_user identified by oracle_password;
GRANT ALL PRIVILEGES TO oracle_user;
```

# Full test inside the docker

```bash
docker run --name <container name> \
-p <host port>:1521 -p <host port>:5500 \
-e ORACLE_SID=<your SID> \
-e ORACLE_PDB=<your PDB name> \
-e ORACLE_PWD=<your database passwords> \
-e INIT_SGA_SIZE=<your database SGA memory in MB> \
-e INIT_PGA_SIZE=<your database PGA memory in MB> \
-e ORACLE_EDITION=<your database edition> \
-e ORACLE_CHARACTERSET=<your character set> \
-e ENABLE_ARCHIVELOG=true \
-v [<host mount point>:]/opt/oracle/oradata \
oracle/database:21.3.0-ee
```

```
docker run -d -it --name oracle_db store/oracle/database-enterprise:12.2.0.1 \
    -p 1521:1521 -p 5500:5500 \
    -e ORACLE_SID=<your SID> \
    -e ORACLE_PDB=<your PDB name> \
    -e ORACLE_PWD=<your database passwords> \
```

## Intial Scripts for the docker
Currently sh and sql extensions are supported. For post-setup scripts just mount the volume `/opt/oracle/scripts/setup` or extend the image to include scripts in this directory. For post-startup scripts just mount the volume `/opt/oracle/scripts/startup` or extend the image to include scripts in this directory. Both of those locations are also represented under the symbolic link `/docker-entrypoint-initdb.d`

After the database is setup and/or started the scripts in those folders will be executed against the database in the container. SQL scripts will be executed as `sysdba`, shell scripts will be executed as the current user. To ensure proper order it is recommended to prefix your scripts with a number. For example `01_users.sql`, `02_permissions.sql`, etc.

# Thorubleshoot
- The image comes with WE8DEC character set. you can change it right after starting the container. i.e:
    `sqlplus connect as sysdba`
    ```sql
    SHUTDOWN IMMEDIATE;
    STARTUP RESTRICT;
    ALTER DATABASE CHARACTER SET INTERNAL_USE WE8ISO8859P9;
    ALTER SYSTEM DISABLE RESTRICTED SESSION;
    ```
    - *"Oracle recommends that databases on ASCII-based platforms are created with the AL32UTF8 character set and the AL16UTF16 national (NCHAR) character set."*
- In order to start OracleDB container when using host directory as volume I had to `chmod 777` the directory as the init script drops privileges and the oracle user cannot create files. Leading to the first error `mkdir: cannot create directory '/ORCL/u01': Permission denied`
- [sqlplus not able to connect to Oracle](https://stackoverflow.com/questions/25465842/sql-plus-not-able-to-connect-to-oracle)
- [Change Archive Log Mode](https://www.oracle.com/ocom/groups/public/@otn/documents/webcontent/283263.htm)

## Resources
- [Docker reviews](https://hub.docker.com/_/oracle-database-enterprise-edition?tab=reviews)
- [Docker Oracle](https://hub.docker.com/u/camilovelasqueza/content/sub-3d19e978-b310-449d-867b-1b28908af2f5)
- [Kafka Connect Oracle CDC](https://docs.confluent.io/home/connect/self-managed/userguide.html#connect-installing-plugins)
- [Oracle CDC Prerequisites](https://docs.confluent.io/kafka-connect-oracle-cdc/current/prereqs-validation.html#turn-on-archivelog-mode)

# TODO:
- Keep going with the prerequisites
    - We are good with the [ArchiveLog](https://docs.confluent.io/kafka-connect-oracle-cdc/current/prereqs-validation.html#connect-oracle-cdc-source-prereqs-archivelog-mode)
    - Missing the other 4. 
- Need to improve the table creation.
    - Validate the Schema where the tables are created
    - [Can we assign/create the schema](https://docs.oracle.com/cd/B19306_01/server.102/b14200/statements_6014.htm)
        ```sql
        CREATE SCHEMA AUTHORIZATION oe
        CREATE TABLE new_product 
            (color VARCHAR2(10)  PRIMARY KEY, quantity NUMBER) 
        CREATE VIEW new_product_view 
            AS SELECT color, quantity FROM new_product WHERE color = 'RED' 
        GRANT select ON new_product_view TO hr; 
        ```
