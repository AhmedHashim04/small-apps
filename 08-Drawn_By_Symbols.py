#خد المدخلات
try:
    Rows=int(input("please give me num of rows : "))
    Symbols=input("please give me symbols of form : ")
    Columns=int(input("please give me num of columns : "))
    for i in range(Rows):    #خشلي ف لوب من عدد الروز
        for x in range(Columns):    #خشلي فلو ف عدد الاعمدة

            print(Symbols,end="")  #
        print("") 

except:raise "plese give me numbers only"
