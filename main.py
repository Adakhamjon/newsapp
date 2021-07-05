
from config import app
from client_views import*
from admin_views import*



@app.context_processor
def inject_category():
	categories = Category.query.all()
	return dict(tiplar = categories)






if __name__ == "__main__":
	app.run(debug = True)