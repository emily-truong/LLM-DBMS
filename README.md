# LLM-DBMS: Talking to Database Management Systems Using Natural Language

### Introduction

------
------

### Database Management Systems Setup

For our project, we used MongoDB as our NoSQL database and MySQL as our RDBMS. We implemented 3 databases (pokemon_db, world, sakila) into these two database management systems. 

**- MongoDB Setup Instructions:**

1. Through the MongoDB website, set up a project and cluster. The default project and cluster works for the scope of this project. In "Clusters", click "Browse Collections". Then click "+ Create Database". Create 3 databases called "pokemon_db", "world", and "sakila". The following are the database names along with their collection names. Please make sure you create/have all collections (case sensitive!) listed under the appropriate database before proceeding to the next step.
    - pokemon_db
        - base_stats
        - pokemon
        - pokemon_types
        - types
    - World
        - City
        - Country
        - CountryLanguage
    - sakila
        - actor
        - film
        - film_actor
2. In "Network Access", add the necessary IP address(es) for connecting to the MongoDB databases, or "Allow access from anywhere", which allows anyone to connect to the MongoDB cluster but be cautious about doing so!

3. Run the Python script called `mongodb_setup.py` in the folder `code`. Note that by default, the MongoDB connection link in the script is the MongoDB cluster we used for our project. In the Python script `mongodb_setup.py`, please edit the MongoDB connection link for the variable "client" to your own MongoDB cluster.
    - `mongodb_setup.py` loads data from the JSON files located in `database_data/MongoDB_json` into the appropriate databases and collections. Additionally for the "pokemon_db" and "sakila" databases, the script further converts specified fields to the integer type (the JSON files for these two databases have all values in double quotes, leading all fields to be of the string type by default).

**- MySQL (Google Cloud) Setup Instructions:**
1. Through the Google Cloud console, navigate to "Buckets" under "Cloud Storage" (use the search feature). Create a bucket using the "Create" button and provide a globally unique name for the bucket. We left the bucket settings as the default options. Once the bucket has been created, upload the .sql files located in the folder `database_data/MySQL` to the bucket. There should be 3 files to upload, a SQL script file for the 3 databases pokemon_db, world, and sakila.

2. Navigate to "SQL" and create an instance using the "Create Instance" button. Select "Choose MySQL". For our project, we chose Enterprise edition with "Development" preset (4 vCPUs) and "Single Zone" availability. Set up an Instance ID and Password. We left the other options as the defaults. Lastly, "Create Instance" to create the MySQL instance (may take a few minutes to create).

3. In the Overview page of the MySQL instance, use "Import" to run the SQL scripts uploaded in step 1. Browse to find the file, select SQL as the file format and "Specified in SQL file" for Destination, and then click "IMPORT". The file will run and the appropriate database will be created. Repeat for the other 2 files/databases.  


### Backend Setup

----
----
