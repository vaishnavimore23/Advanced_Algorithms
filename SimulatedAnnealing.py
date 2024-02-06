
import random
import decimal

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution =[]

    for i in range(len(tsp)):
        randomCity =cities[random.randint(0,len(cities)-1)]
        solution.append(randomCity)
        cities.remove(randomCity)


    return solution

def routelength(tsp,solution):
      routelength =0
      for i in range(len(solution)):
        routelength   += tsp[solution[i-1]][solution[i]]
      return routelength


def getNeighbours(solution):
     neighbours =[]
     for i in range(len(solution)):
        for j in range(i+1,len(solution)):
            neighbour = solution.copy()
            neighbour[i] =solution[j]
            neighbour[j]= solution[i]
            neighbours.append(neighbour)
     return neighbours       

def getBestNeighbours(tsp,neighbours):
    bestRouteLength= routelength(tsp,neighbours[0])
    bestneighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routelength(tsp,neighbour)
        if currentRouteLength<bestRouteLength:
            bestRouteLength =currentRouteLength
            bestneighbour = neighbour

    return bestneighbour, bestRouteLength



def simulatedAnnealing(tsp):
   # current state = initial state
   temp =10000

   # set a cooling factor 
   coolingFactor =0.8
   currentSolution = randomSolution(tsp)
   currentRouteLength = routelength(tsp,currentSolution)
   # for t =1 to max
   while temp>0.1:
     neighbours = getNeighbours(currentSolution)
     bestNeighbour, bestneighbourRouteLength= getBestNeighbours(tsp,neighbours)
     
        # calculate deltaE
     deltaE = bestneighbourRouteLength - currentRouteLength
      
      # calculate probability
     prob = decimal.Decimal(-deltaE/temp).exp()

     if bestneighbourRouteLength < currentRouteLength:
        currentRouteLength =bestneighbourRouteLength
        currentSolution =bestNeighbour
     else:
        if prob < random.randint(0,1):
            currentRouteLength =bestneighbourRouteLength
            currentSolution =bestNeighbour






   # T = temperature(time t)
   temp = (temp*coolingFactor)
   # get the neighbours
   # calculate deltaE
   # if deltaE >0:
       # currentstate = bestNeighbour
    #else:
     #take risk with probability of e^(deltaE/T)

   # return currentstate
   return currentSolution, currentRouteLength


def main():
    tsp = [
    [0,400,500,300],
    [400,0,300,500],
    [500,300,0,400],
    [300,500,400,0]

    ]    
    print("Simulated Annealing")
    print(simulatedAnnealing(tsp))


if __name__ == "__main__":
    main()