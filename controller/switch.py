#!/usr/bin/python

import sys, time
from subprocess import call
import database as dbs

OUTLET = 3

db = dbs.getDatabase()

call(["sudo", "gpio", "mode", "0", "out"])



def on():
    global OUTLET, db
    e = dbs.Event.create(event_type=dbs.Event.MANUAL_HEATING, param_1 = "1")
    e.save()

    s = dbs.Setting.select().where(dbs.Setting.key==dbs.Setting.HEATING_ON).get()
    s.value = "1"
    s.save()


    call(["sudo", "gpio", "write", "0", "0"])

def off():
    global OUTLET, db
    e = dbs.Event.create(event_type=dbs.Event.MANUAL_HEATING, param_1 = "0")
    e.save()

    s = dbs.Setting.select().where(dbs.Setting.key==dbs.Setting.HEATING_ON).get()
    s.value = "0"
    s.save()


    call(["sudo", "gpio", "write", "0", "1"])


s = dbs.Setting.select().where(dbs.Setting.key==dbs.Setting.HEATING_ON).get()


if s.value == "1":
    on()
else:
    off()
