# dict = {
#     "bug" : "moth",
#     "gojo" : "satoru"
#     }

# print(dict["bug"])

# dict["feel"] = "alive"

# # Wipe a dictionary
# # dict = {}
# # print(dict)

# #Edit an item
# dict["feel"] = "more alive"

# for key in dict:
#     print(key)
#     print(dict[key])

# travel_log = {
# "France" : ["Paris", "Lille", "Dijon"],
# "Germany" : ["Stuttgart", "Berlin"],
# }

# print(travel_log["France"][1])

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
}

print(travel_log["Germany"]["cities_visited"][2])