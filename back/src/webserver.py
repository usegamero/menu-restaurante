from xml.dom.minidom import Identified
from flask import Flask, jsonify, request
from flask_cors import CORS
from src.lib.utils import object_to_json
from src.domain.Menu import Menu
from src.domain.Restaurant import Restaurant
from datetime import datetime


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def home():
        return "Bienvenido/a"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)

    @app.route("/api/menus", methods=["GET"])
    def show_menu():
        id_restaurant = request.headers.get("Authorization")
        menu = repositories["menu"].search_by_id_restaurant(id_restaurant)
        return object_to_json(menu)

    @app.route("/api/menus", methods=["POST"])
    def add_menu():
        id_restaurant = request.headers.get("Authorization")
        body = request.json
        save_menu = Menu(
            id=body["id"],
            date=body["date"],
            desc=body["desc"],
            id_restaurant=body["id_restaurant"],
        )
        if id_restaurant == save_menu.id_restaurant:
            repositories["menu"].save(save_menu)

            return "", 200
        else:
            return "", 403

    @app.route("/api/menus", methods=["PUT"])
    def modify_menu():
        id_restaurant = request.headers.get("Authorization")
        body = request.json
        update_menu = Menu(**body)
        if id_restaurant == update_menu.id_restaurant:
            repositories["menu"].modify_a_menu(update_menu)
            return "", 200
        else:
            return "", 403

    @app.route("/api/menus/by-date/<date>", methods=["GET"])
    def show_menu_by_date(date):
        id_restaurant = request.headers.get("Authorization")
        menu = repositories["menu"].get_by_date(date, id_restaurant)
        print(menu)
        if id_restaurant == menu.id_restaurant:
            return object_to_json(menu), 200
        else:
            return "", 403

    @app.route("/api/menus/<id>", methods=["GET"])
    def show_menu_by_id(id):
        id_restaurant = request.headers.get("Authorization")
        menu = repositories["menu"].get_by_id(id)
        if id_restaurant == menu.id_restaurant:
            return object_to_json(menu), 200
        else:
            return "", 403

    @app.route("/api/restaurants", methods=["GET"])
    def restaurants_get_all():
        restaurant = repositories["restaurant"].get_all_restaurants()
        return object_to_json(restaurant)

    @app.route("/api/menus/<origin_date>/copy/<new_date>", methods=["POST"])
    def copy_menu(origin_date, new_date):
        id_restaurant = request.headers.get("Authorization")
        old_menu = repositories["menu"].get_by_date(origin_date, id_restaurant)

        body = request.json
        new_menu = Menu(
            id=body["id"],
            date=new_date,
            desc=old_menu.desc,
            id_restaurant=body["id_restaurant"],
        )

        repositories["menu"].save(new_menu)
        return ""

    @app.route("/auth/login", methods=["POST"])
    def login():
        body = request.json
        restaurant = repositories["restaurant"].get_by_id_restaurant(
            body["id_restaurant"]
        )

        if restaurant is None or (body["password"]) != restaurant.password:

            return "", 401

        return object_to_json(restaurant), 200

    @app.route("/api/menu-today/<name_restaurant>", methods=["GET"])
    def show_menu_today(name_restaurant):
        date = datetime.today().strftime("%Y-%m-%d")
        id_restaurant = repositories["restaurant"].get_by_name(name_restaurant)
        if id_restaurant == None:
            return " ", 404
        else:
            menu = repositories["menu"].get_by_date(date, id_restaurant)
            if menu == None:
                return " ", 404
            menu_object = menu.to_dict()
            return jsonify(menu_object["desc"]), 200

    return app
