import time

def bubbleSort(data, drawData,timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))] )
                time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])


def insertionSort(data,drawData,timeTick):

    # Traverse through 1 to len(arr)
    for i in range(1, len(data)):

        key = data[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < data[j] :
                data[j + 1] = data[j]
                j -= 1
                drawData(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
        drawData(data, ['green' for x in range(len(data))])
        data[j + 1] = key



