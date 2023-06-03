def binary(array, element): #бинарный поиск
    mid = len(array) // 2
    low = 0
    high = len(array) - 1

    while array[mid] != element and low <= high:
        if element > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return -1
    else:
        return mid
def selection_sort(array): #Сортировка выбором
    length = len(array)

    for i in range(length - 1):
        minIndex = i

        for j in range(i + 1, length):
            if array[j] < array[minIndex]:
                minIndex = j

        array[i], array[minIndex] = array[minIndex], array[i]

    return array


a = int(input())
A = [int(x) for x in input().split()]
b = int(input())
B = [int(x) for x in input().split()]
c = int(input())
C = [int(x) for x in input().split()]
AB = []
for i in range(a):    #ищем совпадения из A в B
    x = binary(B, A[i])
    if x != -1:
        AB.append(B[x])
ABC = []
for i in range(len(AB)): #ищем совпадения из A и B в C
    x = binary(C, AB[i])
    if x != -1:
        ABC.append(C[x])
print(len(ABC))




