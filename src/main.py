import os
import sys
sys.path.append('/'.join([os.getcwd(), 'lib']))

import uasyncio as asyncio
import machine

import heartbeat
import logger

async def main():
    await asyncio.gather(
        logger.task(
            logfile='/'.join([os.getcwd(), 'data', 'output.csv']),
            period=2000,  # log every 2sec (unit: ms)
        ),
        heartbeat.task(
            led=machine.Pin('LED', machine.Pin.OUT),  # LED to blink
            period=1000,
        ),
    )

def run():
    asyncio.run(main())
#run()  # <-- un-comment this when copied to hardware

