import random


def randomSolution(tsp):
   cities = list(range(len(tsp)))
   solutions =[]
   for i in range(len(tsp)):
     randomciti =cities[random.randint(0,len(cities))]
     solutions.append(randomciti)
     cities.remove(randomciti)
     
   return solutions

def routeLenght(tsp,solution):
    routeLenght =0
    for i in range(len(solution)):
        routeLenght += tsp[solution[i-1]][solution[i]]
    return routeLenght

def getNeighbours(solution):
    neighbours= []

    for i in range(len(solution)):
        for j in range(i+1,len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j]= solution[i]
            neighbours.append(neighbour)

    return neighbour


def getBestNeighbours(tsp,neighbours):
    bestRoutelength =routeLenght(tsp,neighbours[0])
    bestNeighbour = neighbours[0]

    for neighbour in neighbours:
        currentRoutelength = routeLenght(tsp, neighbour)
        if currentRoutelength < bestNeighbour:
            bestRoutelength= currentRoutelength
            bestNeighbour= neighbour

    return bestNeighbour,bestRoutelength


def hillclimbing(tsp):

    # intialize current state
    # loop:
         # get the best neighbours out of all neighbours
         # if best neighbour not better than current state
            # return current state
         # currentstate= best neighbour
        

    currentSolution=randomSolution(tsp)
    currentRouteLength=routeLenght(tsp,currentSolution)
    neighbours=getNeighbours(currentSolution)
    bestNeighbour,bestNeighbourRouteLength=getBestNeighbours(tsp,neighbours)

    while BestNeighbourRoutelength< currentRoutelength:
     currentSolution = randomSolution(tsp)
     currentRoutelength = routeLenght(tsp,currentSolution)
     neighbours = getNeighbours(currentSolution)
     bestNeighbour , BestNeighbourRoutelength = getBestNeighbours(tsp,neighbours)


    return currentSolution,currentRoutelength



def mapGenerator(numcities):
    tsp=[]
    for i in range

def main():
    tsp= [
    [0,400,500,300],
    [400,0,300,500],
    [500,300,0,400],
    [300,500,400,0]

    ]
    print(hillclimbing(tsp))

if __name__ == "__main__":
    main()