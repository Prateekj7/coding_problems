num = 1234567

result = ""


for i in range(0, len(str(num))):
    rem = num%10
    result += str(rem)
    num = int(num/10)

print("this is reversed number ", result)

"""
# concept of modulus, % - remainder
rem = num%10
print(rem)
result += str(rem)
print("this is result", result)

# 100%10 - remiander?  0
# 89%10 - remainder? 9
# 55%10 -  remainder? 5
num = int(num/10)
print(num)



# doing this again
rem = num%10
print(rem)
result += str(rem)
print("this is result", result)

num = int(num/10)
print(num)

"""


