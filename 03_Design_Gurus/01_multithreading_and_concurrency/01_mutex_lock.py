import threading
import time


class Solution:
    counter = 0
    lock = threading.Lock()

    @staticmethod
    def run_experiment(experiment_name, task):
        Solution.counter = 0

        t1 = threading.Thread(target=task)
        t2 = threading.Thread(target=task)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print(f"Final counter value {experiment_name}: {Solution.counter}\n")

    @staticmethod
    def increment_counter_with_mutex():
        for _ in range(100):
            with Solution.lock:
                temp = Solution.counter
                time.sleep(0.001)  # Sleep for 1 millisecond
                Solution.counter = temp + 1

    @staticmethod
    def increment_counter_no_mutex():
        for _ in range(100):
            temp = Solution.counter
            time.sleep(0.001)  # Sleep for 1 millisecond
            Solution.counter = temp + 1


if __name__ == "__main__":
    Solution.run_experiment(
        "With Mutex Experiment", Solution.increment_counter_with_mutex
    )
    Solution.run_experiment("No Mutex Experiment", Solution.increment_counter_no_mutex)
