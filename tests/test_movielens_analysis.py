import sys
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_DIR))

from movielens_analysis import Movies, Tags, Ratings, Links


def write_file(tmp_path, filename, content):
    path = tmp_path / filename
    path.write_text(content, encoding="utf-8")
    return path


def test_movies_distribution_by_release_year(tmp_path):
    content = (
        "movieId,title,genres\n"
        '1,"Toy Story (1995)",Adventure|Animation|Children|Comedy|Fantasy\n'
        '2,"Jumanji (1995)",Adventure|Children|Fantasy\n'
        '3,"Heat (1995)",Action|Crime|Thriller\n'
        '4,"Matrix, The (1999)",Action|Sci-Fi|Thriller\n'
    )

    path = write_file(tmp_path, "movies.csv", content)

    movies = Movies(path)
    result = movies.dist_by_release()

    assert result == {1995: 3, 1999: 1}


def test_movies_distribution_by_genres(tmp_path):
    content = (
        "movieId,title,genres\n"
        '1,"Toy Story (1995)",Adventure|Animation|Children|Comedy|Fantasy\n'
        '2,"Jumanji (1995)",Adventure|Children|Fantasy\n'
        '3,"Heat (1995)",Action|Crime|Thriller\n'
    )

    path = write_file(tmp_path, "movies.csv", content)

    movies = Movies(path)
    result = movies.dist_by_genres()

    assert result["Adventure"] == 2
    assert result["Children"] == 2
    assert result["Fantasy"] == 2
    assert result["Action"] == 1


def test_movies_most_genres(tmp_path):
    content = (
        "movieId,title,genres\n"
        '1,"Toy Story (1995)",Adventure|Animation|Children|Comedy|Fantasy\n'
        '2,"Jumanji (1995)",Adventure|Children|Fantasy\n'
        '3,"Heat (1995)",Action|Crime|Thriller\n'
    )

    path = write_file(tmp_path, "movies.csv", content)

    movies = Movies(path)
    result = movies.most_genres(2)

    assert result == {
        "Toy Story (1995)": 5,
        "Heat (1995)": 3,
    }


def test_movies_get_title_and_genres(tmp_path):
    content = (
        "movieId,title,genres\n"
        '1,"Toy Story (1995)",Adventure|Animation|Children|Comedy|Fantasy\n'
    )

    path = write_file(tmp_path, "movies.csv", content)

    movies = Movies(path)

    assert movies.get_movie_title(1) == "Toy Story (1995)"
    assert movies.get_movie_genres(1) == [
        "Adventure",
        "Animation",
        "Children",
        "Comedy",
        "Fantasy",
    ]


def test_movies_search_title(tmp_path):
    content = (
        "movieId,title,genres\n"
        '1,"Toy Story (1995)",Adventure|Animation|Children|Comedy|Fantasy\n'
        '2,"Matrix, The (1999)",Action|Sci-Fi|Thriller\n'
    )

    path = write_file(tmp_path, "movies.csv", content)

    movies = Movies(path)
    result = movies.search_title("matrix")

    assert result == [(2, "Matrix, The (1999)")]


def test_tags_most_words(tmp_path):
    content = (
        "userId,movieId,tag,timestamp\n"
        "1,1,classic movie,100\n"
        "2,1,very emotional drama,200\n"
        "3,2,classic movie,300\n"
        "4,2,fun,400\n"
    )

    path = write_file(tmp_path, "tags.csv", content)

    tags = Tags(path)
    result = tags.most_words(2)

    assert result == {
        "very emotional drama": 3,
        "classic movie": 2,
    }


def test_tags_longest(tmp_path):
    content = (
        "userId,movieId,tag,timestamp\n"
        "1,1,classic movie,100\n"
        "2,1,very emotional drama,200\n"
        "3,2,fun,300\n"
    )

    path = write_file(tmp_path, "tags.csv", content)

    tags = Tags(path)
    result = tags.longest(2)

    assert result == [
        "very emotional drama",
        "classic movie",
    ]


