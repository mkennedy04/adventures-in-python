import Tkinter as tk
window = tk.Tk()

def buttonClick():
    button.config(text="Clicked")
    print "Beep!"

button = tk.Button(window, text="Click me!", command=buttonClick)
button.pack()
window.mainloop()
