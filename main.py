from tkinter import *
import wikipedia

root=Tk()

root.title("Wiki Search Engine")
root.geometry("350x400")

textField= Entry(root,width=50,text="Enter Summary")
textField.pack()

def Search():
    myLabel=Label(root,text=wikipedia.search(textField.get()))

    myLabel.pack()

myButton=Button(root,text="Search the topic",command=Search)
myButton.pack()

#developer Label
developerlabel = Label(root,text="Made by   Aditya N Bhatt",font=("jost",15))
developerlabel.pack()

root.mainloop()