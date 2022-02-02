# import tkinker module
from tkinter import *

class mainpage(Tk):
    def __init__(self):

        #Creating object 'root' of Tk()
        root = Tk()

        #Providing Geometry to the form
        root.geometry("1800x1800")

        #Providing title to the form
        root.title('Cardeopedia')

        root.configure(background = "pink")

        label =Label(root,text="WELCOME TO MY CARDEOPEDIA", justify=CENTER, font=("Arial", 40, "italic", "bold", "underline"), bg='pink', bd= 20)
        label.place(x=400,y=30)

        # picture label

        pic1 = PhotoImage(file="plus.png")
        pic1 = pic1.subsample(3, 3)
        pic1label = Label(root, image=pic1)
        pic1label.place(x=0,y=0)

        pic2 = PhotoImage(file="medical.png")
        pic2label = Label(root, image=pic2, width=500, height=530)

        pic2label.place(x=1100, y=250)


        Font = ("arial", 20, "italic", "bold")

        # Creating the buttons
        Button(root, text='View User Profile', width=20, bg="red", fg='white', font=Font, bd=20).place(x=450, y=200)


        Button(root, text='Disease Diagnosis', width=20, bg="red", fg='white', font=Font, bd=20).place(x=450, y=330)

        Button(root, text='Calculate BMI', width=20, bg="red", fg='white', font=Font, bd=20).place(x=450, y=460)

        Button(root, text='Mood Tracker', width=20, bg="red", fg='white', font=Font, bd=20).place(x=450, y=590)

        Button(root, text='Health Blogs', width=20, bg="red", fg='white', font=Font, bd=20).place(x=450, y=720)




        root.mainloop()

m = mainpage()

