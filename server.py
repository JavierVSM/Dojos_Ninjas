from flask import Flask
from dojos_app import app
from dojos_app.controllers import ninjas_controller, dojos_controller

if __name__ == "__main__":
    app.run(debug=True)