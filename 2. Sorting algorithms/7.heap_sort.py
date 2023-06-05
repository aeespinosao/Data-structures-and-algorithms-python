def heapify(elements, n, i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and elements[l] < elements[smallest]:
        smallest = l
    
    if r < n and elements[r] < elements[smallest]:
        smallest = r
    
    if smallest != i:
        elements[i], elements[smallest] = elements[smallest], elements[i]
        heapify(elements, n, smallest)


def heap_sort(elements):
    n = len(elements)
    for i in range(int(n/2)-1, -1, -1):
        heapify(elements, n, i)
    
    for i in range(n-1,0,-1):
        elements[i], elements[0] = elements[0], elements[i]
        heapify(elements, i, 0)
    return elements



print(heap_sort([2,1,7,6,5,3,4,9,8]))