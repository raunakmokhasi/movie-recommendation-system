from numpy import *
from scipy import spatial
import copy



def meanFinder(matrix,rated_or_not):
	num_movies = matrix.shape[0]
	matrix_mean = zeros(shape = (num_movies,1))
	for x in range(num_movies):
		index = where(rated_or_not[x] == 1)[0]
		matrix_mean[x] = mean(matrix[x , index])
	return matrix_mean

def normalise_ratings(matrix,matrix_mean, rated_or_not):
	num_movies = matrix.shape[0]
	matrix_norm = zeros(shape = matrix.shape)
	for x in range(num_movies):
		index = where(rated_or_not[x] == 1)[0]
		matrix_norm[x, index] = matrix[x,index] - matrix_mean[x]
	return matrix_norm


#10 movies 5 users (1 user added later)

#ITEM ITEM

#Hardcoding the array for the initial 5 users

def itemFilter(my_rating):
	matrix = array([[2,1,4,3,5],[3,4,1,2,4],[1,0,4,3,2],[1,1,4,4,0],[0,4,3,2,1],[1,4,0,5,4],[5,3,1,2,5],[1,0,0,5,2],[1,3,3,4,5],[2,2,5,3,1],[5,4,3,2,0],[1,3,4,2,1],[1,5,4,3,5],[5,4,3,2,1],[1,0,3,1,4]])

	my_ratings = zeros((matrix.shape[0], 1))
	my_ratings[0] = my_rating[0]
	my_ratings[1] = my_rating[1]
	my_ratings[2] = my_rating[2]
	my_ratings[3] = my_rating[3]
	my_ratings[4] = my_rating[4]
	

	rated_or_not = (matrix != 0) * 1




	'''
	for x in range(len(ratings_submitted)):
		my_ratings[x] = ratings_submitted[x]
	'''

	matrix = append(my_ratings,matrix,axis = 1 )
	rated_or_not = append(((my_ratings != 0) * 1),rated_or_not,axis = 1)

	# print()
	# print(matrix)
	# print()
	# print()
	# print(rated_or_not)


	matrix_mean = meanFinder(matrix,rated_or_not)
	matrix_norm = normalise_ratings(matrix,matrix_mean, rated_or_not)


	# print()
	# print()
	# print(matrix_mean)
	# print()
	# print()
	# print(matrix_norm)  

	# print()
	# print()
	# print()
	# print()

	similar = zeros((matrix.shape[0], matrix.shape[0]))

	for i in range(0,matrix_norm.shape[0]):
		currMat = matrix_norm[i]
		for j in range(0,matrix_norm.shape[0]):
			nextMat = matrix_norm[j]
			if(i == j):
				similar[i,j] = -9999
			else:
				result = 1 - spatial.distance.cosine(currMat,nextMat)		#Instead of calculating manually by doing squaring and rooting
				if(isnan(result)):
					similar[i,j] = 9999
				else:	
					similar[i,j] = result

	'''
	k = 4

	kLarge = zeros((similar.shape[0], num_movies ))
	kFinal = zeros((similar.shape[0], k ))

	# print()
	# print()

	for x in range(similar.shape[0]):
		kLarge[x] = arr.argsort()[(-1*num_movies):][::-1]
		#kLarge[x] = argpartition(similar[x], (-1 * k))[(-1 * k):]

	for x in range(similar.shape[0]):
		kFinal[x] = arr.argsort()[(-1*k):][::-1]

	for x in kLarge:
		if(x in kFinal):
			kFinal.remove(x)
			kFinal.add(k + 1)
			k += 1

	# print(kLarge) #These are the indices for the k most similar movies for each of the users
	# print()
	# print("FINAL ANS")
	# print()
	# print()
	return (kLarge[0]) #These are the indices for the k most similar movies for US
	'''

	# print(similar[0])

	k = 3

	kLarge = copy.deepcopy(similar[0])
	kLarge = sort(kLarge)
	
	newArr = similar[0].tolist()

	finalArr = []

	ctr = 0
	for x in range(len(kLarge)):
		if(not(newArr.index(kLarge[len(kLarge) - x - 1]) in [0,1,2,3,4])):
			finalArr.append(newArr.index(kLarge[len(kLarge) - x - 1]))
			ctr += 1
		if(ctr > k):
			break

	# print()
	# print()
	# print(newArr)

	# print(finalArr)

	# print(kLarge) #These are the indices for the k most similar movies for each of the users
	# print()
	# print("FINAL ANS")
	# print()
	# print()
	return (finalArr) #These are the indices for the k most similar movies for US

if __name__ == '__main__':
	matrix = array([[2,1,4,3,5],[3,4,1,2,4],[1,0,4,3,2],[1,1,4,4,0],[0,4,3,2,1],[1,4,0,5,4],[5,3,1,2,5],[1,0,0,5,2],[1,3,3,4,5],[2,2,5,3,1],[5,4,3,2,0],[1,3,4,2,1],[1,5,4,3,5],[5,4,3,2,1],[1,0,3,1,4]])
	my_ratings = zeros((matrix.shape[0], 1))

	#Random Test Inputs
	my_ratings[0] = 4
	my_ratings[1] = 5
	my_ratings[2] = 1
	my_ratings[3] = 0
	my_ratings[4] = 2
	'''
	my_ratings[5] = 5
	my_ratings[6] = 0
	my_ratings[7] = 2
	my_ratings[8] = 1
	my_ratings[9] = 3
	'''
	itemFilter(my_ratings)