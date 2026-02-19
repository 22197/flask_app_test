'''website'''
# import stuff
from flask import Flask, request, render_template
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship 
from sqlalchemy import String, Integer, ForeignKey, select 


app = Flask(__name__)


# initialise db
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Base(DeclarativeBase):
    pass


# model goes here using Flask-SQLAlchemy
class Item(Base):
    __tablename__ = "pigs"
    pig_id : Mapped[int] = mapped_column(primary_key=True)
    pig_name : Mapped[str] = mapped_column(String(80))
    farm_id : Mapped[int] = mapped_column(ForeignKey("farm_id"))


# routes go here 
@app.route('/')
def home():
    return render_template("home.html", title="home")


@app.route('/alchemy')
def alchemy():
    pigs = db.session.execute(select(Item)).scalars()
    return render_template('alchemy.html', pigs=pigs)


if __name__ == "__main__":
    app.run(debug=True)