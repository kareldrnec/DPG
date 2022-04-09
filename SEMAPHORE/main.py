import threading
import time

n, m = map(int, input().split())

semaphore = threading.Semaphore(m)

def parse_thread(name):
    x = name.split('-')
    if int(x[1]) < 10:
        return f"Thread-0{x[1]}"
    return name

def print_thread(id):
    name = parse_thread(id)
    #print(f"Count: {semaphore._value}")
    if not semaphore.acquire(True, .1): 
        print(f"{name} is waiting...")
        time.sleep(.3)
    print(f"Hello from {name}!")
    time.sleep(.3)

def fn():
    print_thread(threading.current_thread().name)

threads = [threading.Thread(target=fn) for _ in range(n)]

[t.start() for t in threads]
[t.join() for t in threads]
