from flask import *
from database import *
import json
import time, datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    #return "test"
    return render_template('index.html')


@app.route('/plot')
def plot():
    temps = Event.select().where(Event.event_type==Event.PID_TEMPERATURE).order_by(Event.timestamp.asc())

    temp_objs = {
        'key':'Temperature',
        'values': []
    }

    h_objs = {
        'key':'Heating',
        'values': []    
    }

    for t in temps:
        ts = datetime.datetime(year = t.timestamp.year, month=t.timestamp.month, day=t.timestamp.day, hour=t.timestamp.hour, minute=t.timestamp.minute, second=t.timestamp.second)
        timestamp = int(time.mktime(ts.timetuple()))
        temperature = t.param_3

        temp_objs['values'].append([timestamp*1000, temperature])

    heats = Event.select().where(Event.event_type==Event.PID_HEATING).order_by(Event.timestamp.asc())        

    for t in heats:
        ts = datetime.datetime(year = t.timestamp.year, month=t.timestamp.month, day=t.timestamp.day, hour=t.timestamp.hour, minute=t.timestamp.minute, second=t.timestamp.second)
        timestamp = int(time.mktime(ts.timetuple()))

        state = int(t.param_3)

        h_objs['values'].append([timestamp*1000, state])






    return json.dumps([temp_objs, h_objs])

    return "test"
    pass



@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static',filename)

if __name__ == '__main__':
    app.run(debug=True)