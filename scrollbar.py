from tkinter import*

root = Tk()
root.geometry("500x500")
root.title("Scroll Bar")

label1 = Label(root, text="Items")
label1.pack()

scrollbar = Scrollbar(root)

#Adding verical scrollbar on R.H.S
scrollbar.pack(side=RIGHT, fill=Y)

list = Listbox(root, yscrollcommand=scrollbar.set)

for i in range(1, 31):
    list.insert(END, "item no"+str(i))

list.pack(side=LEFT)    
scrollbar.config(command=list.yview)

root.mainloop()
