import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0,-1):
    seconds = x % 60# this is done to see  how many leftoever we have after taking out the whole minute
    minutes = int(x/60) % 60 # this tells us how many minutes there are and then modulus makes sure it is within 0-59 clock range
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Times up")
