"""
This module loads all 9 raw csv files into pandas DataFraame

The input is raw csv path

The output is 9 pandas DataFrame (Tables)
"""

import pandas as pd

def load_data_to_dataframe() -> pd.DataFrame:
    genome_scores = pd.read_csv("data/raw/genome_scores.csv")
    genome_tags = pd.read_csv("data/raw/genome_tags.csv")
    imdb_data = pd.read_csv("data/raw/imdb_data.csv")
    links = pd.read_csv("data/raw/links.csv")
    movies = pd.read_csv("data/raw/movies.csv")
    sample_submission = pd.read_csv("data/raw/sample_submission.csv")
    tags = pd.read_csv("data/raw/tags.csv")
    test = pd.read_csv("data/raw/test.csv")
    train = pd.read_csv("data/raw/train.csv")

    return genome_scores, genome_tags, imdb_data, links, movies, sample_submission, tags, test, train #type: ignore

genome_scores, genome_tags, imdb_data, links, movies, sample_submission, tags, test, train = load_data_to_dataframe()