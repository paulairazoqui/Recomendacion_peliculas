import pandas as pd
import unicodedata
import ast
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity



# Ruta relativa a los datasets
movies_path = os.path.join('Datasets', 'transformed_movies.csv')
credits_path = os.path.join('Datasets', 'reduced_credits.csv')

# Carga de los datasets
movies = pd.read_csv(movies_path)
credits = pd.read_csv(credits_path)


# Función para eliminar acentos
def eliminar_acentos(texto):
    return ''.join(
        char for char in unicodedata.normalize('NFD', texto)
        if unicodedata.category(char) != 'Mn'
    )


def cantidad_filmaciones_mes(Mes):
    # Ruta relativa a los datasets
    movies_path = os.path.join('Datasets', 'transformed_movies.csv')
    
    # Carga de los datasets
    movies = pd.read_csv(movies_path)
        
    # Diccionario para convertir el mes en español al número correspondiente
    meses = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
        "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
        "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
    }
    
    # Convertir el mes a minúscula y obtener su número
    mes_numero = meses.get(Mes.lower())
    
    # Validar el mes
    if mes_numero is None:
        return f"'{Mes.capitalize()}' no es un mes válido. Por favor, ingrese un mes en español."
    
    # Contar películas estrenadas en el mes
    cantidad = movies[movies['release_month'] == mes_numero].shape[0]
    
    # Devolver el mensaje
    return f"{cantidad} películas fueron estrenadas en el mes de {Mes.capitalize()}."



def cantidad_filmaciones_dia(Dia):
    # Ruta relativa a los datasets
    movies_path = os.path.join('Datasets', 'transformed_movies.csv')
    
    # Carga de los datasets
    movies = pd.read_csv(movies_path)
    
    # Diccionario para convertir el día en español al número correspondiente
    dias = {
        "lunes": 0, "martes": 1, "miercoles": 2, "jueves": 3,
        "viernes": 4, "sabado": 5, "domingo": 6
    }
    
    # Normalizar el día ingresado
    Dia_normalizado = eliminar_acentos(Dia.lower())
    
    # Obtener el número correspondiente al día
    dias_numero = dias.get(Dia_normalizado)
    
    # Validar el día ingresado
    if dias_numero is None:
        return f"'{Dia.capitalize()}' no es un día válido. Por favor, ingrese un día en español."
    
    # Contar películas estrenadas en el día
    cantidad = movies[movies['release_dow'] == dias_numero].shape[0]
    
    # Devolver el mensaje
    return f"{cantidad} películas fueron estrenadas en los días {Dia.capitalize()}."



def score_titulo(titulo_de_la_filmacion):
    # Ruta relativa a los datasets
    movies_path = os.path.join('Datasets', 'transformed_movies.csv')
    # Carga de los datasets
    movies = pd.read_csv(movies_path)
    
    # Normalizar el titulo ingresado
    titulo_normalizado = eliminar_acentos(titulo_de_la_filmacion.lower())

    # Buscar la película por título (ignorando mayúsculas/minúsculas)
    pelicula = movies[movies['title'].str.lower() == titulo_normalizado]
    
    # Validar si se encontró la película
    if pelicula.empty:
        return f"No se encontró una película con el título '{titulo_de_la_filmacion}'."
    
    # Obtener los valores de título, año y score
    titulo = pelicula.iloc[0]['title']
    anio = pelicula.iloc[0]['release_year']
    score = pelicula.iloc[0]['popularity']
    
    # Retornar el mensaje formateado
    return f"La película '{titulo}' fue estrenada en el año {int(anio)} con un score/popularidad de {score:.2f}."


def votos_titulo(titulo_de_la_filmacion):
    # Ruta relativa a los datasets
    movies_path = os.path.join('Datasets', 'transformed_movies.csv')
    
    # Carga de los datasets
    movies = pd.read_csv(movies_path)
    titulo_normalizado = eliminar_acentos(titulo_de_la_filmacion.lower())

    # Buscar la película por título (ignorando mayúsculas/minúsculas y acentos)
    pelicula = movies[movies['title'].str.lower().apply(eliminar_acentos) == titulo_normalizado]
    
    # Validar si se encontró la película
    if pelicula.empty:
        return f"No se encontró una película con el título '{titulo_de_la_filmacion}'."
    
    # Obtener los valores necesarios
    titulo = pelicula.iloc[0]['title']
    anio = pelicula.iloc[0]['release_year']
    votos = pelicula.iloc[0]['vote_count']
    promedio = pelicula.iloc[0]['vote_average']
    
    # Verificar la condición de 2000 valoraciones
    if votos < 2000:
        return f"La película '{titulo}' no cumple con el mínimo de 2000 valoraciones. No se devuelve información adicional."
    
    # Retornar el mensaje formateado
    return f"La película '{titulo}' fue estrenada en el año {int(anio)}. La misma cuenta con un total de {int(votos)} valoraciones, con un promedio de {promedio:.2f}."



