# 🎬 Content-Based Movie Recommendation System

This project is an end-to-end Machine Learning web application that recommends movies based on textual metadata. It was built as part of an AI/ML Engineering workflow, taking raw data through preprocessing, vectorization, similarity computation, and final deployment.

## 🚀 Features
* **Content-Based Filtering:** Recommends movies using plot overviews, genres, and keywords.
* **Smart Text Processing:** Utilizes regular expressions and NLTK for text cleaning and stopword removal.
* **TF-IDF Vectorization:** Extracts meaningful features from natural language data.
* **Instant Recommendations:** Powered by a pre-computed Cosine Similarity matrix for lightning-fast results.
* **Interactive UI:** A clean, user-friendly web interface built with Streamlit.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas
* **Machine Learning:** Scikit-Learn (`TfidfVectorizer`, `cosine_similarity`)
* **Natural Language Processing:** NLTK
* **Frontend/UI:** Streamlit

## 📂 Project Structure
```text
├── app.py                   # The main Streamlit web application script
├── requirements.txt         # List of required Python libraries for deployment
├── movie_list.pkl           # Serialized Pandas DataFrame containing movie titles
├── similarity_matrix.pkl    # Serialized 16-bit Float Cosine Similarity Matrix
└── README.md                # Project documentation
