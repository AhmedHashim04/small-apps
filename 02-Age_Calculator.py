#نزل المكتبات
import datetime
#جهز الوقت الحالي 
Time_Now=[(datetime.datetime.now().year),(datetime.datetime.now().month),(datetime.datetime.now().day)]
#خد من الزبون تاريخ الميلاد والعمله الي هو عايز يحسب بيها
print("#"*20 +" Hello How Are U ? "+"#"*20 )
try:
    X=0
    while X==0:
        Input_Year=int(input("Give me The Year of Ur Birth : "))
        if Input_Year>=2023 or Input_Year<=1910:
            print("Give The True Value !!")
            continue
        else:
            Input_Month=int(input("Give me The Month of Ur Birth : "))
            if Input_Month>12 or Input_Month<1:
                print("Give The True Value !!")
                continue
            else:
                Input_Day=int(input("Give me The Day of Ur Birth : "))
            if Input_Day>31 or Input_Day<1:
                print("Give The True Value !!")
                continue
            X=1
#اطرح تاريخ ميلادة من الوقت الحالي
    Output_Year=Time_Now[0]-int(Input_Year)
    Output_Month=Time_Now[1]-int(Input_Month)
    Output_Day=Time_Now[2]-int(Input_Day)
#خرج المطلوب
    print(f"Hey U Have : {Output_Year} year,{Output_Month} month ,{Output_Day} day")
except:
   print("Please Give Me Correct Number !")