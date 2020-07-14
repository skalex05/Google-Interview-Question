Routes = [
    ["DSM","LGA"],
    ["DSM","DEL"],
    ["LGA","BGI"],
    ["BGI","EYW"],
    ["EYW","HND"],
    ["HND","DEL"],
    ["DSM","EYW"],
    ["HND","SAD"]
    ]

def ExploreRoutes(startingAirport,destination,currentRoute = []):
    #Get Possible Routes From the starting airport
    possible = [route for route in Routes if (route[0] == startingAirport or route[1] == startingAirport) and not route in currentRoute]
    #If there are no more routes to explore, tell the algorithm its a dead end
    if possible == []:
        return [[None,None]]
    reachDest = [x for x in possible if x[0] == destination or x[1] == destination]
    #If the destination can be reached from this airport
    if reachDest != []:
        return reachDest
    else:
        completeRoutes = []
        #Look at the possible routes
        for route in possible:
            #Explore the next possible routes
            if route[0] == startingAirport:
                completeRoutes.append([route] + ExploreRoutes(route[1],destination,currentRoute + [route]))
            else:
                completeRoutes.append([route] + ExploreRoutes(route[0],destination,currentRoute + [route]))
        #Filter out routes that lead to a dead end
        completeRoutes = [route for route in completeRoutes if route[-1][0] != None]
        if completeRoutes != []:
            #Return the shortest route to the destination
            return sorted(completeRoutes,key = lambda r : len(r))[0]
        else:
            #Return an empty list if there are no routes to the destination
            return [[None,None]]

def CalculateRoute(startingAirport,destination,routes):
    route = ExploreRoutes(startingAirport,destination)
    #If the route returns None, there was no possible route
    if route == [[None,None]]:
        return False
    nextStartLoc = startingAirport
    result = []
    #Just flip flight routes for readability
    for flight in route:
        if flight[0] != nextStartLoc:
            result.append(flight[::-1])
        else:
            result.append(flight)
        nextStartLoc = result[-1][1]
    return len(route),result

while True:
    print("\n~~~ CALCULATE FLIGHT ~~~\n")
    result = CalculateRoute(input("Enter a starting airport:\n"),input("Enter a destination airport:\n"),Routes)
    if result != False:
        flightCount,path = result
        journey = path[0][0]
        for flight in path:
            journey += " --> "+flight[1]
        print("Minimum number of flights:",flightCount)
        print(journey)
    else:
        print("There was no possible route between those airports")
    
