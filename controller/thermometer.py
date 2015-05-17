#!/usr/bin/python
import time
import thermolib as therm
import sys


import database



db = database.getDatabase()


therm.init_thermo()

buffer_length = 15
buf = [therm.read_temperature()] * buffer_length

i = 0
k = 0

clean_every = 1000


write_every_seconds = 1.0





while True:
    i+=1
    i%=buffer_length

    k+=1
    k%=clean_every


    buf[i] = therm.read_temperature()

    time.sleep(write_every_seconds / buffer_length)

    # check if we should write data
    s = database.Setting.select().where(database.Setting.key==database.Setting.RECORD_EVENTS).get()
    if s.value != '1':
        continue

    # check if we should quit
    s = database.Setting.select().where(database.Setting.key==database.Setting.CMD_QUIT_THERMOMETER).get()
    if s.value == '1':
        s.value = '0'
        s.save()
        print "Thermometer Exiting"
        sys.exit(0)

    if i == 0:
        t = 0.0

        for j in range(0, buffer_length):
            t+=buf[j]

        t = t / buffer_length

        # write to db
        tInstance = database.Event.create(param_3 = t, event_type = database.Event.TEMPERATURE)
        tInstance.save()
        print t
