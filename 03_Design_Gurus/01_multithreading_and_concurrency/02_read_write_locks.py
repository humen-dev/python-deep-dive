import threading
import time

# Global shared resource
counter = 0
# Shared mutex for synchronization
lock = threading.Lock()
# We will increment counter until it reaches TARGET_VALUE
TARGET_VALUE = 1000

# Write operation - Use write lock
def increment_value():
    global counter
    with lock:  # Acquire the lock
        time.sleep(0.001)  # Sleep for 1 millisecond
        if counter < TARGET_VALUE:
            counter += 1
    return counter

# Read operation - Use shared lock
def read_value():
    with lock:  # Acquire the lock
        time.sleep(0.001)  # Sleep for 1 millisecond
        return counter

def reader():
    while read_value() < TARGET_VALUE:
        time.sleep(0.001)  # Sleep for 1 millisecond

def writer():
    while increment_value() < TARGET_VALUE:
        time.sleep(0.001)  # Sleep for 1 millisecond

def main():
    start = time.time()

    # Creating 8 reader threads
    readers = [threading.Thread(target=reader) for _ in range(8)]

    # Creating 2 writer threads
    writers = [threading.Thread(target=writer) for _ in range(2)]

    for t in readers + writers:
        t.start()

    for t in readers + writers:
        t.join()

    end = time.time()
    print("Time taken:", end - start, "seconds")

if __name__ == "__main__":
    main()
