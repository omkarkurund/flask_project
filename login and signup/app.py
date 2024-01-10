from flask import Flask,render_template,request,flash,redirect,session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    email=db.Column(db.String,primary_key=True)
    passw=db.Column(db.String,nullable=False)
    mob=db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f'email:-{self.email} - mobile_number:-{self.mob}'




@app.route('/')
def Home():
    return render_template("home.html")

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method =="POST":
        uemail =request.form["email"]
        upass= request.form["pass"]
        user = User.query.filter_by(email=uemail,passw=upass).first()
        # print(dir(user))
        if(user.email==uemail and user.passw== upass):
            
            # print("Login Successfully")
            # db.session=True
            # session['logged_in'] = True
            flash(f'{user.email}')
            return redirect('/')
        
    return render_template("login.html")

@app.route('/signup',methods=["GET","POST"])
def signup():

    if request.method =="POST":
        email = request.form["email"]
        passw=request.form["pass"]
        mob=request.form["mob"]
        user = User(email=email,passw=passw,mob=mob)
        db.session.add(user)
        db.session.commit()
    return render_template("signup.html")



if __name__=="__main__":
    app.secret_key='super secret key'
    app.config['SESSION_TYPE']= 'filesystem'
    app.run(debug=True,port=8000)