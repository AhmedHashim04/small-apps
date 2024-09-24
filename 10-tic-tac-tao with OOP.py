class Solution:
    res=0
    m=-3
    def check_3_symbols_in_str(self,password):
        english_S_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        english_U_letters =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for i in password:
            if i in english_S_letters:
                self.m +=1
                break
        for i in password:
            if i in english_U_letters:
                self.m +=1
                break
        for i in password:
            if i.isalnum():
                self.m +=1
                break
        return self.m

    def strongPasswordChecker(self, password: str) -> int:
        if len(password)<6 or len(password)>20 :
            if len(password)<6:return (6-len(password))
            elif len(password)>20:return 20-len(password)
        self.check_3_symbols_in_str(password)
        for i in range(len(password)-3):
            if password[i] == password[i+1] == password[i+2] :
                a=password[i+2]+"u"
                b=+password[i+3:]
                password=a+b
                self.res+=1
                if self.check_3_symbols_in_str(password)==0:
                    self.res-=1
        return self.res
Solution0=Solution()
print(Solution0.strongPasswordChecker("111111111"))
        # 20<len(str)>6
        # in str-> 1 lowcase and 1 upcase

        # 3 repeat chrs repeated
