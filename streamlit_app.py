<<<<<<< HEAD
import pickle
import streamlit as st
import requests

df=pickle.load(open('df.pickle','rb'))
movie_list = df["Movie Name"].tolist()

st.title("🎬 Bollywood Movie Recommendation System")
st.caption("Created by Lovish Aggarwal ❤️")

movie = st.text_input("🔍 Search a Bollywood Movie")

suggestions=[]
selected_movie=""
data={}
movie_data={}

if movie:
    suggestions=[m for m in movie_list
        if movie.lower() in m.lower()
    ][:5] 

    if suggestions:
        st.write("### Suggestions:")
        selected_movie=st.selectbox("Select a movie:",suggestions)
    else:
        st.write("### Movie not found")

n = st.slider(label="Select number of recommendations:",min_value=1,max_value=10,value=5)

if st.button("Recommend"):
    movie_searched=selected_movie if selected_movie!="" else movie
    response = requests.get(f"https://movie-recommendation-96j4.onrender.com/recommend/{movie_searched}?n={n}")

    if response.status_code == 200:
        data = response.json()

        st.subheader("🎥 Recommended Movies:")

if "recommendations" in data:
    for i, m in enumerate(data["recommendations"],start=1):
        st.write(f"{i}. {m}")

st.divider()
st.caption("🎬 Bollywood Movie Recommendation System | Created by Lovish Aggarwal ❤️ | B.Tech CSE(AI ML)")
=======
import pickle
import streamlit as st
import requests

df=pickle.load(open('df.pickle','rb'))
movie_list = df["Movie Name"].tolist()

st.title("🎬 Bollywood Movie Recommendation System")
st.caption("Created by Lovish Aggarwal ❤️")

movie = st.text_input("🔍 Search a Bollywood Movie")

suggestions=[]
selected_movie=""
data={}
movie_data={}

if movie:
    suggestions=[m for m in movie_list
        if movie.lower() in m.lower()
    ][:5] 

    if suggestions:
        st.write("### Suggestions:")
        selected_movie=st.selectbox("Select a movie:",suggestions)
    else:
        st.write("### Movie not found")

n = st.slider(label="Select number of recommendations:",min_value=1,max_value=10,value=5)

if st.button("Recommend"):
    movie_searched=selected_movie if selected_movie!="" else movie
    response = requests.get(f"https://movie-recommendation-96j4.onrender.com/recommend/{movie_searched}?n={n}")

    if response.status_code == 200:
        data = response.json()

        st.subheader("🎥 Recommended Movies:")

if "recommendations" in data:
    for i, m in enumerate(data["recommendations"],start=1):
        st.write(f"{i}. {m}")

st.divider()
st.caption("🎬 Bollywood Movie Recommendation System | Created by Lovish Aggarwal ❤️ | B.Tech CSE(AI ML)")
>>>>>>> 94d9ab3daae1e60a5c27f085d00b1b9aee3c382c
