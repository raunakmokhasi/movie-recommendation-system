#Raunak Mokhasi			IIIT Delhi

from flask import Flask, request, send_from_directory, render_template, session
import pymongo
import json
import userFiltering
import itemFiltering

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/static')
app.secret_key = 'hellothere'

@app.route('/rate', methods=['POST'])
def rate():
	if request.method == "POST":
		rating = request.values.get('rating')
		movie = request.values.get('movie')

		print(rating, movie)

	return render_template('./login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		client = pymongo.MongoClient("mongodb+srv://user:useruser@precog-j9rdb.mongodb.net/test?retryWrites=true")

		username = request.values.get('username')
		password = request.values.get('password')

		if (username == "precog" and password == "pass"):
		# if (username == "lmao" and password == "lmao") or session['logged_in'] == "true":
			# session['logged_in'] = "true"
			client = pymongo.MongoClient("mongodb+srv://user:useruser@precog-j9rdb.mongodb.net/test?retryWrites=true")
			db = client.movie_db
			collection = db.movie_col

			cursor = collection.find({})

			data = []

			for document in cursor:
				data.append(document)
			return render_template("./movies_list.html", data=data)


	return render_template('./login.html')

@app.route('/index.html', methods=['GET', 'POST'])
def index():
	client = pymongo.MongoClient("mongodb+srv://user:useruser@precog-j9rdb.mongodb.net/test?retryWrites=true")
	db = client.movie_db
	collection = db.movie_col

	cursor = collection.find({})

	data = []

	counter = 0

	for document in cursor:
		data.append(document)
		counter += 1
		if(counter > 4):	#5 Movies - Will change it to any random 5 movies later
			break

	return render_template('./index.html',data = data)

@app.route('/submit.html', methods=['GET', 'POST'])
def submit():
	ratings_submitted = []
	ratings_submitted.append(request.form['rating1'])
	ratings_submitted.append(request.form['rating2'])
	ratings_submitted.append(request.form['rating3'])
	ratings_submitted.append(request.form['rating4'])
	ratings_submitted.append(request.form['rating5'])
	# ratings_submitted.append(request.form['rating6'])
	# ratings_submitted.append(request.form['rating7'])
	# ratings_submitted.append(request.form['rating8'])
	# ratings_submitted.append(request.form['rating9'])
	# ratings_submitted.append(request.form['rating10'])
	userFilterData = userFiltering.userFilter(ratings_submitted)
	print()
	print()
	print("UserData = ", userFilterData)
	itemFilterData = itemFiltering.itemFilter(ratings_submitted)
	print()
	print()
	print("ItemData = ", itemFilterData)
	print()
	print()

	client = pymongo.MongoClient("mongodb+srv://user:useruser@precog-j9rdb.mongodb.net/test?retryWrites=true")
	db = client.movie_db
	collection = db.movie_col

	movieItemFilter = []
	for ind in itemFilterData:
		movieItemFilter.append(collection.find()[int(ind)])

	movieUserFilter = []

	for ind in userFilterData:
		movieUserFilter.append(collection.find()[int(ind)])

	# print(movieUserFilter)
	# print(movieItemFilter)

	return render_template('./submit.html',data = movieUserFilter, data2 = movieItemFilter)



if __name__ == "__main__":
	app.run(debug=True)