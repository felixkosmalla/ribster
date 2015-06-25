import serial

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=10.0)



#while True:
#    rcv = port.read(7).strip()
#    print rcv


while True:
    #port.write("\r\nSay something:")
    cont = False
    rcv = "-99"
    try:
        print "waiting..."
        rcv = port.read(6).strip()
        #print rcv
        cont = True
    except (KeyboardInterrupt, SystemExit):
        print "closing port"
        port.close()
        raise
    except:
        print "reading error"

    if cont:
        print rcv
        

port.close()
