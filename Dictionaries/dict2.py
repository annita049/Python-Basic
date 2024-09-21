


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020      # duplicate "key" will overwrite the existing values
}


print(len(car))    # doesnt count duplicate key values
print(car["year"])
j= car.get("model")
print(j)
print(type(j))

car["year"] = 2024       # changing the key value to a different value
print(car.get("year"))

