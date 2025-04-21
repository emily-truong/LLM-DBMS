from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Import functions from each module
from pokemon_mysql import (
    main_mysql_explore_pokemon,
    main_mysql_query_pokemon,
    main_mysql_modify_pokemon
)
from pokemon_mongodb import (
    mongodb_explore_pokemon,
    mongodb_query_pokemon,
    mongodb_modify_pokemon
)
from sakila_mysql import (
    main_mysql_explore_sakila,
    main_mysql_query_sakila,
    main_mysql_modify_sakila
)
from sakila_mongodb import (
    mongodb_explore_sakila,
    mongodb_query_sakila,
    mongodb_modify_sakila
)
from world_mysql import (
    main_mysql_explore_world,
    main_mysql_query_world,
    main_mysql_modify_world
)
from world_mongodb import (
    mongodb_explore_world,
    mongodb_query_world,
    mongodb_modify_world
)

# Initialize app
load_dotenv()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.route("/", methods=["GET"])
def home():
    return "Flask is working and ready to handle routes!"

# Unified route handler
@app.route("/<category>/<action>", methods=["POST"])
def handle_all_routes(category, action):
    data = request.get_json()
    prompt = data.get("prompt", "")

    if category == "pokemon":
        if action == "explore":
            return jsonify(mongodb_explore_pokemon(prompt) if data.get("dbType") == "nosql" else main_mysql_explore_pokemon(prompt))
        elif action == "query":
            return jsonify(mongodb_query_pokemon(prompt) if data.get("dbType") == "nosql" else main_mysql_query_pokemon(prompt))
        elif action == "modify":
            return jsonify(mongodb_modify_pokemon(prompt) if data.get("dbType") == "nosql" else main_mysql_modify_pokemon(prompt))

    elif category == "sakila":
        if action == "explore":
            return jsonify(mongodb_explore_sakila(prompt) if data.get("dbType") == "nosql" else main_mysql_explore_sakila(prompt))
        elif action == "query":
            return jsonify(mongodb_query_sakila(prompt) if data.get("dbType") == "nosql" else main_mysql_query_sakila(prompt))
        elif action == "modify":
            return jsonify(mongodb_modify_sakila(prompt) if data.get("dbType") == "nosql" else main_mysql_modify_sakila(prompt))

    elif category == "world":
        if action == "explore":
            return jsonify(mongodb_explore_world(prompt) if data.get("dbType") == "nosql" else main_mysql_explore_world(prompt))
        elif action == "query":
            return jsonify(mongodb_query_world(prompt) if data.get("dbType") == "nosql" else main_mysql_query_world(prompt))
        elif action == "modify":
            return jsonify(mongodb_modify_world(prompt) if data.get("dbType") == "nosql" else main_mysql_modify_world(prompt))

    return jsonify({"error": "Invalid category or action."}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
