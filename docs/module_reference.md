# Module Reference

## Module

```text
src/movielens_analysis.py
```

This module contains the core logic of the project.

It provides four main classes:

```text
Movies
Ratings
Tags
Links
```

The module is designed to analyze the MovieLens Latest Small dataset using object-oriented Python.

The core module only uses the Python standard library.

---

# Movies Class

## Purpose

The `Movies` class analyzes the `movies.csv` file.

Expected file:

```text
data/movies.csv
```

Expected columns:

```text
movieId,title,genres
```

## Initialization

```python
from movielens_analysis import Movies

movies = Movies("data/movies.csv")
```

## Main Methods

### get_movie_title(movie_id)

Returns the title of a movie by its `movieId`.

```python
movies.get_movie_title(1)
```

Example output:

```text
Toy Story (1995)
```

---

### get_movie_genres(movie_id)

Returns the list of genres for a movie.

```python
movies.get_movie_genres(1)
```

Example output:

```python
["Adventure", "Animation", "Children", "Comedy", "Fantasy"]
```

---

### dist_by_release()

Returns the distribution of movies by release year.

The release year is extracted from the movie title.

```python
movies.dist_by_release()
```

Example output:

```python
{
    1995: 3,
    1999: 1
}
```

The result is sorted by count descending.

---

### dist_by_genres()

Returns the distribution of movies by genre.

```python
movies.dist_by_genres()
```

Example output:

```python
{
    "Drama": 4361,
    "Comedy": 3756,
    "Thriller": 1894
}
```

The result is sorted by count descending.

---

### most_genres(n)

Returns the top `n` movies with the highest number of genres.

```python
movies.most_genres(10)
```

Example output:

```python
{
    "Rubber (2010)": 10,
    "Patlabor: The Movie (Kidô keisatsu patorebâ: The Movie) (1989)": 8
}
```

---

### movies_by_genre(genre)

Returns all movie titles that contain a specific genre.

```python
movies.movies_by_genre("Comedy")
```

Example output:

```python
[
    "Toy Story (1995)",
    "Jumanji (1995)"
]
```

---

### search_title(pattern, ignore_case=True)

Searches movie titles using a regular expression pattern.

```python
movies.search_title("matrix")
```

Example output:

```python
[
    (2571, "Matrix, The (1999)")
]
```

---

# Tags Class

## Purpose

The `Tags` class analyzes the `tags.csv` file.

Expected file:

```text
data/tags.csv
```

Expected columns:

```text
userId,movieId,tag,timestamp
```

## Initialization

```python
from movielens_analysis import Tags

tags = Tags("data/tags.csv")
```

## Main Methods

### unique_tags()

Returns all unique tags sorted alphabetically.

```python
tags.unique_tags()
```

---

### most_words(n)

Returns the top `n` tags with the highest number of words.

```python
tags.most_words(10)
```

Example output:

```python
{
    "based on a true story": 5,
    "adapted from book": 3
}
```

---

### longest(n)

Returns the top `n` longest tags by number of characters.

```python
tags.longest(10)
```

Example output:

```python
[
    "thought-provoking and emotional",
    "based on a true story"
]
```

---

### most_words_and_longest(n)

Returns the intersection between:

```text
top-n tags with the most words
top-n longest tags by character length
```

```python
tags.most_words_and_longest(10)
```

---

### most_popular(n)

Returns the most frequently used tags.

```python
tags.most_popular(10)
```

Example output:

```python
{
    "In Netflix queue": 131,
    "atmospheric": 36
}
```

---

### tags_with(word)

Returns all unique tags that include a specific word.

```python
tags.tags_with("movie")
```

Example output:

```python
[
    "classic movie",
    "movie night"
]
```

---

### tags_for_movie(movie_id)

Returns all tags assigned to a specific movie.

```python
tags.tags_for_movie(1)
```

---

### tags_for_user(user_id)

Returns all tags created by a specific user.

```python
tags.tags_for_user(10)
```

---

# Ratings Class

## Purpose

The `Ratings` class analyzes the `ratings.csv` file.

Expected file:

```text
data/ratings.csv
```

Expected columns:

```text
userId,movieId,rating,timestamp
```

The class can optionally receive the path to `movies.csv` in order to return movie titles instead of only movie IDs.

## Initialization

```python
from movielens_analysis import Ratings

ratings = Ratings(
    "data/ratings.csv",
    movies_path="data/movies.csv"
)
```

If `movies_path` is not provided, movie-level methods return labels like:

```text
movieId=1
```

## Main Direct Methods

### get_ratings_by_movie(movie_id)

Returns all ratings for a movie, sorted ascending.

```python
ratings.get_ratings_by_movie(1)
```

Example output:

```python
[3.0, 4.0, 4.5, 5.0]
```

---

### get_ratings_by_user(user_id)

Returns all ratings made by a user, sorted ascending.

```python
ratings.get_ratings_by_user(1)
```

---

