# Project Overview

## Project Title

**MovieLens OOP Analysis**

## Summary

MovieLens OOP Analysis is a Python project for exploring and analyzing the MovieLens Latest Small dataset using an object-oriented programming approach.

The project provides reusable Python classes for working with movie metadata, user ratings, tags, and external movie identifiers. It also includes unit tests and a notebook-based analysis report.

This project was originally developed as part of a School 21 Russia programming assignment and later reorganized as a professional portfolio project with cleaner structure, documentation, and testing.

## Dataset

The project uses the **MovieLens Latest Small** dataset provided by GroupLens Research.

The dataset contains:

- movie metadata;
- user ratings;
- user-generated tags;
- links to external movie databases such as IMDb and TMDB.

The required files are:

```text
movies.csv
ratings.csv
tags.csv
links.csv
```

The dataset files are not included in this repository. They should be downloaded from the official GroupLens source and placed inside the `data/` directory.

## Main Objective

The main objective of this project is to build a clean Python toolkit that can analyze MovieLens data without relying on heavy external libraries in the core module.

The project focuses on:

- object-oriented design;
- CSV parsing;
- data aggregation;
- movie-level statistics;
- user-level statistics;
- tag analysis;
- external ID mapping;
- unit testing;
- reproducible notebook reporting.

## Core Components

### Movies

The `Movies` class analyzes `movies.csv`.

It supports:

- extracting release years from movie titles;
- calculating movie distribution by release year;
- calculating movie distribution by genre;
- finding movies with the highest number of genres;
- searching movie titles by regular expression;
- retrieving movie titles and genres by `movieId`.

### Ratings

The `Ratings` class analyzes `ratings.csv`.

It supports:

- grouping ratings by movie;
- grouping ratings by user;
- calculating rating distributions;
- extracting rating years from timestamps;
- finding top movies by number of ratings;
- finding top movies by average or median rating;
- finding controversial movies using rating variance;
- analyzing user rating behavior.

### Tags

The `Tags` class analyzes `tags.csv`.

It supports:

- finding tags with the highest number of words;
- finding longest tags;
- finding popular tags;
- finding tags containing a specific word;
- retrieving tags by movie or user.

### Links

The `Links` class analyzes `links.csv`.

It supports:

- mapping MovieLens IDs to IMDb IDs;
- mapping MovieLens IDs to TMDB IDs;
- generating IMDb URLs;
- generating TMDB URLs;
- joining external links with movie metadata.

## Technical Approach

The project uses a modular structure:

```text
src/
└── movielens_analysis.py
```

The main code is implemented in a single reusable Python module with four main classes:

```text
Movies
Ratings
Tags
Links
```

The core module uses only the Python standard library. This makes the project lightweight and easy to run in different environments.

The notebook and reports may use additional libraries such as `pandas` and `matplotlib` for presentation and visualization.

## Testing

The project includes unit tests located in:

```text
tests/test_movielens_analysis.py
```

The tests cover:

- movie release year extraction;
- genre distribution;
- tag analysis;
- rating distribution;
- top-rated movie calculations;
- controversial movie detection;
- user-level rating analysis;
- IMDb and TMDB link generation;
- error handling.

Tests can be executed with:

```bash
python -m pytest tests -v
```

## Project Value

This project demonstrates practical Python development skills beyond simple notebook analysis.

It shows the ability to:

- design reusable classes;
- work with structured data;
- implement clean data-processing logic;
- write tests;
- document a project clearly;
- organize a portfolio-ready repository.

## Skills Demonstrated

- Python
- Object-Oriented Programming
- CSV Parsing
- Data Analysis
- Unit Testing
- Pytest
- Technical Documentation
- Project Structuring
- Notebook Reporting
- GitHub Portfolio Preparation

## Portfolio Context

This project complements more advanced machine learning projects by showing strong fundamentals in Python software design and data analysis.

It is especially relevant for roles such as:

- Python Developer
- Data Analyst
- Junior Data Scientist
- Machine Learning Intern
- Technical Writer with Python/Data focus