"""
Flask API for the recommender:  python app.py
Then:  GET /recommendations/<user_id>?n=10  ->  JSON list of recommended movies.

Wires the recommender/ functions together. Build the model once at startup,
then serve top-N per request. Implement the stubs in recommender/ first.
"""
from flask import Flask, jsonify, request

from recommender import load_ratings, clean_ratings, build_matrix, item_similarity, top_n

app = Flask(__name__)

# Build the model once at startup (cleaned ratings -> matrix -> similarity).
ratings = clean_ratings(load_ratings("data/ratings.csv"))
MATRIX = build_matrix(ratings)
SIMILARITY = item_similarity(MATRIX)


@app.get("/recommendations/<int:user_id>")
def recommendations(user_id: int):
    n = request.args.get("n", default=10, type=int)
    movie_ids = top_n(MATRIX, SIMILARITY, user_id, n=n)
    return jsonify({"user_id": user_id, "n": n, "recommendations": movie_ids})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
