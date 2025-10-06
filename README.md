# Movie-Recommendation-System
### 🧠 Overview:
- A content-based movie recommender using the TMDB 5000 dataset. It extracts features like genres, cast, crew, and keywords, builds similarity using CountVectorizer and cosine similarity, and provides interactive movie recommendations via Streamlit with poster images.

---

### 📂 Dataset:
- Two CSV files from The Movie Database (TMDB 5000) are used:
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`
They are merged on the `title` column to create a unified dataset with comprehensive movie metadata.

--- 

### ⚙️ Features & Workflow:
## 🧹 **Data Preprocessing:**

   - Merge movie and credits datasets.
   - Extract key fields: movie_id, title, overview, genres, keywords, cast, crew.
   - Parse complex JSON-like columns using ast.literal_eval.
   - Extract top 3 cast members and the director.
   - Combine text data into a single field called “tags”.
     
## 🔤 **Feature Vectorization:**

   - Convert movie tags into numerical vectors using:
     ```bash
     CountVectorizer(max_features=5000, stop_words='english')
     ```
   - Compute cosine similarity between all movie pairs.

## 🤖 **Recommendation Logic:**

   - When a movie is selected, retrieve its similarity scores.
   - Sort and recommend the top 5 most similar movies. 
     
