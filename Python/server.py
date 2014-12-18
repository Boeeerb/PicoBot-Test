from nrf24 import NRF24
import time
from time import gmtime, strftime
import re

#pipes = [[0xf0, 0xf0, 0xf0, 0xf0, 0xd2],[0xf0, 0xf0, 0xF0, 0xF0, 0xf0]]
pipes = [[0xab, 0xcd, 0xab, 0xcd, 0x71],[0xab, 0xcd, 0xab, 0xcd, 0x61],[0xab, 0xcd, 0xab, 0xcd, 0x51],[0xab, 0xcd, 0xab, 0xcd, 0x41]]
serverpipe = [0xE8, 0xE8, 0xF0, 0xF0, 0xE1]

radio = NRF24()
radio.begin(0, 0,25,18) #set gpio 25 as CE pin
radio.setRetries(15,15)
radio.setPayloadSize(32)
radio.setChannel(0x4c)
radio.setDataRate(NRF24.BR_250KBPS)
radio.setPALevel(NRF24.PA_MAX)
radio.setAutoAck(1)
#radio.openWritingPipe(pipes[0])
radio.openReadingPipe(1,serverpipe)

radio.startListening()
radio.stopListening()

radio.printDetails()
radio.startListening()

colours = ["6","7","8","9"]
colcount = 0

while True:
    radio.startListening()
    recv_buffer = []
    radio.read(recv_buffer)
    out = ''.join(chr(i) for i in recv_buffer)
    cmd = out.strip().split()
    if cmd[0] == "NEW":

      print "New device: "+cmd[1]

#      blah = re.findall(r'.{1,2}',cmd[1],re.DOTALL)
#      print blah[1]

      pipe = cmd[1][2:12]  # Strip 0x and LL from address and reply with chr 6
      
      pipe = map(ord, pipe.decode('hex'))


#      packet=[ for p in packet]

#      packet=[str(p).decode("hex") for p in packet]
#      packet=[int(p,16) for p in packet]
#      print packet
#      blah2= []*5
#      pipes[0] = packet

      print pipe
      radio.stopListening()
      radio.openWritingPipe(pipe)

#      buffer = ['H','E','L','L','O']
#      radio.write(buffer)
      radio.write("6")


      pipe = [0x55, 0x1c, 0x24, 0x46, 0x38]
      radio.openWritingPipe(pipe)
      radio.write("6")
#551c244638

    time.sleep(0.1)



#1 = 49, 2 = 50, 3 = 51, 4 = 52
# A = 65


#    pipe = [0]
#    while not radio.available(pipe, True):
#        time.sleep(1000/1000000.0)
#    recv_buffer = []
#    radio.read(recv_buffer)
#    print recv_buffer
