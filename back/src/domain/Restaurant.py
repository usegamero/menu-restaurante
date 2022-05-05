import sqlite3
import json


class Restaurant:
    def __init__(self, id_restaurant, name, password="NO PASSWORD"):
        self.id_restaurant = id_restaurant
        self.name = name
        self.password = password

    def to_dict(self):
        return {
            "id_restaurant": self.id_restaurant,
            "name": self.name,
        }


class RestaurantRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            CREATE table if not exists restaurants (
                id_restaurant varchar PRIMARY KEY,
                name varchar,
                password varchar
               
            )
        """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all_restaurants(self):
        sql = """SELECT * FROM restaurants """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        list_restaurants = cursor.fetchall()
        list_of_dicts_restaurants = []
        for item in list_restaurants:
            restaurant_class = Restaurant(
                id_restaurant=item["id_restaurant"], name=item["name"]
            )
            list_of_dicts_restaurants.append(restaurant_class)
        return list_of_dicts_restaurants

    # ---------------------------------------------------

    def get_by_id_restaurant(self, id_restaurant):
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            """SELECT * FROM restaurants WHERE id_restaurant =?""", (id_restaurant,)
        )
        data = cursor.fetchone()
        if data == None:
            restaurant = None

        else:

            restaurant = Restaurant(
                id_restaurant=data["id_restaurant"],
                name=data["name"],
                password=data["password"],
            )
        return restaurant

    def save_restaurants(self, restaurant):
        sql = """INSERT INTO restaurants (id_restaurant,name, password) VALUES (
            :id_restaurant, :name, :password
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "id_restaurant": restaurant.id_restaurant,
                "name": restaurant.name,
                "password": restaurant.password,
            },
        )
        conn.commit()

    def get_by_name(self, name):
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM restaurants WHERE name =?""", (name,))
        data = cursor.fetchone()
        if data == None:
            restaurant = None
            return restaurant

        else:

            restaurant = Restaurant(
                id_restaurant=data["id_restaurant"],
                name=data["name"],
                password=data["password"],
            )
            return restaurant.id_restaurant
