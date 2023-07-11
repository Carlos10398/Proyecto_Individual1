# Proyecto_Individual1
# Proyecto personal nmro 1 del bootcamp SoyHenry
![image](https://github.com/Carlos10398/Proyecto_Individual1/assets/75910244/e0c9690a-5239-46e2-b2d1-254d5137e423)

 Operaciones de Aprendizaje Automático (MLOps)
Procedimiento - Definición del problema (Contexto y papel a desempeñar)
En este proyecto, llevaré a cabo un proceso de ETL (Extracción, Transformación y Carga), la creación de una API (Interfaz de Programación de Aplicaciones), EDA (Análisis Exploratorio de Datos) y concluiremos con un modelo de aprendizaje automático (ML) para la recomendación de películas.
 Contexto
¿Cómo llevarás tu modelo de recomendación, que produce buenas métricas, al mundo real? 
 El ciclo de vida de un proyecto de aprendizaje automático debe considerar desde el manejo y recopilación de datos (tareas de ingeniería de datos) hasta la formación y mantenimiento del modelo de ML a medida que llegan nuevos datos.
 Papel a desempeñar
Acabas de empezar a trabajar como Científico de Datos en una start-up que ofrece servicios de agregación de plataformas de streaming. Vas a crear tu primer modelo de ML que resuelve un problema de negocio: un sistema de recomendación que aún no ha sido implementado!
 Al revisar los datos, te das cuenta de que la madurez de los mismos es baja: los datos están anidados, sin transformar, y no existen procesos automatizados para la actualización de nuevas películas o series, entre otras cosas, lo que hace tu trabajo muy difícil.
 Tendrás que empezar desde cero, realizando un rápido trabajo de ingeniería de datos y tener un Producto Mínimo Viable (MVP) para el cierre del proyecto. Aunque la tarea parece abrumadora, al menos tienes una idea clara del camino a seguir. Así que superas tus miedos y te pones manos a la obra.
 ETL (Extracción, Transformación y Carga)
Descripción de mis Datos: Característica\Descripción
 adult: Indica si la película es clasificada como X, exclusiva para adultos.
belongs_to_collection: Un diccionario que muestra a qué franquicia o serie de películas pertenece la película.
budget: El presupuesto de la película, en dólares.
genres: Un diccionario que muestra todos los géneros asociados a la película.
homepage: La página web oficial de la película.
id: ID de la película.
imdb_id: ID de IMDB de la película.
original_language: Idioma original de la película.
original_title: Título original de la película.
overview: Breve resumen de la película.
popularity: Puntuación de popularidad de la película, asignada por TMDB (TheMoviesDataBase).
poster_path: URL del póster de la película.
production_companies: Lista de las compañías productoras asociadas a la película.
production_countries: Lista de los países donde se produjo la película.
release_date: Fecha de lanzamiento de la película.
revenue: Recaudación de la película, en dólares.
runtime: Duración de la película, en minutos.
spoken_languages: Lista de los idiomas que se hablan en la película.
status: Estado actual de la película (si fue anunciada, si ya se estrenó, etc).
tagline: Frase célebre asociada a la película.
title: Título de la película.
video: Indica si hay o no un tráiler en video disponible en TMDB.
vote_average: Puntuación promedio de las reseñas de la película.
vote_count: Número de votos recibidos por la película, en TMDB.
Transformaciones: Para este MVP no necesitas perfección, ¡necesitas rapidez! ⏩ Harás estas, y solo estas, transformaciones a los datos:
 Eliminar las columnas que no serán utilizadas, video, imdb_id, adult, original_title, poster_path y homepage.
 Los valores nulos de los campos revenue, budget deben ser rellenados con el número 0.
 Crear la columna con el retorno de inversión, llamada return con los campos revenue y budget, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.
 Los valores nulos del campo release date deben eliminarse. Si hay fechas, deben tener el formato AAAA-mm-dd, además deberán crear la columna release_year donde extraerán el año de la fecha de estreno.
 Algunos campos, como belongs_to_collection, production_companies y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán desanidarlos para poder y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos.
 encontraremos este proceso en el archivo Datos-ETL.ipynb
 API (Interfaz de Programación de Aplicaciones)
Desarrollo: Sugieres hacer disponibles los datos de la empresa utilizando el marco de trabajo FastAPI. Las consultas que sugieres son las siguientes:
 Deben crear 6 funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).
