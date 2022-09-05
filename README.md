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

### Arquitecura - Canalizar datos

![image](https://user-images.githubusercontent.com/20784371/188360932-bfc42b5f-e9dd-4ff2-b15d-6b199bfe8a35.png)

1. Github - repositorio de código: En github se carga el código fuente de la aplicación
2. AWSCodePipeline: Utilizado para crear la canalización de datos se utilizó porque permite automatizar la carga de los datos, compilarlos, probarlos e implementarlos de una manera rápida

![image](https://user-images.githubusercontent.com/20784371/188361181-a48f8382-41de-48a2-8556-0ad6830de4bd.png)
![image](https://user-images.githubusercontent.com/20784371/188361192-557df5e3-6c15-4240-9fcf-b056fb1940f4.png)

3. AWS CodeBuild: Permite compilar la aplicación de una manera sencilla especificando paso por paso como se hará utilizando el archivo buildspec.yml
![image](https://user-images.githubusercontent.com/20784371/188361387-433979b1-76af-4cb5-a33d-d4a0536ae204.png)
![image](https://user-images.githubusercontent.com/20784371/188361465-6535aaf6-8737-4478-be10-e8de13c5fad7.png)

4. EC2: Se crea una instancia en EC2 que permitirá ejecutar la aplicación utilizando codeDeploy
![image](https://user-images.githubusercontent.com/20784371/188361547-59cd41d2-44fa-4a78-95d1-dd6037b827e2.png)

5. AWS CodeDeploy: Desplega la solución basandose en el archivo appspec.yml
![image](https://user-images.githubusercontent.com/20784371/188361653-e7796834-4378-4994-a9f4-100f33582767.png)
![image](https://user-images.githubusercontent.com/20784371/188361728-4cf96126-9534-45be-bfa2-5e5dc9eb4612.png)

6. AWS s3: Aloja los archivos de insumo y resultado. Además también se deja log de la ejecución paso por paso y queda registro de errores

![image](https://user-images.githubusercontent.com/20784371/188361803-141a3c82-f508-4e1d-b1b3-c7ee42c7d7c9.png)
![image](https://user-images.githubusercontent.com/20784371/188361978-cb5cf419-429a-4088-85d3-4381f4024df2.png)


### ETL 

Se utiliza AWS Glue para realizar cruce entre los 3 datasets

![image](https://user-images.githubusercontent.com/20784371/188362087-a2ef2274-0692-4ba2-8566-d6bdd5843c89.png)

¿Cuál es el objetivo?

El objetivo del proyecto es integrar información de publicaciones, perfiles y locaciones para identificar relación entre datos relevantes como número de comentarios en la red social,número de seguidores número de publicaciones, comentarios, likes y determinar en que lugares del mundo existe mayor interacción en la red
¿Qué preguntas quieres hacer?
Cuál es la locación que tiene mayor interacción? Cuales son las cuentas que tienen mayor interacción en la red personales o empresariales? Cuál es el nuvel de Concentración de interacción por pais?, Que relación existe entre el número de publicaciones y reacciones como me gusta y comentarios o pueden existir usuarios con pocas publicaciones pero con un tráfico de interacción mayor? 
¿Por qué eligió el modelo que eligió?
Permite realizar un análisis con una buena cantidad de variables paraidentificar niveles de interacción, concentraciones de acuerdo a locación y responder a diferentes preguntas





