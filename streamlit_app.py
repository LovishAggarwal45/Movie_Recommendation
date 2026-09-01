import pickle
import streamlit as st
import requests

df = pickle.load(open('df.pickle', 'rb'))
movie_list = df["Movie Name"].tolist()

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed",
)

API = "https://movie-recommendation-96j4.onrender.com/recommend"

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        #MainMenu, footer, header {visibility: hidden;}

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 760px;
        }

        .app-header {
            text-align: center;
            padding: 2.6rem 1.4rem 2.3rem 1.4rem;
            background: linear-gradient(135deg, #1a0b2e 0%, #3d1e4f 45%, #6b2b5c 100%);
            border-radius: 18px;
            margin-bottom: 1.8rem;
            box-shadow: 0 10px 28px rgba(26, 11, 46, 0.35);
            position: relative;
            overflow: hidden;
        }
        .app-header::before {
            content: "";
            position: absolute;
            top: -70px;
            left: -70px;
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(255, 200, 87, 0.14) 0%, rgba(255,255,255,0) 70%);
        }
        .app-header::after {
            content: "";
            position: absolute;
            bottom: -80px;
            right: -80px;
            width: 220px;
            height: 220px;
            background: radial-gradient(circle, rgba(255, 87, 140, 0.13) 0%, rgba(255,255,255,0) 70%);
        }
        .app-header .eyebrow {
            display: inline-block;
            color: #f6c667;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            margin-bottom: 0.7rem;
        }
        .app-header h1 {
            font-family: 'Playfair Display', serif;
            color: #ffffff;
            font-size: 2.5rem;
            font-weight: 800;
            margin: 0 0 0.5rem 0;
            letter-spacing: -0.01em;
            line-height: 1.15;
        }
        .app-header h1 span {
            background: linear-gradient(90deg, #f6c667 0%, #ff7eb3 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .app-header p {
            color: #d9c9e6;
            font-size: 0.95rem;
            margin: 0;
            font-weight: 400;
        }

        .section-title {
            font-size: 1rem;
            font-weight: 700;
            color: #2a1b3d;
            margin: 1.5rem 0 0.7rem 0;
            padding-bottom: 0.4rem;
            border-bottom: 2px solid #f0e9f5;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 14px !important;
            border: 1px solid #ece3f2 !important;
            padding: 0.4rem 0.2rem !important;
            background: #ffffff;
        }

        div.stButton > button {
            border-radius: 10px;
            font-weight: 700;
            font-size: 0.95rem;
            padding: 0.68rem 0;
            background: linear-gradient(135deg, #6b2b5c 0%, #ab3d6b 100%);
            border: none;
            color: #ffffff;
            transition: all 0.15s ease-in-out;
        }
        div.stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 16px rgba(107, 43, 92, 0.35);
        }

        .rec-card {
            display: flex;
            align-items: center;
            gap: 0.9rem;
            padding: 0.85rem 1.1rem;
            border-radius: 12px;
            background: linear-gradient(135deg, #fdf9f2 0%, #fbeee8 100%);
            border: 1px solid #f2e2d8;
            margin-bottom: 0.55rem;
        }
        .rec-rank {
            font-family: 'Playfair Display', serif;
            font-size: 1.3rem;
            font-weight: 800;
            color: #ab3d6b;
            min-width: 32px;
        }
        .rec-name {
            font-size: 0.95rem;
            font-weight: 600;
            color: #2a1b3d;
        }

        .empty-state {
            text-align: center;
            padding: 1.6rem 1rem;
            color: #8a7d93;
            font-size: 0.9rem;
            background: #faf7fb;
            border-radius: 12px;
            border: 1px dashed #e4d9ea;
        }

        .app-footer {
            text-align: center;
            color: #a89bb0;
            font-size: 0.78rem;
            margin-top: 2.2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="app-header">
        <span class="eyebrow">Cinema · Personalized Picks</span>
        <h1>🎬 Bolly<span>wood</span> Recommender</h1>
        <p>Find your next favourite film, tailored to what you already love</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-title">🔍 Search</div>', unsafe_allow_html=True)

movie = st.text_input("Search a Bollywood movie", placeholder="e.g. Dilwale")

suggestions = []
selected_movie = ""
data = {}

if movie:
    suggestions = [m for m in movie_list if movie.lower() in m.lower()][:5]

    if suggestions:
        selected_movie = st.selectbox("Matching titles", suggestions)
    else:
        st.markdown(
            '<div class="empty-state">🎞️ No matching movie found. Try a different title.</div>',
            unsafe_allow_html=True,
        )

st.markdown('<div class="section-title">⚙️ Preferences</div>', unsafe_allow_html=True)

n = st.slider("Number of recommendations", min_value=1, max_value=10, value=5)

st.write("")

if st.button("✨ Get Recommendations", type="primary", use_container_width=True):
    movie_searched = selected_movie if selected_movie != "" else movie

    if not movie_searched:
        st.warning("Please search and select a movie first.")
    else:
        with st.spinner("🎥 Curating recommendations for you..."):
            response = requests.get(f"{API}/{movie_searched}?n={n}")

            if response.status_code == 200:
                data = response.json()
            else:
                st.error("Something went wrong while fetching recommendations. Please try again.")

if "recommendations" in data and data["recommendations"]:
    st.markdown('<div class="section-title">🎥 Recommended For You</div>', unsafe_allow_html=True)
    for i, m in enumerate(data["recommendations"], start=1):
        st.markdown(
            f"""
            <div class="rec-card">
                <div class="rec-rank">{i:02d}</div>
                <div class="rec-name">{m}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="app-footer">
        Bollywood Movie Recommendation System &nbsp;•&nbsp; Built by Lovish Aggarwal &nbsp;•&nbsp; B.Tech CSE (AI &amp; ML)
    </div>
    """,
    unsafe_allow_html=True,
)