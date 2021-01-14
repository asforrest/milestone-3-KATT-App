import time
def time_convert(secs):
    mins = secs // 60
    secs = secs % 60
    hours = mins // 60
    min = mins % 60
    print("Duration = {0}:{1}:{2}".format(int(hours),int(mins),int(secs)))
input("Press Enter to start")
start_time = time.time()
try:
    hours = 0
    while True:
        for minutes in range(0, 60):
            for seconds in range(0, 60):
                time.sleep(1)
                print(hours, ":", minutes, ":", seconds+1)
except KeyboardInterrupt:
    end_time = time.time()
    time_duration = end_time - start_time
    time_convert(time_duration)