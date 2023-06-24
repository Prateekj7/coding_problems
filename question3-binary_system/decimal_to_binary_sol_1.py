num = int(input("Please give a input number "))

print(f"This is the input number {num}")

# 4 - decimal numer, if i want to convert to a binary number - I have to do a prime factorization method

# 4/2 = 0, 2/2 = 0, 5 decimal -  101
# ecimal 6 - binary 110

storage = []
while(num>=1):
    rem = num%2 
    quot = int(num/2) #CDividing and converting the float to a integer
    num = quot
    storage.append(rem) # we are stroing the remainders as they are the binary bit values

print(f" This is the binary form of the deciaml input number in reverse {storage}")  # 011  -  110 .    

print(f"Lenght of storage is {len(storage)}") # this will give ouptut as 3 for [0, 1, 1]

start_of_storage = 0 # it will check the current lenght and stop when its greater than storage length
end_of_storage = len(storage)-1 # this is the end index of storage


# 0 1 1;
while(start_of_storage <=  end_of_storage):
    temporary = storage[start_of_storage]

    #now swap
    storage[start_of_storage] = storage[end_of_storage]
    storage[end_of_storage] = temporary

    start_of_storage += 1
    end_of_storage -=1

print(f"This is the reversed version of sotrage {storage}")

#2 numeric data types - int and float. int - Alll integers, float - All decimal numbers.
#When we do divsion, it always gives the output in float format.

#int() basically converts any number (decimal or not) into a integer

# decimal number 4 , binary number 100