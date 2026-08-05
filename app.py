import pickle
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI

vectorizer=pickle.load(open('vectorizer.pkl','rb'))
X=pickle.load(open('X.pkl','rb'))
indices=pickle.load(open('indices.pkl','rb'))
df=pickle.load(open('df.pickle','rb'))

app=FastAPI()

@app.get("/recommend/{movie}")
def recommend(movie:str, n:int=5):
    if movie not in df['Movie Name'].values:
        return {"recommendations":['Movie not found in our Data!!']}
    else:
        idx=indices[movie]
        sim_score=cosine_similarity(X[idx],X).flatten()
        sim_score[idx] = -1
        sim=sim_score.argsort()[::-1][1:n+1]
        return {"recommendations":df['Movie Name'].iloc[sim].tolist()}