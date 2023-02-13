To deploy the airflow-pg-metabase toolset:
    
    1. create directory for local volumes
    
    2. open it in terminal
    
    3. run command in bash:
    mkdir -p ./dags ./logs ./plugins ./api_keys ./root ./config
    mkdir -p ./dags/sql ./dags/json_data ./root/lib ./root/var
    echo -e "AIRFLOW_UID=$(id -u)" > config.env
    docker compose up airflow-init
    
    4. wait until the airflow-init container finished with exit code 0
    
    5. run command in bash:
    docker compose up
