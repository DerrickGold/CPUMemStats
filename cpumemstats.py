#!/usr/bin/env python3

#
# Update CPU and Memory Stats
# Python v3.4
#

import asyncio
import websockets
import signal
import sys
import psutil
import time

class SignalHandler:

    _do_exit = False
    
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_handler)
        signal.signal(signal.SIGTERM, self.exit_handler)

    def exit_handler(self, signum, frame):
        self._do_exit = True

    def getExitStatus(self):
        return self._do_exit





def makeCmd(cmd, data):
    return "{\"command\":\"" + cmd + "\", \"data\":" + data + "}"


def jsCommand(cmd, args):
    jscmd = "{\"fn\":\"" + cmd + "\",\"args\":" + args + "}"
    return makeCmd("jsPluginCmd", jscmd)
    

    
    
    
@asyncio.coroutine
def socketHandler(protocol, port):

    print("Protocol: " + protocol)
    print("Port: " + port)
    sigExit = SignalHandler()

    #headers={"Sec-WebSocket-Protocol": protocol}
    #protocolHandler=[ClientProtocol]
    protocolHandler=[protocol]
    websocket = yield from websockets.connect('ws://localhost:' + port, subprotocols=protocolHandler)
    

    #cmd = "{\"command\":\"jsPluginCmd\",\"data\":{\"fn\":\"printMsg\",\"args\":\"Hello, World\"}}"
    while not sigExit.getExitStatus():

        #send current cpu usage
        cpuUsage = psutil.cpu_percent(percpu=True)
        
        yield from websocket.send(jsCommand("updateCpu", str(cpuUsage)))
        #update every second
        time.sleep(1)


    yield from websocket.close()



#program entry
asyncio.get_event_loop().run_until_complete(socketHandler(sys.argv[1], sys.argv[2]))



    
