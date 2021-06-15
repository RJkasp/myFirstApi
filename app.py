from flask import Flask, request, Response
import json

from werkzeug.wrappers import response
app=Flask(__name__)

animals = ["deer", "moose", "caribou", "elk", "bear"]
jsonStr = json.dumps(animals)
@app.get("/")
def get_animals():
   return "<p>"+jsonStr+"</p>"
    # return "<form action='/' method='POST'><input type='text' name='animals'><input type='submit' value='add'></form>"

@app.post("/")
def add_animal():
   animals.append("snake")
   return Response(json.dumps(animals), mimetype='application/json', status=200)

@app.patch("/")
def edit_animal():
   animals[0]="whitetail deer"
   return Response("successful edit")

@app.delete("/")
def delete_animal():
   animals.pop(3)
   return "successfull delete"

app.run(debug=True)

