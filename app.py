import logging
import os
import sys

from flask import (
    Flask,
    jsonify,
    render_template,
    request
)
from logger import log
from db import DB




logging.basicConfig(filename="LOG_ansible.log",
                    filemode="a",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    datefmt='[%Y-%m-%d %H:%M:%S]')




app = Flask(__name__)


    # "GET /" pour renvoyer le template de bienvenue

    # "GET /inc" qui incrément l'id dans la bdd

    # "GET /id" qui renvoie l'id en cours




@app.route("/")
@log
def index():
    return render_template('index.html')

#------------- init flask .py------------
@log
@app.route('/id', methods=['GET', 'POST'])
@app.route('/id/<name>', methods=['GET', 'POST'])
def id(name='undefine'):
    r = request.form
    user = r['user']
    if not user:
        return render_template('id.html', name=name) 
    else:
        return render_template('id.html', name=user) 

@log
@app.route('/json', methods=['GET', 'POST'])
def results():
    resp = jsonify(DB.get_users())
    return resp

@app.route("/inc")
@log
def inc():
    DB.insert_user(name)



@log
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@log
@app.errorhandler(500)
def special_exception_handler(error):
    return 'Database connection failed', 500

@log
@app.route('/hello/<name>')
def hello(name):
    return 'Hello {} !'.format(name.capitalize())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['FLASK_RUN_PORT'], debug=True)