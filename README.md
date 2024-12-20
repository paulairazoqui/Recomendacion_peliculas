# Sistema de Recomendación de Películas

## Tabla de Contenido

- [Introducción](#introducción)
- [Descripción del Proyecto](#descripción-del-proyecto)
- [Instalación y Requisitos](#instalación-y-requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso y Ejecución](#uso-y-ejecución)
- [Funciones Disponibles](#funciones-disponibles)
- [Datos y Fuentes](#datos-y-fuentes)
- [Metodología](#metodología)
- [Resultados y Conclusiones](#resultados-y-conclusiones)
- [Contribución y Colaboración](#contribución-y-colaboración)
- [Licencia](#licencia)

---

## Introducción

Este proyecto implementa un sistema de recomendación de películas que permite a los usuarios obtener información detallada sobre diversas métricas cinematográficas y recibir sugerencias personalizadas basadas en sus preferencias.

## Descripción del Proyecto

El sistema se desarrolló desde cero, abarcando desde la recolección y transformación de datos hasta la implementación de un modelo de recomendación funcional. Se procesaron datos de películas para ofrecer funcionalidades que incluyen conteo de filmaciones por mes y día, puntuaciones y votos de títulos, información sobre actores y directores, y recomendaciones basadas en similitudes.

---

## Instalación y Requisitos

### Requisitos

- Python 3.7 o superior
- Bibliotecas: pandas, numpy, scikit-learn

### Pasos de Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/paulairazoqui/Recomendacion_peliculas.git
   ```
2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activar el entorno virtual:
   - **Windows**: `venv\Scripts\activate`
   - **macOS/Linux**: `source venv/bin/activate`
4. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## Estructura del Proyecto

```
├── datasets/
│   ├── transformed_movies.csv
│   ├── reduced_credits.csv
│   ├── movies_reduced.csv
│   └── movies_features.npz
├── notebooks/
│   ├── ETL1 - General.ipynb
│   └── ETL2 - Fx recomendacion.ipynb
├── README.md
├── requirements.txt
├── utils.py
└── main.py
```

- **notebooks/**: Notebooks de Jupyter para exploración y análisis preliminar.
- **datasets/**: Contiene los datos que utilizan las funciones.
- **archivos**: Código fuente, incluyendo funciones principales y utilidades.

---

## Uso y Ejecución

### Ejecución del Sistema de Recomendación

1. Importar las funciones desde `utils.py`:
   ```python
   from utils import (
       cantidad_filmaciones_mes,
       cantidad_filmaciones_dia,
       score_titulo,
       votos_titulo,
       get_actor,
       get_director,
       recomendacion
   )
   ```
2. Llamar a la función deseada con los parámetros correspondientes. Por ejemplo, para obtener recomendaciones basadas en un título:
   ```python
   resultado = recomendacion("Moana")
   print(resultado)
   ```

---

## Funciones Disponibles

A continuación, se detallan las funciones disponibles en el sistema:

### `cantidad_filmaciones_mes(mes: str) -> int`

Devuelve la cantidad de filmaciones realizadas en un mes específico.

- **Parámetro**: `mes` - Nombre del mes en español (e.g., "enero").
- **Retorno**: Número entero con la cantidad de filmaciones.

### `cantidad_filmaciones_dia(dia: str) -> int`

Devuelve la cantidad de filmaciones realizadas en un día específico de la semana.

- **Parámetro**: `dia` - Nombre del día en español (e.g., "lunes").
- **Retorno**: Número entero con la cantidad de filmaciones.

### `score_titulo(titulo: str) -> dict`

Proporciona el puntaje de una película dado su título.

- **Parámetro**: `titulo` - Título de la película.
- **Retorno**: Diccionario con el título y su puntaje.

### `votos_titulo(titulo: str) -> dict`

Devuelve el número de votos de una película y su promedio de puntuación.

- **Parámetro**: `titulo` - Título de la película.
- **Retorno**: Diccionario con el título, número de votos y promedio de puntuación.

### `get_actor(nombre_actor: str) -> dict`

Proporciona información sobre un actor específico, incluyendo la cantidad de películas en las que ha participado y el promedio de retorno de dichas películas.

- **Parámetro**: `nombre_actor` - Nombre del actor.
- **Retorno**: Diccionario con el nombre del actor, número de películas y promedio de retorno.

### `get_director(nombre_director: str) -> dict`

Proporciona información sobre un director específico, incluyendo la lista de películas dirigidas y el retorno total de dichas películas.

- **Parámetro**: `nombre_director` - Nombre del director.
- **Retorno**: Diccionario con el nombre del director, lista de películas y retorno total.

### `recomendacion(titulo: str) -> list`

Ofrece una lista de películas recomendadas basadas en la similitud con el título proporcionado.

- **Parámetro**: `titulo` - Título de la película de referencia.
- **Retorno**: Lista de diccionarios, cada uno con el título de la película recomendada y su nivel de similitud.

---

## Datos y Fuentes

### Fuentes

Los datos utilizados en este proyecto provienen de archivos CSV ([link](https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5?usp=drive_link)) que contienen información detallada sobre películas, incluyendo títulos, popularidad, colecciones y géneros codificados.

### Procesamiento

Se realizaron diversas transformaciones a los datos para normalizar y escalar características como popularidad y colecciones, y para convertir los géneros en representaciones binarias adecuadas para el cálculo de similitudes.

---

## Metodología

El proyecto abarca dos etapas principales de transformación de datos (ETL1 y ETL2) para preparar y estructurar la información, y finalmente la implementación del sistema de recomendación.

### **ETL1 - General**

En esta etapa, se realizó un proceso exhaustivo de transformación de los datos crudos provenientes de los archivos `movies_dataset.csv` y `credits.csv`. Los pasos principales fueron:

#### **Procesamiento del Dataset `movies_dataset.csv`**

1. **Cálculo del Retorno de Inversión (`return`)**:
   - Se aseguraron los valores numéricos en las columnas `revenue` y `budget`, reemplazando valores nulos por `0`.
   - Se calculó el retorno como `revenue / budget`, reemplazando valores indefinidos (división por 0) y nulos con `0`.

2. **Procesamiento de Fechas (`release_date`)**:
   - Las fechas de lanzamiento se transformaron al formato `datetime`.
   - Se crearon las columnas:
     - `release_year`: Año de lanzamiento.
     - `release_month`: Mes de lanzamiento.
     - `release_dow`: Día de la semana de lanzamiento.
   - Se eliminaron los registros sin año válido.

3. **Extracción de Colecciones (`belongs_to_collection`)**:
   - Los valores de esta columna fueron tratados como diccionarios.
   - Se extrajo el nombre de la colección a una nueva columna llamada `collection`.

4. **Codificación de Géneros (`genres`)**:
   - Los géneros, almacenados como listas de diccionarios, fueron transformados usando `LabelEncoder`:
     - Se extrajeron los nombres únicos de géneros.
     - Se codificaron los géneros como listas de enteros en una nueva columna `genres_encoded`.

5. **Eliminación de Columnas Irrelevantes**:
   - Se eliminaron columnas redundantes o no utilizadas como `video`, `imdb_id`, `homepage`, entre otras.

6. **Normalización y Eliminación de Duplicados**:
   - Se aseguró que la columna `popularity` tuviera valores numéricos.
   - Se eliminaron registros duplicados en `title`, conservando el registro con mayor popularidad.

7. **Guardado del Dataset Transformado**:
   - El archivo resultante, `transformed_movies.csv`, contiene las siguientes columnas clave:
     - `title`: Título de la película.
     - `popularity`: Popularidad normalizada.
     - `collection`: Nombre de la colección a la que pertenece la película.
     - `genres_encoded`: Lista de géneros codificados.
     - `release_year`, `release_month`, `release_dow`: Año, mes y día de la semana de lanzamiento.
     - `return`: Retorno de inversión.

---

#### **Procesamiento del Dataset `credits.csv`**

1. **Extracción de Directores (`crew`)**:
   - Se procesó la columna `crew` para extraer el nombre del director de cada película.

2. **Extracción de Actores (`cast`)**:
   - Se transformó la columna `cast` para obtener una lista de los actores principales.

3. **Creación del Dataset Reducido**:
   - Se generó un nuevo archivo reducido, `reduced_credits.csv`, con las columnas clave:
     - `id`: Identificador de la película.
     - `director_name`: Nombre del director.
     - `actors`: Lista de actores principales.

---

Ambos archivos procesados, `transformed_movies.csv` y `reduced_credits.csv`, se utilizan en las funciones `cantidad_filmaciones_mes`, `cantidad_filmaciones_dia`, `score_titulo`, `votos_titulo`, `get_actor` y `get_director`. Además se realizaron etapas de transformaciones adicionales (ETL2) para construir las matrices de características para el sistema de recomendación.

---

### **ETL2 - Construcción de Características**

En esta etapa, se prepararon los datos procesados en el **ETL1** para generar matrices de características que serían utilizadas por el sistema de recomendación.

---

#### **Carga y Preprocesamiento**

1. **Carga del Dataset**:
   - Se cargó el archivo procesado `transformed_movies.csv` con columnas clave: `title`, `popularity`, `collection` y `genres_encoded`.

2. **Relleno de Valores Nulos en `collection`**:
   - Las películas sin colección fueron marcadas como `"No Collection"`.

3. **Validación de Géneros (`genres_encoded`)**:
   - Los géneros se aseguraron como listas de enteros. Se eliminaron registros con valores nulos o géneros vacíos para garantizar la calidad de los datos.

---

#### **Transformaciones**

1. **Codificación Binaria de Géneros**:
   - Usando `MultiLabelBinarizer`, se generó una matriz de géneros binarizados, donde cada columna representaba un género.

2. **Codificación y Escalado de Colecciones**:
   - Se codificaron las colecciones usando `LabelEncoder`, asignando valores únicos a cada colección.
   - Las películas sin colección (`"No Collection"`) fueron asignadas con el valor `0`.
   - Usando `MinMaxScaler`, los valores de las colecciones se escalaron a un rango entre `0` y `1`.

3. **Normalización de la Popularidad**:
   - La columna `popularity` se normalizó usando `MinMaxScaler` y se integró en las matrices de características como `popularity_scaled`.
   - La columna original `popularity` fue eliminada para evitar redundancias.

---

#### **Integración de Características**

Se combinaron las siguientes características en una única matriz final:
   - Géneros binarizados.
   - Colecciones escaladas (`collection_scaled`).
   - Popularidad normalizada (`popularity_scaled`).

---

#### **Exportación de Resultados**

1. **Matriz de Características**:
   - Se guardó la matriz combinada en un archivo comprimido llamado `movies_features.npz`, que será utilizado directamente por el sistema de recomendación.

2. **Dataset Reducido**:
   - Se guardó un dataset reducido, `movies_reduced.csv`, con las columnas necesarias:
     - `title`: Título de la película.
     - `popularity`: Popularidad original.
     - `collection`: Nombre de la colección.
     - `genres_encoded`: Géneros codificados como listas de enteros.

---

## Funcionamiento de las Funciones

Una vez procesados los datos, se implementaron las siguientes funciones que permiten responder preguntas clave relacionadas con las películas en el dataset.

---

### **Cantidad de Filmaciones por Mes  `cantidad_filmaciones_mes()`**

**Cálculo**:

1. Convierte el nombre del mes ingresado por el usuario en español al número correspondiente utilizando un diccionario.
2. Filtra las películas que coinciden con el mes proporcionado y cuenta cuántas hay.
3. Devuelve un mensaje indicando la cantidad de películas estrenadas ese mes.

**Consideraciones**:

- Los datos se normalizan para aceptar tanto mayúsculas como minúsculas.
- Maneja casos donde el nombre del mes es inválido, devolviendo un mensaje de error.

---

### **Cantidad de Filmaciones por Día `cantidad_filmaciones_dia()`**

**Cálculo**:

1. Convierte el nombre del día en español al número correspondiente utilizando un diccionario.
2. Filtra las películas según el día de la semana en que se estrenaron.
3. Devuelve un mensaje con el conteo de películas estrenadas en ese día.

**Consideraciones**:

- Acepta entradas en español, normalizando días con o sin acentos.
- Maneja entradas incorrectas devolviendo mensajes de error.

---

### **Score por Título `score_titulo()`**

**Cálculo**:

1. Busca la película por título dentro del dataset transformado.
2. Obtiene la popularidad (score) de la película junto con el año de estreno.
3. Devuelve un mensaje formateado con la información del título, año y score.

**Consideraciones**:

- Utiliza normalización para manejar títulos ingresados con o sin mayúsculas/acentos.
- Si no se encuentra la película, devuelve un mensaje indicando el error.

---

### **Votos por Título `votos_titulo()`**

**Cálculo**:

1. Busca la película por título en el dataset transformado.
2. Obtiene el número de votos y el promedio de votaciones.
3. Devuelve un mensaje con el total de votos y el promedio si supera las 2000 valoraciones.
4. Si la película tiene menos de 2000 votos, devuelve un mensaje indicando que no cumple con el mínimo.

**Consideraciones**:

- Maneja títulos normalizados y errores en caso de títulos no encontrados.
- Garantiza que solo se procesen películas con suficientes valoraciones.

---

### **Métricas por Actor `get_actor()`**

**Cálculo**:

1. Filtra las películas en las que aparece el actor ingresado, usando una lista normalizada de actores para evitar errores por diferencias en mayúsculas/acentos.
2. Calcula el retorno total sumando los valores de retorno de todas las películas en las que aparece.
3. Calcula el retorno promedio dividiendo el total entre la cantidad de películas del actor.
4. Devuelve un mensaje con las métricas de retorno total y promedio.

**Consideraciones**:

- Maneja casos en los que el actor no tiene películas registradas.
- Elimina errores relacionados con formatos de listas de actores en los datos.

---

### **Métricas por Director `get_director()`**

**Cálculo**:

1. Filtra las películas dirigidas por el director ingresado, utilizando una lista normalizada de nombres.
2. Une las películas dirigidas con el dataset transformado para obtener métricas adicionales (retorno, presupuesto, ingresos, etc.).
3. Calcula el retorno total sumando los valores de retorno de todas las películas dirigidas.
4. Genera un mensaje con información detallada de cada película y el retorno total del director.

**Consideraciones**:

- Maneja entradas incorrectas y directores no encontrados.
- Calcula métricas financieras detalladas, incluyendo ganancias individuales por película.

---

### **Recomendación de Películas `recomendacion()`**

**Cálculo**:

1. Divide las características de las películas en tres categorías: géneros, colección y popularidad.
2. Utiliza similitud de coseno para comparar cada categoría por separado.
3. Combina las similitudes con pesos predeterminados (géneros 70%, colección 20%, popularidad 10%) para obtener una similitud total.
4. Ajusta la similitud si las películas pertenecen a la misma colección.
5. Devuelve una lista con las cinco películas más similares.

**Consideraciones**:

- Maneja casos en los que el título de la película no está en el dataset.
- Asegura resultados relevantes ajustando pesos según la importancia relativa de las características.

---

## Resultados y Conclusiones

- **Desempeño**: El sistema genera recomendaciones relevantes basadas en géneros, popularidad y colecciones.
- **Limitaciones**: Actualmente, las recomendaciones dependen exclusivamente de los datos transformados y no están conectadas a una base de datos en tiempo real.

### Ejemplos de Salidas:

**Función `cantidad_filmaciones_mes()`**
```python
import utils
mes = utils.cantidad_filmaciones_mes("abril")
print(mes) 
3206 películas fueron estrenadas en el mes de Abril.
```

**Función `cantidad_filmaciones_dia()`**
```python
>>> import utils            
>>> dia = utils.cantidad_filmaciones_dia("domingo")
>>> print(dia)
3290 películas fueron estrenadas en los días Domingo.
```

**Función `score_titulo()`**
```python
>>> import utils 
>>> puntuacion = utils.score_titulo("Moana")
>>> print(puntuacion)
La película 'Moana' fue estrenada en el año 2016 con un score/popularidad de 9.14.
```

**Función `votos_titulo()`**
```python
>>> import utils 
>>> votos = utils.votos_titulo("Moana")
>>> print(votos)
La película 'Moana' fue estrenada en el año 2016. La misma cuenta con un total de 3471 valoraciones, con un promedio de 7.30.
```

**Función `get_actor()`**
```python
>>> import utils
>>> actor = utils.get_actor("Brad Pitt")
>>> print(actor)
El actor Brad pitt ha participado de 57 cantidad de filmaciones, el mismo ha conseguido un retorno de 12396514.34 con un promedio de 217482.71 por filmación.
```

**Función `get_director()`**
```python
>>> import utils
>>> director = utils.get_director("Tim Burton")
>>> print(director)
El director Tim burton ha tenido un éxito total medido en un retorno de 57.60.
Detalle de sus películas:
- 'Ed Wood' lanzada el 1994-09-27, retorno: 0.33, costo: 18000000.00, ganancia: -12112543.00
- 'Batman' lanzada el 1989-06-23, retorno: 11.75, costo: 35000000.00, ganancia: 376348924.00
- 'Batman Returns' lanzada el 1992-06-19, retorno: 3.50, costo: 80000000.00, ganancia: 200000000.00
- 'Mars Attacks!' lanzada el 1996-12-12, retorno: 1.45, costo: 70000000.00, ganancia: 31371017.00
- 'Beetlejuice' lanzada el 1988-02-29, retorno: 4.89, costo: 15000000.00, ganancia: 58326666.00
- 'Edward Scissorhands' lanzada el 1990-12-05, retorno: 2.65, costo: 20000000.00, ganancia: 33000000.00
- 'Sleepy Hollow' lanzada el 1999-11-18, retorno: 2.06, costo: 100000000.00, ganancia: 106071502.00
- 'Pee-wee's Big Adventure' lanzada el 1985-07-26, retorno: 6.82, costo: 6000000.00, ganancia: 34940662.00
- 'Big Fish' lanzada el 2003-12-25, retorno: 1.76, costo: 70000000.00, ganancia: 52919055.00
- 'Charlie and the Chocolate Factory' lanzada el 2005-07-13, retorno: 3.17, costo: 150000000.00, ganancia: 324968763.00
- 'Vincent' lanzada el 1982-01-01, retorno: 0.00, costo: 60000.00, ganancia: -60000.00
- 'Corpse Bride' lanzada el 2005-09-09, retorno: 2.93, costo: 40000000.00, ganancia: 77195061.00
- 'Sweeney Todd: The Demon Barber of Fleet Street' lanzada el 2007-12-20, retorno: 3.04, costo: 50000000.00, ganancia: 102000000.00
- 'Alice in Wonderland' lanzada el 2010-03-03, retorno: 5.13, costo: 200000000.00, ganancia: 825491110.00
- 'Dark Shadows' lanzada el 2012-05-08, retorno: 1.64, costo: 150000000.00, ganancia: 95527149.00
- 'Frankenweenie' lanzada el 2012-10-04, retorno: 0.90, costo: 39000000.00, ganancia: -3712212.00
- 'Big Eyes' lanzada el 2014-12-24, retorno: 2.89, costo: 10000000.00, ganancia: 18883511.00
- 'Miss Peregrine's Home for Peculiar Children' lanzada el 2016-09-28, retorno: 2.70, costo: 110000000.00, ganancia: 186485719.00
```

**Función `recomendacion()`**
```python
>>> import utils
>>> recomendacion = utils.recomendacion("Moana")
>>> print(recomendacion)
[{'titulo': 'The Land Before Time III: The Time of the Great Giving', 'similitud': 0.8}, {'titulo': 'Sinbad: Legend of the Seven Seas', 'similitud': 0.8}, {'titulo': "The True Story of Puss 'n Boots", 'similitud': 0.8}, {'titulo': "Clifford's Really Big Movie", 'similitud': 0.8}, {'titulo': 'The Jungle Book 2', 'similitud': 0.8}]
```


---