def get_actor(nombre_actor):
    # Ruta relativa a los datasets
    movies_path = os.path.join('Datasets', 'transformed_movies.csv')
    credits_path = os.path.join('Datasets', 'reduced_credits.csv')

    # Carga de los datasets
    movies = pd.read_csv(movies_path)
    credits = pd.read_csv(credits_path)

    # Convertir las strings de 'actors' en listas reales
    credits['actors'] = credits['actors'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
    
    # Normalizar el nombre ingresado
    actor_normalizado = eliminar_acentos(nombre_actor.lower())
    
    # Asegurarnos de normalizar los nombres en 'actors'
    credits['actors_normalized'] = credits['actors'].apply(
        lambda actors: [eliminar_acentos(actor.lower()) for actor in actors]
    )

    # Filtrar películas en las que aparece el actor
    credits['actor_in_cast'] = credits['actors_normalized'].apply(
        lambda actors: actor_normalizado in actors
    )

    # Dataset reducido con solo las películas del actor
    actor_films = credits[credits['actor_in_cast']].merge(
        movies[['id', 'return']], on='id', how='inner'
    )
    
    # Validar si el actor tiene películas
    if actor_films.empty:
        return f"No se encontró al actor '{nombre_actor}' en el dataset."
    
    # Calcular métricas
    total_return = actor_films['return'].sum()
    cantidad_peliculas = actor_films['id'].nunique()
    promedio_retorno = total_return / cantidad_peliculas
    
    # Retornar el mensaje formateado
    return (
        f"El actor {nombre_actor} ha participado de {cantidad_peliculas} cantidad de filmaciones, "
        f"el mismo ha conseguido un retorno de {total_return:.2f} con un promedio de {promedio_retorno:.2f} por filmación."
    )



def get_director(nombre_director):
        # Ruta relativa a los datasets
    movies_path = os.path.join('Datasets', 'transformed_movies.csv')
    credits_path = os.path.join('Datasets', 'reduced_credits.csv')

    # Carga de los datasets
    movies = pd.read_csv(movies_path)
    credits = pd.read_csv(credits_path)

    # Normalizar el nombre del director ingresado
    director_normalizado = eliminar_acentos(nombre_director.lower())
    
    # Filtrar las películas dirigidas por el director
    director_films = credits[credits['director_name'].apply(
        lambda d: eliminar_acentos(d.lower()) if isinstance(d, str) else '') == director_normalizado]
    
    # Validar si el director tiene películas
    if director_films.empty:
        return f"No se encontró al director '{nombre_director}' en el dataset."
    
    # Hacer el join con el dataset de películas por 'id'
    director_films = director_films.merge(
        movies[['id', 'title', 'release_date', 'return', 'budget', 'revenue']],
        on='id',
        how='inner'
    )
    
    # Calcular la ganancia individual de cada película
    director_films['profit'] = director_films['revenue'] - director_films['budget']
    
    # Calcular el retorno total del director
    total_return = director_films['return'].sum()
    
    # Crear el mensaje con los detalles de cada película
    peliculas_info = []
    for _, row in director_films.iterrows():
        peliculas_info.append(
            f"- '{row['title']}' lanzada el {row['release_date']}, "
            f"retorno: {row['return']:.2f}, costo: {row['budget']:.2f}, ganancia: {row['profit']:.2f}"
        )
    
    # Formatear la respuesta
    return (
        f"El director {nombre_director} ha tenido un éxito total medido en un retorno de {total_return:.2f}.\n"
        "Detalle de sus películas:\n" + "\n".join(peliculas_info)
    )


def recomendacion(titulo: str):
    # Ruta relativa al archivo
    movies_path = os.path.join('Datasets', 'muestra_movies.csv')
    combined_features_path = os.path.join('Datasets', 'muestra_combined_features.npz')

    # Cargar las bases de datos
    movies = pd.read_csv(movies_path)
    combined_features = np.load(combined_features_path)['arr_0']
    
    # Encuentra el índice de la película en el DataFrame
    try:
        idx = movies[movies['title'].str.lower() == titulo.lower()].index[0]
    except IndexError:
        return [{"error": f"La película '{titulo}' no se encuentra en el dataset."}]

    # Calcular la similitud de coseno entre la película seleccionada y todas las demás
    similitudes = cosine_similarity(combined_features[idx].reshape(1, -1), combined_features)

    # Ordenar las películas por similitud (exceptuando la película actual)
    indices_similares = similitudes[0].argsort()[::-1][1:6]  # Toma las 5 más similares, excluyendo la misma

    # Generar la lista de recomendaciones
    recomendaciones = [
        {
            "titulo": movies.iloc[i]['title'],
            "similitud": float(similitudes[0][i])
        }
        for i in indices_similares
    ]

    return recomendaciones
