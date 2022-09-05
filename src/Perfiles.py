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

# Cargar archivo con perfiles de instagram formato csv separado por tabulador
s3_file_key = 'instagram_profiles.csv'
bucket = 'insumosprueba'
s3 = boto3.client('s3')
obj = s3.get_object(Bucket=bucket, Key=s3_file_key)
perfiles = pd.read_csv(io.BytesIO(obj['Body'].read()),sep=',')


print('archivo perfiles leido correctamente')

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

perfiles["is_business_account"].fillna("Not Defined", inplace = True)

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

csv_buffer = StringIO()
perfiles.to_csv(csv_buffer)
s3_resource = boto3.resource('s3')
s3_resource.Object(bucket, 'resultado_instagram_profiles.csv').put(Body=csv_buffer.getvalue())
