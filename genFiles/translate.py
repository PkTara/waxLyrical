
with open("translateKey.txt", "r") as file:
	translateKey = file.read()

def translateWord(word:str, fromLanguage:str, toLanguage:str):

	import requests

	url = "https://google-translate113.p.rapidapi.com/api/v1/translator/html"

	payload = {
		"from": fromLanguage,
		"to": toLanguage,
		"html": word
	}
	headers = {
		"x-rapidapi-key": translateKey,
		"x-rapidapi-host": "google-translate113.p.rapidapi.com",
		"Content-Type": "application/json"
	}

	response = requests.post(url, json=payload, headers=headers)

	return(response.json()["trans"])
