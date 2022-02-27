import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code

switch = True
window.config(bg="black")

def toggleSwitch():
    global button
    global window
    global switch
    if switch:
        print("light is on")
        window.config(bg="yellow")
        button.config(text="Switch light off")
        switch = False
    else:
        print("light is off")
        window.config(bg="black")
        button.config(text="Switch light on")
        switch = True

button.config(text="Switch light on", command=toggleSwitch)


# schijf hier tussen je code

window.mainloop()