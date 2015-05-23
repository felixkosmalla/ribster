import serial

port = serial.Serial("/dev/ttyAMA0", baudrate=1200, timeout=3.0)



#while True:
#    rcv = port.read(7).strip()
#    print rcv


while True:
    #port.write("\r\nSay something:")
    cont = False
    rcv = "-99"
    try:
	#print "waiting..."
        rcv = port.read(7).strip()
	#print rcv
        cont = True
    except (KeyboardInterrupt, SystemExit):
	print "closing port"
        port.close()
        raise
    except:
        print "reading error"

    if cont:
        try:
            temp = float(rcv)
            print temp
        except (KeyboardInterrupt, SystemExit):
	    print "closing port"
            port.close()
            raise

        except:
            #raise
            print "convertion error"
    #port.write("\r\nYou sent:" + repr(rcv))

port.close()
