import time
import random
import threading


time_limit = 60
timer_running = True
sum = 0

def timer():
    global timer_running, time_limit
    for t in range(time_limit, -1, -1):
        print("Time: ",t)
        time.sleep(1)
    timer_running = False

def play_game():
    sum = 0
    count = 0
    while timer_running:
        random_number = random.randint(1, 20)
        print(f"Add {random_number}. Current sum: {sum}")
        try:
            ans = int(input("New sum: "))
        except ValueError:
            print("That’s not even a number.")
            continue
        if ans == sum + random_number:
            sum = ans
            count += 1
        else:
            print("Wrong! -1 sec")
            global time_left
            time_left = max(0, time_left - 1)
    print(f"Total Count: {count}")
13

t1 = threading.Thread(target=timer)
t2 = threading.Thread(target=play_game)

t1.start()
t2.start()

t1.join()
t2.join()