### get_average_rating(movie_id)

Returns the average rating for a movie.

```python
ratings.get_average_rating(1)
```

Example output:

```python
3.92
```

---

# Ratings Movie-Level Analysis

Movie-level analysis is available through:

```python
ratings.movie_analysis
```

## Methods

### dist_by_year()

Returns the distribution of ratings by year.

Years are extracted from Unix timestamps.

```python
ratings.movie_analysis.dist_by_year()
```

Example output:

```python
{
    1996: 6040,
    1997: 1916
}
```

---

### dist_by_rating()

Returns the distribution of rating values.

```python
ratings.movie_analysis.dist_by_rating()
```

Example output:

```python
{
    0.5: 1370,
    1.0: 2811,
    1.5: 1791,
    2.0: 7551
}
```

---

### top_by_num_of_ratings(n)

Returns top `n` movies by number of ratings.

```python
ratings.movie_analysis.top_by_num_of_ratings(10)
```

Example output:

```python
{
    "Forrest Gump (1994)": 329,
    "Shawshank Redemption, The (1994)": 317
}
```

---

### top_by_ratings(n, metric="average")

Returns top `n` movies by average or median rating.

Supported metrics:

```text
average
median
```

Example:

```python
ratings.movie_analysis.top_by_ratings(10, metric="average")
```

Example output:

```python
{
    "Movie Title (Year)": 4.75
}
```

---

### top_controversial(n)

Returns top `n` movies by rating variance.

A higher variance means users disagreed more strongly about the movie.

```python
ratings.movie_analysis.top_controversial(10)
```

Example output:

```python
{
    "Movie Title (Year)": 5.12
}
```

---

# Ratings User-Level Analysis

User-level analysis is available through:

```python
ratings.user_analysis
```

## Methods

### dist_by_num_of_ratings()

Returns the distribution of users by number of ratings made.

```python
ratings.user_analysis.dist_by_num_of_ratings()
```

Example output:

```python
{
    414: 2698,
    599: 2478
}
```

---

### dist_by_rating(metric="average")

Returns users sorted by their average or median rating.

Supported metrics:

```text
average
median
```

Example:

```python
ratings.user_analysis.dist_by_rating(metric="average")
```

---

### top_controversial(n)

Returns top `n` users with the highest variance in their ratings.

```python
ratings.user_analysis.top_controversial(10)
```

---

# Links Class

## Purpose

The `Links` class analyzes the `links.csv` file.

Expected file:

```text
data/links.csv
```

Expected columns:

```text
movieId,imdbId,tmdbId
```

The class maps MovieLens movie IDs to IMDb and TMDB identifiers.

## Initialization

```python
from movielens_analysis import Links

links = Links("data/links.csv")
```

## Main Methods

### get_imdb_id(movie_id)

Returns the IMDb ID for a MovieLens movie ID.

```python
links.get_imdb_id(1)
```

Example output:

```python
114709
```

---

### get_tmdb_id(movie_id)

Returns the TMDB ID for a MovieLens movie ID.

```python
links.get_tmdb_id(1)
```

Example output:

```python
862
```

---

### get_imdb_url(movie_id)

Returns the full IMDb URL for a MovieLens movie ID.

```python
links.get_imdb_url(1)
```

Example output:

```text
https://www.imdb.com/title/tt0114709/
```

---

### get_tmdb_url(movie_id)

Returns the full TMDB URL for a MovieLens movie ID.

```python
links.get_tmdb_url(1)
```

Example output:

```text
https://www.themoviedb.org/movie/862
```

---

### join_with_movies(movies, movie_id)

Joins external movie IDs with movie metadata from the `Movies` class.

```python
links.join_with_movies(movies, 1)
```

Example output:

```python
{
    "movieId": 1,
    "title": "Toy Story (1995)",
    "genres": ["Adventure", "Animation", "Children", "Comedy", "Fantasy"],
    "imdbId": 114709,
    "tmdbId": 862,
    "imdbUrl": "https://www.imdb.com/title/tt0114709/",
    "tmdbUrl": "https://www.themoviedb.org/movie/862"
}
```

---

### get_external_links(movie_ids)

Returns external links for multiple movie IDs.

```python
links.get_external_links([1, 2, 3])
```

---

# Error Handling

The module raises:

```text
FileNotFoundError
```

when a required CSV file does not exist.

The `Ratings` class raises:

```text
ValueError
```

when an invalid metric is provided.

Example:

```python
ratings.movie_analysis.top_by_ratings(10, metric="invalid")
```

Valid metrics are:

```text
average
median
```

---

# Design Notes

The module was designed with the following principles:

- clear object-oriented structure;
- lightweight dependencies;
- reusable methods;
- readable outputs;
- testable logic;
- separation between source code and notebooks;
- portfolio-ready organization.

The module intentionally avoids web scraping. The original School 21 task included IMDb page parsing, but this professional version focuses on stable local analysis using the provided MovieLens files.