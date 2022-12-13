import pandas as pd
import numpy as np
import pickle
import streamlit as st

df = pd.read_csv('csv_limio.csv')
scaler = pickle.load(open('scaler.py','rb'))

st.title("Viviendas .")
st.write("Bienvenido a nuestra aplicación. Aquí puede seleccionar lo que quiere hacer, ejecutando la aplicación de predicción de casas o buscar casas en nuestra base de datos.")

st.title("Aplicación de predicción de viviendas.")
st.write("Obtendrá el precio de una casa en función de las diferentes características de la casa")

habitaciones = st.number_input("Número de habitaciones: ")
banos = st.number_input("Número de baños: ")
sqft_living = st.number_input("Metros cuadrados de la vivienda: ")
sqft_lot = st.number_input("Metros cuadrados del terreno: ")
floors = st.number_input("Número de plantas: ")
waterfront = st.number_input("Vistas al mar: ")
view = st.number_input("Vistas (0-4): ")
condition = st.number_input("Condición (1-5): ")
grade = st.number_input("Calificación (1-13): ")
sqft_above = st.number_input("Metros cuadrados de la vivienda por encima del suelo: ")
sqft_basement = st.number_input("Metros cuadrados de la vivienda por debajo del suelo: ")
yr_built = st.number_input("Año de construcción: ")
yr_renovated = st.number_input("Año de renovación: ")
zipcode = st.number_input("Código postal: ")
lat = st.number_input("Latitud: ")
long = st.number_input("Longitud de la casa: ")
sqft_living15 = st.number_input("Metros cuadrados de la vivienda en 2015: ")
sqft_lot15 = st.number_input("Metros cuadrados del terreno en 2015: ")

if st.button("Predicción de la casa: "):
    y= pd.DataFrame({'bedrooms':habitaciones, 'bathrooms':banos, 'sqft_living':sqft_living, 'sqft_lot':sqft_lot, 'floors':floors, 'waterfront':waterfront, 'view':view, 'condition':condition, 'grade':grade, 'sqft_above':sqft_above, 'sqft_basement':sqft_basement, 'yr_built':yr_built, 'yr_renovated':yr_renovated, 'zipcode':zipcode, 'lat':lat, 'long':long, 'sqft_living15':sqft_living15, 'sqft_lot15':sqft_lot15})

    x_scaled = scaler.transform(y)
    df_scaled = pd.DataFrame(x_scaled, columns = y.columns)

    predicción = np.exp(linear.predict(df_scaled))
    predicción= np.trunc(predicción)

st.write('El precio de la casa es: ', predicción)