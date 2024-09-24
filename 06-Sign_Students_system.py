from tkinter import*
from tkinter import ttk
#إنشاء نافذة البرنامج
window=Tk()
window.geometry("1366x768+1+1")
window.title("برنامج ادارة المدارس")
window.configure(bg="silver")
window.state("zoomed")
window.resizable(0,0)

lb_title=Label(window,bg="#1AAECB",text="[---نظام إدارة المدرسة وتسجيل الطلاب---]",font=("حمدين بولد",17,"bold"))
lb_title.pack(fill="x")

#نظام البحث عن الطلاب

search_Frame=Frame(window,bg="white",bd=3,relief="groove")
search_Frame.place(x=0,y=35,width=1055,height=50)

lb_search=Label(search_Frame,bg="white",text="البحث عن طالب",font=("حمدين بولد",10,"bold"),bd=2,justify="right")
lb_search.pack(side="right")

compo_search=ttk.Combobox(search_Frame,state="readonly",justify="right")
compo_search["value"]=("الرقم التسلسلي","إسم الطالب","إيميل الطالب","هاتف الطالب")
compo_search.pack(side="right",padx=10)

ent_search=Entry(search_Frame,bg="white",text="",font=("tahoma",10,"bold"),bd=2,justify="center")
ent_search.pack(side="right",padx=20)

bt_search=Button(search_Frame,bg="#3498D8",text="بحث",activebackground="black",activeforeground="silver",font=("tahoma",10,"bold"),bd=1,justify="center")
bt_search.place(x=500,y=7,width=100,height=30)

#أدوات الإدخال للبرنامج
input_Frame=Frame(window,bg="white",bd=8,relief="groove")
input_Frame.place(x=1055,y=34,width=310,height=410)

lb_serial=Label(input_Frame,bg="white",text="الرقم التسلسلي",font=("حمدين بولد",10,"bold"),bd=2,justify="center")
lb_serial.pack()

ent_serial=Entry(input_Frame,bg="white",text="الرقم التسلسلي",font=("tahoma",10,"bold"),bd=2,justify="center")
ent_serial.pack()

lb_name=Label(input_Frame,bg="white",text="إسم الطالب",font=("حمدين بولد",10,"bold"),bd=2,justify="center")
lb_name.pack()

ent_name=Entry(input_Frame,bg="white",text="إسم الطالب",font=("tahoma",10,"bold"),bd=2,justify="center")
ent_name.pack()

lb_mail=Label(input_Frame,bg="white",text="إيميل الطالب",font=("حمدين بولد",10,"bold"),bd=2,justify="center")
lb_mail.pack()

ent_mail=Entry(input_Frame,bg="white",text="إيميل الطالب",font=("tahoma",10,"bold"),bd=2,justify="center")
ent_mail.pack()


lb_num=Label(input_Frame,bg="white",text="هاتف الطالب",font=("حمدين بولد",10,"bold"),bd=2,justify="center")
lb_num.pack()

ent_num=Entry(input_Frame,bg="white",text="هاتف الطالب",font=("tahoma",10,"bold"),bd=2,justify="center")
ent_num.pack()

lb_train=Label(input_Frame,bg="white",text="مؤهلات الطالب",font=("حمدين بولد",10,"bold"),bd=2,justify="center")
lb_train.pack()

ent_train=Entry(input_Frame,bg="white",text="مؤهلات الطالب",font=("tahoma",10,"bold"),bd=2,justify="center")
ent_train.pack()

lb_gender=Label(input_Frame,bg="white",text="جنس الطالب/ة",font=("حمدين بولد",10,"bold"),bd=2,justify="center")
lb_gender.pack()

combo_gender=ttk.Combobox(input_Frame,state="readonly")
combo_gender["value"]=("ذكر","انثي")
combo_gender.pack()

lb_address=Label(input_Frame,bg="white",text="عنوان الطالب",font=("حمدين بولد",10,"bold"),bd=2,justify="center")
lb_address.pack()

ent_address=Entry(input_Frame,bg="white",text="عنوان الطالب",font=("tahoma",10,"bold"),bd=2,justify="center")
ent_address.pack()

lb_delete=Label(input_Frame,bg="white",text="حذف طالب بالإسم",fg="red",font=("حمدين بولد",10,"bold"),bd=2,justify="center")
lb_delete.pack()

ent_delete=Entry(input_Frame,bg="white",text="حذف طالب بالإسم",font=("tahoma",10,"bold"),bd=2,justify="center")
ent_delete.pack()

#ازرار الإدخال للبرنامج.

input_Frame=Frame(window,bg="white",bd=8,relief="groove")
input_Frame.place(x=1055,y=430,width=310,height=309)

lb_title_control=Label(input_Frame,bg="#1AAECB",text="[---أدوات التحكم---]",font=("حمدين بولد",17,"bold"))
lb_title_control.pack(fill="x",pady=5)

bt_add=Button(input_Frame,bg="silver",text="إضافة طالب ",activebackground="black",activeforeground="silver",font=("tahoma",10,"bold"),bd=2,justify="center",width=20)
bt_add.pack(pady=5)

bt_del=Button(input_Frame,bg="silver",text="حذف طالب ",activebackground="black",activeforeground="silver",font=("tahoma",10,"bold"),bd=2,justify="center",width=20)
bt_del.pack(pady=5)

bt_edit=Button(input_Frame,bg="silver",text="تعديل بيانات طالب ",activebackground="black",activeforeground="silver",font=("tahoma",10,"bold"),bd=2,justify="center",width=20)
bt_edit.pack(pady=5)

bt_fill=Button(input_Frame,bg="silver",text="إفراغ الحقول",activebackground="black",activeforeground="silver",font=("tahoma",10,"bold"),bd=2,justify="center",width=20)
bt_fill.pack(pady=5)

bt_who=Button(input_Frame,bg="silver",text="من نحن ",activebackground="black",activeforeground="silver",font=("tahoma",10,"bold"),bd=2,justify="center",width=20)
bt_who.pack(pady=5)

bt_exit=Button(input_Frame,bg="red",text="الخروج من البرنامج",activebackground="black",activeforeground="silver",font=("tahoma",10,"bold"),bd=2,justify="center",width=20)
bt_exit.pack(pady=5)
#قاعدة البيانات
info_Frame=Frame(window,bg="white",bd=3,relief="groove")
info_Frame.place(x=5,y=90,width=1045,height=650)

scrollx=Scrollbar(info_Frame,orient="horizontal")
scrolly=Scrollbar(info_Frame,orient="vertical") 
scrollx.pack(side="bottom",fill=X)
scrolly.pack(side="right",fill=Y)



window.mainloop()