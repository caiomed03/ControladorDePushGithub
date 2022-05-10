from flask import Flask, render_template, request
from pytz import HOUR
from connector import Connector
from own_email import Email
from visualization import show
import datetime


app = Flask(__name__)

@app.route('/payload/', methods=['POST'])
def payload():
    data = request.get_json()
    usu = data['pusher']['name']
    Connector.update(usu=usu)
    Email.send_email(usu)
    return data

@app.route('/grafico', methods=['GET'])
def graf():
    now = datetime.datetime.now()
    now = str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)
    if (show(now) !=None):
        return render_template('imagen.html', image='static/images/'+now+'.jpg')
    else:
        return 'No hay datos'


app.run(debug=True, port=2250)
