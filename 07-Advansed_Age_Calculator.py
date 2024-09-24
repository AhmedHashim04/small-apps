import datetime
#تاريخ اليوم
year_now=str(datetime.datetime.now().year)
month_now=str(datetime.datetime.now().month)
day_now=str(datetime.datetime.now().day)
list_Now=[year_now,month_now,day_now]
list_Now_join="-".join(list_Now)
#تاريخ ميلاده
birthday=input("plese write ur birthday as 2024-01-30 : ")
birthday_list=[]

for i in birthday:
    if i=="-":continue
    else:birthday_list.append(i)
birth_year="".join(birthday_list[0:4])
birth_month="".join(birthday_list[4:6])
birth_day="".join(birthday_list[6:-1])
try:
    year_age=int(year_now)-int(birth_year)
    month_age=int(month_now)-int(birth_month)
    day_age=int(day_now)-int(birth_day)

    if month_age <0:
        year_age-=1
        month_age=12+month_age
    print(f" U Have : {year_age} ages,{month_age} monthes,{day_age} days")
except:print("plese write ur birthday as 2024-01-30")
