from fastapi import FastAPI # type: ignore
from utils import (
    cantidad_filmaciones_mes,
    cantidad_filmaciones_dia,
    score_titulo,
    votos_titulo,
    get_actor,
    get_director,
    recomendacion
)

app = FastAPI()

# Ruta para la raíz del servidor
@app.get("/")
async def read_root():
    return {"¡Te doy la bienvenida a la API de recomendaciones de Películas de Paula!"}

# Endpoint para cantidad_filmaciones_mes
@app.get("/cantidad_filmaciones_mes/")
async def cantidad_filmaciones_mes_endpoint(mes: str):
    return {cantidad_filmaciones_mes(mes)}

# Endpoint para cantidad_filmaciones_dia
@app.get("/cantidad_filmaciones_dia/")
async def cantidad_filmaciones_dia_endpoint(dia: str):
    return {cantidad_filmaciones_dia(dia)}

# Endpoint para score_titulo
@app.get("/score_titulo/")
async def score_titulo_endpoint(titulo: str):
    return {score_titulo(titulo)}

# Endpoint para votos_titulo
@app.get("/votos_titulo/")
async def votos_titulo_endpoint(titulo: str):
    return {"resultado": votos_titulo(titulo)}

# Endpoint para get_actor
@app.get("/get_actor/")
async def get_actor_endpoint(nombre_actor: str):
    return {get_actor(nombre_actor)}

# Endpoint para get_director
@app.get("/get_director/")
async def get_director_endpoint(nombre_director: str):
    return {get_director(nombre_director)}

@app.get("/recomendacion/")
async def recomendacion_endpoint(titulo: str):
    resultado = recomendacion(titulo)
    return {"resultados": resultado}
