import time


# bubble sort Algorithm
def bubbleSort(data, drawData, timeTick):
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawData(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])


# insertion sort Algorithm
def insertionSort(data, drawData, timeTick):
    # Traverse through 1 to len(data)
    for i in range(1, len(data)):
        key = data[i]
        # Move elements of data[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            drawData(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))])
            time.sleep(timeTick)
        drawData(data, ['green' for x in range(len(data))])
        data[j + 1] = key

        

# quick sort Algorithm
def partition( data,head, tail, drawData, timeTick):
    boarder = head
    pivot = data[tail]
    for i in range(head,tail):
        if data[i] < data[tail]:
            data[boarder],data[i] = data[i],data[boarder]
            boarder+=1
    data[boarder],data[tail] = data[tail],data[boarder]
    return boarder

def quick_sort(data,head, tail, drawData, timeTick):
    if head < tail:
        paratitionIdx = partition(data,head,tail,drawData,timeTick)
        #left partition 
        quick_sort(data,head,paratitionIdx-1,drawData,timeTick)
        #right partition 
        quick_sort(data,paratitionIdx+1,tail,drawData,timeTick)
    return data


data = [10, 80, 30, 90, 40, 50, 70]
data = quick_sort(data,0, len(data)-1,0,0)
print(data)
