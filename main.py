import pandas as pd
import numpy as np
from datetime import datetime
from fastapi import FastAPI

import uvicorn

from sklearn.metrics.pairwise        import cosine_similarity
from sklearn.utils.extmath           import randomized_svd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise        import linear_kernel


app = FastAPI()

df = pd.read_csv('final.csv',sep = ',')
#FUNCION 1
@app.get("/score_titulo/{titulo_de_la_filmación}")
def score_titulo(titulo_de_la_filmación):
    vote_count = df.loc[df['title'] == titulo_de_la_filmación , 'vote_count'].values[0]
    score = df.loc[df['title'] == titulo_de_la_filmación, 'popularity'].values[0]
    year = df.loc[df['title'] == titulo_de_la_filmación, 'year'].values[0]
    vote_average = df.loc[df['title'] == titulo_de_la_filmación, 'vote_average'].values[0]
    if vote_count > 2000:
        return 'La película ' + titulo_de_la_filmación + ' fue estrenada en el año ' + str(year) + '. La misma cuenta con un total de ' + str(vote_count) + ' valoraciones, con un promedio de ' + str(vote_average)
    else:
        return 'La película que busca no cumple con la condición de más de 2000 votos, por ende no se devolverá ningún valor.'
#FUNCION 2
@app.get("/get_actor/{nombre_actor}")
def get_actor(nombre_actor):
    actor_rows = df[df['cast_names'].str.contains(nombre_actor)]
    numero = len(actor_rows)
    actor_revenue = df[df['cast_names'].str.contains(nombre_actor)]['revenue'].sum()
    promedio = (actor_revenue/numero)
    return ' El actor '+ nombre_actor + ' ha participado de ' + str(numero) + ' cantidad de filmaciones, el mismo ha conseguido un retorno de ' + str(actor_revenue) +' con un promedio de '+ str(promedio) + 'por filmación'
get_actor('Tom Hanks')
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
        print('La película', info, 'fue estrenada en el año.', year, 'La misma cuenta con un total de', vote_count,'valoraciones, con un promedio de', vote_average)
    else:
        print('la pelicula que busca no cumple con la condicion de mas de 2000 votos por ende no se devolvera ningun valor') 
    print('el año fue :', year, 'y la puntuacion fue', score)
#FUNCION 5
@app.get("/extract_month/{date_string}")
def extract_month(date_string):
    if pd.isna(date_string):
        return None
    try:
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        return date_object.month
    except ValueError: 
        return None
def extract_day(date_string):
    if pd.isna(date_string):
        return None
    try:
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        return date_object.weekday() + 1
    except ValueError: 
        return None

meses = {
    'enero': 1,
    'febrero': 2,
    'marzo': 3,
    'abril': 4,
    'mayo': 5,
    'junio': 6,
    'julio': 7,
    'agosto':8,
    'septiembre': 9,
    'octubre': 10,
    'noviembre': 11,
    'diciembre': 12
}
dias = {
    'lunes': 1,
    'martes': 2,
    'miércoles': 3,
    'jueves': 4,
    'viernes': 5,
    'sábado': 6,
    'sabado' : 6,
    'domingo': 7
}

info = date_string.lower()
if info in meses:
    mes = meses[info]   
else:
    print('El mes ingresado no es válido.')

df['month'] = df['release_date'].apply(extract_month)
df['day'] = df['release_date'].apply(extract_day)

month = df.loc[df['month'] == mes, 'month'].count()
day = df.loc[df['day'] == dia, 'day'].shape[0]
print(month)
#FUNCION 6
@app.get("/extract_day/{date_string}")
def extract_day(date_string):
    if pd.isna(date_string):
        return None
    try:
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        return date_object.month
    except ValueError: 
        return None
def extract_day(date_string):
    if pd.isna(date_string):
        return None
    try:
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        return date_object.weekday() + 1
    except ValueError: 
        return None

meses = {
    'enero': 1,
    'febrero': 2,
    'marzo': 3,
    'abril': 4,
    'mayo': 5,
    'junio': 6,
    'julio': 7,
    'agosto':8,
    'septiembre': 9,
    'octubre': 10,
    'noviembre': 11,
    'diciembre': 12
}
dias = {
    'lunes': 1,
    'martes': 2,
    'miércoles': 3,
    'jueves': 4,
    'viernes': 5,
    'sábado': 6,
    'sabado' : 6,
    'domingo': 7
}

info2 = date_string.lower()
if info2 in dias:
    dia = dias[info2]
else:
    print('El dia ingresado no es válido.')   


df['month'] = df['release_date'].apply(extract_month)
df['day'] = df['release_date'].apply(extract_day)

month = df.loc[df['month'] == mes, 'month'].count()
day = df.loc[df['day'] == dia, 'day'].shape[0]
print(day)
