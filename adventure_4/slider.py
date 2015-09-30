import Tkinter as tk
window = tk.Tk()

def sliderMove(source):
    sliderVal = slider.get()
    slider_value.config(text=sliderVal)
    
slider_comment = tk.Label(window, text="Move the slider!")
slider_value = tk.Label(window)
slider = tk.Scale(window, from_=0, to=100, command=sliderMove)
#button = tk.Button(window, text="get it!!!", command=sliderMove())

slider.pack()
slider_comment.pack()
slider_value.pack()
#button.pack()

tk.mainloop()
