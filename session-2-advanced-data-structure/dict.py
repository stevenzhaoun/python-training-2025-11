# Dict - Dictionary

# create dict

person = {"name": "Steven", "age": 25, "city": "beijing"}
empty = {}

# accessing value
print(person["name"])
print(person.get("age"))
# print(person["country"]) # raise error
print(person.get("country"))
print(person.get("country", "China"))

# search value
print("name" in person)

# interate
for key, value in person.items():
    print(f"{key} : {value}")

# update
person["name"] = 'John'
print(person)
person.update({"country": "China", "name": "Brad"})
print(person)

# combine
defaults = {"color": "Red", "size": "m"}
custom = {"size": "L"}

final = {**defaults, **custom}
print(final)

# dict common methods
print(person.keys())
print(person.items())
print(person.values())

# dict comprehension

evens_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(evens_dict)

prices = {"apple": 1.5, "pear": 2}
discounted_prices = {name: price * 0.9 for name, price in prices.items()}
print(discounted_prices)


