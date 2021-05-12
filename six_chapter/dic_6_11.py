cities = {
    "beijing": {
        "country": "china",
        "population": 500000,
        "fact": "It is the capital of China."
        },
    "new york": {
        "country": "UAS",
        "population": 400000,
        "fact": "It is the economic center of USA."
        },
    "seoul": {
        "country": "south korea",
        "population": 200000,
        "fact": "It is the capital of South Korea."
        },
    }
for city, values in cities.items():
    print("\n" + city.title() + "'s information are: ")
    for key, value in values.items():
        print("\tThe " + key + " is: " + str(value))
