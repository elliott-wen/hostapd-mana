import logging
import sys
logging.basicConfig(level=logging.INFO)
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # Shut up Scapy
from scapy.all import *
from scapy.layers.all import *
from scapy.layers import http
from scapy.layers.http import *
from threading import Thread, Lock
import fcntl
import struct
import json
from signal import SIGINT, signal
lock = Lock()
devices = {}
from threading import Thread, Lock
current_milli_time = lambda: int(round(time.time() * 1000))
startup_time = current_milli_time()
def addKeyValue(deviceMac,key,value):
    with lock:
        if deviceMac not in devices:
            devices[deviceMac] = {}
            devices[deviceMac]["qq"] = ""
            devices[deviceMac]["model"] = ""
            devices[deviceMac]["wangwang"] = ""
            devices[deviceMac]["weibo"] = ""
            devices[deviceMac]["mail"] = ""
            devices[deviceMac]["time"] = ""
        devices[deviceMac][key] = value
        print "Add key %s with value %s"%(key,value)

def dumpValue():
    r = []
    with lock:
        for key in devices.keys():
            copyItem = devices[key].copy()
            copyItem["mac"] = key
            r.append(copyItem)
    return r

def handleWeibo(deviceMac, pkt):
    path = pkt[HTTPRequest].Path
    params = path.split('&')
    #print params
    for item in params:
        if "gsid=" in item:
            addKeyValue(deviceMac,"weibo",item[5:])
        elif "ua=" in item:
            addKeyValue(deviceMac,"model",item[3:])

# def validateQQProtocl(pkt):
#     data = pkt[HTTP].load
#     if len(data)>50 and data[0] == '\x00' and data[1] == '\x00':
#             return True
#     return False

def handleQQ(deviceMac,pkt):
    number = ""

    try:
        data = pkt[HTTP].load
        if data[0:2] == '\x00\x00':
            if data[6:6+2] == '\x00\x08':
                ii = 0
                while not (data[ii]>='\x30' and data[ii]<='\x39' and data[ii+1]>='\x30' and data[ii+1]<='\x39' and data[ii+2]>='\x30' and data[ii+2]<='\x39' and data[ii+3]>='\x30' and data[ii+3]<='\x39' and data[ii+4]>='\x30' and data[ii+4]<='\x39' and data[ii+5]>='\x30' and data[ii+5]<='\x39'):
                    ii += 1
                    #print ii
                while data[ii]>='\x30' and data[ii]<='\x39':
                    number += data[ii]
                    ii+=1
                if len(number) >13:
                    number=number[:11]

            if len(number) != 0 and number != '0':
                addKeyValue(deviceMac, "qq", number)
    except:
        pass
        # print "Unable to parse qq"




def pcap_cb(pkt):

    if not pkt.haslayer(TCP):
        return
    deviceMac = pkt.src
    #print pkt.summary()
    if pkt.haslayer(HTTP):
        if pkt.haslayer(HTTPRequest):
            host = pkt[HTTPRequest].Host
            if "sina" in host or "weibo" in host:
                handleWeibo(deviceMac,pkt)
        else:
            handleQQ(deviceMac,pkt)


def stop(signal, frame):
    global runFlag
    runFlag = False
    print "Ready to quit"

def generateClient():
    p = subprocess.Popen(["iw",mon_iface,'station','dump'],stdout=subprocess.PIPE)
    clientFile = open("client.txt","w")

    #clientFile.write("Last updated in %s\n"%(time.time()))
    for line in p.stdout.readlines():
        if "Station" in line:
            clientFile.write(line[8:25]+'\n')
        elif "inactive" in line:
            imstring = line.strip().split("\t")[1]
            updatetime = str(current_milli_time()-startup_time-int(imstring.split(" ")[0]))
            clientFile.write(updatetime+'\n')
        elif "signal:" in line:
            imstring = line.strip().split("\t")[1]
            clientFile.write(imstring.split(" ")[0])
    clientFile.close()




def generateJson():
    r = dumpValue()
    jsonString = json.dumps(r)
    jsonFile = open("data.json","w")
    jsonFile.write(jsonString)
    jsonFile.close()

def generateFile():
    while True:
        time.sleep(2)
        generateJson()
        generateClient()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please specify a device"
        exit(1)
    mon_iface = sys.argv[1]
    conf.iface = mon_iface

    conf.verb = 1
    fileThread = Thread(target=generateFile)
    fileThread.start()
    sniff(iface=mon_iface, store=0, prn=pcap_cb,filter="(tcp dst port 80 ||tcp dst port 8080)")


