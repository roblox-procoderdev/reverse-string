str_in=input("enter a string: ")
class reverse:

    def __init__(self,ss):
        self.ss=ss
    
    def reverso(self):
        reversed_str=""
        for i in str_in:
            reversed_str=i+reversed_str
        print("reversed string: ",reversed_str)
s=reverse(str_in)
print("given string: ",str_in)
s.reverso()