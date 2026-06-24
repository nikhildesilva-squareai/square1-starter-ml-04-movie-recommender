"""
Collaborative-filtering model + recommendation.
Start with item-based kNN on cosine similarity, then try matrix factorisation.
Tests define the contract for top_n.
"""
from __future__ import annotations


def item_similarity(matrix):
    """Compute the item-item similarity matrix (e.g. cosine) from build_matrix.

    Centre / mean-adjust ratings first so popular-but-average items don't
    dominate. Return a movie x movie similarity structure.
    """
    raise NotImplementedError("Implement item_similarity")


def predict(matrix, similarity, user_id, movie_id) -> float:
    """Predict `user_id`'s rating for `movie_id` from neighbour ratings.

    Use the user's already-rated movies weighted by their similarity to
    `movie_id`. Return a float in roughly 1..5.
    """
    raise NotImplementedError("Implement predict")


def top_n(matrix, similarity, user_id, n: int = 10) -> list:
    """Return the top-`n` recommended movie ids for `user_id`.

    TODO:
      - score every movie the user has NOT already rated
      - exclude movies the user has already rated (never re-recommend)
      - return the `n` highest-scoring movie ids, best first
    """
    raise NotImplementedError("Implement top_n")
