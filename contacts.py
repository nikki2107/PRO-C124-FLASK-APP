from flask import Flask,request,jsonify
app=Flask(__name__)

List = [
    {
     'id' : 1,
     'Name' : u'Raju',
     'Contact': u'9567487925',
     'done' : False
    },
    {
      'id' : 2,
      'Name' : u'Shreya',
      'Contact' : u'9768765234',
      'done' : False
    },
] 

@app.route("/add-data",methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide data"
        },
        400)
        
    contact = {
        'id': List[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact',""),
        'done': False
        }
    
    List.append(contact)
    return jsonify({
        "status": "success",
        "message": "Contact added successfully"
    })
        

@app.route("/get-data")
def get_contact():
    return jsonify({
        'data' : List
    })

if (__name__=='__main__'):
    app.run(debug=True)

