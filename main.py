import pandas as pd
df = pd.read_csv('final.csv',sep = ',')
info = input('ingrese el titulo de la pelicula')
vote_count = df.loc[df['title'] == info , 'vote_count'].values[0]
score = df.loc[df['title'] == info, 'popularity'].values[0]
year = df.loc[df['title'] == info, 'year'].values[0]
vote_average = df.loc[df['title'] == info, 'vote_average'].values[0]
if vote_count > 2000:
    print('La película', info, 'fue estrenada en el año.', year, 'La misma cuenta con un total de', vote_count,'valoraciones, con un promedio de', vote_average)
else:
    print('la pelicula que busca no cumple con la condicion de mas de 2000 votos por ende no se devolvera ningun valor') 
print('el año fue :', year, 'y la puntuacion fue', score)

info = input('Ingrese el nombre del actor: ')
actor_rows = df[df['cast_names'].str.contains(info)]
actor_revenue = df[df['cast_names'] == info].groupby('cast_names')['revenue'].sum()
movies_count = len(actor_rows)
print(movies_count)
print(actor_revenue)
print(actor_revenue/movies_count)

info = input('Ingrese el nombre del director: ')

director_films = df[df['directors'].str.contains(info)]
director_movies = df[df['cast_names'] == info]
director_titles = df[df['directors'].str.contains(info, na=False)]['title'].tolist()
director_return = df[df['directors'].str.contains(info, na=False)]['return'].sum()
for movie in director_titles:
    revenue = df.loc[df['title'] == movie, 'revenue'].values[0]
    print('las peliuclas y sus ganancias : ' , movie, revenue)
#movies_returns = director_titles
directors_count = len(director_films)
print('el numero de pelicual que a dirijido fue :', directors_count)
print('sus peliculas fueron ', director_titles)
print(' sus ganancias en total: ', director_return)


info = input('ingrese el titulo de la pelicula')
vote_count = df.loc[df['title'] == info , 'vote_count'].values[0]
score = df.loc[df['title'] == info, 'popularity'].values[0]
year = df.loc[df['title'] == info, 'year'].values[0]

vote_average = df.loc[df['title'] == info, 'vote_average'].values[0]
if vote_count > 2000:
    print('La película', info, 'fue estrenada en el año.', year, 'La misma cuenta con un total de', vote_count,'valoraciones, con un promedio de', vote_average)
else:
    print('la pelicula que busca no cumple con la condicion de mas de 2000 votos por ende no se devolvera ningun valor') 
print('el año fue :', year, 'y la puntuacion fue', score)

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

info = input('Ingrese el mes en español: ').lower()
if info in meses:
    mes = meses[info]   
else:
    print('El mes ingresado no es válido.')

info2 = input('Ingrese el dia en español: ').lower()
if info2 in dias:
    dia = dias[info2]
else:
    print('El dia ingresado no es válido.')   


df['month'] = df['release_date'].apply(extract_month)
df['day'] = df['release_date'].apply(extract_day)

month = df.loc[df['month'] == mes, 'month'].count()
day = df.loc[df['day'] == dia, 'day'].shape[0]
print(month)
print(day)