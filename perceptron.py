import random
def dotproduct(weights, feautures):
    value=0

    for index in  range(2):
        value += weights[index]* feautures[index]
    if value>1:
        return 1 # rain
    else:
        return 0 # no rain

def perceptron(dataset,query):
    #initialise weights
    weights =[random.random() for x in range(2)]
    epochs =20
    # intitalize learning rate 
    learningRate =0.1
    while epochs>0:
        epochs-=1

        # loop over all the datapoints in dataset
        for dataPoint in dataset:

           #predict the output
           y = dotproduct(weights,dataPoint)
           actualOutput =dataPoint[-1]

           #calculate error
           error = actualOutput-y

           #if predicted not equal to actual  
           # update wights 
           if error !=0:
             for index in range(2):
                weights[index] = weights[index]+ (error * dataPoint[index]* learningRate )
    predict = dotproduct(weights,query) 
    return predict


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
    query =[17,90]
    prediction = perceptron(dataset,query)
    if prediction ==1:
        print("Its gona rain")
    else:
        print("no rain")


if __name__ =="__main__":
    main()