st = "hello, my name is prateek"

#reverse

# string is an object in python.

#Object is an instance of a class. Instance means Child of a class.  

# Object oriented progeramming language. eg python, 

class Reverse:
    #Member function
    def reverse(self):
        print("this is an member function/function_variables of class grandparent hello")

    def reverse_str(self, s):
        str = ""
        str_normal = ""
        for i in s:
            str = i + str
            str_normal = str_normal + i
        return str
    


parent = Reverse() # Creating an object, or instance of class grandparent.

parent.reverse()

output = parent.reverse_str(st)

print("This is class output", output)






"""
grandparent
|
|
parents
|
|
you

"""

print(st)
print(st[::-1]) # string reveerse, prints the string in reversed manner

print(st[-1]) #[prints last character

print(st[::]) #prints whole string

