import requests

URL = "https://api.pokemonbattle.ru/v2/"
TOKEN = "38dcb73780753f40e83983f5d2061fa2"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}

body_create = {"name": "Свиночка", "photo_id": -1}

response_create = requests.post(url=f"{URL}pokemons", headers=HEADER, json=body_create)
print(response_create.text)
response_data = response_create.json()
new_pok_id = response_data["id"]


response_get = requests.get(url=f"{URL}pokemons", params={"trainer_id": 30162})
print(response_get.text)
response_data = response_get.json()
pokemons_id = response_data["data"]
first_pokemon_id = pokemons_id[0]["id"]

print(first_pokemon_id)

body_change = {
    "pokemon_id": first_pokemon_id,
    "name": "Маленькая Свиночка",
    "photo_id": -1,
}
response_change = requests.put(url=f"{URL}pokemons", headers=HEADER, json=body_change)
print(response_change.text)

body_catch = {"pokemon_id": new_pok_id}
response_catch = requests.post(
    url=f"{URL}trainers/add_pokeball", headers=HEADER, json=body_catch
)
print(response_catch.status_code)

if response_catch.status_code == 400:
    print("Покемон уже впойман")
    next_pok_id = pokemons_id[1], ["id"]
    body_catch = {"pokemon_id": next_pok_id}

print(response_catch.status_code)
print(response_catch.text)
