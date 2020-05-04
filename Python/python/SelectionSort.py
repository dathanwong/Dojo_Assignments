#time O(n2)
#space O(1)

def selectionSort(list):
    for j in range(len(list)-1):
        min = list[j]
        index = j
        for i in range(j,len(list),1):
            if min > list[i]:
                min = list[i]
                index = i
        list[j], list[index] = list[index], list[j]
    return list

print(selectionSort([4,2,6,2,7,-3,1234,0]))