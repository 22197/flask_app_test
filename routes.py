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

 
@app.route('/')
def home():
    return render_template("home.html", title="home")


# model goes here using Flask-SQLAlchemy
# farm
'''class Type(Base):
    __tablename__ = "farm"
    farm_id : Mapped[int] = mapped_column(primary_key=True)
    farm_name: Mapped[str] = mapped_column(String(80))
    farms : Mapped[list["Item"]] = relationship(back_populates="type")'''


# Pigs
'''class Item(Base):
    __tablename__ = "pigs"
    pig_id : Mapped[int] = mapped_column(primary_key=True)
    pig_name : Mapped[str] = mapped_column(String(80))
    farm_id : Mapped[int] = mapped_column(ForeignKey("farm.farm_id"))
    type : Mapped[Type] = relationship(back_populates="farms")'''


class Type(db.Model):
    __tablename__ = 'farm'
    farm_id = db.Column(db.Integer, primary_key=True)
    farm_name = db.Column(db.String(80))
    farms = db.relationship('Item', back_populates='type')

class Item(db.Model):
    __tablename__ = 'pigs'
    pig_id = db.Column(db.Integer, primary_key=True)
    pig_name = db.Column(db.String(80))
    farm_id = db.Column(db.Integer, db.ForeignKey('farm.farm_id'))
    type = db.relationship('Type', back_populates='farms')


@app.route('/alchemy')
def alchemy():
    '''pigs = db.session.execute(select(Item)).scalars()'''
    pigs = Item.query.all()
    return render_template('alchemy.html', pigs=pigs)


if __name__ == "__main__":
    app.run(debug=True)