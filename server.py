from flask_app import app

#Importación de controladores
from flask_app.controllers import admins_controller

if __name__=="__main__":
    app.run(debug=True)