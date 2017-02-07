#coding=utf-8
import socket
import optparse

def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        print("[+]%d/tcp open" % tgtPort)
        connSkt.close()

    except:
        print("[-]%d/tcp close" % tgtPort)

def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print("[-]cannot connect %s" % tgtIP)
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print("\n[+]Scan results for:" + tgtName[0])
    except:
        print("\n[+]scan results for:" + tgtIP)
        socket.setdefaulttimeout(1)
        for tgtPort in tgtPorts:
            print("scanning port:" + str(tgtPort))
            connScan(tgtHost,tgtPort) 
portScan("www.baidu.com",[80,443,3389,1433,23,445,80])
