# """ when we are dealing with file from python to json and vice versa go with json.load() and json.dump() """

import json

data = {
    "Pune" : 15000,
    "Banglore" : 20000,
    "New York" : 25000
}

city = input("Enter a city name you wanted to add :")
population = int(input("Enter population count :"))
with open("/Prime 2.0 AI-ML/Python/File Handling/Json module/cities.json", "w") as f:
    data[city] = population
    json.dump(data, f, indent=4)

with open("/Prime 2.0 AI-ML/Python/File Handling/Json module/cities.json", "r") as f:
    # result = json.load(f)  # In load pass the file (f) not a dictionary...
    # print(result)
    print(f.read())


