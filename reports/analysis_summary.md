# Analysis Summary

## Project

**MovieLens OOP Analysis**

This report summarizes the main analytical capabilities implemented in the project and the type of insights that can be extracted from the MovieLens Latest Small dataset.

The project analyzes four dataset files:

```text
movies.csv
ratings.csv
tags.csv
links.csv
```

The analysis is implemented through an object-oriented Python module located in:

```text
src/movielens_analysis.py
```

---

## 1. Movie Metadata Analysis

Movie metadata is analyzed with the `Movies` class.

### Main Questions

The movie analysis module helps answer questions such as:

- Which release years have the highest number of movies?
- Which genres are the most frequent?
- Which movies are assigned the largest number of genres?
- Which movies belong to a specific genre?
- Which movies match a specific title pattern?

### Implemented Methods

```python
movies.dist_by_release()
movies.dist_by_genres()
movies.most_genres(n)
movies.movies_by_genre(genre)
movies.search_title(pattern)
```

### Expected Insights

This analysis can reveal:

- the most represented years in the dataset;
- the most common movie genres;
- genre diversity across movies;
- title patterns and keyword-based search results.

---

## 2. Ratings Analysis

Ratings are analyzed with the `Ratings` class.

The class provides both movie-level and user-level analysis.

---

## 2.1 Movie-Level Ratings Analysis

Movie-level analysis is available through:

```python
ratings.movie_analysis
```

### Main Questions

The movie-level rating analysis helps answer questions such as:

- How are ratings distributed across years?
- What are the most common rating values?
- Which movies received the highest number of ratings?
- Which movies have the highest average or median rating?
- Which movies are the most controversial based on rating variance?

### Implemented Methods

```python
ratings.movie_analysis.dist_by_year()
ratings.movie_analysis.dist_by_rating()
ratings.movie_analysis.top_by_num_of_ratings(n)
ratings.movie_analysis.top_by_ratings(n, metric="average")
ratings.movie_analysis.top_controversial(n)
```

### Expected Insights

This analysis can reveal:

- rating activity over time;
- user rating tendencies;
- highly rated movies;
- widely watched or frequently rated movies;
- movies with strong disagreement among users.

---

## 2.2 User-Level Ratings Analysis

User-level analysis is available through:

```python
ratings.user_analysis
```

### Main Questions

The user-level rating analysis helps answer questions such as:

- Which users rated the largest number of movies?
- Which users tend to give higher or lower ratings?
- Which users have the highest rating variance?

### Implemented Methods

```python
ratings.user_analysis.dist_by_num_of_ratings()
ratings.user_analysis.dist_by_rating(metric="average")
ratings.user_analysis.top_controversial(n)
```

### Expected Insights

This analysis can reveal:

- the most active users;
- user rating behavior;
- users with consistent or inconsistent rating patterns;
- users with strong rating variation across movies.

---

## 3. Tag Analysis

Tags are analyzed with the `Tags` class.

### Main Questions

The tag analysis module helps answer questions such as:

- Which tags are the most popular?
- Which tags contain the highest number of words?
- Which tags are the longest by character length?
- Which tags contain a specific word?
- Which tags were assigned to a specific movie?
- Which tags were created by a specific user?

### Implemented Methods

```python
tags.unique_tags()
tags.most_words(n)
tags.longest(n)
tags.most_words_and_longest(n)
tags.most_popular(n)
tags.tags_with(word)
tags.tags_for_movie(movie_id)
tags.tags_for_user(user_id)
```

### Expected Insights

This analysis can reveal:

- common user-generated descriptors;
- descriptive or phrase-based tagging behavior;
- frequently repeated tags;
- movies associated with specific themes or keywords.

---

## 4. External Link Analysis

External identifiers are analyzed with the `Links` class.

### Main Questions

The link analysis module helps answer questions such as:

- What is the IMDb ID of a MovieLens movie?
- What is the TMDB ID of a MovieLens movie?
- What is the IMDb URL for a specific movie?
- What is the TMDB URL for a specific movie?
- How can movie metadata be joined with external movie links?

### Implemented Methods

```python
links.get_imdb_id(movie_id)
links.get_tmdb_id(movie_id)
links.get_imdb_url(movie_id)
links.get_tmdb_url(movie_id)
links.join_with_movies(movies, movie_id)
links.get_external_links(movie_ids)
```

### Expected Insights

This analysis allows the local MovieLens dataset to be connected to external movie databases such as IMDb and TMDB.

---

## 5. Testing Summary

The project includes unit tests in:

```text
tests/test_movielens_analysis.py
```

The tests validate the main behavior of the project, including:

- release year extraction;
- genre counting;
- movie title search;
- tag frequency analysis;
- rating distribution;
- top-rated movies;
- controversial movies;
- user-level rating statistics;
- IMDb and TMDB URL generation;
- error handling.

The tests can be executed with:

```bash
python -m pytest tests -v
```

---

## 6. Technical Summary

The project demonstrates the following technical skills:

- Python programming;
- object-oriented design;
- CSV file processing;
- data aggregation;
- dictionary/list transformations;
- sorting logic;
- timestamp processing;
- statistical calculations;
- unit testing with pytest;
- clean project organization;
- technical documentation.

---

## 7. Limitations

The project focuses on local analysis of the MovieLens dataset.

Current limitations:

- the core module does not use advanced data visualization;
- the core module does not perform recommendation modeling;
- IMDb web scraping is intentionally not included;
- the dataset must be downloaded manually from GroupLens;
- analysis depends on the MovieLens Latest Small dataset structure.

