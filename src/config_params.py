"""
This module entails SQL query in a single variable that creates 9 views from the 9 raw csv datasets

This query will be executed by DuckDB
"""


sql_query = """
CREATE OR REPLACE VIEW movies AS
    SELECT * FROM read_csv_auto('data/raw/movies.csv');

CREATE OR REPLACE VIEW genome_scores AS
    SELECT * FROM read_csv_auto('data/raw/genome_scores.csv');

CREATE OR REPLACE VIEW genome_tags AS
    SELECT * FROM read_csv_auto('data/raw/genome_tags.csv');

CREATE OR REPLACE VIEW imdb_data AS
    SELECT * FROM read_csv_auto('data/raw/imdb_data.csv');

CREATE OR REPLACE VIEW links AS
    SELECT * FROM read_csv_auto('data/raw/links.csv');

CREATE OR REPLACE VIEW sample_submission AS
    SELECT * FROM read_csv_auto('data/raw/sample_submission.csv');

CREATE OR REPLACE VIEW tags AS
    SELECT * FROM read_csv_auto('data/raw/tags.csv');

CREATE OR REPLACE VIEW test AS
    SELECT * FROM read_csv_auto('data/raw/test.csv');

CREATE OR REPLACE VIEW train AS
    SELECT * FROM read_csv_auto('data/raw/train.csv');
"""

