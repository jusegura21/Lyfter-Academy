#Ejercicio JSON
#Pendiente generar el ciclo del menu para conotinuar añadiendo pokemons y poner los exceptions. 
import json
import os

def open_and_add(path,data):
    with open(path, 'r+',encoding='utf-8') as file:
        x=file.read()
        y=json.loads(x)
        y.append(data)
        file.seek(0)
        z=json.dumps(y, indent=4)
        file.write(z)
        
def create_pokemon():
    pokemon={
    'name': {'english': ''},
    'type': [''],
    'base': {
      'HP': 0,
      'Attack': 0,
      'Defense': 0,
      'Sp. Attack': 0,
      'Sp. Defense':0,
      'Speed':0
    }}
    return pokemon

def main():
    while True:
        pokemon=create_pokemon()
        print("You are about to add a pokemon to the Pokedex. Press Enter to continue")
        pokemon['name']['english']=input("Add the pokemon name ")
        pokemon["type"][0]=input("Add the pokemon type ")
        pokemon['base']['HP']=input("Add the pokemon Health Points ")
        pokemon['base']['Attack']=input("Add the pokemon Attack ")
        pokemon['base']['Defense']=input("Add the pokemon Defense ")
        pokemon['base']['Sp. Attack']=input("Add the pokemon Sp. Attack ")
        pokemon['base']['Sp. Defense']=input("Add the pokemon Sp. Defense ")
        pokemon['base']['Speed']=input("Add the pokemon Speed ")
        open_and_add('pokemon.json',pokemon)
        print(f"Pokemon {pokemon['name']['english']} added succesfully.")
        while True:
            try: 
                print("Press 1 to add another pokemon or any other number to close the program... :")
                a=int(input())
                break
            except ValueError as error:
                print(f"Invalid input:{error}")

        if a!=1:
            break
    
    
os.chdir(os.path.dirname(os.path.abspath(__file__))) #defining the path of the current folder
main()