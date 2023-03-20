import chromance, hub, profileManager, network, colours, time
import uasyncio as asyncio

wlan = network.WLAN(network.STA_IF)

def connectToNetwork():
    ssid = ""
    password = ""

    wlan.active(True)
    wlan.connect(ssid, password)

    timeout = 10
    connectionTime = 0

    while connectionTime < timeout:
        if wlan.status() < 0 or wlan.status() >= 3: break
        connectionTime += 1
        time.sleep(1)
    
    if wlan.status() != 3:
        raise RuntimeError("Network connection failed")
    else:
        status = wlan.ifconfig()
        
async def checkForClients(reader, writer):
    request_line = await reader.readline()
    request = str(request_line)[2:-1]
    profileManager.setProfile(request)

async def main():
    connectToNetwork()
    asyncio.create_task(asyncio.start_server(checkForClients, "192.168.1.123", 9876))
    
    while True:
        profileManager.doUpdateForCurrentProfile(chromance.profile)
        chromance.update()
        chromance.writeUpdates()
        
        if chromance.trackCurrent:
            print(f'{chromance.getCurrent()}mA')
            
        await asyncio.sleep(chromance.speed)
            
##################### Main Script #####################

chromance.off()
chromance.trackCurrent = True
profileManager.setProfile(profileManager.heart)

try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()
