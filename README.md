# Cloud SQL API for MySQL

## Setup

Reinforcement Learning

`cloud-sql-proxy.exe` in `Program Files` Folder and the path to system environment variable.
Enable Cloud SQL Admin API
<!-- login to your gcp account -->
gcloud auth login
Login with your Google account.
<!-- see your current account -->
gcloud config list account
<!-- see your project list -->
gcloud projects list
<!-- set your project id -->
gcloud config set project PROJECT_ID
<!--  check if project has been select -->
gcloud config list project / gcloud config get-value project
<!-- set this in  -->
gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
<!-- gcloud auth application-default login
gcloud auth application-default print-access-token -->
<!-- cloud-sql-proxy my-project:your-connection-name -->
run this command to connect
cloud-sql-proxy --gcloud-auth project-001-cloud-storage:us-central1:ucup **this the right one**

```json
{
  "table_name": "employees",
  "columns": [
    {"name": "coloumn_name", "type": "data_type"},
    {"name": "coloumn_name", "type": "data_type"},
    {"name": "coloumn_name", "type": "data_type"}
  ]
}
```

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
