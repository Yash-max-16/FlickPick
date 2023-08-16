# FlickPick
FlickPick is a movie recommender web app developed using content based filtering. User can select a movie from a pool of available movies and the web app will recommend 5 similar movies(with movie names and posters). Similarity of movies is obtained using cosine similarity concept.  
The recommendation system was developed using the dataset obtained from TMDB. The filtering was done by vectorizing the movie descriptions. Before vectorizing, the movie descriptions were processed using NLTK for better performance of the system. Then similarity values of each movie with all other movies in the database was calculated and stored in [similarity.pkl](https://drive.google.com/file/d/1XueRul-mLGrgO5kgTi7y9ZhvEYJF2F5N/view?usp=drive_link). So, whenever a user selects a movie, the recommendations is provided by fetching 5 movies with highest similarity with the selected movie.  
The poster of the movies are fetched from the TMDB database using their API.  
The web app was developed using streamlit library of python.  
[Here](https://drive.google.com/file/d/1iWuR9cJ9Qapkb3hj-Z_wMC9ZybHjBP1C/view?usp=drive_link) is a video to demonstrate the working of the web app.
