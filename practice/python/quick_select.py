import random, time

def partition(array, left, right, pivotIndex):
    if left == right:
        return left
    
    array[pivotIndex], array[right] = array[right], array[pivotIndex]
    count = left
    for i in xrange(left, right):
        if array[i] < array[right]:
            array[i], array[count] = array[count], array[i]
            count += 1
    array[count], array[right] = array[right], array[count]
    return count

def quickSelect(array, left, right, rankToFind):
        if left > right:
                return None
        while left <= right:
		pivotIndex = random.randint(left, right)
		pivotIndex = partition(array, left, right, pivotIndex)
		if pivotIndex == rankToFind:
			break
		elif pivotIndex < rankToFind:
			left = pivotIndex + 1
		else:
			right = pivotIndex - 1
                #print array, pivotIndex
                #time.sleep(0.5)
        #print array, pivotIndex
	return array[pivotIndex]

def quickSort(array, left, right):
    if left >= right:
        return

    mediumIndex = (right + left) / 2
    quickSelect(array, left, right, mediumIndex)
    print array
    quickSort(array, left, mediumIndex - 1)
    quickSort(array, mediumIndex + 1, right)
    return

def main():
    a = [5,76,23,2,6,78,2,121,3,4,6, 2, 1, 324,6,2,41,235,6345,7,876]
    quickSort(a, 0, len(a) - 1)
    print a

main()
