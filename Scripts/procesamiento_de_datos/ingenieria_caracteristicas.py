import pandas as pd
import numpy as np

# Función para cargar los datos procesados.
def cargar_datos_procesados(ruta_csv):

    return pd.read_csv(ruta_csv)

def guardar_datos_procesados(df, ruta_csv):
    df.to_csv(ruta_csv, index = False)

# Lista de palabras claves relacionadas con tecnología.
palabras_clave = [
    # Tecnología.
    'ai', 'artificial intelligence', 'machine learning', 'deep learning', 
    'blockchain', 'cryptocurrency', 'bitcoin', 'nft', '5g', 'cloud computing', 
    'cybersecurity', 'data breach', 'privacy', 'quantum computing', 'iot', 
    'internet of things', 'smartphone', 'autonomous vehicle', 'drone', 
    'big data', 'robotics', 'virtual reality', 'vr', 'augmented reality', 
    'ar', 'metaverse', 'social media', 'startup', 'innovation', 'tech giant',
    'car', 'tesla', 'starlink', 'web', 'app', 'server', 'spacex', 'ibm', 'openia',

    # Personas influyentes.
    'elon musk', 'mark zuckerberg', 'jeff bezos', 'tim cook', 'bill gates',
    'donald trump', 'joe biden', 'president', 'government', 'regulation',

    # Aplicaciones y plataformas populares.
    'facebook', 'twitter', 'x', 'instagram', 'whatsapp', 'snapchat', 'tiktok', 
    'youtube', 'linkedin', 'google', 'apple', 'microsoft', 'amazon', 'netflix', 
    'spotify', 'uber', 'airbnb', 'tesla', 'zoom', 'reddit', 'binance', 'telegram',
    'snapchat', 'chat-gpt',

    # Términos financieros.
    'investment', 'loss', 'profit', 'revenue', 'stock', 'share', 'market',
    'funding', 'valuation', 'ipo', 'merger', 'acquisition', 'debt', 'capital',
    'venture capital', 'angel investor', 'bankruptcy', 'economy', 'finance',

    # Componentes de computadoras y tecnología.
    'nvidia', 'amd', 'ryzen', 'intel', 'graphics card', 'gpu', 'cpu', 
    'motherboard', 'ram', 'ssd', 'hard drive', 'usb', 'monitor', 'keyboard', 
    'mouse', 'laptop', 'desktop', 'server', 'network', 'router', 'wifi', 'ethernet'
]

# Función para crear nuevas características.
def contiene_palabras_clave(titulo, palabras_clave):

    titulo = titulo.lower()
    palabras_titulo = set(titulo.split())
    return int(any(palabra.lower() in palabras_titulo for palabra in palabras_clave))

# Función para crear nuevas características.
def crear_caracteristicas(df):

    # Contamos las palabras en el título.
    df['conteo_palabras'] = df['titulo'].apply(lambda x: len(x.split()))

    # Identificamos si el título tiene palabras claves.
    df['contiene_palabras_clave'] = df['titulo'].apply(lambda x: contiene_palabras_clave(x, palabras_clave))

    return df

if __name__ == "__main__":

    # Ruta del archivo CSV con datos procesados.
    ruta_csv = 'Datos/procesados/datos_reddit_limpios.csv'

    # Ruta delarchivo CSV para guardar los datos con características.
    ruta_datos_con_caracteristicas = 'Datos/final/datos_reddit_con_caracteristicas.csv'

    # Cargamos los datos.
    df = cargar_datos_procesados(ruta_csv)
    print(f'Datos cargados: {len(df)} filas.')

    # Creamos nuevas características.
    df = crear_caracteristicas(df)
    print('Características creadas.')

    # Guardamos los datos con las nuevas características.
    guardar_datos_procesados(df, ruta_datos_con_caracteristicas)
    print('Datos con características guardados.')