import asyncio
import random

#asyncio 비동기처리 library

async def show(x):
    x = random.sample([1,2,3], k = 1)
    await(asyncio.sleep(x[0]))
    print(x)
count = 0

async def main():
    await asyncio.gather(
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
    )
    
    
asyncio.run(main())