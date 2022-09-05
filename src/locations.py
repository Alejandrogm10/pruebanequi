# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 21:14:09 2022

@author: Alejandro
"""


import pandas as pd
import seaborn as sb
import boto3
import io
from io import StringIO

locations = pd.read_csv(r'C:\Users\Alejandro\Prueba\instagram_locations.csv', sep=',')

s3_file_key = 'instagram_locations'
bucket = 'insumosprueba'
s3 = boto3.client('s3')
obj = s3.get_object(Bucket=bucket, Key=s3_file_key)
perfiles = pd.read_csv(io.BytesIO(obj['Body'].read()), sep=',')
print('locations cargado')

# =============================================================================
# 1. Información Básica sobre el DataSet'''
# =============================================================================
#Vista Previa
print(locations.head())
#Dimensionalidad
print('El DataSet tiene {} filas y {} columnas'.format(locations.shape[0],locations.shape[1])) 
#Describir la información
print(locations.describe().apply(lambda x: x.apply('{0:.0f}'.format)))
#Información basica - tipos de datos
print(locations.info())
# =============================================================================
# 2. Valores Duplicados'''
# =============================================================================
#Valores duplicados en el dataframe
print('El DataSet tiene {} registros duplicados'.format(locations.duplicated().sum()))

# =============================================================================
# 3. Valores Nulos
# =============================================================================
print(locations.isnull().sum())


# =============================================================================
# 4. Valores Únicos
# =============================================================================
print(locations['city'].unique())
print(sb.countplot(locations['city']))

# =============================================================================
# 5. Eliminar columnas innecesarias en el modelo
# =============================================================================
locations = locations.drop(['region'], axis=1)


csv_buffer = StringIO()
locations.to_csv(csv_buffer)
s3_resource = boto3.resource('s3')
s3_resource.Object(bucket, 'resultado_instagram_locations.csv').put(Body=csv_buffer.getvalue())
