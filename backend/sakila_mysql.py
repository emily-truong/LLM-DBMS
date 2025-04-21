import mysql.connector
import google.generativeai as genai
import os
import re
from dotenv import load_dotenv

# Loading API keys from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash-001")

def mysql_helper_conn(database_input, query, return_json=False):
    """
    connects to MySQL server and executes query
    """
    mysql_conn = mysql.connector.connect(
        host="34.136.221.112",
        user="root",
        password="toothbrush",
        database=database_input
    )
    cursor = mysql_conn.cursor()
    result = []
    try:
        cursor.execute(query)
        if cursor.with_rows:
            rows = cursor.fetchall()
            if return_json:
                columns = [desc[0] for desc in cursor.description]
                result = [dict(zip(columns, row)) for row in rows]
            else:
                result = rows
        else:
            mysql_conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        result = [("Error", str(e))]
    cursor.close()
    mysql_conn.close()
    return result

def extract_sql_from_response(response_text):
    """
    processes/cleans the LLM output
    """
    if response_text.startswith("```sql"):
        match = re.search(r"```sql\n(.*?)```", response_text, re.DOTALL)
        return match.group(1).strip() if match else response_text
    return response_text.strip()

# Exploration function 
def main_mysql_explore_sakila(input):
    prompt = ("Given a MySQL database called sakila, with 3 tables named actor, film, and film_actor."
              "The actor table has 3 columns: actor_id, first_name, and last_name."
              "The film table has 12 columns: film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, and special_features."
              "The film_actor table has 2 columns: actor_id and film_id."
              "film_actor.actor_id is a foreign key that references actor.actor_id."
              "film_actor.film_id is a foreign key that references film.film_id."
              "I want to explore the database."
              f'Can you help me write a MySQL query that addresses the following prompt: "{input}"'
              "Please return only the MySQL query and nothing else."
    )
    try:
        response = model.generate_content(prompt)
        print(f"LLM result:\n{response.text}")
        sql_code = extract_sql_from_response(response.text)
        print(f"MySQL query to execute:\n`{sql_code}`")
        result = mysql_helper_conn("sakila", sql_code, return_json=True)
        return {"query": sql_code, "result": result}
    except Exception as e:
        print(f"Error: {e}")

# Query function
def main_mysql_query_sakila(input):
    prompt = ("Given a MySQL database called sakila, with 3 tables named actor, film, and film_actor."
              "The actor table has 3 columns: actor_id, first_name, and last_name."
              "The film table has 12 columns: film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, and special_features."
              "The film_actor table has 2 columns: actor_id and film_id."
              "film_actor.actor_id is a foreign key that references actor.actor_id."
              "film_actor.film_id is a foreign key that references film.film_id."
              "I want to query the tables of the database."
              f'Can you help me write a MySQL query that addresses the following prompt: "{input}"'
              "Please return only the MySQL query and nothing else."
    )
    try:
        response = model.generate_content(prompt)
        print(f"LLM result:\n{response.text}")
        sql_code = extract_sql_from_response(response.text)
        print(f"MySQL query to execute:\n`{sql_code}`")
        result = mysql_helper_conn("sakila", sql_code, return_json=True)
        return {"query": sql_code, "result": result}
    except Exception as e:
        print(f"Error: {e}")

# Modification function
def main_mysql_modify_sakila(input):
    prompt = ("Given a MySQL database called sakila, with 3 tables named actor, film, and film_actor."
              "The actor table has 3 columns: actor_id, first_name, and last_name."
              "The film table has 12 columns: film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, and special_features."
              "The film_actor table has 2 columns: actor_id and film_id."
              "film_actor.actor_id is a foreign key that references actor.actor_id."
              "film_actor.film_id is a foreign key that references film.film_id."
              "I want to modify the data of the database like inserting, deleting, or updating."
              f'Can you help me write a MySQL query that addresses the following prompt: "{input}"'
              "Please return only the MySQL query and nothing else."
    )
    try:
        response = model.generate_content(prompt)
        print(f"LLM result:\n{response.text}")
        sql_code = extract_sql_from_response(response.text)
        print(f"Data modification code:\n`{sql_code}`")
        result = mysql_helper_conn("sakila", sql_code, return_json=True)
        return {"query": sql_code, "result": "Data modified!"}
    except Exception as e:
        print(f"Error: {e}")