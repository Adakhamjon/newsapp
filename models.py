from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import app
db = SQLAlchemy(app)


class Category(db.Model):
	id = db.Column("ID",db.Integer,primary_key=True,unique = True)
	name = db.Column("Kategoriya",db.String(255),nullable = False,default ="Noma'lum kategoriya")



class News(db.Model):
	id = db.Column("ID",db.Integer,primary_key = True,unique = True)
	title = db.Column("Sarlavha",db.String(255), nullable = False,default = "No'malum sarlavha")
	content = db.Column("Mazmun",db.Text, nullable = False, default = "")
	date_added = db.Column("Sana",db.DateTime,default = datetime.now)
	views = db.Column("Ko'rishlar soni",db.Integer,default = 0)
	is_published=db.Column( "Chop etish",db.Boolean)
	photo = db.Column("Muqova rasmi",db.String(255))

	category = db.Column(db.Integer,db.ForeignKey("category.ID"))

db.create_all()

	