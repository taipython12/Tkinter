from tkinter import*

root = Tk()

# Creating entry field:
entry = Entry(root, width=50, borderwidth=10, bg="white", fg="black" )
entry.pack()

# Write something on the entry box:
entry.insert(0,"Enter your name:")

def myClick():
    mylabel = Label(root, text="hello, " + entry.get(), fg="blue", bg="black")
    mylabel.pack()

myButton = Button(root, text="Enter your name", padx=50, pady=50, command=myClick, fg="red", bg="black")
myButton.pack()

root.mainloop()