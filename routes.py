'''website'''
# import stuff
from flask import Flask, request, render_template
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship 
from sqlalchemy import String, Integer, ForeignKey, select 


app = Flask(__name__)


DATABASE = "database.db"


# initialise db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


# model goes here using Flask-SQLAlchemy
class Item(db.Model):
    __tablename__ = "pigs"
    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(80))
    farm_id : Mapped[int] = mapped_column(ForeignKey("farm_id"))


# routes go here 
@app.route('/')
def home():
    return render_template("home.html", title="home")


@app.route('/2')
def two():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pigs"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return render_template("two.html", title="two", results=results)

@app.route('/alchemy')
def alchemy():
    pigs = db.session.execute(select(Item)).scalars()
    return render_template('alchemy.html', pigs=pigs)


if __name__ == "__main__":
    app.run(debug=True)