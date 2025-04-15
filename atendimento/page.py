import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from atendimento.models import Atendimento


def show_atendimento():
    st.write('Lista Atendimentos')

    # Consulta os objetos do modelo Atendimento
    atendimentos = Atendimento.objects.all().values()  # Retorna uma QuerySet como uma lista de dicionários

    # Converte a lista de dicionários em um DataFrame
    df = pd.DataFrame(atendimentos)

    # Exibe o DataFrame na tabela AgGrid
    AgGrid(
        data=df,
        reload_data=True,
        key='atendimento_grid',
    )

    st.title('Cadastrar novo Atendimento')
    name = st.text_input('Novo Atendimento')
    if st.button('Cadastrar'):
        st.success(f'Atendimento de "{name}" cadastrado com sucesso')
