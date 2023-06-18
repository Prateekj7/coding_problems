string = ['a','y','a','a','n']

#output - "naaya"
"""
swap fist character and last character
n y a a a
swap second character and second last character
n a a y a

"""

left = 0
right = len(string)-1

while(left<right):
    print(left, right)
    temp = string[right]
    string[right] = string[left]
    string[left] = temp
    left+=1
    right-=1


print(string)









