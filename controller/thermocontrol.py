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

