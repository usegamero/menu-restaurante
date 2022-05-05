from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.Menu import *


def test_should_copy_menu():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()

    menu_restaurant_1 = Menu(
        id="01",
        date="2020-01-05",
        desc={
            "firsts": [
                {
                    "id_dish": "01",
                    "name_dish": "ensalada mixta",
                    "allergens": "ensalada con cebolla",
                }
            ]
        },
        id_restaurant="0001",
    )
    menu_restaurant_2 = Menu(
        id="02",
        date="2022-04-20",
        desc={
            "firsts": [
                {
                    "id_dish": "01",
                    "name_dish": "ensalada mixta",
                    "allergens": "ensalada con cebolla",
                }
            ]
        },
        id_restaurant="0002",
    )

    menu_repository.save(menu_restaurant_2)
    body = {"id": "12", "id_restaurant": "0002"}
    headers = {"Authorization": "0002"}
    response = client.post(
        "/api/menus/2022-04-20/copy/2022-10-04",
        json=body,
        headers={"Authorization": "0002"},
    )

    assert response.status_code == 200
    menu_get = client.get("/api/menus/by-date/2022-10-04", headers=headers)
    assert menu_get.json == {
        "id": "12",
        "date": "2022-10-04",
        "desc": {
            "firsts": [
                {
                    "id_dish": "01",
                    "name_dish": "ensalada mixta",
                    "allergens": "ensalada con cebolla",
                }
            ]
        },
        "id_restaurant": "0002",
    }
