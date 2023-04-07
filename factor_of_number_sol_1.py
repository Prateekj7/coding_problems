#We need to calculate the number of factors of a number

num = 18
# 18 - 1, 2, 3, 6, 9, 18.. 1 to 18. We checked if the remained is 0

count_of_factors = 0

for iterator in range(1, 19):
    if num%iterator == 0:
        print(iterator)
        count_of_factors = count_of_factors+1
    
print(count_of_factors)


# NUM/ITERATOR -->QUOTIENT 18/2 = 9
# NUM%ITERATOR -->REMAINDER 18%2 = 0