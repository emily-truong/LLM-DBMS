from pymongo import MongoClient
import google.generativeai as genai 
import re
import json
import os
from dotenv import load_dotenv

# Loading API keys from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash-001")

# Explore schemas and data function
def mongodb_explore_sakila(input):
    prompt = ("Given a MongoDB database called sakila, with 3 collections named actor, film, and film_actor."
              "The actor collection has 3 fields: actor_id, first_name, and last_name."
              "The film collection has 12 fields: film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, and special_features."
              "The film_actor collection has 2 fields: actor_id and film_id."
              "film_actor.actor_id is a foreign key that references actor.actor_id."
              "film_actor.film_id is a foreign key that references film.film_id."
              "I want to query the collections of the database."
              "Please use the specified fields and do not use the default '_id: ObjectId' field from the collections for any of the requests."
              f'Can you help me write a MongoDB query for pymongo that addresses the following prompt: "{input}"'
              "Please return only the chain-method query and nothing else."
    )   
    try:
        response = model.generate_content(prompt)
        print(f"LLM output:\n{response.text.strip()}")
        query = re.search(r"(db\..*)", response.text.strip("```"), re.DOTALL)
        query = query.group(1)
        print(f"pymongo query to execute:\n{query}")
    except Exception as e:
        print(f"Error: {e}")
    client = MongoClient("mongodb+srv://adityave:DSCI551@dsci551.siuts.mongodb.net/?retryWrites=true&w=majority&appName=DSCI551")
    db = client["sakila"]
    allowed_globals = {"db": db}
    if query:
        try:
            query_result = eval(query, allowed_globals)
            result = [object for object in list(query_result)]
            client.close()
            return {"query": query, "result": result}
        except Exception as e:
            print(f"Error: {e}")
    client.close()
    return None

# Query function
def mongodb_query_sakila(input):
    prompt = ("Given a MongoDB database called sakila, with 3 collections named actor, film, and film_actor."
              "The actor collection has 3 fields: actor_id, first_name, and last_name."
              "The film collection has 12 fields: film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, and special_features."
              "The film_actor collection has 2 fields: actor_id and film_id."
              "film_actor.actor_id is a foreign key that references actor.actor_id."
              "film_actor.film_id is a foreign key that references film.film_id."
              "I want to explore the collections of the database and get sample data from the database."
              "Please use the specified fields and do not use the default '_id: ObjectId' field from the collections for any of the requests."
              f'Can you help me write a MongoDB query for pymongo that addresses the following prompt: "{input}"'
              "Please return only the chain-method query and nothing else."
    )  
    try:
        response = model.generate_content(prompt)
        print(f"LLM output:\n{response.text.strip()}")
        query = re.search(r"(db\..*)", response.text.strip("```"), re.DOTALL)
        query = query.group(1)
        print(f"pymongo query to execute:\n{query}")
    except Exception as e:
        print(f"Error: {e}")
    client = MongoClient("mongodb+srv://adityave:DSCI551@dsci551.siuts.mongodb.net/?retryWrites=true&w=majority&appName=DSCI551")
    db = client["sakila"]
    allowed_globals = {"db": db}
    if query:
        try:
            query_result = eval(query, allowed_globals)
            result = [object for object in list(query_result)]
            client.close()
            return {"query": query, "result": result}
        except Exception as e:
            print(f"Error: {e}")
    client.close()
    return None

# Data modification function
def mongodb_modify_sakila(input):
    prompt = ("Given a MongoDB database called sakila, with 3 collections named actor, film, and film_actor."
              "The actor collection has 3 fields: actor_id, first_name, and last_name."
              "The film collection has 12 fields: film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, and special_features."
              "The film_actor collection has 2 fields: actor_id and film_id."
              "film_actor.actor_id is a foreign key that references actor.actor_id."
              "film_actor.film_id is a foreign key that references film.film_id."
              "I want to modify (i.e. insert, delete, update) the collections of the database."
              "Please use the specified fields and do not use the default '_id: ObjectId' field from the collections for any of the requests."
              f'Can you help me write a MongoDB query for pymongo that addresses the following prompt: "{input}"'
              "Please return only the chain-method query and nothing else."
    ) 
    try:
        response = model.generate_content(prompt)
        print(f"LLM output:\n{response.text.strip()}")
        query = re.search(r"(db\..*)", response.text.strip("```"), re.DOTALL)
        query = query.group(1)
        print(f"pymongo query to execute:\n{query}")
    except Exception as e:
        print(f"Error: {e}")
    client = MongoClient("mongodb+srv://adityave:DSCI551@dsci551.siuts.mongodb.net/?retryWrites=true&w=majority&appName=DSCI551")
    db = client["sakila"]
    allowed_globals = {"db": db}
    if query:
        try:
            result = eval(query, allowed_globals)
            print("Modification was a success!")
            print(result)
            client.close()
            return {"query": query, "result": result}
        except Exception as e:
            print(f"Error: {e}")
    client.close()
    return None
