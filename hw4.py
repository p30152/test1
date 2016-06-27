import argparse, socket, sys
import getpass
import threading
import time

Hz={'49':'261','50':'293','51':'329','52':'349','53':'392','54':'440','55':'493.9',"56":"0","57":"0"}  #56 57 大鼓與小鼓

def subThreadIn(myconnection,range):
  
  while True:    
    message = myconnection.recv(1024).decode("utf-8") 
    print(message) # print the receiving message
    music = message.split(",")
    rythm=int(Hz.get(music[0]))   #transform the system key(string) to int -->Do re mi
    
    up_down= music[1]  
    try:
      up_down=int(up_down) #transform the system key(string) to int --> + - or null 
    except:
      up_down=1 #if null, set=1
   
    SumHZ=0
    if(up_down==107 or up_down==109):
        if(up_down==107 and range<=2):  # +:107
          range+=1
          SumHZ=range*rythm 
        elif(up_down==109 and range>1): # -:109
          range-=1
          SumHZ=range*rythm
        else:                           # if range <0 or range >3 
          SumHZ=range*rythm
    else:                               #if null
          SumHZ=range*rythm
    print(range)
    print(SumHZ)                    # broadcast the HZ
    print("HZ")
       
   
def server(interface, port):
 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 sock.bind((interface, port))
 sock.listen(2) 
 sock.settimeout(40)         # set Time 40 sec
 print("server Start~~")
 while True:
  connection, addr = sock.accept() 
  try:
    range=1 # set the +- range from 1
    mythread = threading.Thread(target=subThreadIn, args=(connection,range))
    mythread.setDaemon(True)
    mythread.start()
  except :  
    pass
    #sock.close()


def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print("client Start~~")   
    while True:
       try:
           num_item = input() # key the Do re mi fa so 
           adjust= input() # key + -
           pair=num_item+","+adjust 
           sock.send(pair.encode("utf-8"))
       except:
           print('lose connection!')
           break

    #sock.close()



if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)