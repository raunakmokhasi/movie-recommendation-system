# movie-recommendation-system

I've built a movie recommendation system, which asks a user to rate a small set of movies and based on these ratings, suggests more movies which will suit their taste.

In order to scrape a wide variety of movies I used the Movielens "ml-latest-small" Database. I noticed that the first few thousand ratings were only 1995 - 1997. So I randomly sorted them first and then only used it to get the links of movies. (This ensured that I had Latest movies and also old ones). Then i went to the respective links and scraped the websites to get all the required information. (Movie Name,Year,Image,Synopsis etc). I used Beautiful Soup for the process of web scraping. I stored all this on an online MongoDB Atlas Database.

For the Movie Recommendation System - 
I referred to Stanford's video for learning what Collaborative Filtering actually is. (Link - https://www.youtube.com/watch?v=h9gpufJFF-0)
I followed the formulas in the video to calculate mean,normalisation and centered cosine distance exactly as per the video.

I implemented User-User and Item-Item Collaborative Filtering methods of recommendation.

The web application with a user interface was built using Bootstrap (on a Flask server). 

To run the whole web application run app.py. And then go to http://127.0.0.1:5000/login.

Then you'll get a list of all the movies.

On the next page you'll get a list of 5 movies to rate. After submitting your ratings you'll get a list of 4 movies from each of the collaborative filtering methods.

Enjoy :)
