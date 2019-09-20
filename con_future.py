import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping for {seconds} second")
    time.sleep(seconds)
    return f"Done Sleeping......{seconds}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [1,5,6,4,3,2]
    results = [executor.submit(do_something, sec) for sec in secs ]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

    '''Returns the result in the order it was started'''
    # results = executor.map(do_something, secs)
    # for result in results:
    #     print(result)

# threads = []

# for _ in range(10):
#     t = threading.Thread(target= do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()


finish = time.perf_counter()
answer = round(finish-start, 2)
print(f"Finished in {answer} seconds")