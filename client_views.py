from flask import request,render_template 
from config import app
from models import News,Category
from utils import highlight_words
@app.route("/<int:_id>/")
def single_new_view(_id):
	single_news = News.query.filter_by(id = _id).first_or_404()
	categories = Category.query.all()
	return render_template("single_news.html",yakka_yangilik = single_news)
@app.route("/")
def all_news_view():
	cat_id = request.args.get("category",None)
	term = request.args.get("search-term",None)
	if cat_id:
		all_news = News.query.filter_by(category = cat_id).all()
	else:
		all_news = News.query.all()
	categories = Category.query.all()

	# if term:
	# 	all_news = News.query.filter(News.title.contains(term.strip())|News.content.contains(term.strip()))

	# 	temp = []
	# 	for single_new in all_news:
	# 		single_new.title = highlight_words(single_new.title,term,"<span style='color:black;font-weight:bold;background-color:yellow;'>","</span>")
	# 		single_new.content = highlight_words(single_new.content,term,"<span style='color:black;font-weight:bold;background-color:yellow;'>","</span>")
	# 		temp.append(single_new)
	# 	all_news=temp
	# else:
	# 	all_news = News.query.all()

	return render_template("client/all_news.html",barcha_yangiliklar = all_news,tiplar=categories,qidirilayotgan_soz=term)

