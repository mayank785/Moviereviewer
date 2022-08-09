import imdb
hr = imdb.IMDb()

movie_name = input("Enter the movie name : ")
movies = hr.search_movie(str(movie_name))

index = movies[0].getID()
movie = hr.get_movie(index)
title = movie['title']
year = movie['year']
cast = movie['cast']
list_of_cast = ','.join(map(str, cast))

print('Title : ', title)
print('Year : ', year)
print('Cast : ', list_of_cast)
