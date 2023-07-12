# from http import client
import plistlib
import string
import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://database:ngr2TTKh9xkrUTUF@cluster0.qjvazqb.mongodb.net/?retryWrites=true&w=majority")
db = client["test"]
name_database = db["testin_bus_details"]

a = "Athwa Gate"

bus_stops_details = name_database.find_one({"name": a}, {"_id": 0, "nextStops": 1})

# bus_stops_list= bus_stops_details

nextStops = list(bus_stops_details["nextStops"])
# print(type(nextStops))

b = "Kamrej"

nextStops.append(b)

print("repeated ", nextStops)

nextStops = list(dict.fromkeys(nextStops))

print("non repeated", nextStops)

myquerry = bus_stops_details

newvalues = {"$set": {"nextStops": nextStops}}


name_database.update_one(myquerry, newvalues)

# print(bus_stops_list)


# # _id = 11
# route = ["Adajan Gam", "Athwa Gate", "SVNIT", "Rander"]
# durations = [8, 5, 7]
# fares = [8, 11, 6]
# distance = [6, 8, 4]
# timings = ["9:00", "9:13", "9:18"]
#
#
# name="1593 B"
#
#
# bus_rec1 = {
#         "name": name,
#         "route": route,
#         "timings": timings,
#         "durations": durations,
#         "distance": distance,
#         "fares": fares,
#         "status": "on_time",
#     }

# rec_id1 = bus_details.insert_one(bus_rec1)


# delete_rec={
#         "name": "123 A"
# }
#
# delete= bus_details.delete_one(delete_rec)
