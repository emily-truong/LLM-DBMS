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
def main_mysql_explore_world(input):
    prompt = ("Given a MySQL database called world, with 3 tables named city, country, and countrylanguage."
              "The city table has 5 columns: ID, Name, CountryCode, District, Population."
              "The country table has 15 columns: Code, Name, Continent, Region, SurfaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2."
              "The countrylanguage table has 4 columns: CountryCode, Language, IsOfficial, Percentage."
              "city.CountryCode is a foreign key that references country.Code."
              "countrylanguage.CountryCode is a foreign key that references country.Code."
              "I want to explore the database."
              f'Can you help me write a MySQL query that addresses the following prompt: "{input}"'
              "Please return only the MySQL query and nothing else."
    )
    try:
        response = model.generate_content(prompt)
        print(f"LLM result:\n{response.text}")
        sql_code = extract_sql_from_response(response.text)
        print(f"MySQL query to execute:\n`{sql_code}`")
        result = mysql_helper_conn("world", sql_code, return_json=True)
        return {"query": sql_code, "result": result}
    except Exception as e:
        print(f"Error: {e}")

# Query function
def main_mysql_query_world(input):
    prompt = ("Given a MySQL database called world, with 3 tables named city, country, and countrylanguage."
              "The city table has 5 columns: ID, Name, CountryCode, District, Population."
              "The country table has 15 columns: Code, Name, Continent, Region, SurfaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2."
              "The countrylanguage table has 4 columns: CountryCode, Language, IsOfficial, Percentage."
              "city.CountryCode is a foreign key that references country.Code."
              "countrylanguage.CountryCode is a foreign key that references country.Code."
              "I want to query the tables of the database."
              f'Can you help me write a MySQL query that addresses the following prompt: "{input}"'
              "Please return only the MySQL query and nothing else."
    )
    try:
        response = model.generate_content(prompt)
        print(f"LLM result:\n{response.text}")
        sql_code = extract_sql_from_response(response.text)
        print(f"MySQL query to execute:\n`{sql_code}`")
        result = mysql_helper_conn("world", sql_code, return_json=True)
        return {"query": sql_code, "result": result}
    except Exception as e:
        print(f"Error: {e}")

# Modification function
def main_mysql_modify_world(input):
    prompt = ("Given a MySQL database called world, with 3 tables named city, country, and countrylanguage."
              "The city table has 5 columns: ID, Name, CountryCode, District, Population."
              "The country table has 15 columns: Code, Name, Continent, Region, SurfaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2."
              "The countrylanguage table has 4 columns: CountryCode, Language, IsOfficial, Percentage."
              "city.CountryCode is a foreign key that references country.Code."
              "countrylanguage.CountryCode is a foreign key that references country.Code."
              "I want to modify the data of the database like inserting, deleting, or updating."
              f'Can you help me write a MySQL query that addresses the following prompt: "{input}"'
              "Please return only the MySQL query and nothing else."
    )
    try:
        response = model.generate_content(prompt)
        print(f"LLM result:\n{response.text}")
        sql_code = extract_sql_from_response(response.text)
        print(f"Data modification code:\n`{sql_code}`")
        result = mysql_helper_conn("world", sql_code, return_json=True)
        return {"query": sql_code, "result": "Data modified!"}
    except Exception as e:
        print(f"Error: {e}")