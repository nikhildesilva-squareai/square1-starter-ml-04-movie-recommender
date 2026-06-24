"""Movie Recommendation Engine — Square 1 AI starter."""
from .data import load_ratings, clean_ratings, build_matrix
from .model import item_similarity, predict, top_n

__all__ = [
    "load_ratings",
    "clean_ratings",
    "build_matrix",
    "item_similarity",
    "predict",
    "top_n",
]
