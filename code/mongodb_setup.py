from pymongo import MongoClient, InsertOne
import json

# MongoDB connection 
# edit to your own MongoDB connection, we have provided our own as a default
client = MongoClient("mongodb+srv://adityave:DSCI551@dsci551.siuts.mongodb.net/?retryWrites=true&w=majority&appName=DSCI551")


# World database
# Load json data into Country collection of World database
db = client.World
country_collection = db.Country
requesting = []
with open(r"../database_data/MongoDB_json/world/country-mongodb.json") as f:
    for json_object in f:
        myDict = json.loads(json_object)
        requesting.append(InsertOne(myDict))
result1 = country_collection.bulk_write(requesting)

# Load json data into City collection of World database
city_collection = db.City
requesting2 = []
with open(r"../database_data/MongoDB_json/world/city-mongodb.json") as f2:
    for json_object in f2:
        myDict = json.loads(json_object)
        requesting2.append(InsertOne(myDict))
result2 = city_collection.bulk_write(requesting2)

# Load json data into CountryLanguage collection of World database
clanguage_collection = db.CountryLanguage
requesting3 = []
with open(r"../database_data/MongoDB_json/world/countrylanguage-mongodb.json") as f3:
    for json_object in f3:
        myDict = json.loads(json_object)
        requesting3.append(InsertOne(myDict))
result3 = clanguage_collection.bulk_write(requesting3)


# pokemon_db database
# Load json data into pokemon collection of pokemon_db database
db = client.pokemon_db
pokemon_collection = db.pokemon
requesting = []
with open(r"../database_data/MongoDB_json/pokemon_db/pokemon.json") as f1:
    for json_object in f1:
        myDict = json.loads(json_object)
        requesting.append(InsertOne(myDict))
result1 = pokemon_collection.bulk_write(requesting)

# Load json data into pokemon_types collection of pokemon_db database
pokemon_types_collection = db.pokemon_types
requesting = []
with open(r"../database_data/MongoDB_json/pokemon_db/pokemon_types.json") as f2:
    for json_object in f2:
        myDict = json.loads(json_object)
        requesting.append(InsertOne(myDict))
result2 = pokemon_types_collection.bulk_write(requesting)

# Load json data into base_stats collection of pokemon_db database
base_stats_collection = db.base_stats
requesting = []
with open(r"../database_data/MongoDB_json/pokemon_db/base_stats.json") as f3:
    for json_object in f3:
        myDict = json.loads(json_object)
        requesting.append(InsertOne(myDict))
result3 = base_stats_collection.bulk_write(requesting)

# Load json data into types collection of pokemon_db database
types_collection = db.types
requesting = []
with open(r"../database_data/MongoDB_json/pokemon_db/types.json") as f4:
    for json_object in f4:
        myDict = json.loads(json_object)
        requesting.append(InsertOne(myDict))
result4 = types_collection.bulk_write(requesting)

pokemon_collection = db.pokemon
pokemon_collection.update_many(
    {},  # Match all documents
    [
        {
            "$set": {
                "pok_id": { "$toInt": "$pok_id" },
                "pok_height": { "$toInt": "$pok_height" },
                "pok_weight": { "$toInt": "$pok_weight" },
                "pok_base_experience": { "$toInt": "$pok_base_experience" }
            }
        }
    ]
)
pokemon_types_collection = db.pokemon_types
pokemon_types_collection.update_many(
    {},  # Match all documents
    [
        {
            "$set": {
                "pok_id": { "$toInt": "$pok_id" },
                "type_id": { "$toInt": "$type_id" },
                "slot": { "$toInt": "$slot" }
            }
        }
    ]
)
types_collection = db.types
types_collection.update_many(
    {},  # Match all documents
    [
        {
            "$set": {
                "type_id": { "$toInt": "$type_id" },
                "damage_type_id": { "$toInt": "$damage_type_id" }
            }
        }
    ]
)
base_stats_collection = db.base_stats
base_stats_collection.update_many(
    {},  # Match all documents
    [
        {
            "$set": {
                "pok_id": { "$toInt": "$pok_id" },
                "b_hp": { "$toInt": "$b_hp" },
                "b_atk": { "$toInt": "$b_atk" },
                "b_def": { "$toInt": "$b_def" },
                "b_sp_atk": { "$toInt": "$b_sp_atk" },
                "b_sp_def": { "$toInt": "$b_sp_def" },
                "b_speed": { "$toInt": "$b_speed" }
            }
        }
    ]
)


# sakila database
# Load json data into actor collection of sakila database
db = client.sakila
actor_collection = db.actor
requesting = []
with open(r"../database_data/MongoDB_json/sakila/actor.json") as f1:
    for json_object in f1:
        myDict = json.loads(json_object)
        requesting.append(InsertOne(myDict))
result1 = actor_collection.bulk_write(requesting)

# Load json data into film collection of sakila database
film_collection = db.film
requesting = []
with open(r"../database_data/MongoDB_json/sakila/film.json") as f2:
    for json_object in f2:
        myDict = json.loads(json_object)
        requesting.append(InsertOne(myDict))
result2 = film_collection.bulk_write(requesting)

# Load json data into film_actor collection of sakila database
film_actor_collection = db.film_actor
requesting = []
with open(r"../database_data/MongoDB_json/sakila/film_actor.json") as f3:
    for json_object in f3:
        myDict = json.loads(json_object)
        requesting.append(InsertOne(myDict))
result3 = film_actor_collection.bulk_write(requesting)

actor_collection.update_many(
    {},  # Match all documents
    [
        {
            "$set": {
                "actor_id": { "$toInt": "$actor_id" }
            }
        }
    ]
)
film_collection.update_many(
    {},  # Match all documents
    [
        {
            "$set": {
                "film_id": { "$toInt": "$film_id" },
                "release_year": { "$toInt": "$release_year" },
                "language_id": { "$toInt": "$language_id" },
                "original_language_id": { "$toInt": "$original_language_id" },
                "rental_duration": { "$toInt": "$rental_duration" },
                "rental_rate": { "$toDouble": "$rental_rate" },
                "length": { "$toInt": "$length" },
                "replacement_cost": { "$toDouble": "$replacement_cost" }
            }
        }
    ]
)
film_actor_collection.update_many(
    {},  # Match all documents
    [
        {
            "$set": {
                "actor_id": { "$toInt": "$actor_id" },
                "film_id": { "$toInt": "$film_id" }
            }
        }
    ]
)
