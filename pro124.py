from _typeshed import ReadableBuffer
from flask import Flask,jsonify,request

app =  Flask(__name__)

# to create an array of task 

task = [
    {
        "id":1,
        "contact":u"845654546465",
        "name":u"Raju",
        "done":False,
    
    },
    {
        "id":2,
        "contact":u"45645474564",
        "name":u"Rahul",
        "done":False,
    },
     {
        "id":3,
        "contact":u"6545456545",
        "name":u"john ",
        "done":False,
    },
]

@app.route("/add-task",methods=["POST"])

def addtask() :
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"provide the data",
        },400)
    inputtask =  {
        "id":task[-1]["id"]+1,
        "contact":request.json["contact"],
        "name":request.json.get("name",""),
        "done":False,
  
    },   
    task.append(inputtask)
    return jsonify({
            "status":"success",
            "message":"task added successfuly",
        },400)
    
    
@app.route("/get-data")

def gettask() :
    return jsonify ({
        "data":task,
        
    })
    

   
if __name__ == "__main__":
    app.run(debug=True)