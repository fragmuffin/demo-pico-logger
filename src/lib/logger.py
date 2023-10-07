import uasyncio as asyncio
import machine
import time

INTERFACE_MAP = (
    ('GP0',  machine.Pin('GP0', machine.Pin.IN)),
    ('GP1', machine.Pin('GP0', machine.Pin.IN)),
    ('ADC0', machine.ADC(0)),
    ('ADC1', machine.ADC(1)),
)

DEFAULT_PERIOD = 1000


def collect():
    for (name, obj) in INTERFACE_MAP:
        value = ''
        if isinstance(obj, machine.Pin):
            value = obj.value()
        elif isinstance(obj, machine.ADC):
            value = obj.read_u16()
        yield (name, value)

async def task(logfile:str, period:int=DEFAULT_PERIOD):
    with open(logfile, 'a') as csv:
        if csv.seek(0, 2) == 0: # seek to end of file; file is empty
            csv.write(','.join(name for (name, _) in INTERFACE_MAP) + '\n')  # write header

        while True:
            loop_start = time.ticks_ms()
            csv.write(','.join(f'{val}' for (_, val) in collect()) + '\n')
        
            await asyncio.sleep_ms(max(0, min(period - time.ticks_diff(time.ticks_ms(), loop_start), period)))