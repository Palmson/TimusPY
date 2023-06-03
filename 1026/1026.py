def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

n = int(input())
F = []
for i in range(0, n):
    F.append(int(input()))
trash = input()
k = int(input())
A = []
quickSort(F, 0, len(F)-1)
for i in range(0, k):
    A.append(int(input()))
    print(F[A[i] - 1])

