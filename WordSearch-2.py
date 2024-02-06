# Below lists detail all eight possible movements from a cell
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


# Function to check if it is possible to go to position next
# from the current position. The function returns false if next is
# not in a valid position, or it is already visited
def isValid(mat, x, y, path):
	return (0 <= x < len(mat)) and (0 <= y < len(mat[0])) and (x, y) not in path


def DFS(mat, word, i, j, path=[], index=0):
	# first check if the letter we are on is in the word
	if mat[i][j] is not word[index]:
		return
	else:
		# add letter to path
		path.append([i,j])
		# increment index of word so we can look for next letter
		index = index + 1
		
		# if we matched the word 
		if index is len(word):
			# print the word and return it to stop the loop
			print(path)
			return path
		else:
			# initialize counter for loop
			x = 0
			# loop through possible movements
			for x in range(len(row)):
				# add indexes for possible movements
				k = i + row[x]
				l = j + col[x]
				# check if index is within range
				if isValid(mat, k, l, path):
					# check if the possible movement is the next word
					if mat[k][l] is word[index]:
						# if it is then we continue on with checking the rest of the path
						DFS(mat, word, k, l, path[:], index)
				# increment counter
				x = x + 1
		# remove letter from path if we do not have a match to the word
		return path.pop()


def WordSearch(mat, word):
	# base case
	if not mat or not len(mat) or not len(word):
		return

	for i in range(len(mat)):
		for j in range(len(mat[0])):
			DFS(mat, word, i, j)


if __name__ == '__main__':

	mat = [
		['A', 'D', 'E', 'B', 'C'],
		['O', 'O', 'C', 'A', 'X'],
		['S', 'C', 'D', 'K', 'C'],
		['O', 'D', 'E', 'H', 'L']
	]
	word = 'CODE'

	WordSearch(mat, word)
