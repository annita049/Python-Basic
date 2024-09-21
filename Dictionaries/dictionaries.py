# ... Dictionaries are ...

# Ordered (Iterable)
# Changeable
# Dont allow Duplicate values


chatbot = {"model": "gpt-3.5",
           "company": "openai",
           "year": 2020}

country_capitals = {
    "Canada": "Ottawa",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Japan": "Tokyo",
    "China": "Beijing"
}

sqaures_dict = {x: x*x for x in range(5)}

print(chatbot["year"])
chatbot["model"] = "gpt-4"
print(chatbot["model"])

print(len(chatbot))
print(chatbot.keys())
print(chatbot.values())

for items in sqaures_dict:
    print(items)

print("\n")

for key in country_capitals:
    print(key, country_capitals[key])

print("\n")   

del country_capitals["Canada"]

for key in country_capitals:
    print(key, country_capitals[key])

print("\n")

for keys, values in chatbot.items():
    print(keys, values)

print("Italy" in country_capitals)  # prints True or False