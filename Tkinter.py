import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("My first gui")

label = tk.Label(root, text="TKinter Test GUI", font=('Arial', 20))
label.pack(padx=20, pady=20)

#general text box
textbox = tk.Text(root, height=2, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

#used for user access
#myentry = tk.Entry(root)
#myentry.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

button_one = tk.Button(buttonframe, text="1", font=('Arial', 16))
button_one.grid(row=0, column=0, sticky=tk.W+tk.E)

button_two = tk.Button(buttonframe, text="2", font=('Arial', 16))
button_two.grid(row=0, column=1, sticky=tk.W+tk.E)

button_three = tk.Button(buttonframe, text="3", font=('Arial', 16))
button_three.grid(row=0, column=2, sticky=tk.W+tk.E)

button_four = tk.Button(buttonframe, text="4", font=('Arial', 16))
button_four.grid(row=1, column=0, sticky=tk.W+tk.E)

button_five = tk.Button(buttonframe, text="5", font=('Arial', 16))
button_five.grid(row=1, column=1, sticky=tk.W+tk.E)

button_six = tk.Button(buttonframe, text="6", font=('Arial', 16))
button_six.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

#manual place buttons
diffbutton = tk.Button(root, text="Test")
diffbutton.place(x=0, y=0, height=30, width=30)

root.mainloop()