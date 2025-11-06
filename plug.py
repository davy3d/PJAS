#!/usr/bin/env python3
import sys
import asyncio
from kasa.iot import IotPlug
from pathlib import Path
import datetime
#from datetime import datetime
import time
eMon = ('emeter_status.txt')

IP = "192.168.1.137"

async def off():
    p = IotPlug(IP)

    await p.update()  # Request the update
    print(p.alias)  # Print out the alias
    #print(p.emeter_realtime)  # Print out current emeter status

    await p.turn_off()  # Turn the device off


async def on():
    p = IotPlug(IP)

    await p.update()  # Request the update
    print(p.alias)  # Print out the alias
    #print(p.emeter_realtime)  # Print out current emeter status
    
    await p.turn_on()  # Turn the device on

async def status():
    p = IotPlug(IP)
    pa = Path('emeter_status.txt')
    await p.update()
    print(datetime.datetime.now(), p.emeter_realtime)
    em = str(p.emeter_realtime)
    dt = str(datetime.datetime.now())
    text = pa.read_text()
    pa.write_text(f"{text}\n{em}\n{dt}\n")

async def loop():
    while True:
        p = IotPlug(IP)
        await p.turn_on()
        #print('on')
        time.sleep(600)
        await p.turn_off()
        #print('off')
        time.sleep(600)

async def bcp():
    while True:
        p = IotPlug(IP)
        await p.turn_on()
        print('Boom')
        time.sleep(0.5)
        print('chicka')
        time.sleep(0.5)
        print('pop')
        time.sleep(0.5)
        await p.turn_off()
        print('chicka')
        time.sleep(0.5)
        print('chicka')
        time.sleep(0.5)
        print('pop')
        time.sleep(0.5)
        print('chicka')
        time.sleep(0.5)
        #print('off')
       # time.sleep(600)

#print(sys.argv)
if len(sys.argv) == 1:
    print('Add on, off ,or status. (or bcp:)')
    pass

elif sys.argv[1] == 'on':
    print("we will turn it on")
    asyncio.run(on())
    if IP != "192.168.1.116":
        asyncio.run(status())
    pass
    
elif sys.argv[1] == 'off':
    print("we will turn it off")
    asyncio.run(off())
    if IP != "192.168.1.116":
        asyncio.run(status())
    pass
    
elif sys.argv[1] == 'status':
    if IP != "192.168.1.16":
        asyncio.run(status())
    pass
    
elif sys.argv[1] == 'loop':
    if IP != "192.168.1.16":
        asyncio.run(status())
    asyncio.run(loop())
    pass
    
elif sys.argv[1] == 'bcp':
    print("we will beatbox!")
    time.sleep(1)
    asyncio.run(bcp())
    if IP != "192.168.1.116":
        asyncio.run(status())
    pass