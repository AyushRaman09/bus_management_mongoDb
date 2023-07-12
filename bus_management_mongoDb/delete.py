import pymongo


def delete_bus_nextStops(bus_name_for_delete):
    client = pymongo.MongoClient(
        "mongodb+srv://database:ngr2TTKh9xkrUTUF@cluster0.qjvazqb.mongodb.net/?retryWrites=true&w=majority")
    db = client["test"]
    bus_details = db["testing_bus_details"]
    bus_stops = db["testing_bus_stops"]

    # bus_name_for_delete = "231U"

    route_dict = (bus_details.find_one({"name": bus_name_for_delete}, {"_id": 0, "route": 1}))

    print(route_dict)

    bus_route_list = list(route_dict["route"])

    bus_route_list = list(dict.fromkeys(bus_route_list))

    # ***************
    # Dividing the route in list of 2 consecutive stops
    route_list = bus_route_list

    list_of_grp_two = []

    for i in range(0, (len(route_list))):

        if i != (len(route_list) - 1):
            grp_two = [route_list[i]]

            for j in range((i + 1), (i + 2)):
                if j != len(route_list):
                    grp_two.append(route_list[j])

            list_of_grp_two.append(grp_two)

            del grp_two

    for k in list_of_grp_two:
        print(k)

    list_to_pass_on=[]

    for i in range(len(bus_route_list)):
        print("Main Loop")
        print("*************************")
        print(bus_route_list[i])
        b = bus_stops.find_one({"name": bus_route_list[i]},
                               {"_id": 0, "buses": 1, "nextStops": 1})  # Getting the names of the buses from database
        bus_name_from_route = list(b["buses"])
        nextStops = list(b["nextStops"])
        print("Next Stops of the Stops of the route of the bus to be deleted : ", nextStops)

        verify_list = []

        for j in bus_name_from_route:
            print("2nd Loop")
            print(j)
            c = bus_details.find_one({"name": j}, {"_id": 0, "route": 1})
            route_of_buses = list(c["route"])
            route_of_buses = list(dict.fromkeys(route_of_buses))
            print(route_of_buses)

            for k in range(0, len(route_of_buses)):
                # print(list_of_grp_two[m][0])
                if list_of_grp_two[i][0] == route_of_buses[k]:
                    break

            length_of_route = len(route_of_buses)

            if k != (length_of_route - 1):
                if list_of_grp_two[i][1] == route_of_buses[k + 1]:
                    # print(list_of_grp_two[m][1])
                    print("Route have consecutive stops")
                    verify_list.append(1)
                else:
                    print("Routes don't have consecutive stops")
                    verify_list.append(0)

        verify_list = list(dict.fromkeys(verify_list))

        if len(verify_list) == 1:
            if verify_list[0] == 1:
                print("Nothing Changed")
            elif verify_list[0] == 0:
                print("deleted")
                nextStops_for_delete = nextStops

                list_to_pass_on.append(nextStops_for_delete)

                print("nextStops without change :- ", nextStops)

                # querry_for_deleting = {"nextStops": nextStops_for_deletion}
                #
                # print(querry_for_deleting)

                updated_nextStops = nextStops

                updated_nextStops.remove(list_of_grp_two[i][1])

                list_to_pass_on.append(updated_nextStops)

                print("NextStops After updations :- " ,updated_nextStops)

                # newValues_for_nextStops = {"$set": {"nextStops": updated_nextStops}}

                # bus_stops.update_one(querry_for_deleting, newValues_for_nextStops)

    print("****************list to pass on :-  ", list_to_pass_on)


    return "Done",list_to_pass_on





def delteing_bus_from_busStops(bus_name_for_delete):
    client = pymongo.MongoClient(
        "mongodb+srv://database:ngr2TTKh9xkrUTUF@cluster0.qjvazqb.mongodb.net/?retryWrites=true&w=majority")
    db = client["test"]
    bus_details = db["testing_bus_details"]
    bus_stops = db["testing_bus_stops"]

    # bus_name_for_delete = "231U"

    route_dict = (bus_details.find_one({"name": bus_name_for_delete}, {"_id": 0, "route": 1}))

    print(route_dict)

    bus_route_list = list(route_dict["route"])

    bus_route_list = list(dict.fromkeys(bus_route_list))

    for i in range(len(bus_route_list) ):
        # print("Main Loop")
        # print("*************************")
        print(bus_route_list[i])
        b = bus_stops.find_one({"name": bus_route_list[i]},
                               {"_id": 0, "buses": 1, "nextStops": 1})  # Getting the names of the buses from database
        bus_name_from_route = list(b["buses"])
        print(bus_name_from_route)

        updated_bus_name_for_route = bus_name_from_route

        updated_bus_name_for_route.remove(bus_name_for_delete)

        myquerry = {"name": bus_route_list[i]}
        print(myquerry)

        print(updated_bus_name_for_route)

        newvalues = {"$set": {"buses": updated_bus_name_for_route}}

        bus_stops.update_one(myquerry, newvalues)

    return "Done"
