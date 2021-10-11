from flask import render_template, request, redirect
from dojos_app import app
from dojos_app.models.dojo import Dojo

#Index page
@app.route("/")
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos)

#Generate dojo
@app.route("/AddDojo", methods=["POST"])
def addDojo():
    data = {
        "name": request.form["name"],
    }
    result= Dojo.add_dojo(data)
    return redirect('/')

#Show dojo
@app.route("/show", methods=['POST'])
def defineValues():
    id = request.form ['id']
    dojo_detail=Dojo.Display_Dojo(id)
    result = Dojo.Display_Data(id)
    return render_template("dojo_show.html", spec_data = result, onedojo=dojo_detail)  