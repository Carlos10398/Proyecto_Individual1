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
#FUNCION 3
@app.get("/obtener_informacion_franquicia/{franquicia}")
def obtener_informacion_franquicia(franquicia):
    franquicia_df = df[df["name"].str.contains(franquicia, na=False)]
    cantidad_peliculas = len(franquicia_df)
    ganancia_total = franquicia_df["revenue"].sum()
    ganancia_promedio = franquicia_df["revenue"].mean()
    return f"La franquicia {franquicia} posee {cantidad_peliculas} películas, una ganancia total de {ganancia_total} y una ganancia promedio de {ganancia_promedio}."
#FUNCION 4
@app.get("/peliculas_pais/{Pais}")
def peliculas_pais( Pais: str ):
    pais = df[df["production_countries"].str.contains(Pais, na=False)]
    cantidad_peliculas = len(pais)
    return f"Se produjeron ", {cantidad_peliculas},  "películas en el país ", {Pais}
#FUNCION 5
@app.get("/productora_exitosa/{productora}")
def productora_exitosa(productora:str):
    productora_filtro = df[df['production_companies'] == productora]
    cantidad = productora_filtro['revenue'].sum()
    cantidad_peliculas = productora_filtro['production_companies'].shape[0]
    return{'productora:':productora, 'ganancias totales:':cantidad, 'cantidad de peliculas generadas:':cantidad_peliculas}
productora_exitosa('Universal Pictures')
#FUNCION 6
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
@app.get("/recomendacion/{titulo}")
def recomendacion(titulo: str):
    idx = muestra_aleatoria[muestra_aleatoria['title'] == titulo].index[0] # Buscamos el indice titulo en nuestro datasets

    sim_cosine = list(enumerate(cosine_similarity[idx])) # Accedemos a la fila 'idx' de la matriz 'simitulud coseno' enumeramos filas, creamos lista de 
                                                             #tuplas, donde cada tupla contiene el indice y similitud coseno de la pelicula
    

    sim_scores = sorted(sim_cosine, key=lambda x: x[1], reverse=True) # Ordenamos la lista de tuplas en funcion de la similitud coseno de manera descendente,
                                                                         #guardamos resultados en variable sim_scores
    

    similar_indices = [i for i, _ in sim_scores[1:6]] # Creamos lista de las 5 mejores primeras peliculas

    similar_movies = muestra_aleatoria['title'].iloc[similar_indices].values.tolist() # Seleccionamos los titulos segun los indices y los pasamos a una lista
    
    return similar_movies #Retornamos la lista
