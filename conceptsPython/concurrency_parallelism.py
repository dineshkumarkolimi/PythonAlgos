# Concurrency can be achieved with threads. There are different ways to do this. 

# I/O-bound tasks:
# When tasks involve waiting for external resources (like disk I/O or network I/O), 
# using threads (threading, concurrent.futures.ThreadPoolExecutor) or asyncio can 
# significantly improve performance.

# CPU-bound tasks:
# When tasks involve heavy computations, using processes (multiprocessing, 
# concurrent.futures.ProcessPoolExecutor) can take advntage of multiple CPU cores for parallel processing

# Key Concepts
# Global Interpreter Lock (GIL): Python’s GIL ensures that only one thread executes Python bytecode
# at a time, which limits the performance of CPU-bound multi-threaded applications. 
# To bypass this limitation, use multiprocessing.

# Event Loop: In asyncio, the event loop runs asynchronous tasks in an efficient, non-blocking manner.

# Summary
# Concurrency: Manage multiple tasks making progress over time (e.g., using threads or asyncio).
# Parallelism: Run multiple tasks at the same time on different CPU cores (e.g., using multiprocessing).
# Libraries: threading, multiprocessing, concurrent.futures, asyncio are the main libraries for handling concurrency and parallelism in Python.
# GIL: Limits CPU-bound multi-threaded performance; use multiprocessing to overcome it.
# Use Cases: Choose threading/asyncio for I/O-bound tasks and multiprocessing for CPU-bound tasks.

import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import asyncio

#first way
def print_num():
    for i in range(5):
        print(i)
        
thread = threading.Thread(target=print_num)
thread.start()
thread.join()

#second way
def fetch_url(url):
    return f"url fetched {url}"

urls = ['http://example.com', 'http://example.org', 'http://example.net']

# use concurrent.futures.ProcessPoolExecutor for multiprocesing
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(fetch_url, url) for url in urls]
    
for future in as_completed(futures):
    print(future.result())
    
# third way
async def main():
    for url in urls:
        result = await fetch_url()
        print(result)

asyncio.run(main())


#Multiprocessing
import multiprocessing

def square(x):
    return x*x
with multiprocessing.Pool(pool_size=4) as pool:
    results = pool.map(sqaure, L)
    print(result)
    
    
