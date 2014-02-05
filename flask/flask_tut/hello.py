from flask import Flask
app = Flask(__name__)

@app.route('/<user>')
def hello_world(user):
    user = user[0:1]
    return "%s" % user

if __name__ == '__main__':
    app.run()