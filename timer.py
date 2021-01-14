# Code adapted from Codegnan tutorial
# https://www.youtube.com/watch?v=ekOeCnCSyUc
from datetime import *
current_time = datetime.now()
print(current_time)

print(current_time.year)
print(current_time.month)
print(current_time.day)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)




"""
import time

a = time.time()
print(a)


b = time.localtime(a)
print(b)


c = time.ctime(a)
print(c)


start = input("Press enter to start the timer")

print("The timer has started")

# starts the timer
begin = time.time()
print(begin)

# when the user presses 'enter' the timer will stop
endtimer = input("Press enter to stop the timer")

# gets the time at the point the user presses enter
end = time.time()
print(end)

# works out the difference between when the timer started
# and when the user presses enter
elapsed = end - begin
# casts it to an integer to get rid of the decimals
elapsed = int(elapsed)

print("The time elapsed is" ,elapsed, "seconds")

"""