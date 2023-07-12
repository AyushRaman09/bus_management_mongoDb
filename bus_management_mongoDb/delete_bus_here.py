from delete import delteing_bus_from_busStops, delete_bus_nextStops
import pymongo

bus_name = input("Please Enter the Bus Name you Wanted to Delete :")
b = delteing_bus_from_busStops(bus_name)

if b == "Done":
    e = delete_bus_nextStops(bus_name)

    print("*************************")
    print(e)
    print("*************************")

    client = pymongo.MongoClient(
        "mongodb+srv://database:ngr2TTKh9xkrUTUF@cluster0.qjvazqb.mongodb.net/?retryWrites=true&w=majority")
    db = client["test"]
    bus_details = db["testing_bus_details"]
    bus_stops = db["testing_bus_stops"]

    if e[0] == 'Done':
        if len(e) > 1:
            for j in range(0, len(e[1]), 2):
                nextStops = e[1][j]
                print(nextStops)
                querry_for_deleting = {"nextStops": nextStops}

                updated_nextStops = e[1][j + 1]
                newValues_for_nextStops = {"$set": {"nextStops": updated_nextStops}}
                print(updated_nextStops)

                bus_stops.update_one(querry_for_deleting, newValues_for_nextStops)



