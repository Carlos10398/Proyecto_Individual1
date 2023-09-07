                                                    # Proyecto_Individual 1 - Carlos Vargas
<p align="center">
  <img src="https://github.com/Carlos10398/Proyecto_Individual1/assets/75910244/e0c9690a-5239-46e2-b2d1-254d5137e423" alt="image">
</p>PROYECTO INDIVIDUAL Nº1
Machine Learning Operations (MLOps)
Henry's Labs
Por Carlos Vargas Trujillo 
ESTRUCTURA DEL PROYECTO ⚪
Los principales archivos desarrollados (que en el apartado siguiente se describirán en forma detallada y precisa su contenido, son:

ETL.ipynb
EDA.ipynb
APIS.ipynb
main.py
DESARROLLO DE LA SOLUCIÓN (PROYECTO) ⚪
1. Etapa del proceso ETL ➡️
Cargamos el archivos csv con la libereria pandas.

Luego hacemos todo el trabajo ETL(Extract,Transform,Load)

Pasamos los valores nulos o vacios de 'revenue' con 0 y igualmente lo hacemos con la columna 'budget'.

Reordenamos el orden de fecha como nos piden al formato '%Y-%m-%d'.

Separamos el año a una nueva columna que la llamaremos release_year.

Desanidamos por el valor que queremos necesarios de las columnas 'genres', 'belongs_to_collection', 'production_companies' 'production_countries', 'spoken_languages'

En una nueva columna que la llamaremos return sacar el resultado de la division entre las columnas revenue y budget.

Eliminamos las columnas que no serán utilizadas, video,imdb_id,adult,original_title,vote_count,poster_path y homepage.

En una nueva columna tengo que sacar el nombre del mes que tengo en la columna release_date, que lo pondremos en la columna month y igualmente hacemos con los dias de la semana que la pondremos en la columna que llamaremos day.

En la columna 'day' tengo miércoles y sábado con tildes, le quitaremos las tildes para que nos pueda funcionar.

En la columna de belongs_to_collection lo pasaremos a todo con minusculas con lower.

Y por ultimo lo exportamos para hacer las APIS.

3. Etapa de desarrollo API ➡️
def peliculas_mes(mes): '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes (nombre del mes, en str, ejemplo 'enero') historicamente''' return {'mes':mes, 'cantidad':respuesta}

def peliculas_dia(dia): '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia (de la semana, en str, ejemplo 'lunes') historicamente''' return {'dia':dia, 'cantidad':respuesta}

def franquicia(franquicia): '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio''' return {'franquicia':franquicia, 'cantidad':respuesta, 'ganancia_total':respuesta, 'ganancia_promedio':respuesta}

def peliculas_pais(pais): '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo''' return {'pais':pais, 'cantidad':respuesta}

def productoras(productora): '''Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron''' return {'productora':productora, 'ganancia_total':respuesta, 'cantidad':respuesta}

def retorno(pelicula): '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo''' return {'pelicula':pelicula, 'inversion':respuesta, 'ganacia':respuesta,'retorno':respuesta, 'anio':respuesta}

3. Etapa del proceso EDA ➡️
4. 
Ya con la data limpia, se hace si existen outliers con un boxplot.

Analizar cuantos valores nulos hay por cada columna, lo visualizamos con un gráfico que elaboré

Vemos si existe alguna correlación. . Se aprecia el Top 10 años con mas popularidad, igualmente con Películas con mayor ganancia.

La relacion entre revenue y budget con un scatter.

6. Etapa del Sistema de Recomendación ➡️
   
. def recomendacion('titulo'): '''Ingresas un nombre de pelicula y te recomienda las similares en una lista de 5 valores''' return {'lista recomendada': respuesta}

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