def test_tags_most_words_and_longest(tmp_path):
    content = (
        "userId,movieId,tag,timestamp\n"
        "1,1,classic movie,100\n"
        "2,1,very emotional drama,200\n"
        "3,2,fun,300\n"
    )

    path = write_file(tmp_path, "tags.csv", content)

    tags = Tags(path)
    result = tags.most_words_and_longest(2)

    assert result == [
        "classic movie",
        "very emotional drama",
    ]


def test_tags_most_popular(tmp_path):
    content = (
        "userId,movieId,tag,timestamp\n"
        "1,1,classic,100\n"
        "2,1,classic,200\n"
        "3,2,fun,300\n"
        "4,2,classic,400\n"
    )

    path = write_file(tmp_path, "tags.csv", content)

    tags = Tags(path)
    result = tags.most_popular(2)

    assert result == {
        "classic": 3,
        "fun": 1,
    }


def test_tags_with_word(tmp_path):
    content = (
        "userId,movieId,tag,timestamp\n"
        "1,1,classic movie,100\n"
        "2,1,emotional drama,200\n"
        "3,2,movie night,300\n"
    )

    path = write_file(tmp_path, "tags.csv", content)

    tags = Tags(path)
    result = tags.tags_with("movie")

    assert result == [
        "classic movie",
        "movie night",
    ]


def test_ratings_dist_by_year(tmp_path):
    content = (
        "userId,movieId,rating,timestamp\n"
        "1,1,4.0,788918400\n"
        "2,1,5.0,788918400\n"
        "3,2,3.0,915148800\n"
    )

    path = write_file(tmp_path, "ratings.csv", content)

    ratings = Ratings(path)
    result = ratings.movie_analysis.dist_by_year()

    assert result == {
        1995: 2,
        1999: 1,
    }


def test_ratings_dist_by_rating(tmp_path):
    content = (
        "userId,movieId,rating,timestamp\n"
        "1,1,4.0,100\n"
        "2,1,5.0,200\n"
        "3,2,4.0,300\n"
    )

    path = write_file(tmp_path, "ratings.csv", content)

    ratings = Ratings(path)
    result = ratings.movie_analysis.dist_by_rating()

    assert result == {
        4.0: 2,
        5.0: 1,
    }


def test_ratings_top_by_num_of_ratings_with_movie_titles(tmp_path):
    ratings_content = (
        "userId,movieId,rating,timestamp\n"
        "1,1,4.0,100\n"
        "2,1,5.0,200\n"
        "3,2,3.0,300\n"
    )

    movies_content = (
        "movieId,title,genres\n"
        '1,"Toy Story (1995)",Adventure|Animation|Children|Comedy|Fantasy\n'
        '2,"Jumanji (1995)",Adventure|Children|Fantasy\n'
    )

    ratings_path = write_file(tmp_path, "ratings.csv", ratings_content)
    movies_path = write_file(tmp_path, "movies.csv", movies_content)

    ratings = Ratings(ratings_path, movies_path=movies_path)
    result = ratings.movie_analysis.top_by_num_of_ratings(2)

    assert result == {
        "Toy Story (1995)": 2,
        "Jumanji (1995)": 1,
    }


def test_ratings_top_by_average_rating(tmp_path):
    ratings_content = (
        "userId,movieId,rating,timestamp\n"
        "1,1,4.0,100\n"
        "2,1,5.0,200\n"
        "3,2,3.0,300\n"
        "4,2,3.0,400\n"
    )

    movies_content = (
        "movieId,title,genres\n"
        '1,"Toy Story (1995)",Adventure|Animation|Children|Comedy|Fantasy\n'
        '2,"Jumanji (1995)",Adventure|Children|Fantasy\n'
    )

    ratings_path = write_file(tmp_path, "ratings.csv", ratings_content)
    movies_path = write_file(tmp_path, "movies.csv", movies_content)

    ratings = Ratings(ratings_path, movies_path=movies_path)
    result = ratings.movie_analysis.top_by_ratings(2, metric="average")

    assert result == {
        "Toy Story (1995)": 4.5,
        "Jumanji (1995)": 3.0,
    }


