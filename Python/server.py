from nrf24 import NRF24
import time
from time import gmtime, strftime

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
radio.openWritingPipe(pipes[0])
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
    if ( recv_buffer[0] == 1 ):
      #0xABCDABCD71LL
      radio.stopListening()
      radio.openWritingPipe(pipes[0])
      radio.write("6")
      print "Got 0xABCDABCD71LL"

    if ( recv_buffer[0] == 2 ):
      #0xABCDABCD61LL
      radio.stopListening()
      radio.openWritingPipe(pipes[1])
      radio.write("7")
      print "Got 0xABCDABCD61LL"


    if ( recv_buffer[0] == 3 ):
      #0xABCDABCD51LL
      radio.stopListening()
      radio.openWritingPipe(pipes[2])
      radio.write("8")
      print "Got 0xABCDABCD51LL"

    if ( recv_buffer[0] == 4 ):
      #0xABCDABCD41LL
      radio.stopListening()
      radio.openWritingPipe(pipes[3])
      radio.write("9")
      print "Got 0xABCDABCD41LL"

    time.sleep(0.1)



#1 = 49, 2 = 50, 3 = 51, 4 = 52
# A = 65


#    pipe = [0]
#    while not radio.available(pipe, True):
#        time.sleep(1000/1000000.0)
#    recv_buffer = []
#    radio.read(recv_buffer)
#    print recv_buffer
