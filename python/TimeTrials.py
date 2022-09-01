from datetime import datetime
from distutils.file_util import write_file
from email import message
from tkinter import Y

#start_time = "2.30.00"
#end_time = "24.46.38"
#rider_name = "Troy"
print("\n")
f = open("TimeTrial.txt","a")
f.write("Time Trials   DateTime:  " + str(datetime.now()) + "\n")
print("Welcome to Time Trials!!!\n") 



cont = True

while cont:
    print("\n")
    rider_name = input("Enter Rider's Name: ")
    
    start_time = input("Enter Start Time: ")
        
    end_time = input("Enter End Time: ")
    
    print("\n")
    # convert time string to datetime
    t1 = datetime.strptime(start_time, "%M.%S.%f")
    print('Start time:', t1.time())

    t2 = datetime.strptime(end_time, "%M.%S.%f")
    print('End time:', t2.time(),)
    print("\n")
    # get difference
    delta = t2 - t1

    # time difference in seconds
    
    message = "Name: " + rider_name + "  |  " + "Time: " + str(delta) + "\n"
    print("Name: ",rider_name,"Time: ", delta)
    f.write(message)
    
    
    

    print("Continue?")
    print("Enter: Y/N")
    inpt = input()
    if inpt.lower() == ("n"):
        cont = False

print("\n")
print("Great Ride!!!")
print("\n")
f.close()





# time difference in milliseconds
#ms = delta.total_seconds() * 1000
#print(f"Time difference is {ms} milliseconds")
#print(f"Time difference is {delta.total_seconds()} seconds")