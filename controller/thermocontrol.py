import database as dbs



db = dbs.getDatabase()


def on():
    s = dbs.Setting.select().where(dbs.Setting.key==dbs.Setting.RECORD_EVENTS).get()
    s.value = "1"
    return s.save()

def off():
    s = dbs.Setting.select().where(dbs.Setting.key==dbs.Setting.RECORD_EVENTS).get()
    s.value = "0"
    return s.save()

def pid_on():
    s = dbs.Setting.select().where(dbs.Setting.key==dbs.Setting.PID_RUNNING).get()
    s.value = "1"
    return s.save()

def pid_off():
    s = dbs.Setting.select().where(dbs.Setting.key==dbs.Setting.PID_RUNNING).get()
    s.value = "0"
    return s.save()

def setpoint(temperature = False):
    s = dbs.Setting.select().where(dbs.Setting.key==dbs.Setting.TARGET_TEMPERATURE).get()

    if not temperature == False:
        s.value = str(temperature)

    s.save()
    return s.value
