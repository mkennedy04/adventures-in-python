import Tkinter as tk
window = tk.Tk()

count01 = 0
count02 = 0

def button01Click():
    global count01
    count01 = count01 + 1
    button01.config(text=str(count01))
    
def button02Click():
    global count02
    count02 = count02 + 1
    button02.config(text=str(count02))

button01 = tk.Button(window, text="Click Button 01!", command=button01Click)
button02 = tk.Button(window, text="Click Button 02!", command=button02Click)
button01.pack()
button02.pack()
window.mainloop()