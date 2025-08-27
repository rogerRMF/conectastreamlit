
import streamlit as st 
import pandas as pd 
import pygsheets 
import os 

credenciais = pygsheets.authorize(service_file=os.getcwd() + '/cred.json') 

meuArquivoGoogleSheets= "https://docs.google.com/spreadsheets/d/16d4yI58TXd0BbEXqGg4Ty7wx30iskWn2nxP5pxVeKeU/"
arquivo = credenciais.open_by_url(meuArquivoGoogleSheets)
aba = arquivo.worksheet_by_title("streamlit") 
data = aba.get_all_values() 
df = pd.DataFrame(data)
st.write(df)

st.title("APRENDENDO A CONECTA GOOGLE SHEETS COM STREAMLIT") 
st.subheader("Importando dados do Google Sheets")
