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
def mongodb_explore_world(input):
    prompt = ("Given a MongoDB database called World, with 3 collections named City, Country, and CountryLanguage."
              "The City collection has 5 fields: _id, Name, CountryCode, District, Population. City _id has an Object with 'ID' as key."
              "The Country collection has 15 fields: _id, Name, Continent, Region, SurfaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2."
              "Country _id has an Object with 'Code' as key."
              "The CountryLanguage collection has 3 fields: _id, IsOfficial, Percentage."
              "CountryLanguage _id has an Object with two keys: 'CountryCode' and 'Language'."
              "City.CountryCode is a foreign key that references Country._id.Code."
              "CountryLanguage._id.CountryCode is a foreign key that references Country._id.Code."
              "I want to explore the collections of the database and get sample data from the database."
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
    db = client["World"]
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
def mongodb_query_world(input):
    prompt = ("Given a MongoDB database called World, with 3 collections named City, Country, and CountryLanguage."
              "The City collection has 5 fields: _id, Name, CountryCode, District, Population. City _id has an Object with 'ID' as key."
              "The Country collection has 15 fields: _id, Name, Continent, Region, SurfaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2."
              "Country _id has an Object with 'Code' as key."
              "The CountryLanguage collection has 3 fields: _id, IsOfficial, Percentage."
              "CountryLanguage _id has an Object with two keys: 'CountryCode' and 'Language'."
              "City.CountryCode is a foreign key that references Country._id.Code."
              "CountryLanguage._id.CountryCode is a foreign key that references Country._id.Code."
              "I want to query the collections of the database."
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
    db = client["World"]
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
def mongodb_modify_world(input):
    prompt = ("Given a MongoDB database called World, with 3 collections named City, Country, and CountryLanguage."
              "The City collection has 5 fields: _id, Name, CountryCode, District, Population. City _id has an Object with 'ID' as key."
              "The Country collection has 15 fields: _id, Name, Continent, Region, SurfaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2."
              "Country _id has an Object with 'Code' as key."
              "The CountryLanguage collection has 3 fields: _id, IsOfficial, Percentage."
              "CountryLanguage _id has an Object with two keys: 'CountryCode' and 'Language'."
              "City.CountryCode is a foreign key that references Country._id.Code."
              "CountryLanguage._id.CountryCode is a foreign key that references Country._id.Code."
              "I want to modify (i.e. insert, delete, update) the collections of the database."
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
    db = client["World"]
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
