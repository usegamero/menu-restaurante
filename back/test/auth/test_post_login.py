from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.Restaurant import Restaurant, RestaurantRepository


def setup():
    user_repository = RestaurantRepository(temp_file())
    app = create_app(repositories={"restaurant": user_repository})
    client = app.test_client()

    restaurant = Restaurant(
        id_restaurant="restaurant_01", name="Tía Maruca", password="password01"
    )
    restaurant1 = Restaurant(
        id_restaurant="restaurant_02", name="Don Satur", password="password02"
    )
    user_repository.save_restaurants(restaurant)
    user_repository.save_restaurants(restaurant1)

    return client


def test_should_validate_login():
    client = setup()

    body = {"id_restaurant": "restaurant_01", "password": "password01"}
    response = client.post("/auth/login", json=body)

    assert response.status_code == 200
    assert response.json == {"id_restaurant": "restaurant_01", "name": "Tía Maruca"}
