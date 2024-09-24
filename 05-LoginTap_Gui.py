from tkinter import*
#جهز الشباك
Login_Window=Tk()
Login_Window.geometry("600x100+500+200")
Login_Window.resizable(0,0)
Login_Window.configure(background="gray")
Login_Window.title("Login Window")
#حط العناوين
Label_Title=Label(Login_Window,text="  please write Username and Password  :  ",
                  bg="gray",
                  bd=2,
                  relief="ridge",
                  font=("time",11,"bold"))
Label_Title.place(x=160,y=5)

Label_Username=Label(Login_Window,text="Username",font=("time",10,"bold"),bg="gray")
Label_Username.place(x=5,y=38)

Label_Password=Label(Login_Window,text="Password",font=("time",10,"bold"),bg="gray")
Label_Password.place(x=280,y=38)
#شغل برمجة
acc=StringVar()
acc.set("")

user_var=StringVar()
pass_var=StringVar()

#المربعين الي هيتكتب فيهم
Entry_Username=Entry(Login_Window,
                     bd=6,
                     relief="groove",
                     font=("time",10,"bold"),
                     justify="left",
                     fg="black",
                     width=25,
                     textvariable=user_var)
Entry_Username.pack(side="left",padx=80)

Entry_Password=Entry(Login_Window,
                     bd=6,
                     relief="groove",
                     font=("time",10,"bold"),
                     justify="left",
                     fg="black",
                     width=25,
                     show="*",
                     textvariable=pass_var)
Entry_Password.pack(side="left",padx=0)


#زرار اللوجين وشغله
def loginbutton():
    if Entry_Username.get()=="ahmed" and Entry_Password.get()=="123":acc.set(" welcome to your account .")
    else:acc.set("invalid username or password .")

Login_Button=Button(Login_Window,text="Login",bg="gray",activebackground="gray",font=("time",10,"bold"),command=loginbutton)
Login_Button.place(x=550,y=35)

#الرسالة الي هتظهر 

Label_SorF=Label(Login_Window,textvariable=acc,
                  bg="gray",
                  font=("time",10,"bold"))
Label_SorF.place(x=225,y=77)

Login_Window.mainloop()
