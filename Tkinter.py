import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("My first gui")

label = tk.Label(root, text="Family Recipes", font=('Arial', 20))
label.pack(padx=20, pady=20)

#general text box
textbox = tk.Text(root, height=2, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

#used for user access
myentry = tk.Entry(root)
myentry.pack()


root.mainloop()