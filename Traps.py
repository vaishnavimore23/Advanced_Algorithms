# check if specified row and column are valid matrix index
from collections import deque


  
t_list=deque()
n_of_states =0




def isValid(i, j, N, M):
	return (0 <= i < M) and (0 <= j < N)


# check boundary condition
def check_boundary(state,h,w):
    i,j= state
    return (0 <= i < h)and (0 <= j < w)
    
# check if node is visited
def checkVisited(i,j,matrix):
	return matrix[i][j] != 'V' and  matrix[i][j] == 'O'



#update the predefined values of T and W in result matrix
def updateTAndW(result):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 'T':
                 result[i][j]=0
            elif mat[i][j]=='W':
                 result[i][j]=-1
            else:
                continue

#function to calculate the shortest distance of O from nearest T
def shortestDistanceToTraps(mat):
	#check for T in mat and store coordinates of T in t_list deque
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			if mat[i][j] == 'T':
				t_list.append((i,j,0))
	
	h= len(mat)
	w = len(mat[0])
	#create result matrix with the same dimentions as mat
	result= [([0]*w) for i in range(h)] 
	updateTAndW(result)
	
	 
	# list to get the indices of neighbours of current state
	row = [0, -1, 0, 1]
	col = [-1, 0, 1, 0]
	
	
	while t_list:
		#remove first element of the queue
		l, m, distance = t_list.popleft()
		
		#iterate for each neighbour
		for i in range(len(row)):
			if check_boundary((l+row[i],m+col[i]),h,w): 
				if checkVisited(l+row[i],m+col[i],mat) :
					result[l + row[i]][m + col[i]] = distance + 1
					mat[l + row[i]][m + col[i]]='V'
					t_list.append((l + row[i], m + col[i], distance + 1))
					
				
	return result




if __name__ == '__main__':

	mat = [
		['O', 'O', 'T', 'O', 'O'],
		['O', 'W', 'O', 'T', 'O'],
		['W', 'T', 'O', 'O', 'W'],
		['O', 'O', 'O', 'O', 'O']
	]

	result = shortestDistanceToTraps(mat)

	# print results
	for r in result:
		print(r)

