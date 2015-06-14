#!/usr/bin/python
import database as dbs
import switch, thermocontrol, sys

db = dbs.getDatabase()

def help():
    print "h1  - Turn heating on"
    print "h0  - Turn heating off"
    print "t1  - Turn thermometer writing on"
    print "t0  - Turn thermometer writing off"
    print "p1  - Turn PID Controller on"
    print "p0  - Turn PID Controller off"
    print "s   - setpoint"
    print "cdb - clear database"
    print "g   - get current temperature"
    print "x   - quit" 
    print "?   - print this"
    


help()

while True:
    i = raw_input("command: ")

    if (i == "h1"):
        switch.on()
        print "switched heating on"
        continue

    if (i == "h0"):
        switch.off()
        print "switchted heating off"
        continue

    if (i == "t1"):
        thermocontrol.on()
        print "recording switched on"
        continue
        
    if (i == "t0"):
        thermocontrol.off()
        print "recording switched off"
        continue

    
    if (i == "p1"):
        thermocontrol.pid_on()
        print "PID switched on"
        continue
        
    if (i == "p0"):
        thermocontrol.pid_off()
        print "PID switched off"
        continue


    if (i == "s"):
        print "new temperature, leaf blank for get"
        setpoint = raw_input("temperature: ")

        if setpoint == "":
            print "temp:"
            print thermocontrol.setpoint(False)
        else:
            print "new temp:"
            print thermocontrol.setpoint(setpoint)
            


    if (i == "?"):
        help()
        continue

    if (i == "x"):
        sys.exit(0)
        continue

    if (i == "cdb"):
        q = dbs.Event.delete()
        print "deleted: " + str(q.execute())
        continue

    if (i == "g"):
        reading = dbs.Event.select().where(dbs.Event.event_type == dbs.Event.TEMPERATURE).order_by(dbs.Event.timestamp.desc()).limit(1)[0]
        print str(reading.param_3)
        continue


