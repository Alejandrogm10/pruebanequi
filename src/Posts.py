# -*- coding: utf-8 -*-
"""
@author: Alejandro Gutiérrez
"""

import pandas as pd
import seaborn as sb
import boto3
import io
from io import StringIO

# =============================================================================
# EDA: Exploratory Data Analysis
# =============================================================================




s3_file_key = 'instagram_posts.parquet'
bucket = 'insumosprueba'
s3 = boto3.client('s3')
obj = s3.get_object(Bucket=bucket, Key=s3_file_key)
posts = pd.read_parquet(io.BytesIO(obj['Body'].read()), engine='pyarrow')
print('posts cargado')
# =============================================================================
# 1. Información Básica sobre el DataSet'''
# =============================================================================
#Vista Previa
print(posts.head())
#Dimensionalidad
print('El DataSet tiene {} filas y {} columnas'.format(posts.shape[0],posts.shape[1])) 
#Describir la información
print(posts.describe().apply(lambda x: x.apply('{0:.0f}'.format)))
#Información basica - tipos de datos
print(posts.info())
# =============================================================================
# 2. Valores Duplicados'''
# =============================================================================
#Valores duplicados en el dataframe
print('El DataSet tiene {} registros duplicados'.format(posts.duplicated().sum()))
posts = posts.drop_duplicates()
print('El DataSet tiene {} registros duplicados'.format(posts.duplicated().sum()))
# =============================================================================
# 3. Valores Nulos
# =============================================================================
print(posts.isnull().sum())
#Elimina filas que tengan en los campos location_id valores nulos
posts = posts.dropna(axis=0, subset=['location_id'])

# =============================================================================
# 4. Valores Únicos
# =============================================================================
print(posts['post_type'].unique())
print(sb.countplot(posts['post_type']))

# =============================================================================
# 5. Eliminar columnas innecesarias en el modelo
# =============================================================================
posts = posts.drop(['cts'], axis=1)


# =============================================================================
# Guardar Archivo en S3
# =============================================================================

csv_buffer = StringIO()
posts.to_csv(csv_buffer)
s3_resource = boto3.resource('s3')
s3_resource.Object(bucket, 'resultado_instagram_posts.csv').put(Body=csv_buffer.getvalue())

