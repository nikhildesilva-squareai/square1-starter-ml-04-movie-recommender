"""Contract tests — fail against the starter stubs; make them pass.

Tiny inline ratings, fully offline (no network, no big CSV).
"""
import pandas as pd

from recommender import clean_ratings, build_matrix, item_similarity, top_n


def _ratings() -> pd.DataFrame:
    """A tiny ratings frame with one duplicate and one out-of-range row.

    Users 1 & 2 both love movies 10 & 20 (so they're similar); user 1 has not
    seen movie 30, which user 2 rated highly — a clean top-N target for user 1.
    Row (user 1, movie 10) appears twice: the LATER timestamp rating (5) wins.
    Row (user 1, movie 99, rating 7) is out of range and must be dropped.
    """
    return pd.DataFrame(
        [
            {"user_id": 1, "movie_id": 10, "rating": 3, "timestamp": "2024-01-01 00:00:00"},
            {"user_id": 1, "movie_id": 10, "rating": 5, "timestamp": "2024-06-01 00:00:00"},
            {"user_id": 1, "movie_id": 20, "rating": 5, "timestamp": "2024-02-01 00:00:00"},
            {"user_id": 1, "movie_id": 99, "rating": 7, "timestamp": "2024-03-01 00:00:00"},
            {"user_id": 2, "movie_id": 10, "rating": 5, "timestamp": "2024-01-05 00:00:00"},
            {"user_id": 2, "movie_id": 20, "rating": 4, "timestamp": "2024-02-05 00:00:00"},
            {"user_id": 2, "movie_id": 30, "rating": 5, "timestamp": "2024-03-05 00:00:00"},
        ]
    )


def test_clean_ratings_dedupes_latest_and_drops_out_of_range():
    out = clean_ratings(_ratings())
    # out-of-range rating (7) dropped; all remaining ratings are 1..5
    assert out["rating"].between(1, 5).all()
    # one row per (user, movie)
    assert not out.duplicated(subset=["user_id", "movie_id"]).any()
    # the later rating wins for the duplicated (user 1, movie 10)
    kept = out[(out["user_id"] == 1) & (out["movie_id"] == 10)]
    assert len(kept) == 1 and int(kept["rating"].iloc[0]) == 5


def test_build_matrix_is_user_by_item():
    matrix = build_matrix(clean_ratings(_ratings()))
    # accept a DataFrame (user x item) or a (matrix, users, items) tuple
    mat = matrix[0] if isinstance(matrix, tuple) else matrix
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]
    assert n_rows == 2   # users 1 and 2
    assert n_cols == 3   # movies 10, 20, 30


def test_top_n_returns_unseen_items():
    clean = clean_ratings(_ratings())
    matrix = build_matrix(clean)
    sim = item_similarity(matrix)
    recs = top_n(matrix, sim, user_id=1, n=1)
    assert len(recs) == 1
    # user 1 has already rated 10 and 20 -> must not be recommended
    assert 10 not in recs and 20 not in recs
    # the only unseen movie for user 1 is 30
    assert recs[0] == 30
