profile = {
    "name": "Ayoko Delia",
    "email": "d3liaayoko@gmail.com",
    "age": "20",
    "phone number": 674972661
}
print(profile)
profile.update({"gender":"Female"})
print(profile)
profile["name"] = "John Junior"
print(profile)
print(profile["name"])

des = profile
desdup = profile.copy()

profile["name"] = "Karlson"
profile["name"] = "Delia"

print(des)
print(desdup)