from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static',filename)

if __name__ == '__main__':
    app.run()