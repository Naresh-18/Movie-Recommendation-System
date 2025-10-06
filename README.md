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

## 🧾 **Model Persistence:**

   - Store processed data for reuse:
     ```bash
     pickle.dump(new, open('movie_list.pkl', 'wb'))
     pickle.dump(similarity, open('similarity.pkl', 'wb'))
     ```
--- 

### 💻 Streamlit Web Application
- An interactive web interface built using Streamlit allows users to:
    - Select any movie from a dropdown list.
    - View top 5 similar movie recommendations with posters.

## 🎨 **UI Enhancements:**
  - Custom CSS styling for a dark theme.
  - Movie posters fetched via TMDB API.
  - Responsive horizontal layout for recommended movie grid.
    ```bash
    st.header('Movie Recommender System')
    selected_movie = st.selectbox("Type or select a movie", movie_list)
    if st.button('Show Recommendation'):
       recommend(selected_movie)
    ```
---

### 🧱 Tech Stack: 

| Component           | Technology       |
|---------------------|------------------|
| **Language**        | Python |
| **Framework**       | Streamlit |
| **Libraries**       | Pandas, NumPy, scikit-learn, Requests, Pickle |
| **Data Source**     | TMDB 5000 Dataset |
| **Vectorization**   | CountVectorizer |
| **Similarity Metric** | Cosine Similarity |
| **API**               | TMDB API for movie posters |

     