def test_ratings_top_controversial_movies(tmp_path):
    ratings_content = (
        "userId,movieId,rating,timestamp\n"
        "1,1,1.0,100\n"
        "2,1,5.0,200\n"
        "3,2,3.0,300\n"
        "4,2,3.0,400\n"
    )

    movies_content = (
        "movieId,title,genres\n"
        '1,"Toy Story (1995)",Adventure|Animation|Children|Comedy|Fantasy\n'
        '2,"Jumanji (1995)",Adventure|Children|Fantasy\n'
    )

    ratings_path = write_file(tmp_path, "ratings.csv", ratings_content)
    movies_path = write_file(tmp_path, "movies.csv", movies_content)

    ratings = Ratings(ratings_path, movies_path=movies_path)
    result = ratings.movie_analysis.top_controversial(2)

    assert result["Toy Story (1995)"] == 8.0
    assert result["Jumanji (1995)"] == 0.0


def test_users_distribution_by_number_of_ratings(tmp_path):
    content = (
        "userId,movieId,rating,timestamp\n"
        "1,1,4.0,100\n"
        "1,2,5.0,200\n"
        "2,1,3.0,300\n"
    )

    path = write_file(tmp_path, "ratings.csv", content)

    ratings = Ratings(path)
    result = ratings.user_analysis.dist_by_num_of_ratings()

    assert result == {
        1: 2,
        2: 1,
    }


def test_users_distribution_by_average_rating(tmp_path):
    content = (
        "userId,movieId,rating,timestamp\n"
        "1,1,4.0,100\n"
        "1,2,5.0,200\n"
        "2,1,3.0,300\n"
    )

    path = write_file(tmp_path, "ratings.csv", content)

    ratings = Ratings(path)
    result = ratings.user_analysis.dist_by_rating(metric="average")

    assert result == {
        1: 4.5,
        2: 3.0,
    }


def test_users_top_controversial(tmp_path):
    content = (
        "userId,movieId,rating,timestamp\n"
        "1,1,1.0,100\n"
        "1,2,5.0,200\n"
        "2,1,3.0,300\n"
        "2,2,3.0,400\n"
    )

    path = write_file(tmp_path, "ratings.csv", content)

    ratings = Ratings(path)
    result = ratings.user_analysis.top_controversial(2)

    assert result[1] == 8.0
    assert result[2] == 0.0


def test_links_get_ids_and_urls(tmp_path):
    content = (
        "movieId,imdbId,tmdbId\n"
        "1,114709,862\n"
        "2,113497,8844\n"
    )

    path = write_file(tmp_path, "links.csv", content)

    links = Links(path)

    assert links.get_imdb_id(1) == 114709
    assert links.get_tmdb_id(1) == 862
    assert links.get_imdb_url(1) == "https://www.imdb.com/title/tt0114709/"
    assert links.get_tmdb_url(1) == "https://www.themoviedb.org/movie/862"


def test_links_join_with_movies(tmp_path):
    links_content = (
        "movieId,imdbId,tmdbId\n"
        "1,114709,862\n"
    )

    movies_content = (
        "movieId,title,genres\n"
        '1,"Toy Story (1995)",Adventure|Animation|Children|Comedy|Fantasy\n'
    )

    links_path = write_file(tmp_path, "links.csv", links_content)
    movies_path = write_file(tmp_path, "movies.csv", movies_content)

    links = Links(links_path)
    movies = Movies(movies_path)

    result = links.join_with_movies(movies, 1)

    assert result == {
        "movieId": 1,
        "title": "Toy Story (1995)",
        "genres": ["Adventure", "Animation", "Children", "Comedy", "Fantasy"],
        "imdbId": 114709,
        "tmdbId": 862,
        "imdbUrl": "https://www.imdb.com/title/tt0114709/",
        "tmdbUrl": "https://www.themoviedb.org/movie/862",
    }


def test_invalid_metric_raises_error(tmp_path):
    content = (
        "userId,movieId,rating,timestamp\n"
        "1,1,4.0,100\n"
    )

    path = write_file(tmp_path, "ratings.csv", content)

    ratings = Ratings(path)

    with pytest.raises(ValueError):
        ratings.movie_analysis.top_by_ratings(1, metric="invalid")


def test_missing_file_raises_error(tmp_path):
    missing_path = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        Movies(missing_path)