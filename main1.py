import MOODTRACKER
# import tkinker module
from tkinter import *
from PIL import ImageTk, Image
import webbrowser as wb
import random
from tkinter import messagebox
class mainpage(Tk):
    def __init__(self):

        #Creating object 'root' of Tk()
        root = Tk()

        #Providing Geometry to the form
        root.geometry("1800x1800")

        #Providing title to the form
        root.title('Cardeopedia')

        root.configure(background = "pink")

        label =Label(root,text="WELCOME TO MY CAREOPEDIA", justify=CENTER, font=("Arial", 40, "italic", "bold", "underline"), bg='pink', bd= 20)
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
        Button1=Button(root, text='View User Profile', width=20, bg="red", fg='white', font=Font, bd=20).place(x=450, y=200)


        Button2=Button(root, text='Disease Diagnosis', width=20, bg="red", fg='white', font=Font, bd=20).place(x=450, y=330)

        Button3=Button(root, text='Calculate BMI', width=20, bg="red", fg='white', font=Font, bd=20).place(x=450, y=460)
        
        #HEALTH CLASS IMPLEMENTED 
        def p():
            class health(Tk):
                root = Tk()
                topFrame = Frame(root)
                topFrame.pack(side= TOP)
                bottomFrame = Frame(root)
                bottomFrame.pack(side=BOTTOM)
                rightFrame=Frame(root)
                rightFrame.pack(side=RIGHT)
                root.title('Health blogs')
                root.configure(bg='pink')
                l = Label(root, text ="CAREOPEDIA", justify= CENTER, font=("Arial", 30,"italic","bold","underline"),bd=20, fg="black",bg="pink")
                l.place(x=800, y=100, anchor=CENTER)
                l2 = Label(root, text ="Health blogs", justify= CENTER, font=("Arial", 20,"italic","bold","underline"),bd=20,fg="black", bg="pink")
                l2.place(x=800, y=250, anchor=CENTER)
                l3 = Label(root, text ="_________________________________________________________________________", justify= CENTER, font=("Arial", 30,"italic","bold","underline"),bd=20, fg="black",bg="pink")
                l3.place(x=800, y=175, anchor=CENTER)
                #CREATE BUTTON FUNCTIONALITIES
                def  b1():
                  wb.open("https://www.webmd.com")
                  return
                def  b2():
                 wb.open("https://www.medicalnewstoday.com")
                 return
                def  b3():
                  wb.open("https://www.foodpolitics.com")
                  return
                def  b4():
                   wb.open("https://www.healthline.com")
                   return
                #HEALTH BLOG BUTTONS
                button1 = Button(root,text="Health Blog 1 by",font=("Arial", 20,"italic","bold","underline"),fg="white",bg="red")
                button1.place(x=300,y=300)
                button1['command']=b1
                button2 = Button(root,text="Health Blog 2 by",font=("Arial", 20,"italic","bold","underline"),fg="white",bg="red")
                button2.place(x=950,y=300)
                button2['command']=b2
                button3 = Button(root,text="Health Blog 3 by",font=("Arial", 20,"italic","bold","underline"),fg="white",bg="red")
                button3.place(x=300,y=400)
                button3['command']=b3
                button4 = Button(root,text="Health Blog 4 by",font=("Arial", 20,"italic","bold","underline"),fg="white",bg="red")
                button4.place(x=950,y=400)
                button4['command']=b4
                button5 = Button(root,text="Back",justify=RIGHT,font=("Arial",20,"italic","bold","underline"),bd=20,fg="white",bg="red")
                button5.place(relx=0.8,rely=0.8)
                button5['command']=root.destroy
                #CREATING HEALTH TIPS GENERATOR
                def popupmsg():
                        root = Tk()
                        root.title("health tips")
                        health_tips = ["Drink at least 8 glasses of water per day","Good ways to improve gut health include eating probiotic foods like yogurt","Vegetables and fruits are loaded with prebiotic fiber, vitamins, minerals, and antioxidants","Reduce your salt intake to 5g per day, equivalent to about one teaspoon","Fats consumed should be less than 30% of your total energy intake","Check your blood pressure regularly to avoid hyper tension"]
                        random_num = random.choice(health_tips)
                        h=str(random_num)
                        label = Label(root, text=h)
                        label.pack(side='top',fill='x',pady=10)
                        B1 = Button(root, text="Got it!", command = root.destroy)
                        B1.pack(side=RIGHT)
                        root.mainloop()
                a = Button(root,text="Health tips",font=("Arial",15,"bold"),bd=20,fg='white',bg='red')
                a['command']=popupmsg
                a.place(relx=0.45,rely=0.82)
                root.mainloop()
        def md():
                   root1 = Tk()
                   topFrame = Frame(root1)
                   topFrame.pack(side= TOP)
                   bottomFrame = Frame(root1)
                   bottomFrame.pack(side=BOTTOM)
                   root1.title('Mood Tracker')
                   #set window color
                   root1.configure(bg='pink')
                   #MOOD TIPS FUNCTION
                   def mood_tip_suggest1(button):
                       if  button == ("button1"):
                            root1= Tk()
                            root1.title("Mood care tips")
                            l1= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                            l1.place(x=300,y=100)
                            l2=Label(root1,text="You should observe taking deep breaths, and visualize yourself calmn.",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                            l2.place(x=750,y=350,anchor=CENTER)
                            l3=Label(root1,text="Be mindful of your thoughts and admit that you are nervous and try to change your focus.",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                            l3.place(x=740,y=470,anchor=CENTER)
                            l4 = Label(root1, text ="Mood care tips", justify= CENTER, font=("Times", 25,"bold","underline"),bd=20,fg="salmon", bg="peach puff")
                            l4.pack(side=TOP)
                            l5= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                            l5.pack(side=BOTTOM)
                            root1.configure(bg="peach puff")
                            root1.mainloop()
                       elif  button == ("button2"):
                           root1= Tk()
                           root1.title("Mood care tips")
                           l1= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                           l1.place(x=300,y=100)
                           l2=Label(root1,text="A positive emotion to be felt indeed! Try to be persistent in maintaing happiness.",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                           l2.place(x=750,y=350,anchor=CENTER)
                           l3=Label(root1,text="Be grateful and think less of negativitiy, embrace your personality and think positively quite often.",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                           l3.place(x=740,y=470,anchor=CENTER)
                           l4 = Label(root1, text ="Mood care tips", justify= CENTER, font=("Times", 25,"bold","underline"),bd=20,fg="salmon", bg="peach puff")
                           l4.pack(side=TOP)
                           l5= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                           l5.pack(side=BOTTOM)
                           root1.configure(bg="peach puff")
                           root1.mainloop()
                       elif  button == ("button3"):
                           root1= Tk()
                           root1.title("Mood care tips")
                           l1= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                           l1.place(x=300,y=100)
                           l2=Label(root1,text="A healthy emotion to be felt but not too often.Do not despair over minute issues and do whatever makes you happy.",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                           l2.place(x=750,y=350,anchor=CENTER)
                           l3=Label(root1,text="Do not stress about what makes you sad, take proper amount of sleep.Re-call your happy times and rejuvenate!",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                           l3.place(x=740,y=470,anchor=CENTER)
                           l4 = Label(root1, text ="Mood care tips", justify= CENTER, font=("Times", 25,"bold","underline"),bd=20,fg="salmon", bg="peach puff")
                           l4.pack(side=TOP)
                           l5= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                           l5.pack(side=BOTTOM)
                           root1.configure(bg="peach puff")
                           root1.mainloop()
                       elif  button == ("button"):
                           root1= Tk()
                           root1.title("Mood care tips")
                           l1= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                           l1.place(x=300,y=100)
                           l2=Label(root1,text="Take a break from your work and express your feelings to others. Avoid caging your feelings and thoughts",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                           l2.place(x=750,y=350,anchor=CENTER)
                           l3=Label(root1,text="Contemplate on your decisions, relax and take gradual steps to overcome frusteration",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                           l3.place(x=740,y=470,anchor=CENTER)
                           l4 = Label(root1, text ="Mood care tips", justify= CENTER, font=("Times", 25,"bold","underline"),bd=20,fg="salmon", bg="peach puff")
                           l4.pack(side=TOP)
                           l5= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                           l5.pack(side=BOTTOM)
                           root1.configure(bg="peach puff")
                           root1.mainloop()
                       elif  button == ("button5"):
                          root1 = Tk()
                          root1.title("Mood care tips")
                          l1= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                          l1.place(x=300,y=100)
                          l2=Label(root1,text="Do not let things get to your head.Avoid getting into fights with others. Try to stay sensible and act maturely",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                          l2.place(x=750,y=350,anchor=CENTER)
                          l3=Label(root1,text="Do not intake unhealthy food too often. It will eventually improve your temper",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                          l3.place(x=740,y=470,anchor=CENTER)
                          l4=Label(root1,text="Take deep breaths and divert your focus when feeling angry!",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                          l4.place(x=740,y=550,anchor=CENTER)
                          l5 = Label(root1, text ="Mood care tips", justify= CENTER, font=("Times", 25,"bold","underline"),bd=20,fg="salmon", bg="peach puff")
                          l5.pack(side=TOP)
                          l6= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                          l6.pack(side=BOTTOM)
                          root1.configure(bg="peach puff")
                          root1.mainloop()
                       elif  button == ("button6"):
                          root1= Tk()
                          root1.title("Mood care tips")
                          l1= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                          l1.place(x=300,y=100)
                          l2=Label(root1,text="Avoid overthinking, monitor your stress levels and maintain boundaries from anxious things.",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                          l2.place(x=750,y=350,anchor=CENTER)
                          l3=Label(root1,text="Be gentle to yourself and welcome positivity. Do not pay attention to disturbing thoughts and be persistent in your process",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                          l3.place(x=740,y=470,anchor=CENTER)
                          l4 = Label(root1, text ="Mood care tips", justify= CENTER, font=("Times", 20,"bold","underline"),bd=20,fg="salmon", bg="peach puff")
                          l4.pack(side=TOP)
                          l5= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                          l5.pack(side=BOTTOM)
                          root1.configure(bg="peach puff")
                          root1.mainloop()
                       elif  button == ("button7"):
                          root1= Tk()
                          root1.title("Mood care tips")
                          l1= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                          l1.place(x=300,y=100)
                          l2=Label(root1,text="Take things slowly.Be comfortable in taking gradual steps towards your goals. Maintain a healthy and productive routine",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                          l2.place(x=750,y=350,anchor=CENTER)
                          l3=Label(root1,text="Be confident in your personality and take your tasks seriously.",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                          l3.place(x=740,y=470,anchor=CENTER)
                          l4 = Label(root1, text ="Mood care tips", justify= CENTER, font=("Times", 25,"bold","underline"),bd=20,fg="salmon", bg="peach puff")
                          l4.pack(side=TOP)
                          l5= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                          l5.pack(side=BOTTOM)
                          root1.configure(bg="peach puff")
                          root1.mainloop()
                       elif  button == ("button8"):
                          root1= Tk()
                          root1.title("Mood care tips")
                          l1= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                          l1.place(x=300,y=100)
                          l2=Label(root1,text="Good to maintain enthusiasism! Make sure to balance life as well, stay away from work obsession.",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                          l2.place(x=750,y=350,anchor=CENTER)
                          l3=Label(root1,text="Be confident over your personality and take small breaks in between to preserve your energy!",font=("Times",20),bd=20, fg="salmon",bg="bisque")
                          l3.place(x=740,y=470,anchor=CENTER)
                          l4 = Label(root1, text ="Mood care tips", justify= CENTER, font=("Times", 25,"bold","underline"),bd=20,fg="salmon", bg="peach puff")
                          l4.pack(side=TOP)
                          l5= Label(root1,text="********************************************************************",font=("Times",20),bd=20,fg="salmon",bg="bisque")
                          l5.pack(side=BOTTOM)
                          root1.configure(bg="peach puff")
                          root1.mainloop()
                   #BUTTON FUNCTIONALITIES FOR IMAGES
                   def b1():
                        button1["command"]=mood_tip_suggest1("button1")
                   def b2():
                       button2["command"]=mood_tip_suggest1("button2")
                   def b3():
                       button3["command"]=mood_tip_suggest1("button3")
                   def b4():
                       button["command"]=mood_tip_suggest1("button")    
                   def b5():
                       button5["command"]=mood_tip_suggest1("button5")
                   def b6():
                       button6["command"]=mood_tip_suggest1("button6")
                   def b7():
                       button7["command"]=mood_tip_suggest1("button7")
                   def b8():
                       button8["command"]=mood_tip_suggest1("button8")
                   #ADDING IMAGES AND BUTTONS IN MAIN WINDOW
                   v=Tk.Toplevel() 
                   image = Image.open("nervous.jpg")
                   photo = ImageTk.PhotoImage(image)
                   my_label1 = Label(v,image = photo,height = 150, width = 225)
                   my_label1.image=photo
                   my_label1.place(x=100,y=200)
                   button1 = Button(root1,text="Nervous",font=("Arial", 10,"italic","bold","underline"),fg="white",bg="red")
                   button1.place(x=200,y=400)
                   button1["command"]=b1
                       
                   my_image2 = ImageTk.PhotoImage(Image.open("happy.jpg"))
                   my_label2= Label(image = my_image2, height= 150,width = 225 )
                   my_label2.place(x=450,y=200)
                   button2 = Button(root1,text="Happy",font=("Arial", 10,"italic","bold","underline"),fg="white",bg="red")
                   button2["command"]=b2
                   button2.place(x=550,y=400)
                   my_image3 = ImageTk.PhotoImage(Image.open("sad.jpg"))
                   my_label3= Label(image = my_image3, height= 150,width = 225 )
                   my_label3.place(x=800,y=200)
                   button3 = Button(root1,text="Sad",font=("Arial", 10,"italic","bold","underline"),fg="white",bg="red")
                   button3.place(x=900,y=400)
                   button3["command"]=b3
                   my_image4= ImageTk.PhotoImage(Image.open("frusterated.jpg"))
                   my_label4= Label(image = my_image4, height= 150,width = 225 )
                   my_label4.place(x=1150,y=200)
                   button = Button(root1,text="Frusterated",font=("Arial", 10,"italic","bold","underline"),fg="white",bg="red")
                   button.place(x=1220,y=400)
                   button["command"]=b4
                   my_image5= ImageTk.PhotoImage(Image.open("angry.jpg"))
                   my_label5= Label(image = my_image5, height= 150,width = 225 )
                   my_label5.place(x=100,y=450)
                   button5 = Button(root1,text="Angry",font=("Arial", 10,"italic","bold","underline"),fg="white",bg="red")
                   button5.place(x=200,y=650)
                   button5["command"]=b5
                   my_image6= ImageTk.PhotoImage(Image.open("anxious.jpg"))
                   my_label6= Label(image = my_image6, height= 150,width = 225 )
                   my_label6.place(x=450,y=450)
                   button6 = Button(root1,text="Anxious",font=("Arial", 10,"italic","bold","underline"),fg="white",bg="red")
                   button6.place(x=550,y=650)
                   button6["command"]=b6
                   my_image7= ImageTk.PhotoImage(Image.open("demotivated.jpg"))
                   my_label7= Label(image = my_image7, height= 150,width = 225 )
                   my_label7.place(x=800,y=450)
                   button7 = Button(root1,text="Demotivated",font=("Arial", 10,"italic","bold","underline"),fg="white",bg="red")
                   button7.place(x=880,y=650)
                   button7['command']=b7
                   my_image8= ImageTk.PhotoImage(Image.open("enthusiastic.png"))
                   my_label8= Label(image = my_image8, height= 150,width = 225 )
                   my_label8.place(x=1150,y=450)
                   button8 = Button(root1,text="Enthusiastic",font=("Arial", 10,"italic","bold","underline"),fg="white",bg="red")
                   button8.place(x=1220,y=650)
                   button8["command"]=b8
                   #TITLE OF WINDOW "MOOD TRACKER"
                   l = Label(root1, text ="MOOD TRACKER", justify= CENTER, font=("Arial", 30,"italic","bold","underline"),bd=20, fg="black",bg="pink")
                   l2 = Label(root1, text ="How are you feeling today?", justify= CENTER, font=("Arial", 20,"italic","bold","underline"),bd=20,fg="black", bg="pink")
                   l.place(x=800, y=50, anchor=CENTER)
                   l2.place(x=800, y=150, anchor=CENTER)
                   #EXIT BUTTON
                   button_quit = Button(bottomFrame,text="Exit", justify = CENTER,font=("Arial",20,"italic","bold","underline"),bd=20,fg="white",bg="red")
                   button_quit.pack()
                   button_quit['command']=root1.destroy
                   root1.mainloop()    
        Button5=Button(root, text='Health Blogs', width=20, bg="red", fg='white', font=Font, bd=20,command=p).place(x=450, y=720) 
        Button4=Button(root, text='Mood Tracker', width=20, bg="red", fg='white', font=Font, bd=20,command=md).place(x=450, y=590)
        root.mainloop()

m = mainpage()

