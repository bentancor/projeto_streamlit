import streamlit as st
import pandas as pd

dados = pd.read_csv('projeto_pratico/clientes.csv')

st.title('Clientes Cadastrados')
st.dataframe(dados)