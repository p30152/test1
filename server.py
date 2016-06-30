import socket
import math
import pyaudio

Hz={'1':'262','2':'294','3':'330','4':'349','5':'392','6':'440','7':'494','z':'88','x':'100'}

PyAudio = pyaudio.PyAudio

def playTone(rate,wave,time,channel):
  data = ''.join([chr(int(math.sin(x/((rate/wave)/math.pi))*127+128)) for x in range(rate)])
  p = PyAudio()

  stream = p.open(format =
    p.get_format_from_width(1),
    channels = channel,
    rate = rate,
    output = True)
  for DISCARD in range(int(time)):
      stream.write(data)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 8888)
print ('starting up on %s port %s' %server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
print ('waiting for a connection...')

while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    try:
        print ('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            if data:

                get = data.decode('ascii')
                lv = int(get.split(":")[0])
                note = get.split(":")[1]

                playTone(44000, int(Hz[note])*lv, 1,1)

                break
            else:
                print ('no more data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
