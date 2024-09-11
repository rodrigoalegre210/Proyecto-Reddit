import praw
import pandas as pd
from configuracion import CLIENT_ID, CLIENT_SECRET, USER_AGENT


"""

Obtenemos los datos de publicaciones de un subreddit específico.

Parametros:
- subrredit: Nombre del subrredit del cual esxtraemos los datos.
- limit: Número de publicaciones a extraer.

"""
def obtener_datos_reddit(subreddit_name, limit = 500):

    # Configuración de la API.
    reddit = praw.Reddit(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        user_agent = USER_AGENT
    )

    subreddit = reddit.subreddit(subreddit_name)

    # Obtenemos datos del subreddit.
    posts = []
    for post in subreddit.hot(limit = limit):
        posts.append({
            'id': post.id,
            'titulo': post.title,
            'autor': post.author.name if post.author else 'N/A',
            'fecha': post.created_utc,
            'url': post.url,
            'upvotes': post.score,
            'comentarios': post.num_comments
        })

    df = pd.DataFrame(posts)
    return df
    
if __name__ == "__main__":
    df_technology = obtener_datos_reddit('technology', limit = 500)
    print(f'Número de publicaciones extraídas: {len(df_technology)}')
    df_technology.to_csv('Datos/crudos/datos_reddit.csv', index = False)
    print(f"Datos extraídos y guardados en 'datos/crudos/datos_reddit.csv'")