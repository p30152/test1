import argparse, socket, sys
import getpass
import threading
import time

account={'G1':'qwer','G2':'56789','G3':'asdf','G4':'12345','G5':'zxcv'}  # user account
status={'G1':'offline','G2':'offline','G3':'offline','G4':'offline','G5':'offline'}  # user status
G1_list=['G2','G4','G5']
G2_list=['G1','G3','G4']
G3_list=['G2','G4','G5']
G4_list=['G1','G2','G5']
G5_list=['G1','G3','G4']
port_num={}
sock_num={}
off_message={}
file=[]
def isfriend(who,check):  #check user's and the other is friend or not
 result = {
        'G1': G1_list,
        'G2': G2_list,
        'G3': G3_list,
        'G4': G4_list,
        'G5': G5_list,
    }[who]
 if(check in result):
  return True
 else:
  return False
 
def checkstatus(check):    #check user's status
 if(status[check]=="online"):
  return True
 else:
  return False
def add_delfriend(who,someone,sign):  # add/delete friends 
  result = {
        'G1': G1_list,
        'G2': G2_list,
        'G3': G3_list,
        'G4': G4_list,
        'G5': G5_list,
    }[who] 
  if(sign==2.1):
    result.append(someone)
    doublefriend(someone,who,2.1)
    print("user: ")
    print(result)
    return
  elif(sign==2.2):
    result.remove(someone)
    print("user: ")
    print(result)
    doublefriend(someone,who,2.2)
    return
def doublefriend(someone,who,sign):  # add/delete friends on other side 
  result = {
        'G1': G1_list,
        'G2': G2_list,
        'G3': G3_list,
        'G4': G4_list,
        'G5': G5_list,
    }[someone]
  print("other: ")
  if(sign==2.1):
    result.append(who)
    print(result)
    return
  elif(sign==2.2):
    result.remove(who)
    print(result)
    return 
    
def friend(who,sign):
    result = {
        'G1': G1_list,
        'G2': G2_list,
        'G3': G3_list,
        'G4': G4_list,
        'G5': G5_list,
    }[who]
    friend_lists=""   
    for element in result:
     friend_status=status[element]
     friend_lists+=element+" "+friend_status+"\n"
    return friend_lists
  
def sendsock(who):              # user port num
 who_sock=sock_num[who]
 return who_sock

def sendafile(otherconnection,who_send):
    filename=file[0]
    other=sock_num[who_send]
    f =open(filename, 'rb') #open in binary
    mes = f.read(1024)
    while(mes):
     other.send(mes)
     mes = f.read(1024)




def log_out(account):
   status[account]='offline'
   print(account+" is offline")
   sys.exit(0)
   return
def offline_m(account,who,mes):
       
    mes=mes.decode("utf-8")
    if(off_message.get(account)!=None):
     Origin_m="" 
     Origin_m=off_message.get(account)
     off_message[who]=Origin_m+"Message from "+account+": "+mes+"\n"
    else:
     off_message[who]="Message from "+account+": "+mes+"\n"
    print(off_message[who])
    print(account)

def sendcheck(account,myconnection,filename,who):
      check_list=isfriend(account,who)
      if(check_list):
        peo_status=checkstatus(who)
        file.append(filename)
        print(file[0])
        filename=filename.encode('utf-8')
        if(peo_status):              
          who_sock=sendsock(who)  
          a=bytes(account+" wants to send you a file : ","utf-8")
          who_sock.send(a+filename)          
        else:
          myconnection.send(b"User is offline")
      else:
          myconnection.send(b"The person is not in the friendlist")

def tellOthers(account,myconnection,message,who): #send online message to friends      
      check_list=isfriend(account,who)
      if(check_list):
        peo_status=checkstatus(who)
        mes=message.encode('utf-8')
        if(peo_status):              
          who_sock=sendsock(who)
          who_sock.send(mes)
        else:
          myconnection.send(b"User is offline,the message will be saw when logging in")
          offline_m(account,who,mes)
      else:
          myconnection.send(b"The person is not in the friendlist")

def tellones(account,myconnection,message,who):
    if(message=="friend_lists"):
      fri_list=friend(account,1)
      myconnection.send(fri_list.encode("utf-8"))
    elif(message=="add_friend"):
      check_list=isfriend(account,who)
      if(check_list):
        myconnection.send(b"Already in the friendlist")
      else:
        add_delfriend(account,who,2.1)
        addfriend_m=bytes(who+" added into the friend list", 'utf-8')
        myconnection.send(addfriend_m)
    elif(message=="rm_friend"):   #delete the friend
      check_list=isfriend(account,who)
      if(check_list):
        add_delfriend(account,who,2.2)
        deletefriend_m=bytes(who+" removed from the friend list", 'utf-8')
        myconnection.send(deletefriend_m)
      else:
         myconnection.send(b"The person is not in the friendlist")

