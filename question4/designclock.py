def convert_12hr_to_24hr(time):
    print("hello 12hr")
    return 24

def convert_24hr_to12hr(time):
    print('hello 24hr')
    return 12




def clock():
    time = input("Enter the time: ")
    print(time)

    #12 hr - 12pm, 01pm, 01am
    #24hr - 23, 11, 07, 15
    #Check whst kind of time it is

    # check using length, Calculate time
    time_24 = 0
    time_12 = 0
    if len(time) == 4:
        time_24 = convert_12hr_to_24hr(time)
    
    if len(time) == 2:
        time_12 = convert_24hr_to12hr(time)

    # check using am/pm is there or not
    hour = time[2:]                             #--slicing  , a cake and we slice it to different pieces. time = 12am , 12 am
    if time[2:] == 'am' or time[2:] == 'pm':
        time_24 = convert_12hr_to_24hr(time)
    else:
        time_12 = convert_24hr_to12hr(time)

    

    #write the output
    print("This is the 12hr format in converted form ", time_24)
    print("This is the 24hr format in converted form ", time_12)


clock()