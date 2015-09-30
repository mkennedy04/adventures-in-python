import Tkinter as tk
import time
window = tk.Tk()

clicks = 0
start = 0
goal = 100

def buttonClick():
    global clicks
    global start

    if clicks == 0:
        start = time.time()
        clicks = clicks + 1
    elif clicks + 1 >= goal:
        score = time.time() - start
        label.config(text="time: " + str(score))
        clicks = 0
    else:
        clicks = clicks + 1
        slider.set(clicks)

#def noMe():
#    for x in range(10):
#        buttonClick()

button = tk.Button(window, text="Click me", command=buttonClick)
slider = tk.Scale(window, from_=0, to=goal)
label = tk.Label(window)

#button02 = tk.Button(window, text="No...  click me.", command=noMe)

button.pack()
#button02.pack()
slider.pack()
label.pack()
window.mainloop()

