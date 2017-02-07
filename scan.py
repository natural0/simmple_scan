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
            connScan(tgtHost,int(tgtPort)) 

def main():
    parser = optparse.OptionParser()
    parser.add_option("-H","--Host",dest='tgtHost',help='input Host address')
    parser.add_option("-p","--Ports",dest='tgtPort',help='input ports')
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    args.append(tgtPort)
    if (tgtPort == None) | (tgtHost == None):
        print('----you must input Host and Port----')
        exit(0)
    portScan(tgtHost,args)
if __name__=='__main__':
    main()
