import streamlit as st
import pandas as pd
import pygsheets
import json

# Lê credenciais do secrets
creds = st.secrets["gcp_service_account"]
creds_dict = json.loads(json.dumps(dict(creds)))

# Autoriza com pygsheets
client = pygsheets.authorize(service_account_json=creds_dict)

# Abrir planilha
meuArquivoGoogleSheets = "https://docs.google.com/spreadsheets/d/16d4yI58TXd0BbEXqGg4Ty7wx30iskWn2nxP5pxVeKeU/"
arquivo = client.open_by_url(meuArquivoGoogleSheets)
aba = arquivo.worksheet_by_title("streamlit")

# Pega dados
data = aba.get_all_values()
df = pd.DataFrame(data)

st.write(df)
st.title("APRENDENDO A CONECTAR GOOGLE SHEETS COM STREAMLIT")
st.subheader("Importando dados do Google Sheets")
