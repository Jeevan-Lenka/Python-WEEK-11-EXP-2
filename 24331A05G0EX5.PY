import tkinter as tk
def show():
	result.config(text=f"Hello {entry.get()}")
root = tk.Tk()
root.title("Entry Demo")
tk.Label(root, text="Enter name:").pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Submit", command=show).pack()
result = tk.Label(root, text="")
result.pack()
root.mainloop()
