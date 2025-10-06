# Movie-Recommendation-System
### 🧠 Overview:
- A content-based movie recommender using the TMDB 5000 dataset. It extracts features like genres, cast, crew, and keywords, builds similarity using CountVectorizer and cosine similarity, and provides interactive movie recommendations via Streamlit with poster images.

---

### 📂 Dataset:
- Two CSV files from The Movie Database (TMDB 5000) are used:
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`
They are merged on the `title` column to create a unified dataset with comprehensive movie metadata.
