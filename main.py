from fastapi import FastAPI
from utils import (
    cantidad_filmaciones_mes,
    cantidad_filmaciones_dia,
    score_titulo,
    votos_titulo,
    get_actor,
    get_director
)

app = FastAPI()

@app.get("/cantidad_filmaciones_mes/")
def get_cantidad_filmaciones_mes(mes: str):
    return {"result": cantidad_filmaciones_mes(mes)}

@app.get("/cantidad_filmaciones_dia/")
def get_cantidad_filmaciones_dia(dia: str):
    return {"result": cantidad_filmaciones_dia(dia)}

@app.get("/score_titulo/")
def get_score_titulo(titulo: str):
    return {"result": score_titulo(titulo)}

@app.get("/votos_titulo/")
def get_votos_titulo(titulo: str):
    return {"result": votos_titulo(titulo)}

@app.get("/actor/")
def get_actor_info(nombre_actor: str):
    return {"result": get_actor(nombre_actor)}

@app.get("/director/")
def get_director_info(nombre_director: str):
    return {"result": get_director(nombre_director)}
