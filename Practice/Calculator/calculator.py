import tkinter as tk

window = tk.Tk()
window.title("CALCULATOR")

window.geometry("500x600")

for i in range(0, 10):
    button = tk.Button(window, text = str(i))
    button.pack()

window.mainloop()