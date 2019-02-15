#Raunak Mokhasi			IIIT Delhi

import pymongo
import csv
from bs4 import BeautifulSoup
import requests
import json

client = pymongo.MongoClient("mongodb+srv://user:useruser@precog-j9rdb.mongodb.net/test?retryWrites=true")
db = client.movie_db
collection = db.movie_col

#The CSV is sorted randomly, orelse all the movies would've been 1995-1997 (done through MS Excel)

with open('links.csv',newline='') as linksFile:
	reader = csv.DictReader(linksFile)
	count = 0
	for row in reader:
		imdb_id = row['imdbId']
		domain = "https://www.imdb.com/title/tt0" + str(imdb_id) + "/"
		res = requests.get(domain)
		soup = BeautifulSoup(res.text,'lxml')
		movieTitle = None
		movieRating = None
		movieYear = None
		movieSynopsis = None
		imageURL = None
		movieFound  = False
		
		try:
			imageURL = soup.find('div', class_= 'poster').a.img['src']
			movieSynopsis = soup.find('div',class_= 'summary_text').contents[0].strip()
			movieTitle = soup.find('h1').contents[0].strip()
			movieYear = soup.find('h1').find('span').find('a').contents[0]
			for span in soup.findAll('span'):
				if span.has_attr('itemprop'):
					if span['itemprop'] == 'ratingValue':
						movieRating = span.contents[0]
			movieFound = True			
			
		except:
			pass

		if(movieFound):
			count += 1
			collection.insert_one({'Movie_Name':movieTitle,'Movie_Rating':movieRating,'Movie_Year':movieYear,'Movie_Synopsis':movieSynopsis,'Movie_Image':imageURL})
			'''
			print(movieTitle + " Rating " + str(movieRating) + " Year " + str(movieYear))
			print()
			print()
			'''

		if(count > 250):
			break
		