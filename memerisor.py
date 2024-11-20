from tkinter import*
from tkinter.filedialog import*
root = Tk()
root.geometry("500x500")

def save_file():
    fout=asksaveasfile(defaultextension=".txt")
    if fout is not None:
        for i in list.get(0, END):
            print(item.strip(),file=fout)
        listbox.delete(0,END)

def openFile():
    fin=askopenfile(title='Open File')
    if fin is not None:
        listbox.delete()
        item=fin.readlines()# read from file
        for item in items: # to insert in listbox
            listbox.insert(END, item.strip())

# to add item to listbox
def addItems():
    listbox.insert(END, item.get())
    # to delete from textbox
    item.delete(0, END)

def deleteItems():
    index=listbox.curselection()
    if index:
        listbox.delete(index)





save_button = Button(root, text="Save", command=save_file)
open_button = Button(root, text="Open", command=openFile)
add_button = Button(root, text="Add", command=addItems)
delete_button = Button(root, text="Delete", command=deleteItems)

save_button.pack()
open_button.pack()
add_button.pack(side=LEFT)
delete_button.pack(side=RIGHT)

item = Entry(root)

item.pack()

frame = Frame(root)
frame.pack()
scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame, yscrollcommand=scrollbar.set, width=40)

for i in range(1, 101):
    listbox.insert(END, "item no"+str(i))

listbox.pack(side=LEFT, padx=5)
scrollbar.config(command=listbox.yview)





root.mainloop()