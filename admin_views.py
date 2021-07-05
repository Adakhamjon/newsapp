from flask import request,render_template,url_for,redirect
import os
from uuid import uuid4
from config import app
from models import News,Category,db


@app.route("/admin/news/")
def news_list_view():
	if ("action" and "_id") in request.args:
		try:
			_id =int( request.args.get("_id"))
		except :
			return redirect(url_for('news_list_view'))
		if request.args.get("action")=="make_active":
			chosen_new = News.query.filter_by(id=_id).first_or_404()
			chosen_new.is_published=True
			db.session.commit()

		elif request.args.get("action")=="make_inactive":
			chosen_new = News.query.filter_by(id=_id).first_or_404()
			chosen_new.is_published=False
			db.session.commit()

		elif request.args.get("action")=="delete":
			chosen_new = News.query.filter_by(id=_id).first_or_404()
			db.session.delete(chosen_new)
			db.session.commit()


		return redirect(url_for('news_list_view'))
		
	all_news = News.query.order_by(News.id.desc()).all()
	return render_template("admin/news_list.html",yangiliklar=all_news)

@app.route("/categories/")
def categories_view():
	if ("action" and "_id") in request.args:
		try:
			_id =int( request.args.get("_id"))
		except :
			return redirect(url_for('categories_view'))

	if request.args.get("action")=="delete":
			chosen_cat = Category.query.filter_by(id=_id).first_or_404()
			db.session.delete(chosen_cat)
			db.session.commit()
	return render_template("admin/category_list.html")


@app.route("/new_category/",methods=["POST","GET"])
def new_category_view():
	name = request.form.get("category_name", None)

	if name:
		c = Category(name=name)
		db.session.add(c)
		db.session.commit()
	return render_template("add_category.html")


@app.route("/admin/news/create/",methods = ["GET","POST"])
def add_news_view():
	if request.method =="POST":
		n = News()
		n.title  = request.form.get("news_title","")
		n.content  = request.form.get("news_content","")
		n.is_published  = bool(request.form.get("publish_status","False"))
		cat_id = int(request.form.get("news_category",0))
		if cat_id:
			n.category=cat_id


		photo  = request.files.get("news_photo","")
		if photo:
			photo_name = (str(uuid4())+photo.filename.split(".")[-1])
			photo.save(os.path.join("static","uploads","images",photo_name))
			n.photo=filename

		db.session.add(n)
		db.session.commit()
	return render_template("add_news.html")

@app.route("/admin/news/<int:_id>",methods=["GET","POST"])
def update_news_view(_id):
	news = News.query.filter_by(id=_id).first_or_404()
	if request.method =="POST":
		news.title  = request.form.get("news_title","")
		news.content  = request.form.get("news_content","")
		news.is_published  = bool(request.form.get("publish_status","False"))
		cat_id = int(request.form.get("news_category",0))
		if cat_id:
			news.category=cat_id
		else:
			return redirect(url_for('update_news_view'))


		photo  = request.files.get("news_photo","")
		if photo:
			photo_name = (str(uuid4())+photo.filename.split(".")[-1])
			photo.save(os.path.join("static","uploads","images",photo_name))
			news.photo=filename
		db.session.commit()
		return redirect(url_for('update_news_view',_id=_id))

	if request.args.get("action",None) == "delete-thumb":
		try:
			os.unlink(os.path.join("static","uploads","images", news.photo))
		except:
			pass

		news.photo = ""
		db.session.commit()
		return redirect(url_for('update_news_view',_id=_id))
	

	return render_template("admin/update_news.html", yangilik = news)

