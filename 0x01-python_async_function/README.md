# Python Async Cheatsheet

## Async Basics

### Async Functions

``` Python
async def async_function():
    # Define asynchronous functions using the async keyword.
    # Asynchronous code can be executed within these functions.
```

### Event Loop

``` Python
import asyncio

async def main():
    # The event loop manages asynchronous tasks and coroutines.
    # Use asyncio.gather() to run multiple coroutines concurrently.
    await asyncio.gather(coroutine1(), coroutine2())

if __name__ == "__main__":
    # Run the main event loop using asyncio.run().
    asyncio.run(main())
```

## Coroutine Control Flow

### `await`

``` Python
result = await coroutine()
# Use the await keyword to pause execution until the coroutine completes.
```

### `asyncio.gather()`

``` Python
await asyncio.gather(coroutine1(), coroutine2())
# Concurrently run multiple coroutines and await their completion.
```

### `asyncio.wait()`

``` Python
done, pending = await asyncio.wait([coroutine1(), coroutine2()])
# Wait for any of the specified coroutines to complete.
```

## Timers

### `asyncio.sleep()`

``` Python
await asyncio.sleep(1)
# Suspend the coroutine for the specified number of seconds.
```

### `asyncio.timeout()`

``` Python
with asyncio.timeout(5):
    await some_coroutine()
# Timeout a coroutine if it doesn't complete within the specified time.
```

## Tasks

### `asyncio.create_task()`

``` Python
task1 = asyncio.create_task(coroutine1())
task2 = asyncio.create_task(coroutine2())
# Create tasks to run coroutines concurrently and await their completion.
```

## Locks and Semaphores

### `asyncio.Lock()`

``` Python
lock = asyncio.Lock()

async with lock:
    # Use locks to manage access to shared resources in a coroutine.
    # Enter a critical section using async with lock.
```

### `asyncio.Semaphore()`

``` Python
semaphore = asyncio.Semaphore(5)

async with semaphore:
    # Use semaphores to limit the number of coroutines that can run concurrently.
    # Enter a critical section with a limited number of permits.
```

## Error Handling

### `try`-`except`

``` Python
try:
    result = await some_coroutine()
except SomeException as e:
    print(f"An error occurred: {e}")
# Use try-except blocks to handle exceptions in asynchronous code.
```

## Communication Between Coroutines

### Queues

``` Python
queue = asyncio.Queue()

async def producer():
    await queue.put(data)

async def consumer():
    data = await queue.get()
# Use asyncio.Queue for communication between producer and consumer coroutines.
```

## Running Sync Code in Async

### `loop.run_in_executor()`

``` Python
import concurrent.futures

def sync_function():
    # synchronous code

await loop.run_in_executor(None, sync_function)
# Run synchronous code in an executor to prevent blocking the event loop.
```

## External Libraries

### `httpx`

``` Python
import httpx

async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.text
# Use httpx for asynchronous HTTP requests with a simple and flexible API.
```

### `aiohttp`

``` Python
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.text()
# Aiohttp is an asynchronous HTTP client that supports multiple protocols.
# Use it for making asynchronous HTTP requests.
```
