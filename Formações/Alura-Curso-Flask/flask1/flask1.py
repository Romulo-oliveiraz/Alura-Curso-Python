
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# CLASS GAME 
####################################################################################################

app = Flask(__name__)
app.config.from_pyfile('config.py')
    
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from rotas import *

#inicia o app
#É possivel definir um host e uma porta na hora de iniciar
#ex: app.run(host='0.0.0.0', port=8080)
if __name__ == '__main__':
    app.run(debug=True)