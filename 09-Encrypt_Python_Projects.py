import marshal
#خد المسار

Path_or_Name=input("write Path of file : ") 

#ظبط مسار الملف لأسم الملف

if Path_or_Name.rfind("\\") ==0:
    pass
else:
    Path_or_Name=Path_or_Name[Path_or_Name.rfind("\\")+1:]


#افتح الملف واقرأه

open_file=open(Path_or_Name,"r").read()

#كود التشفير

compile_file=compile(open_file,'',"exec")
encrypt=marshal.dumps(compile_file)

#سمي الملف المشفر

encrypt_file=open("Encrypt_"+str(Path_or_Name),"w")

# شفر الملف

encrypt_file.write("import marshal\n")
encrypt_file.write("exec(marshal.loads("+repr(encrypt)+"))")

#إشعار ان الملف اتشفر

print("the file encrypted :  "+str(Path_or_Name))