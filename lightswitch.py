import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code

switch = False

def toggleSwitch():
    global button
    if switch:
        button.config(text="lightswitch off")
    else:
        button.config(text="lightswitch on")

button.config(text="lightswitch off", command=toggleSwitch)


# schijf hier tussen je code

window.mainloop()