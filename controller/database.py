from peewee import *
import datetime


db = SqliteDatabase('ribster.db')





class Event(Model):

    event_type = IntegerField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    param_1 = CharField(null=True)
    param_2 = CharField(null=True)
    param_3 = FloatField(null=True)

    TEMPERATURE = 1
    HEATING = 2


    class Meta:
        database = db




class Setting(Model):
    key = CharField(index=True, primary_key = True)
    value = CharField()

    # Settings
    RECORD_EVENTS = "record_events"
    PID_RUNNING = "pid_running"
    TARGET_TEMPERATURE = "target_temperature"

    # Commands
    CMD_QUIT_THERMOMETER = "quit_thermometer"


    class Meta:
        database = db


default_settings = [
        (Setting.RECORD_EVENTS, "0"),
        (Setting.PID_RUNNING, "0"),
        (Setting.TARGET_TEMPERATURE, "0"),
        (Setting.CMD_QUIT_THERMOMETER, "0"),
    ]


def getDatabase():

    global db
    

    db.connect()

    created = False

    try:
        db.create_tables([Event,Setting,])
        print "Tables created"
        print "Creating Default entries"
        created = True

    except:
        print "Tables already created"

    if created == True:
        # settings
        for d in default_settings:
            (k,v) = d
            s = Setting.create(key= k, value= v)
            s.save()
        


    return db