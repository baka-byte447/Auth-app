from flask import Flask, redirect, render_template, request, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///credentials.db"
db = SQLAlchemy(app)
app.secret_key = 'secret_key'

# CREATE USER TABLE
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))


with app.app_context():
    db.create_all()

@app.route('/')
def home():

    return render_template("index.html")


@app.route("/register", methods=['GET','POST'])
def register():
    
    errors = {}

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if not name or name.strip() == "":
            errors['name'] = "Name is Required"

        if not email or email.strip() == "":
            errors['email'] = "Email is Required"

        if not password:
            errors['password'] = "Password should not be Empty"
        elif len(password) < 6:
            errors['password'] = "Password should be at least 6 characters"

        if not errors:
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                errors['email'] = "This Email has already been used"

        if errors:
            return render_template("register.html", errors=errors, name=name, email=email)

        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')
    
    return render_template("register.html", errors={})


@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/dashboard')
        else:
            return render_template('login.html',error='Invalid Password')
        
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
        return render_template("dashboard.html", user=user.name)
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login') 





if __name__ == "__main__":
    app.run(debug=True)