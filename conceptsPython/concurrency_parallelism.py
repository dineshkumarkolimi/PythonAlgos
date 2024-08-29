# Concurrency can be achieved with threads. There are different ways to do this. 


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
    
    
