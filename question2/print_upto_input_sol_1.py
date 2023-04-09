input_integer = input("Print any number greater than 0 - ")

# 1 , 2, 3, 4,5 ,6, 7,8 , 9.........N - natural numbers

start_number = 1

#end_number is my input_integer

current_number = start_number #1
end_number = input_integer    # 10

#Run a loop. Loop is a piece of code which runs continuously until it satisfies a condition. But we have to be aware to give the proper condition.

while(current_number <= int(end_number)):
    print(current_number, end=", ")
    current_number = current_number+1












