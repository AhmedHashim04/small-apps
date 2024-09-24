#خد الكلمة منو
x=input("please give me the word that u want to reverse : ")
#حط حروفها فليسته
y=[]
for i in x:
    y.append(i)
#اعكس عناصر اليستة
y.reverse()
#دخل مكان الكومة فراغات
y="".join(y[0:])
#خرجلو الكلمة
print ("Ur reversed word : ",y)