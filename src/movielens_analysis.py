"""
MovieLens OOP Analysis Toolkit

This module provides object-oriented utilities for analyzing the MovieLens
ml-latest-small dataset.

Supported files:
- movies.csv
- ratings.csv
- tags.csv
- links.csv

The module intentionally uses only the Python standard library so it can be
run in simple environments without additional data-analysis dependencies.
"""

from __future__ import annotations

import csv
import re
import statistics
from collections import Counter, defaultdict, OrderedDict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


def _read_csv(path: str | Path, limit: Optional[int] = None) -> List[Dict[str, str]]:
    """
    Read a CSV file and return a list of dictionaries.

    Parameters
    ----------
    path:
        Path to the CSV file.
    limit:
        Optional maximum number of rows to read.

    Returns
    -------
    list[dict]
        CSV rows represented as dictionaries.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    rows: List[Dict[str, str]] = []

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for index, row in enumerate(reader):
            if limit is not None and index >= limit:
                break

            rows.append(row)

    return rows


def _sort_dict_by_value_desc(data: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Sort a dictionary by value descending and key ascending.
    """
    return dict(sorted(data.items(), key=lambda item: (-item[1], item[0])))


def _round_dict_values(data: Dict[Any, float], decimals: int = 2) -> Dict[Any, float]:
    """
    Round all numeric dictionary values.
    """
    return {key: round(value, decimals) for key, value in data.items()}


class Movies:
    """
    Analyze data from movies.csv.

    Expected columns:
    - movieId
    - title
    - genres
    """

    def __init__(self, path_to_the_file: str | Path, limit: Optional[int] = None):
        self.path = Path(path_to_the_file)
        self.limit = limit
        self.rows = _read_csv(self.path, limit=self.limit)

        self.movies_by_id = {
            int(row["movieId"]): row["title"]
            for row in self.rows
        }

        self.genres_by_id = {
            int(row["movieId"]): self._split_genres(row["genres"])
            for row in self.rows
        }

    @staticmethod
    def _split_genres(genres_raw: str) -> List[str]:
        """
        Split the MovieLens pipe-separated genre format.
        """
        if not genres_raw or genres_raw == "(no genres listed)":
            return []

        return genres_raw.split("|")

    @staticmethod
    def _extract_year(title: str) -> Optional[int]:
        """
        Extract release year from a movie title.

        Example:
        "Toy Story (1995)" -> 1995
        """
        match = re.search(r"\((\d{4})\)\s*$", title)

        if not match:
            return None

        return int(match.group(1))

    def get_movie_title(self, movie_id: int) -> str:
        """
        Return movie title by movieId.
        """
        return self.movies_by_id.get(int(movie_id), "")

    def get_movie_genres(self, movie_id: int) -> List[str]:
        """
        Return movie genres by movieId.
        """
        return list(self.genres_by_id.get(int(movie_id), []))

    def dist_by_release(self) -> Dict[int, int]:
        """
        Return distribution of movies by release year.

        The dictionary keys are release years and values are counts.
        The result is sorted by counts descending.
        """
        counts: Counter[int] = Counter()

        for row in self.rows:
            year = self._extract_year(row["title"])

            if year is not None:
                counts[year] += 1

        return _sort_dict_by_value_desc(dict(counts))

    def dist_by_genres(self) -> Dict[str, int]:
        """
        Return distribution of movies by genre.

        The dictionary keys are genres and values are counts.
        The result is sorted by counts descending.
        """
        counts: Counter[str] = Counter()

        for row in self.rows:
            for genre in self._split_genres(row["genres"]):
                counts[genre] += 1

        return _sort_dict_by_value_desc(dict(counts))

    def most_genres(self, n: int) -> Dict[str, int]:
        """
        Return top-n movies with the largest number of genres.

        The dictionary keys are movie titles and values are the number of genres.
        The result is sorted by number of genres descending.
        """
        movie_genre_counts = {
            row["title"]: len(self._split_genres(row["genres"]))
            for row in self.rows
        }

        sorted_items = sorted(
            movie_genre_counts.items(),
            key=lambda item: (-item[1], item[0])
        )

        return dict(sorted_items[:n])

    def movies_by_genre(self, genre: str) -> List[str]:
        """
        Return movie titles that contain a specific genre.
        """
        result = []

        for row in self.rows:
            genres = self._split_genres(row["genres"])

            if genre in genres:
                result.append(row["title"])

        return sorted(result)

    def search_title(self, pattern: str, ignore_case: bool = True) -> List[Tuple[int, str]]:
        """
        Search movies by regular expression pattern.

        Returns a list of tuples:
        (movieId, title)
        """
        flags = re.IGNORECASE if ignore_case else 0
        regex = re.compile(pattern, flags=flags)

        result = []

        for row in self.rows:
            title = row["title"]

            if regex.search(title):
                result.append((int(row["movieId"]), title))

        return sorted(result, key=lambda item: item[1])


