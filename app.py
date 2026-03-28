import streamlit as st

# Configuração da página (Título que aparece na aba do navegador)
st.set_page_config(page_title="LuhVee Stores - Assistente", page_icon="🛍️")

# --- DESIGN DA INTERFACE ---
st.title("🛍️ Bem-vindo à LuhVee Stores")
st.write("Olá! Sou o seu assistente virtual de ofertas.")

nome = st.text_input("Como podemos te chamar?")

if nome:
    st.write(f"Prazer em te atender, *{nome}*! Escolha uma das opções abaixo:")
    
    # Criando botões bonitos para o cliente clicar
    if st.button("✨ ACESSAR VITRINE COMPLETA"):
        st.success("Clique no link abaixo para abrir nossas ofertas:")
        st.markdown("[👉 CLIQUE AQUI PARA ABRIR A LOJA](https://luhveestore-unbgvh5h.manus.space)")

    if st.button("📱 Falar com Suporte Humano"):
        st.info("Você será redirecionado para o nosso WhatsApp de suporte.")
        # Substitua pelo seu número real abaixo
        st.markdown("[Falar no WhatsApp](https://wa.me/5511948021428)")

st.divider()
st.caption("LuhVee Stores - Afiliado Autorizado Mercado Livre, Shopee e Digistore24")
