This app gets data from api, puts weather data into database, and another DAG creates diagram with temperature difference in 7 days

To start project 1. You need to install all of the packages from requirements.txt ----> pip install -r requirements.txt
                 2. Create table in you're database with name "weather". 
                                                                    CREATE TABLE weather (
                                                                    id SERIAL PRIMARY KEY,
                                                                    city VARCHAR(50) NOT NULL,
                                                                    temp FLOAT NOT NULL,
                                                                    description VARCHAR(100),
                                                                    dt TIMESTAMP NOT NULL,
                                                                    sunrise TIMESTAMP,
                                                                    sunset TIMESTAMP
                                                                    );
                 3. Create database connection in you're Airflow Admin->Connections.
                 4.Start DAGs in the Airflow.
                 
