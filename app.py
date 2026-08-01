# vibecoding - programar copiloto - IA

# procoding - programação convencional  - documentação


import streamlit as st 
import pandas as pd 


st.title('Minha web page')


dados  = pd.read_csv('dados.csv')
df = pd.DataFrame(dados)
st.write(dados)

#gráficos

st.bar_chart(df, x = 'vendedor', y = 'vendas')

#imagem

st.image('img.png')

st.map()