class Tags:
    """
    Analyze data from tags.csv.

    Expected columns:
    - userId
    - movieId
    - tag
    - timestamp
    """

    def __init__(self, path_to_the_file: str | Path, limit: Optional[int] = None):
        self.path = Path(path_to_the_file)
        self.limit = limit
        self.rows = _read_csv(self.path, limit=self.limit)

    @staticmethod
    def _normalize_tag(tag: str) -> str:
        """
        Normalize tag text for duplicate handling.
        """
        return tag.strip()

    @staticmethod
    def _word_count(tag: str) -> int:
        """
        Count words inside a tag.
        """
        words = tag.split()
        return len(words)

    def unique_tags(self) -> List[str]:
        """
        Return all unique tags sorted alphabetically.
        """
        tags = {self._normalize_tag(row["tag"]) for row in self.rows}
        return sorted(tags)

    def most_words(self, n: int) -> Dict[str, int]:
        """
        Return top-n tags with the highest number of words.

        The dictionary keys are tags and values are word counts.
        Duplicates are removed.
        """
        tag_word_counts = {
            tag: self._word_count(tag)
            for tag in self.unique_tags()
        }

        sorted_items = sorted(
            tag_word_counts.items(),
            key=lambda item: (-item[1], item[0])
        )

        return dict(sorted_items[:n])

    def longest(self, n: int) -> List[str]:
        """
        Return top-n longest tags by number of characters.

        Duplicates are removed.
        """
        sorted_tags = sorted(
            self.unique_tags(),
            key=lambda tag: (-len(tag), tag)
        )

        return sorted_tags[:n]

    def most_words_and_longest(self, n: int) -> List[str]:
        """
        Return the intersection between:
        - top-n tags with the most words
        - top-n longest tags by character length
        """
        most_words_tags = set(self.most_words(n).keys())
        longest_tags = set(self.longest(n))

        return sorted(most_words_tags.intersection(longest_tags))

    def most_popular(self, n: int) -> Dict[str, int]:
        """
        Return top-n most popular tags by frequency.

        The dictionary keys are tags and values are counts.
        """
        counts: Counter[str] = Counter(
            self._normalize_tag(row["tag"])
            for row in self.rows
        )

        sorted_items = sorted(
            counts.items(),
            key=lambda item: (-item[1], item[0])
        )

        return dict(sorted_items[:n])

    def tags_with(self, word: str) -> List[str]:
        """
        Return all unique tags that include the given word.

        The result is sorted alphabetically.
        """
        word_lower = word.lower()

        result = [
            tag
            for tag in self.unique_tags()
            if word_lower in tag.lower().split()
        ]

        return sorted(result)

    def tags_for_movie(self, movie_id: int) -> List[str]:
        """
        Return all tags for a specific movieId.
        """
        movie_id = int(movie_id)

        tags = [
            self._normalize_tag(row["tag"])
            for row in self.rows
            if int(row["movieId"]) == movie_id
        ]

        return sorted(tags)

    def tags_for_user(self, user_id: int) -> List[str]:
        """
        Return all tags created by a specific userId.
        """
        user_id = int(user_id)

        tags = [
            self._normalize_tag(row["tag"])
            for row in self.rows
            if int(row["userId"]) == user_id
        ]

        return sorted(tags)


