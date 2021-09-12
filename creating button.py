from tkinter import*

root = Tk()

def myClick():
    mylabel = Label(root, text="Clicked button", fg="blue", bg="black")
    mylabel.pack()

#creating button:
myButton = Button(root, text="Click me", padx=50, pady=50, command=myClick, fg="red", bg="black")
myButton.pack()

root.mainloop()