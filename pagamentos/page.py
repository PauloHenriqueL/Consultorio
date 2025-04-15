import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from pagamentos.models import Pagamento



def show_pagamentos():
    st.write('Lista Pagamentos')

    # Consulta os objetos do modelo Pagamentos
    Pagamentos = Pagamento.objects.all().values()  # Retorna uma QuerySet como uma lista de dicionários

    # Converte a lista de dicionários em um DataFrame
    df = pd.DataFrame(Pagamentos)

    # Exibe o DataFrame na tabela AgGrid
    AgGrid(
        data=df,
        reload_data=True,
        key='pagamentos_grid',    
    )

    st.title('Cadastrar novo Pagamento')
    name = st.text_input('Novo Pagamento')
    if st.button('Cadastrar'):
        st.success(f'Pagamento de "{name}" cadastrado com sucesso')
