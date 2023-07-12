import pymongo

list_3 = ['Done', [['Athwa Gate', 'SVNIT'], ['Adajan Gam', 'Rander'], ['Ved Darwaja', 'Gajera Circle'],
                   ['Railway Station', 'Hero']]]

client = pymongo.MongoClient(
        "mongodb+srv://database:ngr2TTKh9xkrUTUF@cluster0.qjvazqb.mongodb.net/?retryWrites=true&w=majority")
db = client["test"]
bus_details = db["testing_bus_details"]
bus_stops = db["testing_bus_stops"]

if list_3[0] == 'Done':
    if len(list_3) > 1:
        for j in range(0, len(list_3[1]), 2):
                nextStops = list_3[1][j]
                print(nextStops)
                querry_for_deleting = {"nextStops": nextStops}

                updated_nextStops = list_3[1][j + 1]
                newValues_for_nextStops = {"$set": {"nextStops": updated_nextStops}}
                print(updated_nextStops)

                bus_stops.update_one(querry_for_deleting, newValues_for_nextStops)

