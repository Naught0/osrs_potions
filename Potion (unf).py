import requests, json
from lxml import html

data = None
with open("item-data.json", "r") as f:
	data = json.load(f)
	
def getPrice(item, kind):
	burl = "https://api.rsbuddy.com/grandExchange?a=guidePrice&i=%i"
	md = requests.get((burl % data[item]["id"])).text
	jmd = json.loads(md)
	return jmd[kind]

def getUnfProfit(name, item1, vow, item2):
	print("%s:\nPrice: %i\nProfit: %i\n"  % 
		  (name, (item2 + vow), (item1 + vow - item2)))

currp = {}

for item in ["tarromin", "harralander", "ranarr weed", "toadflax", "irit leaf", "avantoe", "kwuarm",
			 "vial of water", 
			 "tarromin potion (unf)", 
			 "harralander potion (unf)",
			 "ranarr potion (unf)",
			 "toadflax potion (unf)",
			 "irit potion (unf)",
			 "avantoe potion (unf)", 
			 "kwuarm potion (unf)"]:
	currp[item] = getPrice(item, "buying")

getUnfProfit("Tarromin", currp["tarromin potion (unf)"], 
		  currp["vial of water"], currp["tarromin"])
getUnfProfit("Harralander", currp["harralander potion (unf)"], 
		  currp["vial of water"], currp["harralander"])
getUnfProfit("Ranarr", currp["ranarr potion (unf)"], 
		  currp["vial of water"], currp["ranarr weed"])
getUnfProfit("Toadflax", currp["toadflax potion (unf)"], 
		  currp["vial of water"], currp["toadflax"])
getUnfProfit("Irit leaf", currp["irit potion (unf)"], 
		  currp["vial of water"], currp["irit leaf"])
getUnfProfit("Avantoe", currp["avantoe potion (unf)"],
		  currp["vial of water"], currp["avantoe"])
getUnfProfit("Kwuarm", currp["kwuarm potion (unf)"], 
		  currp["vial of water"], currp["kwuarm"])
