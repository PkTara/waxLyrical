import json

def readJSON():
    with open("../songDatabase.json", "r") as json_data:
        data = json.load(json_data)
        lengthJSON = len(data.keys())
        return(data, lengthJSON)

def writeJSON(JSON_input):
    data, lengthJSON = readJSON()
    data[str(lengthJSON + 1)] = JSON_input

    
    with open("../songDatabase.json", "w") as json_data:
        data[str(lengthJSON + 1)] = JSON_input
        json_data.write(json.dumps(data))
