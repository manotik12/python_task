# create and initialize a set
ea_cities = {"kampala", "nairobi", "arusha", "mombasa", "nairobi"}

print(ea_cities)
# printing length of cities
print(f"thre are {len(ea_cities)}cities in the set")
# print type of the data structure
print(type(ea_cities))
# adding items
ea_cities.add("kigali")
print(ea_cities)

west_african_continents = {"lagos", "accra"}
south_african_cities = {"cape town", "durban"}

master_city_list = {"new york"}
master_city_list.update(ea_cities)
print(master_city_list)
# master_city_list.update(west_african_continents)
# master_city_list.update(south_african_cities)
