#!/usr/bin/python

import serial
import time
import thermolib as therm
import sys
import database


port = serial.Serial("/dev/ttyAMA0", baudrate=1200, timeout=3.0)


def checkNquit():
    # check if we should quit
    s = database.Setting.select().where(database.Setting.key==database.Setting.CMD_QUIT_THERMOMETER).get()
    if s.value == '1':
        s.value = '0'
        s.save()
        print "Thermometer Exiting"
        sys.exit(0)

def shouldWeWrite():
    # check if we should write data
    s = database.Setting.select().where(database.Setting.key==database.Setting.RECORD_EVENTS).get()
    return s.value == '1'
        
def writeTemp(_t):
    # write to db
    tInstance = database.Event.create(param_3 = _t, event_type = database.Event.TEMPERATURE)
    tInstance.save()



if __name__=="__main__":
    print "Starting thermometer..."
    while True:

        checkNquit()

        cont = False
        rcv = "-99"

        # trying to read
        try:
            rcv = port.read(7).strip()
            cont = True

        except (KeyboardInterrupt, SystemExit):
            print "closing port"
            port.close()
            raise
        except:
	    #raise
            print "reading error"

        # if read successful, try to convert to float
        if cont and shouldWeWrite():
            try:
		print "rec: "+rcv
                temp = float(rcv)
                print temp

                writeTemp(temp)

            except (KeyboardInterrupt, SystemExit):
                print "closing port"
                port.close()
                raise

            except:
                print "convertion error"
        


    port.close()
