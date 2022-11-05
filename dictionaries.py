# declaring a dictionary
my_phone = {
    "brand": "samsung",
    "make": "galaxy",
    "model": "s22",
    "yom": "2022",
    "origin": "south korea"
}
print(my_phone)
# printing just the brand and the make

print(f"my phone is a {my_phone['brand']} and it's a {my_phone['make']}")
# nested dictinary
my_phones = {
    "phone_one": {
        "brand": "samsung",
        "make": "galaxy",
        "model": "s22",
        "yom": "2022",
        "origin": "south korea"
    },
    "phone_two": {
        "brand": "node",
        "make": "galaxy",
        "model": "s22",
        "yom": "2022",
        "origin": "south korea"
    }
}

print(my_phones["phone_two"])

print("printing all the phones in the dictionary")
for phone in my_phones:
    print(my_phones[phone])
