import pytest
import requests
import allure

base_url= "https://swagger.rv-school.ru/api/v3/pet"

@allure.feature ("Питомец")
class TestPet:
    @allure.title("Добавление нового питомца")
    def test_add_pet(self):

        with allure.step("Подготовка данных"):

            body = {
                "id": 10,
                "name": "doggie",
                "category": {
                    "id": 1,
                    "name": "Dogs"
                },
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 0,
                        "name": "string"
                    }
                ],
                "status": "available"
            }
        response = requests.post(url=base_url, json=body)

        assert response.status_code == 200


