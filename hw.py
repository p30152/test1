import argparse,socket
import struct
from uuid import getnode as get_mac
from random import randint
from datetime import datetime


def getMacInBytes():  #get mac address
    mac = str(hex(get_mac()))
    mac = mac[2:]
    while len(mac) < 12 :
        mac = '0' + mac
    macb = b''
    for i in range(0, 12, 2) :
        m = int(mac[i:i + 2], 16)
        macb += struct.pack('!B', m)
    return macb

class DHCPDiscover:
    def __init__(self):
        self.transactionID = b''      # 
        

    def buildPacket(self):
        macb = getMacInBytes()
        packet = b''
        packet += b'\x01'   #Message type: Boot Request (1)
        packet += b'\x01'   #Hardware type: Ethernet
        packet += b'\x06'   #Hardware address length: 6
        packet += b'\x00'   #Hops: 0 
        packet += b'\x39\x03\xF3\x26'       #Transaction ID
        packet += b'\x00\x00'    #Seconds elapsed: 0
        packet += b'\x80\x00'   #Bootp flags: 0x8000 (Broadcast) + reserved flags
        packet += b'\x00\x00\x00\x00'   #Client IP address: 0.0.0.0
        packet += b'\x00\x00\x00\x00'   #Your (client) IP address: 0.0.0.0
        packet += b'\x00\x00\x00\x00'   #Next server IP address: 0.0.0.0
        packet += b'\x00\x00\x00\x00'   #Relay agent IP address: 0.0.0.0
       # packet +=  b'\x54\xA0\x50\x87\x57\xEF'   #Client MAC address: 54:A0:50:87:57:EF
        packet += macb
        packet += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'   #Client hardware address padding: 00000000000000000000
        packet += b'\x00' * 67  #Server host name not given
        packet += b'\x00' * 125 #Boot file name not given
        packet += b'\x63\x82\x53\x63'   #Magic cookie: DHCP
        packet += b'\x35\x01\x01'   #Option: (t=53,l=1) DHCP Message Type = DHCP Discover
        #packet += b'\x3d\x06\x00\x26\x9e\x04\x1e\x9b'   #Option: (t=61,l=6) Client identifier
        packet += b'\x3d\x06' + macb
        packet += b'\x37\x03\x03\x01\x06'   #Option: (t=55,l=3) Parameter Request List
        packet += b'\xff'   #End Option
        return packet

     
        
    def buildOfferPacket(self):
        offerIP="192.168.1.100"
        macb = getMacInBytes()
        packet = b''
        packet += b'\x02'   #Message type: Boot Request (1)
        packet += b'\x01'   #Hardware type: Ethernet
        packet += b'\x06'   #Hardware address length: 6
        packet += b'\x00'   #Hops: 0 
        packet += b'\x39\x03\xF3\x26'      #Transaction ID
        packet += b'\x00\x00'    #Seconds elapsed: 0
        packet += b'\x80\x00'   #Bootp flags: 0x8000 (Broadcast) + reserved flags
        packet += b'\x00\x00\x00\x00'   #Client IP address: 0.0.0.0
        packet += b'\xC0\xA8\x01\x64'   #Your (client) IP address: 192.168.1.100
        packet += b'\xC0\xA8\x01\x01'   #Next server IP address: 192.168.1.1
        packet += b'\x00\x00\x00\x00'   #Relay agent IP address: 0.0.0.0
       # packet +=  b'\x54\xA0\x50\x87\x57\xEF'   #Client MAC address: 54:A0:50:87:57:EF
        packet += macb
        packet += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'   #Client hardware address padding: 00000000000000000000
        packet += b'\x00' * 67  #Server host name not given
        packet += b'\x00' * 125 #Boot file name not given
        packet += b'\x63\x82\x53\x63'   #Magic cookie: DHCP
        packet += b'\x35\x01\x02'   #Option: (t=53,l=2) DHCP Message Type = DHCP offer
        #packet += b'\x3d\x06\x00\x26\x9e\x04\x1e\x9b'   #Option: (t=61,l=6) Client identifier
        packet += b'\x3d\x06' + macb
        packet += b'\x37\x03\x03\x01\x06'   #Option: (t=55,l=3) Parameter Request List
        packet += b'\xff'   #End Option
        return packet

    def buildRequestPacket(self):
        macb = getMacInBytes()
        packet = b''
        packet += b'\x01'   #Message type: Boot Request (1)
        packet += b'\x01'   #Hardware type: Ethernet
        packet += b'\x06'   #Hardware address length: 6
        packet += b'\x00'   #Hops: 0 
        packet += b'\x39\x03\xF3\x26'     #Transaction ID
        packet += b'\x00\x00'    #Seconds elapsed: 0
        packet += b'\x80\x00'   #Bootp flags: 0x8000 (Broadcast) + reserved flags
        packet += b'\x00\x00\x00\x00'   #Client IP address: 0.0.0.0
        packet += b'\x00\x00\x00\x00'   #Your (client) IP address: 0.0.0.0
        packet += b'\xC0\xA8\x01\x01'   #Next server IP address: 192.168.1.1
        packet += b'\x00\x00\x00\x00'   #Relay agent IP address: 0.0.0.0
       # packet +=  b'\x54\xA0\x50\x87\x57\xEF'   #Client MAC address: 54:A0:50:87:57:EF
        packet += macb
        packet += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'   #Client hardware address padding: 00000000000000000000
        packet += b'\x00' * 67  #Server host name not given
        packet += b'\x00' * 125 #Boot file name not given
        packet += b'\x63\x82\x53\x63'   #Magic cookie: DHCP
        packet += b'\x35\x01\x03'   #Option: (t=53,l=3) DHCP Message Type = DHCP Request
        #packet += b'\x3d\x06\x00\x26\x9e\x04\x1e\x9b'   #Option: (t=61,l=6) Client identifier
        packet += b'\x3d\x06' + macb
        packet += b'\x37\x03\x03\x01\x06'   #Option: (t=55,l=3) Parameter Request List
        packet += b'\xff'   #End Option
        return packet
    
    def buildAckPacket(self):
        macb = getMacInBytes()
        packet = b''
        packet += b'\x02'   #Message type: Boot Request (1)
        packet += b'\x01'   #Hardware type: Ethernet
        packet += b'\x06'   #Hardware address length: 6
        packet += b'\x00'   #Hops: 0 
        packet += b'\x39\x03\xF3\x26'      #Transaction ID
        packet += b'\x00\x00'    #Seconds elapsed: 0
        packet += b'\x80\x00'   #Bootp flags: 0x8000 (Broadcast) + reserved flags
        packet += b'\x00\x00\x00\x00'   #Client IP address: 0.0.0.0
        packet += b'\xC0\xA8\x01\x64'   #Your (client) IP address: 192.168.1.100
        packet += b'\xC0\xA8\x01\x01'   #Next server IP address: 192.168.1.1
        packet += b'\x00\x00\x00\x00'   #Relay agent IP address: 0.0.0.0
        #packet +=  b'\x54\xA0\x50\x87\x57\xEF'   #Client MAC address: 54:A0:50:87:57:EF
        packet += macb
        packet += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'   #Client hardware address padding: 00000000000000000000
        packet += b'\x00' * 67  #Server host name not given
        packet += b'\x00' * 125 #Boot file name not given
        packet += b'\x63\x82\x53\x63'   #Magic cookie: DHCP
        packet += b'\x35\x01\x05'   #Option: (t=53,l=6) DHCP Message Type = DHCP Ack
        #packet += b'\x3d\x06\x00\x26\x9e\x04\x1e\x9b'   #Option: (t=61,l=6) Client identifier
        packet += b'\x3d\x06' + macb
        packet += b'\x37\x03\x03\x01\x06'   #Option: (t=55,l=3) Parameter Request List
        packet += b'\xff'   #End Option
        return packet