class Ratings:
    """
    Analyze data from ratings.csv.

    Expected columns:
    - userId
    - movieId
    - rating
    - timestamp

    Optionally, a movies.csv path can be provided to map movieId values
    to movie titles in movie-level analysis methods.
    """

    def __init__(
        self,
        path_to_the_file: str | Path,
        movies_path: Optional[str | Path] = None,
        limit: Optional[int] = None,
    ):
        self.path = Path(path_to_the_file)
        self.limit = limit
        self.rows = _read_csv(self.path, limit=self.limit)

        self.movies: Optional[Movies] = Movies(movies_path) if movies_path else None

        self.movie_analysis = self.Movies(self)
        self.user_analysis = self.Users(self)

    def _movie_title(self, movie_id: int) -> str:
        """
        Return movie title if movies.csv is available.
        Otherwise, return a readable movieId label.
        """
        if self.movies is None:
            return f"movieId={movie_id}"

        title = self.movies.get_movie_title(movie_id)
        return title if title else f"movieId={movie_id}"

    def _ratings_by_movie(self) -> Dict[int, List[float]]:
        """
        Group ratings by movieId.
        """
        grouped: Dict[int, List[float]] = defaultdict(list)

        for row in self.rows:
            grouped[int(row["movieId"])].append(float(row["rating"]))

        return grouped

    def _ratings_by_user(self) -> Dict[int, List[float]]:
        """
        Group ratings by userId.
        """
        grouped: Dict[int, List[float]] = defaultdict(list)

        for row in self.rows:
            grouped[int(row["userId"])].append(float(row["rating"]))

        return grouped

    def get_ratings_by_movie(self, movie_id: int) -> List[float]:
        """
        Return all ratings for a movieId sorted ascending.
        """
        movie_id = int(movie_id)

        ratings = [
            float(row["rating"])
            for row in self.rows
            if int(row["movieId"]) == movie_id
        ]

        return sorted(ratings)

    def get_ratings_by_user(self, user_id: int) -> List[float]:
        """
        Return all ratings made by a userId sorted ascending.
        """
        user_id = int(user_id)

        ratings = [
            float(row["rating"])
            for row in self.rows
            if int(row["userId"]) == user_id
        ]

        return sorted(ratings)

    def get_average_rating(self, movie_id: int) -> float:
        """
        Return average rating for a movieId.
        """
        ratings = self.get_ratings_by_movie(movie_id)

        if not ratings:
            return 0.0

        return sum(ratings) / len(ratings)

    class Movies:
        """
        Movie-level analysis based on ratings.csv.
        """

        def __init__(self, parent: "Ratings"):
            self.parent = parent

        def dist_by_year(self) -> Dict[int, int]:
            """
            Return distribution of ratings by year.

            Years are extracted from Unix timestamps.
            The result is sorted by year ascending.
            """
            counts: Counter[int] = Counter()

            for row in self.parent.rows:
                timestamp = int(row["timestamp"])
                year = datetime.utcfromtimestamp(timestamp).year
                counts[year] += 1

            return dict(sorted(counts.items(), key=lambda item: item[0]))

        def dist_by_rating(self) -> Dict[float, int]:
            """
            Return distribution of ratings.

            The dictionary keys are rating values and values are counts.
            The result is sorted by rating ascending.
            """
            counts: Counter[float] = Counter(
                float(row["rating"])
                for row in self.parent.rows
            )

            return dict(sorted(counts.items(), key=lambda item: item[0]))

        def top_by_num_of_ratings(self, n: int) -> Dict[str, int]:
            """
            Return top-n movies by number of ratings.
            """
            grouped = self.parent._ratings_by_movie()

            counts = {
                self.parent._movie_title(movie_id): len(ratings)
                for movie_id, ratings in grouped.items()
            }

            sorted_items = sorted(
                counts.items(),
                key=lambda item: (-item[1], item[0])
            )

            return dict(sorted_items[:n])

        def top_by_ratings(self, n: int, metric: str = "average") -> Dict[str, float]:
            """
            Return top-n movies by average or median rating.

            Parameters
            ----------
            n:
                Number of movies to return.
            metric:
                Either "average" or "median".
            """
            if metric not in {"average", "median"}:
                raise ValueError("metric must be either 'average' or 'median'")

            grouped = self.parent._ratings_by_movie()
            result = {}

            for movie_id, ratings in grouped.items():
                if metric == "average":
                    value = statistics.mean(ratings)
                else:
                    value = statistics.median(ratings)

                result[self.parent._movie_title(movie_id)] = round(value, 2)

            sorted_items = sorted(
                result.items(),
                key=lambda item: (-item[1], item[0])
            )

            return dict(sorted_items[:n])

        def top_controversial(self, n: int) -> Dict[str, float]:
            """
            Return top-n movies by variance of ratings.
            """
            grouped = self.parent._ratings_by_movie()
            result = {}

            for movie_id, ratings in grouped.items():
                if len(ratings) < 2:
                    variance = 0.0
                else:
                    variance = statistics.variance(ratings)

                result[self.parent._movie_title(movie_id)] = round(variance, 2)

            sorted_items = sorted(
                result.items(),
                key=lambda item: (-item[1], item[0])
            )

            return dict(sorted_items[:n])

    class Users:
        """
        User-level analysis based on ratings.csv.
        """

        def __init__(self, parent: "Ratings"):
            self.parent = parent

        def dist_by_num_of_ratings(self) -> Dict[int, int]:
            """
            Return distribution of users by number of ratings made.

            The dictionary keys are userIds and values are rating counts.
            The result is sorted by count descending.
            """
            grouped = self.parent._ratings_by_user()

            counts = {
                user_id: len(ratings)
                for user_id, ratings in grouped.items()
            }

            sorted_items = sorted(
                counts.items(),
                key=lambda item: (-item[1], item[0])
            )

            return dict(sorted_items)

        def dist_by_rating(self, metric: str = "average") -> Dict[int, float]:
            """
            Return distribution of users by average or median rating.

            Parameters
            ----------
            metric:
                Either "average" or "median".
            """
            if metric not in {"average", "median"}:
                raise ValueError("metric must be either 'average' or 'median'")

            grouped = self.parent._ratings_by_user()
            result = {}

            for user_id, ratings in grouped.items():
                if metric == "average":
                    value = statistics.mean(ratings)
                else:
                    value = statistics.median(ratings)

                result[user_id] = round(value, 2)

            sorted_items = sorted(
                result.items(),
                key=lambda item: (-item[1], item[0])
            )

            return dict(sorted_items)

        def top_controversial(self, n: int) -> Dict[int, float]:
            """
            Return top-n users with the highest variance in their ratings.
            """
            grouped = self.parent._ratings_by_user()
            result = {}

            for user_id, ratings in grouped.items():
                if len(ratings) < 2:
                    variance = 0.0
                else:
                    variance = statistics.variance(ratings)

                result[user_id] = round(variance, 2)

            sorted_items = sorted(
                result.items(),
                key=lambda item: (-item[1], item[0])
            )

            return dict(sorted_items[:n])


