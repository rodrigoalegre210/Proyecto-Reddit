<h1 align="center"> Proyecto Reddit </h1>

Este proyecto tiene como objetivo realizar un análisis predicitvo y de sentimientos utilizando datos de Reddit. Al principio, el enfoque era realizar **web scraping** para extraer datos de publicaciones de Reddit, pero después de investigar diferentes opciones, me decidí utilizar la API oficial de Reddit para extraer los datos de manera eficiente y segura.

El proyecto abarca múltiples etapas del flujo de trabajo de ciencia de datos como la recolección de datos, procesamiento y limpieza de datos, ingeniería de características y entrenamientos de modelos de ML(Machine Learning).

## Funcionalidades principales.

* **Extracción de datos usando la API de Reddit**: Los datos se recolectan mediante la API, obteniendo información sobre publicaciones de Reddit como el título, autor, fecha de la publicación, cantidad de upvotes y comentarios.
  
* **Procesameinto de datos**: Los datos extraídos pasan por un proceso de limpieza y estandarización que incluye la eliminación de publicaciones con títulos faltantes, la normalización de texto y lo necesario para poder entrenar los modelos de ML en una forma correcta.
  
* **Modelos predictivos de ML**: Se implementaron un total de 5 modelos para predecir el número de comentarios y upvotes en función de los títulos de las publicaciones.

## Modelos predictivos.

Como se mencionó anteriormente, se realizaron un total de 5 modelos predictivos en este proyecto (Tres modelos para predecir la cantidad de comentarios y dos modelos para predecir la cantidad de upvotes). Los modelos tuvieron dos enfoques: Basados en características y Basados en Word2Vec.

* **Modelos basados en características**: Para entrenar estos modelos se crearon dos columnas nuevas dentro del dataset trabajado en el proyecto. La columna 'conteo_palabras' contiene la cantidad de palabras dentro del título de cada registro, y la columna 'contiene_palabras_clave' contiene '1' si el título contiene alguna palabra clave establecida en el archivo 'ingenieria_caracteristicas.py' o '0' si no contiene ninguna palabra clave. Los resultados obtenidos en estos modelos nos dicen que estas características tienen una relación muy débil con el número de upvotes o comentarios.
  
* **Modelos basados en Word2Vec**: Para estos modelos se usó un enfoque de Word2Vec para vectorizar los títulos de las publicaciones. Estos modelos tampoco pudieron capturar patrones predictivos claros entre los títulos y la cantidad de upvotes o comentarios.

Como conclusión final con estos modelos, se determinó que los títulos de las publicaciones y las características básicas no son buenos predictores del número de upvotes. Esto puede ser a la naturaleza del contenido de Reddit, en donde el contexto y las interacciones entre usuarios son más impactantes que los mísmos títulos.
