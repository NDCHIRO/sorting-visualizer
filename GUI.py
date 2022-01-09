from tkinter import *
from tkinter import ttk
import random
from algorithms import *

data = []
def drawData(data,colorArray):
    canvas.delete("all")
    c_height = 390
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    # normalize data between 0 -> 1
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 360
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))

    #to update after each step
    root.update()


def Generate():
    global data
    #to clear the data
    data = []
    minVal= int(minEntry.get())
    maxVal= int(maxEntry.get())
    size  = int(sizeEntry.get())

    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))

    drawData(data,['red' for x in range(len(data))]) #['red', 'red' ,....])
    print('Algorithm selected ' + selected_alg.get())

def StartAlgorithm():
    global data
    bubbleSort(data, drawData,speedScale.get())


root = Tk()
root.title('sorting Visualizer')
root.maxsize(900, 600)
root.config(bg='black')

selected_alg = StringVar()

# frame and base layout
UI_frame = Frame(root, width=600, height=200, bg='deepskyblue')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=390, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# UI area
# row 0
Label(UI_frame, text="Algorithms", bg="grey").grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)


# row 1
#size bar
sizeEntry = Scale(UI_frame, from_=3, to=22, length=200, resolution=1, orient=HORIZONTAL, label="size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5, sticky=W)

# min value bar
minEntry = Scale(UI_frame, from_=1, to=10, length=200, resolution=1, orient=HORIZONTAL, label="min value")
minEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# max value bar
maxEntry = Scale(UI_frame, from_=10, to=100, length=200, resolution=1, orient=HORIZONTAL, label="max value")
maxEntry.grid(row=1, column=2, padx=5, pady=5, sticky=W)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
