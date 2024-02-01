import json

jsonArr = {
  "Name": "Malakia",
  "Age": "17"
}

with open("newJson.json", "w+") as f:
  json.dump(jsonArr, f, indent=2)
