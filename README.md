🎬 Movie Recommendation System

An end-to-end Movie Recommendation System built using Machine Learning and Natural Language Processing (NLP).

The system analyzes movie information, calculates similarity between movies, and recommends movies based on the selected movie. The application is deployed using Streamlit with an interactive user interface.

🌐 Live Demo

🚀 "Try the Movie Recommendation System" (https://movie-recommendation-lovish-aggarwal.streamlit.app/)

✨ Features

- 🎬 Movie-based recommendations
- 🤖 Machine Learning-based recommendation system
- 🧠 NLP-based text feature processing
- 🔎 Similarity-based movie matching
- 🖥️ Interactive Streamlit interface
- 🌐 Live web deployment

🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLP
- Streamlit
- Pickle

🔄 How It Works

Movie Dataset
     ↓
Data Preprocessing
     ↓
Feature Extraction
     ↓
Text Vectorization
     ↓
Similarity Calculation
     ↓
Movie Recommendations
     ↓
Streamlit Web App

🧠 Recommendation Approach

The system uses movie-related information to create meaningful feature representations.

These features are processed using NLP techniques and transformed into numerical vectors. Similarity between movies is then calculated to identify movies that are most similar to the user's selected movie.

The system returns a list of recommended movies based on these similarity scores.

📂 Project Structure

<pre>
Movie_Recommendation/
├── .devcontainer/
├── .gitattributes
├── Data.csv
├── X.pkl
├── app.py
├── df.pickle
├── indices.pkl
├── movie_recommend.ipynb
├── requirements.txt
├── streamlit_app.py
├── vectorizer.pkl
└── README.md
</pre>📄 File Description

File| Description
"movie_recommend.ipynb"| Data analysis, preprocessing and recommendation model development
"Data.csv"| Movie dataset used for the project
"X.pkl"| Stored processed feature data
"df.pickle"| Stored processed movie DataFrame
"indices.pkl"| Stored movie index mappings
"vectorizer.pkl"| Saved text vectorizer
"app.py"| Application/backend logic
"streamlit_app.py"| Streamlit web application
"requirements.txt"| Required Python dependencies
".devcontainer/"| Development container configuration
".gitattributes"| Git configuration file

📊 Recommendation Pipeline

The recommendation pipeline consists of:

1. Loading and exploring the movie dataset
2. Cleaning and preprocessing the data
3. Combining relevant movie features
4. Applying NLP-based text vectorization
5. Calculating similarity between movie vectors
6. Creating a recommendation function
7. Integrating the recommendation system with Streamlit
8. Deploying the application

🎯 Project Objective

The goal of this project is to build a practical content-based movie recommendation system and demonstrate how Machine Learning and NLP can be integrated into a user-facing application.

Movie Data → NLP → Feature Vectors → Similarity → Recommendations → Web App

🚀 Future Improvements

- Add movie posters and additional movie information
- Improve recommendation quality with additional features
- Add user-based recommendations
- Add ratings and feedback
- Experiment with more advanced recommendation algorithms
- Improve UI and personalization

👨‍💻 Author

Lovish Aggarwal

B.Tech CSE (AI/ML) — UIET Kurukshetra

Interested in AI/ML, Generative AI, Deep Learning, Software Development, and building real-world AI applications.

---

⭐ If you found this project useful, consider giving the repository a star!
