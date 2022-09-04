# -*- coding: utf-8 -*-
"""
@author: Alejandro Gutiérrez
"""

import pandas as pd
import seaborn as sb
from io import StringIO
import boto3

# =============================================================================
# EDA: Exploratory Data Analysis
# =============================================================================

# Cargar archivo con perfiles de instagram formato csv separado por tabulador
perfiles = pd.read_csv('s3://insumosprueba/instagram_profiles.csv',sep='\t')
print('perfiles cargado')

# =============================================================================
# 1. Información Básica sobre el DataSet'''
# =============================================================================
#Vista Previa
print(perfiles.head())
#Dimensionalidad
print('El DataSet tiene {} filas y {} columnas'.format(perfiles.shape[0],perfiles.shape[1])) 
#Describir la información
print(perfiles.describe().apply(lambda x: x.apply('{0:.0f}'.format)))
#Información basica - tipos de datos
print(perfiles.info())
# =============================================================================
# 2. Valores Duplicados'''
# =============================================================================
#Valores duplicados en el dataframe
print('El DataSet tiene {} registros duplicados'.format(perfiles.duplicated().sum()))

# =============================================================================
# 3. Valores Nulos
# =============================================================================
print(perfiles.isnull().sum())
#Elimina filas que tengan en los campos n_posts y profile_id valores nulos
perfiles = perfiles.dropna(axis=0, subset=['n_posts'])
perfiles = perfiles.dropna(axis=0, subset=['profile_id'])
#Reemplaza valores nulos por texto definido
perfiles["description"].fillna("No Description", inplace = True)
perfiles["is_business_account"].fillna("Not Defined", inplace = True)
perfiles["firstname_lastname"].fillna("No Name", inplace = True)
print(perfiles.isnull().sum())
# =============================================================================
# 4. Valores Únicos
# =============================================================================
print(perfiles['is_business_account'].unique())
print(sb.countplot(perfiles['is_business_account']))

# =============================================================================
# 5. Eliminar columnas innecesarias en el modelo
# =============================================================================
perfiles = perfiles.drop(['url'], axis=1)
perfiles = perfiles.drop(['cts'], axis=1)

#Casteo tipo de datos
#perfiles['profile_id'] = pd.to_numeric(perfiles['profile_id'], errors='ignore')
#perfiles['profile_id'] = perfiles['profile_id'].apply(lambda x: x.apply('{0:.0f}'.format))
#Elimina todas las filas que tengan valores nulos
#posts = pd.read_parquet(r'C:\Users\Alejandro\Prueba\instagram_posts.parquet', engine='pyarrow')
#print('posts cargado')

bucket = 'insumosprueba'  # already created on S3
csv_buffer = StringIO()
perfiles.to_csv(csv_buffer)

s3_resource = boto3.resource('s3')
s3_resource.Object(bucket, 'resultado.csv').put(Body=csv_buffer.getvalue())
