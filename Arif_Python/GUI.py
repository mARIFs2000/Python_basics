from tkinter import* 
add_window = Tk() 
add_window.title("ArifWeb")
fist_window = Label(add_window,text="We are in Spectrum",bg="silver",fg="black",font=(("FIXEDSYS","35")))
fist_window.pack()
path1 =PhotoImage(file="C:/Users/Python/Downloads/Spectrum Building.png")
Lbl_image = Label(add_window,image=path1,width=200,height=300)
Lbl_image.place(x=950,y=58)

path2 =PhotoImage(file="C:\Users\Python\Pictures\Camera Roll\Benz png.jpg")
lbl2_image = Label(add_window,image=path2,width=400,height=250)
lbl2_image.place(x=150,y=150)
add_window.geometry("1280x720")
add_window.mainloop()
