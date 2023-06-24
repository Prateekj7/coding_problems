"""
Pattern1
*
**
***
****

Pattern2
****
***
**
*

"""

#Given an Input N, print this pattern

class Patterns:

    def pattern1(self, N):
        # for loop or a while loop
        for iter in range(1, N+1):
            #first loop is keeping track of the row
            for sec_iter in range(iter):
                #second loop is keeping track of the number of stars
                print("*", end=" ")
            print("\r")
        pass

    def pattern2(self, N):
        pass


    def base(self):
        number = input("Give input for pattern - ")
        print("****Pattern1****")
        number = int(number)
        self.pattern1(number) #This runs because the number of strs is equal to number of rows

p = Patterns()
p.base()





