from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "sadfsahfkjsadh fkjhaskfjh sdfhjsadfhsj"
@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    session["Strawberry"] = request.form.get('strawberry')
    session["Raspberry"] = request.form.get('raspberry')
    session["Apple"] = request.form.get('apple')
    session["first_name"] = request.form.get('first_name')
    session["last_name"] = request.form.get('last_name')
    session["sid"] = request.form.get('student_id')
    print("Charging {0} {1} for {2} fruits".format(session["first_name"],session["last_name"], int(session["Strawberry"])+int(session["Raspberry"])+int(session["Apple"])))
    
    
    return redirect('/fruits')

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html", fruits = session)

if __name__=="__main__":   
    app.run(debug=True)    