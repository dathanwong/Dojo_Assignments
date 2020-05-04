
def insertionSort(list):
    for i in range(len(list)):
        index = i
        for j in range(i, -1, -1):
            if list[index] < list[j]:
                list[index], list[j] = list[j], list[index]
                index = j
    return list

print(insertionSort([5,1,36,8,1,3,33,-4,0,-2,2,3]))