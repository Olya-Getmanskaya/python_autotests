import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2/"
TOKEN = "38dcb73780753f40e83983f5d2061fa2"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
TRAINER_ID = "30162"


def test_status_code():
    response = requests.get(url=f"{URL}trainers")
    assert response.status_code == 200


def test_part_of_response():
    response_get = requests.get(url=f"{URL}trainers", params={"trainer_id": TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == "Kvoka"


@pytest.mark.parametrize(
    "key, value",
    [
        ("trainer_name", "Kvoka"),
        ("avatar_id", 11),
        ("city", "Kvokchanskii"),
        ("is_premium", False),
    ],
)
def test_parametrize(key, value):
    response_parametrize = requests.get(
        url=f"{URL}trainers", params={"trainer_id": TRAINER_ID}
    )
    assert response_parametrize.json()["data"][0][key] == value
