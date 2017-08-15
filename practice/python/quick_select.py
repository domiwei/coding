
def quickSelect(array, rankToFind):
	left = 0
	right = len(array) - 1
	pivotIndex = 0
	def partition(array, left, right, pivotIndex):
		array[pivotIndex], array[right] = array[right], array[pivotIndex]
		for i in xrange(left, right)

	while left < right:
		pivotIndex = random.randint(left, right)
		pivotIndex = partition(array, left, right, pivotIndex)
		if pivotIndex == rankToFind:
			break
		elif pivotIndex < rankToFind:
			left = pivotIndex + 1
		else:
			right = pivotIndex - 1
	return pivotIndex
		
