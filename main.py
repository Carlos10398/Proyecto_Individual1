import pandas as pd
import numpy  as np
from datetime import datetime
from fastapi import FastAPI

import uvicorn

from sklearn.metrics.pairwise        import cosine_similarity
from sklearn.utils.extmath           import randomized_svd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise        import linear_kernel


app = FastAPI()
### PRESENTACION:
### Creaoms consulta como presentacion con nuestro nombre
@app.get('/')
def presentacion():
    return 'Carlos_Vargas'

### IMPORTAMOS LOS DATOS
df = pd.read_csv('final.csv',sep = ',')
#FUNCION 1
@app.get("/score_titulo/{titulo_de_la_filmación}")
def peliculas_idioma(idioma:str):
    idioma_filtro = df[df['original_language'] == idioma]
    cantida_pelis =  idioma_filtro['original_language'].shape[0]
    return {'idioma:':idioma, 'cantidad peliculas:':cantida_pelis}
#FUNCION 2
@app.get("/peliculas_duracion/{pelicula}")
def peliculas_duracion(pelicula:str):
    filtro = df[df["title"] == pelicula]
    duracion = filtro["runtime"].values[0] if len(pelicula) > 0 else None
    year = filtro["year"].values[0] if len(pelicula) > 0 else None
    return {'PELICULA:':pelicula,'duracion en minutos:':duracion, 'año de estreno:':year } 
peliculas_duracion('Jumanji')
#FUNCION 3
@app.get("/get_director/{nombre_director}")
def get_director(nombre_director):
    director_films = df[df['directors'].notnull() & df['directors'].str.contains(nombre_director)]
    director_titles = df[df['directors'].notnull() & df['directors'].str.contains(nombre_director, na=False)]['title'].tolist()
    director_return = df[df['directors'].notnull() & df['directors'].str.contains(nombre_director, na=False)]['return'].sum()
    for movie in director_titles:
        revenue = df.loc[df['title'] == movie, 'revenue'].values[0]
        print('Las películas y sus ganancias:', movie, revenue)
    directors_count = len(director_films)
    print('El número de películas que ha dirigido es:', directors_count)
    print('Sus películas fueron:', director_titles)
    print('Sus ganancias totales son:', director_return)
#FUNCION 4
@app.get("/score_titulo/{titulo_de_la_filmación}")
def score_titulo(titulo_de_la_filmación):
    vote_count = df.loc[df['title'] == titulo_de_la_filmación , 'vote_count'].values[0]
    score = df.loc[df['title'] == titulo_de_la_filmación, 'popularity'].values[0]
    year = df.loc[df['title'] == titulo_de_la_filmación, 'year'].values[0]

    vote_average = df.loc[df['title'] == titulo_de_la_filmación, 'vote_average'].values[0]
    if vote_count > 2000:
        print('La película', titulo_de_la_filmación, 'fue estrenada en el año.', year, 'La misma cuenta con un total de', vote_count,'valoraciones, con un promedio de', vote_average)
    else:
        print('la pelicula que busca no cumple con la condicion de mas de 2000 votos por ende no se devolvera ningun valor') 
    print('el año fue :', year, 'y la puntuacion fue', score)
#FUNCION 5
@app.get("/extract_month/{date_string}")
def extract_day(date_string):
    dias = {
        'lunes': 1,
        'martes': 2,
        'miércoles': 3,
        'jueves': 4,
        'viernes': 5,
        'sábado': 6,
        'sabado': 6,
        'domingo': 7
    }
    if pd.isna(date_string):
        return None
    try:
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        return date_object.day
    except ValueError: 
        return None

df['day'] = df['release_date'].apply(extract_day)
dia = 1  # Establece el valor de 'dia' según tus necesidades
day = df.loc[df['day'] == dia, 'day'].shape[0]
print(day)
#FUNCION 6
@app.get("/extract_day/{date_string}")
def extract_day(date_string):
    dias = {
        'lunes': 1,
        'martes': 2,
        'miércoles': 3,
        'jueves': 4,
        'viernes': 5,
        'sábado': 6,
        'sabado': 6,
        'domingo': 7
    }
    if pd.isna(date_string):
        return None
    try:
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        return date_object.day
    except ValueError: 
        return None

df['day'] = df['release_date'].apply(extract_day)
dia = 1  # Establece el valor de 'dia' según tus necesidades
day = df.loc[df['day'] == dia, 'day'].shape[0]
print(day)
