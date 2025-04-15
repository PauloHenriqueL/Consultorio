import streamlit as st
import os
import django
# Configurando o Django para usar o arquivo de configurações correto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')  # Certifique-se de que 'app.settings' está correto
django.setup()
# Importando as páginas
from atendimento.page import show_atendimento
from decano.page import show_decano
from pacientes.page import show_pacientes
from pagamentos.page import show_pagamentos
from Terapeuta.page import show_terapeutas
from home.page import show_home
from login.page import show_login


def main():  # Organizando o código para deixar ele facil de entender
    
    if 'token' not in st.session_state:
        show_login()
    else:    
        st.title('Flix APP')

        menu_option = st.sidebar.selectbox(  # Criando sidebarselecetbox
            'Selecione uma opção',
            ['Início', 'Atendimentos', 'Pacientes', 'Decanos', 'Pagamentos', 'Terapeutas']
        )

        if menu_option == 'Início':  # Definindo caminho das opções do sidebar
            show_home()

        if menu_option == 'Atendimentos':
            show_atendimento()

        if menu_option == 'Pacientes':
            show_pacientes()

        if menu_option == 'Decanos':
            show_decano()

        if menu_option == 'Pagamentos':
            show_pagamentos()

        if menu_option == 'Terapeutas':
            show_terapeutas()


if __name__ == '__main__':
    main()
