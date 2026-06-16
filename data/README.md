# Data

This directory is used to store the MovieLens dataset files required to run the project locally.

The dataset used in this project is:

**MovieLens Latest Small Dataset**  
Source: GroupLens Research  
Download page: https://grouplens.org/datasets/movielens/latest/

## Required Files

After downloading and extracting the dataset, place the following files inside this directory:

```text
data/
├── links.csv
├── movies.csv
├── ratings.csv
└── tags.csv
```

## Dataset Description

The MovieLens Latest Small dataset contains movie ratings and tags collected from the MovieLens recommendation platform.

The main files used in this project are:

| File | Description |
|---|---|
| `movies.csv` | Movie identifiers, titles, and genres. |
| `ratings.csv` | User ratings for movies, including rating values and timestamps. |
| `tags.csv` | User-generated tags assigned to movies. |
| `links.csv` | External identifiers linking MovieLens movies to IMDb and TMDB. |

## Why the CSV Files Are Not Included

The CSV files are not committed to this repository.

They are excluded through `.gitignore` because:

- the dataset belongs to GroupLens/MovieLens;
- the data should be downloaded from the official source;
- the repository should remain lightweight;
- users should be able to reproduce the project with the original dataset.

## How to Download the Data

1. Go to the official MovieLens dataset page:

   https://grouplens.org/datasets/movielens/latest/

2. Download:

   ```text
   ml-latest-small.zip
   ```

3. Extract the archive.

4. Copy these files into the `data/` directory:

   ```text
   links.csv
   movies.csv
   ratings.csv
   tags.csv
   ```

## Expected Local Structure

After adding the dataset files, the local project structure should look like this:

```text
movielens-oop-analysis/
├── data/
│   ├── README.md
│   ├── links.csv
│   ├── movies.csv
│   ├── ratings.csv
│   └── tags.csv
├── notebooks/
├── src/
├── tests/
└── README.md
```

## Notes

The project code and notebook expect the dataset files to be located directly inside the `data/` directory.

Example:

```python
from pathlib import Path

DATA_DIR = Path("data")

movies_path = DATA_DIR / "movies.csv"
ratings_path = DATA_DIR / "ratings.csv"
tags_path = DATA_DIR / "tags.csv"
links_path = DATA_DIR / "links.csv"
```

## Dataset License and Citation

The MovieLens dataset is provided by GroupLens Research at the University of Minnesota.

If you use this dataset in research or publications, cite:

> F. Maxwell Harper and Joseph A. Konstan. 2015.  
> The MovieLens Datasets: History and Context.  
> ACM Transactions on Interactive Intelligent Systems, 5(4), Article 19.  
> https://doi.org/10.1145/2827872

This repository provides code and documentation for educational and portfolio purposes. The dataset itself should be obtained from the official GroupLens source.