
import streamlit as st

# Configuração da página
st.set_page_config(page_title="LuhVee Stores - Oficial", page_icon="🛍️")

# --- 1. EXIBIÇÃO DO LOGO ---
# Tentamos carregar a imagem que você subiu no GitHub
try:
    st.image("1000396187.jpg", width=250) # Use o nome exato do arquivo que você subiu
except:
    st.title("💖 LUHVEE STORES")

# --- 2. BOAS-VINDAS ---
st.write("---")
nome = st.text_input("Olá! Para começar, qual é o seu nome?")

if nome:
    st.subheader(f"Bem-vindo(a), {nome}! ✨")
    st.write("Escolha uma das nossas vitrines especiais abaixo:")

    # --- 3. DESTAQUES EM COLUNAS ---
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎁 Mercado Livre"):
            st.markdown("[Acessar Mercado Livre](https://luhveestore-unbgvh5h.manus.space)")
            
    with col2:
        if st.button("🛍️ Shopee"):
            st.markdown("[Acessar Shopee](https://luhveestore-unbgvh5h.manus.space)")

    st.write("---")
    
    # --- 4. O BOTÃO DOS BALÕES ---
    # Quando o cliente clica aqui, a mágica acontece!
    if st.button("🚀 CLIQUE AQUI PARA VER TODAS AS OFERTAS"):
        st.balloons() # Comando que faz os balões subirem
        st.success(f"Excelente escolha, {nome}!")
        st.markdown("### 🔗 [CLIQUE AQUI PARA ACESSAR NOSSA VITRINE COMPLETA](https://luhveestore-unbgvh5h.manus.space)")

# Rodapé profissional
st.write("---")
st.caption("LuhVee Stores | Afiliado Autorizado | Mercado Livre - Shopee - Digistore24")
