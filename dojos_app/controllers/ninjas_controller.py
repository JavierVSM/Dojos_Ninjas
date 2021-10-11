from flask import render_template, request, redirect
from dojos_app import app
from dojos_app.models.ninja import Ninja 
from dojos_app.models.dojo import Dojo


#Add ninja (1/2) - Display form
@app.route("/addNinja", methods=["POST"])
def displayForm():
    dojos = Dojo.get_all()
    return render_template("ninja.html",all_dojos = dojos)

#New post (2/2) - Add Ninja associated with Dojo
@app.route("/new_ninja", methods=["POST"])
def addninja():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id":request.form["dojo_id"]
    }
    result= Ninja.addninja(data)
    return redirect('/')

#TEST show data
@app.route("/showDojo", methods=["POST"])
def testShow():
    dojo_id = request.form ['id']
    results = Ninja.ninjas_n_dojos( dojo_id )
    return render_template("dojo_show.html", dojos = results) 