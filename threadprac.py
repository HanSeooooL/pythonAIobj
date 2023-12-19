import threading as th
import asyncio as sync

def sum(
    a: int,
    b: int
) -> None:
    print(a, b, a+b)

ths = []

for i in range(10):
    t = th.Thread(target=sum, args=(i, i + 1))
    t.start()
    ths.append(t)