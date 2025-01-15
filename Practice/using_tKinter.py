import tkinter as tk

root = tk.Tk()
root.title("Simple tkinter App")

# Set the size of the window
root.geometry("300x200")

# Create a label widget
label = tk.Label(root, text="Hello, tkinter!", font=("Helvetica", 16))
label.pack(pady=20)  # Add some padding around the label

# Create a button widget
button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack()

# Start the event loop
root.mainloop()
