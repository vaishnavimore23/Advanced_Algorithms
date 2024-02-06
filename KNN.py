
import math
import collections

def eucledianDistance(datapoint1,datapoint2):
        solution=0
        for i in range(len(datapoint1)):
            solution += math.pow((datapoint1[i]-datapoint2[i]),2)


        return math.sqrt(solution)


def knn(dataset, query,k):
    neighbour_distancesand_indices=[]
    #loop through every datapoint in the dataset
    for index,datapoint in enumerate(dataset):


    # calculate distance
       distance= eucledianDistance(datapoint[:-1],query) 

    #add the distances to the list
    neighbour_distancesand_indices.append((distance,index))   

    #sort the distance
    sorted_neighbour_distancesand_indices = sorted(neighbour_distancesand_indices)
     
    #get the first k nearest neighbour
    k_nearest_neighbour = sorted_neighbour_distancesand_indices[:len(sorted_neighbour_distancesand_indices)-k]

    # get the labels of "k" nearest neighbours
    k_nearest_label = [dataset[i][-1] for distance, i in k_nearest_neighbour]

    #return the most common category
    return collections.Counter(k_nearest_label).most_common(1)[0][0]



def main():
    dataset =[
        [22,67,1],
        [23,58,1],
        [21,71,1],
        [18,93,1],
        [19,86,1],
        [25,47,0],
        [27,41,0],
        [29,39,0],
        [31,34,0],
        [45,27,0],
        
    ]
    query =[17,19]
    print(knn(dataset,query,3))


if __name__ =="__main__":
    main()