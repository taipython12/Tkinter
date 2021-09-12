from tkinter import*

root = Tk()

# App title:
root.title("Calculator")

# Creating entry:
entry = Entry(root, bg="white", fg="black", width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

# Creating function:
def MouseClick(number): # to insert the number when ckick a button
    curent = entry.get()
    entry.delete(0, END)
    entry.insert(0,str(curent) + str(number))

def Clear(): # to clear all the number
    entry.delete(0, END) 

def MouseClick_add(): # to add 2 numbers
    first_num = entry.get()
    global nums1
    global math
    math = "addition"
    nums1 = int(first_num)
    entry.delete(0, END)
    
def MouseClick_sub(): # to subtract 2 numbers
    first_num = entry.get()
    global nums1
    global math
    math = "subtraction"
    nums1 = int(first_num)
    entry.delete(0, END)

def MouseClick_mul(): # to multiple 2 numbers
    first_num = entry.get()
    global nums1
    global math
    math = "multiplication"
    nums1 = int(first_num)
    entry.delete(0, END)

def MouseClick_div(): # to divide 2 numbers
    first_num = entry.get()
    global nums1
    global math
    math = "division"
    nums1 = int(first_num)
    entry.delete(0, END)

def MouseClick_equal(): # to insert the answer
    second_num = entry.get()
    nums2 = int(second_num)
    entry.delete(0, END)
    if math == "addition":
        return entry.insert(0, nums1 + nums2)
    elif math == "subtraction":
        return entry.insert(0, nums1 - nums2)
    elif math == "multiplication":
        return entry.insert(0, nums1 * nums2)
    elif math == "division":
        return entry.insert(0, nums1 / nums2)

# Creating number button:
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: MouseClick(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: MouseClick(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: MouseClick(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: MouseClick(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: MouseClick(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: MouseClick(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: MouseClick(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: MouseClick(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: MouseClick(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: MouseClick(9))

button_add = Button(root, text="+", padx=40, pady=20, command= MouseClick_add)   
button_sub = Button(root, text="-", padx=40, pady=20, command= MouseClick_sub)
button_mul = Button(root, text="*", padx=40, pady=20, command= MouseClick_mul)
button_div = Button(root, text="/", padx=40, pady=20, command= MouseClick_div)
button_equal = Button(root, text="=", padx=40, pady=20, command= MouseClick_equal) 

button_clear = Button(root, text="clear", padx=40, pady=20, command= Clear)

# Put button on screen:
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_sub.grid(row=4, column=2)
button_div.grid(row=5, column=1)
button_mul.grid(row=5, column=2)
button_equal.grid(row=5, column=0)
button_clear.grid(row=6, column=0, columnspan=3)

# Run app:
root.mainloop()
