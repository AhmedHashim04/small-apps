#نزل المكتبات
import os
    #خد من المستخدم عدد الفولدرز
try:
    Folder_nums=int(input("please Give me numper of Folders That U want to generator : "))
except:print("plese give Numpers only")
    #  خد منو مكان الفولدرز
print("Plese Give as this form : I:\\\Work\\\Programming\\\Python\\\My_Projects_Ahmed_Hashim\\\ ")
Folder_Place=input("please Give me Place of Folders That U want to generator : ")

if os.path.exists(Folder_Place):
    Folder_Name=input("please Give me Name of Folders That U want to generator : ")
    for i in range(Folder_nums+1):
        word=(f"\{i} - {Folder_Name}")
        os.mkdir(Folder_Place+word)
    print("done")
else:print("plese sure that U Give as this form : I:\\\Work\\\Prgrammin\\\My_Projects_Ahmed_Hashim\\\.")
