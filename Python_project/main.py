import requests
import json

token = 'Здесь будет токен'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Лёлик",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 1485,
    "name": "Болик",
    "photo": ""
})

print(response_put.text)


response_pokebol = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token' : token}, json={
    "pokemon_id": "1485"
})

print(response_pokebol.text)
