import requests
import json

def searchFunction():
	# rating for OU is 1695
	# rating for all other tiers is 1630

	tiers = ['ou', 'uu', 'ru', 'nu', 'pu', 'zu']
	tier = input("What tier do you want usage statistics for? Please enter 'OU', 'UU', 'RU', 'NU', 'ZU', or 'PU'. ").lower()

	while True:
		if tier in tiers:
			break
		else:
			tier = input("Please enter a valid tier ('OU', 'UU', 'RU', 'NU', 'ZU', or 'PU') ").lower()

	rank = 1630

	if tier == 'ou':
		rank = 1695

	pokemon = input("What Pokemon do you want usage statistics for? ")

	response = requests.get("https://smogon-usage-stats.herokuapp.com/2021/08/gen8" + tier + "/" + str(rank) + "/" + pokemon).text
	response_info = json.loads(response)

	print(json.dumps(response_info, indent=4))

	searchAgain = input("\nWould you like to search again? [yes/no] \n").lower()
	if searchAgain == "yes":
		searchFunction()

searchFunction()
    