def client(port): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    discoverPacket = DHCPDiscover()
    packettext=discoverPacket.buildPacket()
    sock.bind(('', 68))     #   server to client   on port 67  
    sock.settimeout(20)
    try:
        while True:
         sock.sendto(packettext, ('<broadcast>', 67))  #client send to server from port 68       
        
         data,address = sock.recvfrom(1024)
         if(data[242]==2):
            print("send request")
            request = discoverPacket.buildRequestPacket()
            sock.sendto(request, ('255.255.255.255', 67))
            break
         elif(data[242]==6):
            print("got ack")
            break
    except socket.timeout as e:
        print(e)
    
    

def server(port):
    #defining the socket
    dhcps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #internet, UDP
    dhcps.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) #broadcast
    dhcps.bind(('', 67))    #   client to server on port 67  
    discoverPacket = DHCPDiscover()
    dhcps.settimeout(20)
    try:
        while True:
          data = dhcps.recv(1024)
          if(data[242]==1):
            print("send offer")
            offer = discoverPacket.buildOfferPacket()
            dhcps.sendto(offer, ('255.255.255.255', 68))  #server to client from port 68
          elif(data[242]==3):
            print("got request")
            Ack = discoverPacket.buildAckPacket()
            dhcps.sendto(Ack, ('255.255.255.255', 68))  #server to client from port 68
            break
    except socket.timeout as e:
        print(e)
    

    

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='port', type=int, default=1060,help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)



