from tkinter import*

root = Tk()
root.geometry("800x500")
root.title("Python GUI Tkinter")

#---------Background Image---------

c= Canvas(root, height=500, width=800)
filename = PhotoImage(file = "Backgrond.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#------------TOP Frame--------------

Tops = Frame(root,width=300,height=50)
Tops.pack(side=TOP)

#-----------Behind Buttons Frame------

f1 = Frame(root,width=800,height=600,bg='steel blue')
f1.pack()
#-----------BOTTOM Frame--------------

f2 = Frame(root,width=800,height=30,bg='steel blue')
f2.pack(side=BOTTOM)

#-----------------TOP Frame Info--------

lblinfo = Label(Tops,bg='steel blue', font=( 'comic sans ms' ,30, 'bold' ),text="Python---GUI---Tkinter",fg="white",bd=10)
lblinfo.grid(row=0,column=0)


#---------Function on Button-----------

def qexit ():
    root.destroy ()


#-----------------------------------------Buttons----------------------------------------------------------------------

btn1=Button(f1,padx=16,pady=8,fg="green",font=('comic sans ms' ,14,'bold'),width=18, text="Button 1",bd=12, bg="silver")
btn1.grid(row=0, column=4,padx = 20 , pady = 10)

btn2=Button(f1,padx=16,pady=8, bd=12 ,fg="green",font=('comic sans ms' ,14,'bold'),width=18, text="Button 2", bg="silver")
btn2.grid(row=2, column=4,padx = 20 , pady = 10)

btn3=Button(f1,padx=16,pady=8, bd=12,fg="green",font=('comic sans ms' ,14,'bold'),width=18, text="Button 3", bg="silver")
btn3.grid(row=3, column=4,padx = 20 , pady = 10)

btn4=Button(f1,padx=16,pady=8, bd=12 ,fg="red",font=('comic sans ms' ,14,'bold'),width=18, text="QUIT", bg="silver",command=qexit)
btn4.grid(row=4, column=4,padx = 20 , pady = 10)

root.mainloop()