def subThreadIn(myconnection, connNumber,account):
 while True:  
   message = myconnection.recv(1024).decode("utf-8")

   if(message=="friend_lists"):  
    tellones(account,myconnection,message,"")
   elif(message=="log out"):
    log_out(account)
    myconnection.close()
    break
   elif(message.find("receive")==0 or message.find("denied")==0):
      who_send=""
      message=message.split(",")
      who_sock=sendsock(message[1])
      for key in sock_num.keys():
          if(sock_num[key] == myconnection):
           who_send=key
      reply=message[0]+" from "+who_send
      who_sock.send(reply.encode("utf-8"))
      if(message[0].find("receive")==0):
        print("success")  
        sendafile(who_sock,who_send)
      else:
        del file[0]
        print("remove success")   

   else:
    message=message.split(",")
    if(message[0]=="add_friend"):
      tellones(account,myconnection,message[0],message[1])
    elif(message[0]=="rm_friend"):
      tellones(account,myconnection,message[0],message[1])
    elif(message[0]=="send"):
      tellOthers(account,myconnection,message[2],message[1])
    elif(message[0]=="sendfile"):
      sendcheck(account,myconnection,message[2],message[1])

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(4) #turning the socket into a passively listening socket, 4: # of waiting conn. allowed
    print('Listening at', sock.getsockname())
    sock.settimeout(50)
    while True:
     connection, addr = sock.accept()
     print('Accept a new connection', connection.getpeername(), connection.fileno())
     login_m= connection.recv(1024).decode("utf-8")
     try:
        #connection.settimeout(5)    
        login_m = login_m.split(",")
        if(login_m[0] in account and login_m[1] == account.get(login_m[0])):
            connection.send(b'Login successful!')
            status[login_m[0]]='online'
            port_num[login_m[0]] = connection.getpeername()
            if(off_message.get(login_m[0])!=None):
              off_mes=off_message.get(login_m[0])
              print(off_mes)
              connection.send(off_mes.encode("utf-8"))
              off_message.clear()  
            sock_num[login_m[0]] = connection
            print('User: '+login_m[0]+" is online")
            mythread = threading.Thread(target=subThreadIn, args=(connection, connection.fileno(),login_m[0]))
            mythread.setDaemon(True)
            mythread.start()           
        else:
            connection.send(b'please go out!')
            connection.close()
     except :  
        pass

    sock.close()


def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    def CsendThreadFunc():   
      while True:
            try:
                choose_item = input()
                sock.send(choose_item.encode("utf-8"))
            except ConnectionAbortedError:
                print('Server closed this connection!')
                break
            except ConnectionResetError:
                print('Server is closed!')
                break
      sock.close()

    def CrecvThreadFunc():
        while True:
            try:
                otherword= sock.recv(1024)
                print(len(otherword))
                print("send from:",sock.getpeername())

                if(len(otherword)>100):
                  otherword=otherword.decode("utf-8")
                  i=1
                  f = open('file_'+ str(i)+".txt",'w') #open in binary
                  i=i+1
                  print(otherword)  
                  while(otherword):
                   f.write(otherword)
                   otherword = sock.recv(1024) 
                  f.close()   
                elif(otherword):
                  print(otherword.decode("utf-8"))            
                else:
                    pass
            except ConnectionAbortedError:
                print('Server closed this connection!')
                break

            except ConnectionResetError:
                print('Server is closed!')
                break
        sock.close()

    print('Client has been assigned socket name', sock.getsockname())
    Login_account=input("login account: ")         # user login        
    Login_passwd =getpass.getpass("password: ") #the address and port if connected socket
    Login_account=bytes(Login_account, 'utf-8')
    Login_passwd=bytes(Login_passwd, 'utf-8')
    sock.sendall(Login_account+b','+Login_passwd) #sent account and password  
    th1 = threading.Thread(target=CsendThreadFunc)
    th2 = threading.Thread(target=CrecvThreadFunc)
    threads = [th1, th2]

    for t in threads :
      t.setDaemon(True)
      t.start()
    t.join() 

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