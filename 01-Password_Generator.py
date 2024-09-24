#نزل المكتبات
import string
import random
#جهز الارقام والحروف صغي8000000000000000� والعلامات==هنسميها المادة الخام
#حط المادة الخام في ليسته واعملها ترتيب عشوائي
Large_Alpha=(list(string.ascii_uppercase))
Small_Alpha=(list(string.ascii_lowercase))
Digits=(list(string.digits))
Sympols=(list(string.punctuation))

random.shuffle(Large_Alpha)
random.shuffle(Small_Alpha)
random.shuffle(Digits)
random.shuffle(Sympols)

#جهز ليسته فيها الباسورد فاضية واعملها ترتيب عشوائي
Password=[]
#اطلب عدد الارقام الي عايزها ويكون اكبر من او يساوي 8 أرقام ولو حط حروف او اي حاجة غير ارقام يرجعو ==هنسميها مطلوب 1
Lenth_of_Pass=0
while type(Lenth_of_Pass) !=int or Lenth_of_Pass < 8 :
    try:
        Lenth_of_Pass=int(input("Give me Lenth of Ur Password 8 at least : "))
    except :
        print("Only Nums")
#خد مطلوب 1 واعمل نسب 30% للحروف الصغيرة و30% للكبيرة و 20% ارقام و20% علامات
Precent_Of_Large_Alpha=round(Lenth_of_Pass*(30/100))
Precent_Of_Small_Alpha=round(Lenth_of_Pass*(30/100))
Precent_Of_Digits=round(Lenth_of_Pass*(20/100))
Precent_Of_Sympols=round(Lenth_of_Pass*(20/100))
#ضيف الحروف والارقام والعلامات للباسورد واعملو ترتيب عشوائي وخرج الناتج
for i in range(Precent_Of_Large_Alpha):
    Password.append(Large_Alpha[i])
for i in range(Precent_Of_Small_Alpha):
    Password.append(Small_Alpha[i])
for i in range(Precent_Of_Digits):
    Password.append(Digits[i])
for i in range(Precent_Of_Sympols):
    Password.append(Sympols[i])
random.shuffle(Password)
Password="".join(Password[0:])
print("#"*50,"|")
print("# Ur Password is : ",Password,(29-len(Password))*" ","|")
print("#"*50,"|")
#----------------------------------------------------------------------------

