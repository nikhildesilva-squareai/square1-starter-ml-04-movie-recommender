"""
Data loading + cleaning + matrix building for collaborative filtering.
Clean BEFORE you model: bad ratings and duplicates will poison similarities.
Tests define the contract.
"""
from __future__ import annotations
import pandas as pd


def load_ratings(path: str) -> pd.DataFrame:
    """Load the ratings CSV into a DataFrame.

    Columns: user_id (int), movie_id (int), rating (int), timestamp (parseable).
    """
    raise NotImplementedError("Implement load_ratings")


def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned ratings frame.

    TODO:
      - drop rows whose `rating` is outside the valid 1..5 range
      - de-duplicate on (`user_id`, `movie_id`), keeping the row with the
        LATEST `timestamp` (a user's most recent rating wins)
    The result has at most one rating per (user_id, movie_id), all in 1..5.
    """
    raise NotImplementedError("Implement clean_ratings")


def build_matrix(df: pd.DataFrame):
    """Build the user x item rating matrix from a cleaned ratings frame.

    TODO: return a structure indexed by user (rows) and movie (columns) whose
    values are ratings, with 0 / NaN where a user has not rated a movie. A
    pandas DataFrame (pivot) or a (matrix, user_index, item_index) tuple is
    fine — just be consistent with what your model code expects.
    """
    raise NotImplementedError("Implement build_matrix")
