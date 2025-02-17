# Cloud SQL API for MySQL

A RESTful API service for managing MySQL databases on Google Cloud SQL.

## Prerequisites

- Google Cloud Platform Account
- Cloud SQL Instance with `MySQL`
- `cloud-sql-proxy` installed
- `gcloud` CLI installed

## Setup & Authentication

### I. Using Cloud SQL Proxy

> [!IMPORTANT]
> Skip this step if you are not using Cloud SQL Proxy.

1. Download cloud-sql-proxy refer from this [Download](https://cloud.google.com/sql/docs/mysql/sql-proxy#install)
2. For Windows:
   - Rename the file to `cloud-sql-proxy.exe`
   - Put the file into a folder `cloud_sql_proxy` in your `Program Files` folder.
   - Copy the path of the folder and add it to the system environment variable.
   - Run `cloud-sql-proxy -v` in CMD to check if the installation is successful.
3. Enable Cloud SQL Admin API in GCP Console.
4. Create a service account and download the service account key.
5. Assign the service account with role `Cloud SQL Admin` in GCP Console.
6. Put the downloaded service account key into the root folder of this project.
7. Authenticate with GCP:
   - `gcloud auth login` to login to your GCP account.
   - `gcloud config list account` to see your current account.
   - `gcloud projects list` to see your project list.
   - `gcloud config set project PROJECT_ID` to set your project ID.
   - `gcloud config list project` to check if project has been select.
   - `gcloud auth activate-service-account --key-file=/PATH/TO/YOUR/SERVICE-ACCOUNT.json` to authenticate with GCP.
8. Run `cloud-sql-proxy --gcloud-auth CONNECTION-NAME` to connect to the Cloud SQL instance.
9. At `.env` file, set `CLOUD_SQL_CONNECTION_NAME` with your Cloud SQL instance name.

### II. Without Cloud SQL Proxy

1. Enable Cloud SQL Admin API in GCP Console.
2. At `.env` file, set :
   - `DB_PORT` with your Cloud SQL instance port.
   - `DB_IP` with your Cloud SQL instance IP.
3. In `src/db.py`, comment in line `8-13` and `35-40`:

   ```python
    conn = mysql.connector.connect(
        user=db_user,
        password=user_password,
        database=db_name,
        unix_socket=SOCKET_PATH  # Use the Cloud SQL Unix socket
    )
   ```

   and uncomment in line `18-24` and `45-51`:

   ```python
    conn = mysql.connector.connect(
        user=db_user,
        password=user_password,
        database=db_name,
        host=DB_IP,  # Use the public IP address of the Cloud SQL instance
        port=DB_PORT  # Default MySQL port
    )
   ```

## Endpoints

1. Testing connection
   - endpoint **GET** : `/`
2. Login database user
   - endpoint **POST** : `/login`
   - Reequired `JSON` body:

     ```json
     {
         "db_name": "db_name",
         "db_user": "db_user",
         "user_password": "user_password"
     }
     ```

### I. Table Management

1. Get all tables
   - Endpoint **GET** : `/tables`
2. Create a table
   - Endpoint **POST** : `/table/create`
   - Required `JSON` body:

     ```json
     {
         "table": "employees",
         "columns": [
            {"name": "coloumn_name", "type": "data_type"},
            {"name": "coloumn_name", "type": "data_type"},
            {"name": "coloumn_name", "type": "data_type"}
         ]
     }
     ```

3. Get all columns of a table
   - Endpoint **GET** : `/table/describe`
   - Required `JSON` body:

     ```json
     {
         "table": "table_name"
     }
     ```

4. Rename a table
   - Endpoint **PUT** : `/table/rename`
   - Required `JSON` body:

     ```json
     {
         "table": "table_name",
         "new_table": "new_table_name"
     }
     ```

5. Delete a table
   - Endpoint **DELETE** : `/table/delete`
   - Required `JSON` body:

     ```json
     {
         "table": "table_name"
     }
     ```

### II. Data Management


1. Display all data from a table
   - Endpoint **GET** : `/contents`
   - Required `JSON` body:
    
     ```json
     {
         "table": "table_name"
     }
     ```

2. Insert data into a table
   - Endpoint **POST** : `/content/add`
   - Required `JSON` body:

     ```json
     {
         "table": "employees",
         "columns": ["name", "salary", "age"],
         "values": [
            ["John Doe", 50000, 30],
            ["Jane Doe", 55000, 28]
         ]
     }
     ```

3. Update data in a table
   - Endpoint **PUT** : `/content/update`
   - Required `JSON` body:
  
     ```json
     {
         "table": "testing",
         "data": {
            "gender": "male",
            "age": 35
         },
         "conditions": {
            "name": "Doe"
         }
     }
     ```

4. Delete data from a table
   - Endpoint **DELETE** : `/content/delete`
   - Required `JSON` body:

     ```json
     {
         "table": "testing",
         "conditions": {
            "age": 30,
            "salary": 50000
         }
     }
     ```

5. Get specific data from a table
   - Endpoint **GET** : `/content/specific
   - Required `JSON` body:
     ```json
     {
         "table": "testing",
         "conditions": {
            "age": 30,
         }
     }


### Response /contents

```json
{
    "contents": [
        {
            "age": 30,
            "id": 1,
            "name": "budi",
            "salary": "3000.20"
        },
        {
            "age": 30,
            "id": 2,
            "name": "asdfa",
            "salary": "300.20"
        },
        {
            "age": 30,
            "id": 3,
            "name": "asdfa",
            "salary": "300.20"
        },
        {
            "age": 30,
            "id": 4,
            "name": "asdfa",
            "salary": "300.20"
        }
    ],
    "table": "testing"
}
```
