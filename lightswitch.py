import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code

def lightSwitch():
    print(":O")

button.config(text="lightswitch off", command=lightSwitch)


# schijf hier tussen je code

window.mainloop()