# django_example
Create API using Django framework

## Setting Postgres DB using Docker
1.Select PostgreSQL image 
docker run --name [CONTAINER_NAME] -e POSTGRES_PASSWORD=[PASSWORD]  -p 5432:5432 -d postgres:latest  

2. Connect via EXEC
docker exec -it [CONTAINER_NAME] bash

Now we have root access to the container. Notice the container ID in the command prompt. To access postgres you need to change to user ‘postgres’ and then run psql. To exit psql, type \q

su postgres

psql

3. Create a user for the project(Optional)
CREATE USER [USER_NAME] WITH password ['PASS_DB'];

4. Create a new DB
CREATE DATABASE [DB_NAME] ENCODING 'UTF8' TEMPLATE template0 OWNER [USER_NAME];

