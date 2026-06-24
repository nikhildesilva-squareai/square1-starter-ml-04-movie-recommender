# Movie Recommendation Engine — Square 1 AI starter

**Part of [Square 1 AI](https://square1-tutor.vercel.app) · Machine Learning · Project 4.**

✅ **Data included.** The dataset is committed in [`dataset/`](dataset/) and is the **same standardized dataset every learner uses** — so results are comparable. It is 100% synthetic and Square 1-owned (no third-party or personal data). You can also download it as a single file from the project page on Square 1.

To run the commands below, copy the files into `data/` (`mkdir -p data && cp -r dataset/* data/`) or point the commands straight at `dataset/`.

MIT licensed — fork it, build on it, put it in your portfolio.

---

# Movie Recommendation Engine — starter

Starter for Square 1 AI **Machine Learning · Project 4**. Build a collaborative-filtering recommender and serve top-N picks behind a Flask API.

## Setup
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Get the data
Download `ratings.csv` and `movies.csv` from your project page (Resources → Dataset) into `data/`.

## Your task
Three tests define the contract — they fail until you implement the stubs in `recommender/data.py` and `recommender/model.py`:
```bash
pytest -q
python app.py            # serves the API, then: GET /recommendations/1?n=10
```
Pipeline: `load_ratings` → `clean_ratings` (drop out-of-range, de-dupe `(user,movie)` keeping the latest) → `build_matrix` (user × item) → fit a CF model (`item_similarity`) → `predict` / `top_n` (n unseen movie ids). Evaluate on a held-out slice: **RMSE vs a global-mean baseline** and **top-N relevance vs a popularity baseline** — beat both. Then wire `top_n` into the Flask endpoint.

Keep the matrix sparse/vectorised (no per-pair Python loops). Full brief, rubric, and references are on your Square 1 project page. MIT licensed.
