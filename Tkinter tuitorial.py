from tkinter import*

root = Tk()

#creating things
label1 = Label(root, text="Hello")
label2 = Label(root, text="My name is Tai")

#put in on screen (can use label.pack())
label1.grid(row=0, column=1)
label2.grid(row=1, column=2)

#another way:
    #label1 = Label(root, text="Hello").grid(row=0, column=1)
    #label2 = Label(root, text="My name is Tai").grid(row=1, column=2)

root.mainloop()
