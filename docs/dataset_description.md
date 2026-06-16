# Dataset Description

## Dataset Name

**MovieLens Latest Small Dataset**

## Source

The dataset used in this project is provided by **GroupLens Research** at the University of Minnesota.

Official download page:

```text
https://grouplens.org/datasets/movielens/latest/
```

The specific dataset version used is:

```text
ml-latest-small
```

## Overview

MovieLens is a movie recommendation platform that collects user ratings and tags for movies.

The `ml-latest-small` dataset contains a compact version of MovieLens data designed for development, education, and experimentation.

It includes:

- movie metadata;
- user ratings;
- user-generated tags;
- links to external movie databases.

## Files Used in This Project

This project uses four CSV files:

```text
movies.csv
ratings.csv
tags.csv
links.csv
```

These files should be placed inside the local `data/` directory.

## File: movies.csv

The `movies.csv` file contains movie metadata.

Expected columns:

```text
movieId,title,genres
```

### Columns

| Column | Description |
|---|---|
| `movieId` | Unique MovieLens identifier for each movie. |
| `title` | Movie title, usually including the release year in parentheses. |
| `genres` | Pipe-separated list of genres assigned to the movie. |

### Example

```text
1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
```

### Used For

This project uses `movies.csv` to:

- extract movie release years;
- calculate movie distribution by release year;
- calculate genre frequencies;
- identify movies with multiple genres;
- map `movieId` values to movie titles;
- search movie titles.

## File: ratings.csv

The `ratings.csv` file contains user ratings.

Expected columns:

```text
userId,movieId,rating,timestamp
```

### Columns

| Column | Description |
|---|---|
| `userId` | Anonymous user identifier. |
| `movieId` | MovieLens movie identifier. |
| `rating` | Rating value given by the user. |
| `timestamp` | Unix timestamp representing when the rating was created. |

### Rating Scale

Ratings are given on a 5-star scale with half-star increments.

Examples:

```text
0.5
1.0
2.5
4.0
5.0
```

### Used For

This project uses `ratings.csv` to:

- analyze rating distribution;
- extract rating years from timestamps;
- find movies with the highest number of ratings;
- calculate average and median movie ratings;
- detect controversial movies using rating variance;
- analyze user rating behavior;
- identify users with high rating variance.

## File: tags.csv

The `tags.csv` file contains user-generated movie tags.

Expected columns:

```text
userId,movieId,tag,timestamp
```

### Columns

| Column | Description |
|---|---|
| `userId` | Anonymous user identifier. |
| `movieId` | MovieLens movie identifier. |
| `tag` | Free-text tag assigned by the user. |
| `timestamp` | Unix timestamp representing when the tag was created. |

### Used For

This project uses `tags.csv` to:

- identify the most popular tags;
- find the longest tags;
- find tags with the highest number of words;
- search tags containing a specific word;
- retrieve tags by movie;
- retrieve tags by user.

## File: links.csv

The `links.csv` file contains external movie identifiers.

Expected columns:

```text
movieId,imdbId,tmdbId
```

### Columns

| Column | Description |
|---|---|
| `movieId` | MovieLens movie identifier. |
| `imdbId` | IMDb movie identifier. |
| `tmdbId` | TMDB movie identifier. |

### Used For

This project uses `links.csv` to:

- map MovieLens IDs to IMDb IDs;
- map MovieLens IDs to TMDB IDs;
- generate IMDb URLs;
- generate TMDB URLs;
- join movie metadata with external links.

## Expected Local Data Structure

After downloading and extracting the dataset, the project expects this structure:

```text
movielens-oop-analysis/
├── data/
│   ├── README.md
│   ├── links.csv
│   ├── movies.csv
│   ├── ratings.csv
│   └── tags.csv
```

## Why the Data Is Not Included in the Repository

The CSV files are not committed to this repository because:

- they belong to GroupLens/MovieLens;
- users should download the dataset from the official source;
- this keeps the repository lightweight;
- this avoids unnecessary duplication of public data;
- this makes the project easier to maintain.

The `.gitignore` file excludes CSV files from the `data/` directory.

## Reproducibility

To reproduce the project:

1. Download `ml-latest-small.zip` from the official MovieLens dataset page.
2. Extract the archive.
3. Copy the following files into `data/`:

```text
links.csv
movies.csv
ratings.csv
tags.csv
```

4. Install the project dependencies:

```bash
pip install -r requirements.txt
```

5. Run the tests:

```bash
python -m pytest tests -v
```

6. Open the notebook:

```text
notebooks/movielens_report.ipynb
```

## Citation

If this dataset is used in research or publications, cite:

> F. Maxwell Harper and Joseph A. Konstan. 2015.  
> The MovieLens Datasets: History and Context.  
> ACM Transactions on Interactive Intelligent Systems, 5(4), Article 19.  
> https://doi.org/10.1145/2827872

## Notes

This repository provides code, documentation, and analysis structure for educational and portfolio purposes.

The dataset itself remains the property of its original providers and should be obtained from the official GroupLens source.