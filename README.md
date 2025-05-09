# ChatDB: Building a Natural Language Query Interface for SQL and NoSQL Databases
### Team Members: Evan Hu, Emily Truong, Aditya Venkat

------

### Introduction

In this project, we built a natural language processing (NLP) interface ChatDB that enables users to query both relational (MySQL) and NoSQL (MongoDB) databases using natural language prompts. Through an interactive web interface, user inputs are converted into executable database queries using a large language model (LLM). Specifically, we integrated Google’s Gemini 2.0 Flash through its API to power this conversion. The system supports three primary operations:

1. Explore: Users would be allowed to ask questions in natural language to view schemas and data of databases, such as names of tables/collections, attribute/field names of those tables/collections, and sample data.

2. Query: The interface and program would accept natural language queries from users, convert them into database queries, execute the queries in the DBMS, and return the query results to the users.
    - For the MySQL databases, it supports common SQL constructs like select, from, where, group by, having, order by, limit, and offset. Queries that involve joining multiple tables are also supported.
    - For the MongoDB databases, it supports MongoDB functions such as find (with projection), aggregate (with $match, $group, $sort, $limit, $skip, $project). Queries that involve joining two collections (using $lookup) are also supported. 
3. Modify: Users would be allowed to send insert, delete, and update requests in natural language. For the MongoDB databases, the program converts the requests into MongoDB functions such as insertOne, updateOne, deleteOne, insertMany, etc.

------

### Database Management Systems Setup

For our project, we used MongoDB as our NoSQL DBMS and MySQL as our relational DBMS. We implemented 3 databases (pokemon_db, world, sakila) into these two database management systems. 

**- MongoDB (Atlas Database) Setup Instructions:**

1. Through the MongoDB Atlas website, set up a project and cluster. The default project and cluster works for the scope of this project. In "Clusters", click "Browse Collections". Then click "+ Create Database". Create 3 databases called "pokemon_db", "World", and "sakila". The following are the database names along with their collection names. Please make sure you create/have all collections (case sensitive!) listed under the appropriate database before proceeding to the next step.
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

4. In the Connections page of the MySQL instance, make sure Public IP connectivity is enabled. Keep in mind the Public IP address as it will be used later to update the backend scripts. In the NETWORKING tab, add the appropriate IP address(es) to the list of Authorized networks. 

------

### Backend Setup

1. Prerequisites:
    - Python 3.8+
    - ```pip``` (Python package manager)
    - Your own API Key for Google Gemini 2.0 Flash
    - DBMS are online and running
        - MongoDB Atlas (with 'World', 'pokemon_db', and 'sakila' databases)
        - MySQL Server (with 'world', 'pokemon_db', and 'sakila' databases)

2. Update the connections to the databases in the Python scripts located in the `backend` folder. As a default in the scripts, we have provided the connections to the database management systems we set up, but please update the connections to your own. Please note that the connection to these databases will not work unless you have properly configured the network access settings by adding the necessary IP address(es). 
    - For the 3 `_mongodb.py` scripts, the connection link has to be updated 3 times for each script. Within each script, the 3 main functions each have a line of code that establishes a connection to the MongoDB cluster. There will be a comment to highlight the need to update the connection link. Thus, there will be a total of **9** changes across the 3 `_mongodb.py` scripts.
    - For the 3 `_mysql.py` scripts, the connection has to be updated only once for each script. Within each script, there is a helper function called 'mysql_helper_conn' that establishes the connection to the MySQL server to handle queries/requests. Update the 'host', 'user', and 'password'. 'host' is the MySQL instance's public IP address, 'user' can be the default "root" user or any other added user, and 'password' is the associated password for the respective user.

3. Setup Steps:
    - Navigate to the backend folder:
      ```
      cd LLM-DBMS/backend
      ```
    - Create a ```.env``` file:
      ```
      touch .env
      ```
    - Add your Gemini API Key:
      ```
      nano .env
      GOOGLE_API_KEY=your_google_api_key_here
      ```
    - Install dependencies:
      ```
      pip install -r requirements.txt
      ```
    - Run the Flask server:
      ```
      python app.py
      ```
    - If successful you should see:
      ```
      * Running on http://127.0.0.1:5001/
      ```
    - Test backend (optional) - open your browser and go to:
      ```
      http://127.0.0.1:5001/
      ```
      You should see a message like: "Flask is working!"
------

### Frontend Setup

1. Prerequisites:
    - Node.js (v16 or newer): [https://nodejs.org](https://nodejs.org)
    - npm (comes with Node.js)

2. Navigate to Frontend folder:
```
cd LLM-DBMS/frontend-gui
```
3. Install frontend dependencies:
```
npm install 
```
4. Start the development server:
```
npm run dev
```
Will most likely output something like this... ```Local: HTTP://localhost:5173/```

5. Open the URL in your browser to interact with the UI. 

