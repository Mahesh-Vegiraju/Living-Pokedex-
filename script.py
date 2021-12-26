import argparse

parser = argparse.ArgumentParser(description="Keeps track of the pokemon that you have caught.")
parser.add_argument("strings", metavar="Pokemon", nargs='+', help="a pokemon that was caught or released")
parser.add_argument("-caught", action="store_true", default=False, help="adds pokemon that you caught")
parser.add_argument("-released", action="store_true", default=False, help="marks pokemon that you have released")
parser.add_argument("-evolved", action="store_true", default=False, help="marks pokemon that you have evolved as unowned and evolution as owned")

args = parser.parse_args()

with open('sinnohDex.txt', 'r') as f:           # read all the pokemon into variable
	sinnohDex_contents = f.readlines()

caught_Dict = {}                                # hashmap for all pokemon and if they are caught

for line in sinnohDex_contents:                 # add all the pokemon and if caught to hashtable
	pokemon_and_caught = line.split(' ')
	pokemon, caught = pokemon_and_caught[0], pokemon_and_caught[1].strip()
	caught_Dict[pokemon] = caught

 
