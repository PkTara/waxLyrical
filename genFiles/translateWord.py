
def translateWord(word:str, fromLanguage:str, toLanguage:str):

	import requests

	url = "https://google-translate113.p.rapidapi.com/api/v1/translator/html"

	payload = {
		"from": fromLanguage,
		"to": toLanguage,
		"html": word
	}
	headers = {
		"x-rapidapi-key": "83fbd70df5mshe78b3baaaa224eap19526bjsn09148140cff0",
		"x-rapidapi-host": "google-translate113.p.rapidapi.com",
		"Content-Type": "application/json"
	}

	response = requests.post(url, json=payload, headers=headers)

	return(response.json())
