from flask import Flask, redirect, render_template, request

from flask_sqlalchemy import SQLAlchemy

# Configure application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///client.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    mail = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Client %r>' % self.id

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        name = request.form["name"]

        phone = request.form["phone"]

        mail = request.form["mail"]

        client = Client(name=name, phone=phone, mail=mail)

        try:
            db.session.add(client)
            db.session.commit()
            return render_template("index.html")
        except:
            return "При подачі заявки сталася помилка"

    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)