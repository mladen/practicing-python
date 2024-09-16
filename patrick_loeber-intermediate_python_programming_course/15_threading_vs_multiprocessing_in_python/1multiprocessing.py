from multiprocessing import Process
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    print(
        f"\nRunning {num_processes} processes on {os.name} which has {os.cpu_count()} CPUs!"
    )

    for i in range(num_processes):
        print(f"Main    : create and start process {i}")
        p = Process(target=square_numbers)
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("All processes done!")
