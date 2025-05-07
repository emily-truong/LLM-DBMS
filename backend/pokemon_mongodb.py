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
def mongodb_explore_pokemon(input):
    prompt = ("Given a MongoDB database called pokemon_db, with 4 collections named pokemon, pokemon_types, types, and base_stats."
              "The pokemon collection has 5 fields: pok_id, pok_name, pok_height, pok_weight, pok_base_experience."
              "The pokemon_types collection has 3 fields: pok_id, type_id, slot."
              "The types collection has 3 fields: type_id, type_name, damage_type_id."
              "The base_stats collection has 7 fields: pok_id, b_hp, b_atk, b_def, b_sp_atk, b_sp_def, b_speed."
              "I want to explore the collections of the database and get sample data from the database."
              "Please use the specified *_id fields and do not use the default '_id: ObjectId' field from the collections for any of the requests."
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
    # Edit line below to replace with appropriate connection
    client = MongoClient("mongodb+srv://adityave:DSCI551@dsci551.siuts.mongodb.net/?retryWrites=true&w=majority&appName=DSCI551")
    db = client["pokemon_db"]
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
def mongodb_query_pokemon(input):
    prompt = ("Given a MongoDB database called pokemon_db, with 4 collections named pokemon, pokemon_types, types, and base_stats."
              "The pokemon collection has 5 fields: pok_id, pok_name, pok_height, pok_weight, pok_base_experience."
              "The pokemon_types collection has 3 fields: pok_id, type_id, slot."
              "The types collection has 3 fields: type_id, type_name, damage_type_id."
              "The base_stats collection has 7 fields: pok_id, b_hp, b_atk, b_def, b_sp_atk, b_sp_def, b_speed."
              "I want to query the collections of the database."
              "Please use the specified *_id fields and do not use the default '_id: ObjectId' field from the collections for any of the requests."
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
    # Edit line below to replace with appropriate connection
    client = MongoClient("mongodb+srv://adityave:DSCI551@dsci551.siuts.mongodb.net/?retryWrites=true&w=majority&appName=DSCI551")
    db = client["pokemon_db"]
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
def mongodb_modify_pokemon(input):
    prompt = ("Given a MongoDB database called pokemon_db, with 4 collections named pokemon, pokemon_types, types, and base_stats."
              "The pokemon collection has 5 fields: pok_id, pok_name, pok_height, pok_weight, pok_base_experience."
              "The pokemon_types collection has 3 fields: pok_id, type_id, slot."
              "The types collection has 3 fields: type_id, type_name, damage_type_id."
              "The base_stats collection has 7 fields: pok_id, b_hp, b_atk, b_def, b_sp_atk, b_sp_def, b_speed."
              "I want to modify (i.e. insert, delete, update) the collections of the database."
              "Please use the specified *_id fields and do not use the default '_id: ObjectId' field from the collections for any of the requests."
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
    # Edit line below to replace with appropriate connection
    client = MongoClient("mongodb+srv://adityave:DSCI551@dsci551.siuts.mongodb.net/?retryWrites=true&w=majority&appName=DSCI551")
    db = client["pokemon_db"]
    allowed_globals = {"db": db}
    if query:
        try:
            result = eval(query, allowed_globals)
            print("Modification was a success!")
            print(result)
            client.close()
            return {"query": query, "result": "Data modified!"}
        except Exception as e:
            print(f"Error: {e}")
    client.close()
    return None
