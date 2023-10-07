import machine
import uasyncio as asyncio

PERIOD = 1000


async def task(led:machine.Pin, period:int=PERIOD):
    while True:
        led.value(1)
        await asyncio.sleep_ms(min(50, period))
        led.value(0)
        await asyncio.sleep_ms(max(0, period - 50))

