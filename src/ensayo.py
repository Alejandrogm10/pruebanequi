# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 18:42:25 2022

@author: Alejandro
"""


import pandas as pd
import boto3
import io

# =============================================================================
# EDA: Exploratory Data Analysis
# =============================================================================

# Cargar archivo con perfiles de instagram formato csv separado por tabulador
s3_file_key = 'instagram_profiles2.csv'
bucket = 'insumosprueba'
s3 = boto3.client('s3')
obj = s3.get_object(Bucket=bucket, Key=s3_file_key)
perfiles = pd.read_csv(io.BytesIO(obj['Body'].read()),sep=',')
