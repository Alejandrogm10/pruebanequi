# pruebanequi

Datasets Instagram
Tomado de Kaggle https://www.kaggle.com/datasets/shmalex/instagram-dataset

1. Instagram_profiles: Dataset que contiene perfiles de instagram de diferentes personas y negocios. Cantidad de registros 4,509,586
Formato CSV
2. Instagram_posts: Dataset que contiene publicaciones de instagram. En kaggle hay disponibles 42,710,197 registros, sin embargo, se utilizan para la prueba se utilizan 1,300,000 registros
Formato PARQUET
3. Instagram_locations: Dataset que contiene diferentes locaciones alrededor del mundo. Contiene 1,204,583 registros
Formato CSV

El caso de uso final de los datos es para tabla de análisis

### Exploratory Data Análisis

![image](https://user-images.githubusercontent.com/20784371/188358721-da7cdc6e-14d8-41fd-b51b-dad6a097e91d.png)


En este análisis exploratorio de datos se siguen los siguientes pasos:

1. Cargar la información a analizar: En este caso se cargan los 3 datasets seleccionados
2. Información del dataset: En este caso se utilizan .head(), describe() e info() para conocer un poco más los datos, nos da descripciones estadisticas y se puede saber con algunas filas que información contiene el dataset
3. Encontrar valores duplicados: En este paso se determina si el datasets presenta valores duplicados, se analiza si es algo normal o realmente se deben eliminar, se utilizan funciones como .drop_duplicates()
4. Valores nulos: Se utiliza .isnull().sum() para determinar cuantos valores nulos hay por columna, en este caso se toma la decisión de si rellenar los valores nulos con algún valor o de eliminar las filas que contengan valores nulos realizandolo con .dropna()
5. Valores únicos: Se puede conocer por columna cuales son los valores únicos que existen, esto para conocer que información trae cada variable
6. Eliminar columnas inncesarias: Se eliminan aquellas columnas que no son relevantes para el modelo o reporte
7. Relación entre variables: Se puede determinar que relación existe entre variables utilizando una matriz de correlación