class Links:
    """
    Analyze data from links.csv.

    Expected columns:
    - movieId
    - imdbId
    - tmdbId

    This class focuses on local identifier mapping. It does not scrape IMDb
    pages because web scraping can be unstable and depends on external website
    structure and access rules.
    """

    def __init__(self, path_to_the_file: str | Path, limit: Optional[int] = None):
        self.path = Path(path_to_the_file)
        self.limit = limit
        self.rows = _read_csv(self.path, limit=self.limit)

        self.links_by_movie_id = {
            int(row["movieId"]): {
                "imdbId": row["imdbId"],
                "tmdbId": row["tmdbId"] if row["tmdbId"] else None,
            }
            for row in self.rows
        }

    @staticmethod
    def _format_imdb_url(imdb_id: str | int) -> str:
        """
        Format an IMDb ID as a full IMDb title URL.
        """
        return f"https://www.imdb.com/title/tt{int(imdb_id):07d}/"

    @staticmethod
    def _format_tmdb_url(tmdb_id: str | int) -> str:
        """
        Format a TMDB ID as a full TMDB movie URL.
        """
        return f"https://www.themoviedb.org/movie/{int(tmdb_id)}"

    def get_imdb_id(self, movie_id: int) -> Optional[int]:
        """
        Return IMDb ID for a movieId.
        """
        movie_id = int(movie_id)
        item = self.links_by_movie_id.get(movie_id)

        if not item:
            return None

        return int(item["imdbId"])

    def get_tmdb_id(self, movie_id: int) -> Optional[int]:
        """
        Return TMDB ID for a movieId.
        """
        movie_id = int(movie_id)
        item = self.links_by_movie_id.get(movie_id)

        if not item or item["tmdbId"] is None:
            return None

        return int(item["tmdbId"])

    def get_imdb_url(self, movie_id: int) -> Optional[str]:
        """
        Return IMDb URL for a movieId.
        """
        imdb_id = self.get_imdb_id(movie_id)

        if imdb_id is None:
            return None

        return self._format_imdb_url(imdb_id)

    def get_tmdb_url(self, movie_id: int) -> Optional[str]:
        """
        Return TMDB URL for a movieId.
        """
        tmdb_id = self.get_tmdb_id(movie_id)

        if tmdb_id is None:
            return None

        return self._format_tmdb_url(tmdb_id)

    def join_with_movies(self, movies: Movies, movie_id: int) -> Dict[str, Any]:
        """
        Join links.csv identifiers with movie title and genres from movies.csv.
        """
        if not isinstance(movies, Movies):
            raise TypeError("movies must be an instance of Movies")

        movie_id = int(movie_id)

        return {
            "movieId": movie_id,
            "title": movies.get_movie_title(movie_id),
            "genres": movies.get_movie_genres(movie_id),
            "imdbId": self.get_imdb_id(movie_id),
            "tmdbId": self.get_tmdb_id(movie_id),
            "imdbUrl": self.get_imdb_url(movie_id),
            "tmdbUrl": self.get_tmdb_url(movie_id),
        }

    def get_external_links(self, movie_ids: Iterable[int]) -> List[Dict[str, Any]]:
        """
        Return IMDb and TMDB links for a list of movieIds.
        """
        result = []

        for movie_id in movie_ids:
            result.append({
                "movieId": int(movie_id),
                "imdbId": self.get_imdb_id(movie_id),
                "tmdbId": self.get_tmdb_id(movie_id),
                "imdbUrl": self.get_imdb_url(movie_id),
                "tmdbUrl": self.get_tmdb_url(movie_id),
            })

        return result