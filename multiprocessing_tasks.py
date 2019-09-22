import concurrent.futures
import time

def do_something(seconds):
        print(f'Sleeping for {seconds} Second...')
        time.sleep(seconds)
        return f'Done Sleeping {seconds} seconds.....'

if __name__ == '__main__':
    start = time.perf_counter()

    secs = [5,4,3,2,1]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(do_something, sec) for sec in secs]

        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2)} seconds....')