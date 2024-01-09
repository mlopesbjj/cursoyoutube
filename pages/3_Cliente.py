import streamlit as st

st.title(":wave: Cadastro de clientes")

form = st.form(key="Clientes", clear_on_submit=True)
paises = ['Brasil', 'Italia' ]

with form:
    input_name = st.text_input("Nome: ", placeholder="Insira seu nome aqui.")
    input_email = st.text_input("E-mail: ", placeholder="Insira seu e-mail aqui.")
    input_password = st.text_input("Senha: ", placeholder="Insira sua senha.", type="password")
    input_pais = st.selectbox("Selecione o pais: ", paises)

    botao_submit = form.form_submit_button("Confirma!")

    if botao_submit:
        st.write("Clicou no botao!")

