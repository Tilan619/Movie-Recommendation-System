import pickle
import streamlit as st
import requests

def get_poster(id):


    #url = "https://api.themoviedb.org/3/movie/{}/images".format(id)
    url = "https://api.themoviedb.org/3/movie/{}?api_key=4936147469ba3fcd1b70372c13ee56ed".format(id)


    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = 'http://image.tmdb.org/t/p/w500/'+poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(sim[index])), reverse=True, key=lambda x: x[1])
    rec_names = []
    rec_posters = []
    for i in distances[1:6]:
        id = movies.iloc[i[0]].movie_id
        rec_posters.append((get_poster(id)))
        rec_names.append(movies.iloc[i[0]].title)
    return rec_names,rec_posters


st.header("Movies Recommendation System")

movies = pickle.load(open('movie_list.pickle','rb'))
sim = pickle.load(open('sim.pickle','rb'))

movie_list = movies['title'].values
movie=st.selectbox('Select a movie',movie_list)

if st.button('Show Recommendations'):
    movies_rec, posters = recommend(movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movies_rec[0])
        st.image(posters[0])
    with col2:
        st.text(movies_rec[1])
        st.image(posters[1])
    with col3:
        st.text(movies_rec[2])
        st.image(posters[2])

    with col4:
        st.text(movies_rec[3])
        st.image(posters[3])

    with col5:
        st.text(movies_rec[4])
        st.image(posters[4])
