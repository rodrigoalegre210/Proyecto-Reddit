import pandas as pd
import re

# Función para cargar los datos.
def cargar_datos(ruta_csv):

    return pd.read_csv(ruta_csv)

# Función para eliminar publicaciones con datos faltantes.
def eliminar_datos_faltantes(df):

    df = df[df['titulo'].notna() & (df['titulo'] != '')]
    
    return df

# Función para remover URLs y estandarizar los títulos.
def limpiar_titulo(titulo):

    titulo = re.sub(r'http\S+', '', titulo) # Eliminamos las URLs.
    titulo = re.sub(r'[^a-zA-Z\s$%€]', '', titulo) # Eliminamos caracteres especiales.
    titulo = titulo.lower() # Convertimos el texto a minúsculas.

    return titulo

# Función para estandarizar otros campos relevantes.
def estandarizar_campos(df, columnas):
    for columna in columnas:
        df[columna] = df[columna].apply(lambda x: str(x).lower().strip())

    return df

# Función para aplicar la limpieza a los datos.
def limpiar_datos(df):
    df['titulo'] = df['titulo'].apply(lambda x: limpiar_titulo(x))

    columnas_a_estandarizar = ['autor']
    df = estandarizar_campos(df, columnas_a_estandarizar)

    return df

# Función para guardar los datos procesados.
def guardar_datos(df, ruta_csv):
    df.to_csv(ruta_csv, index = False)

if __name__ == "__main__":
    # Ruta de los datos crudos.
    ruta_datos_crudos = 'Datos/crudos/datos_reddit.csv'

    # Cargamos los datos.
    df = cargar_datos(ruta_datos_crudos)
    print(f'Datos cargados: {len(df)} filas.')

    # Eliminamos los datos faltantes.
    df = eliminar_datos_faltantes(df)
    print(f'Datos después de eliminar filas con valores faltantes: {len(df)} filas.')

    # Limpiamos y procesamos los datos.
    df = limpiar_datos(df)
    print('¡Datos listos!')

    # Guardamos los datos procesados.
    ruta_datos_procesados = 'Datos/procesados/datos_reddit_limpios.csv'
    guardar_datos(df, ruta_datos_procesados)
    print('Datos guardados.')