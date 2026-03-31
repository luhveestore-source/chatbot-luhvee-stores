import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="Robô Luana - Copywriter Pro", page_icon="🛍️")

# --- BANCO DE LINKS ---
links_luhvee = {
    "Shopee 🛍️": "https://collshp.com/luhveestores?view=storefront",
    "Centralizador 🌐": "https://luhveestore-unbgvh5h.manus.space",
    "Mercado Livre 📦": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "ProDentim Presell 🦷": "http://exclusive-dental-deal.netlify.app",
    "ProDentim Systeme.io 🚀": "https://luhvee-store.systeme.io/prodentim-special"
}

# --- LOGO ---
try:
    st.image("1000396187.jpg", width=200)
except:
    st.title("💖 LUHVEE STORES")

st.title("🤖 Robô Luana: Sua Máquina de Vendas")
st.markdown("---")

# Menu Lateral
with st.sidebar:
    st.header("⚙️ Configurações")
    nicho = st.selectbox("O que vamos vender?", 
                        ["Cozinha e Casa", "Limpeza Prática", "Moda", "Beleza", "Eletrônicos", "ProDentim (USA/English)"])
    
    redes = st.multiselect("Gerar para quais redes?", 
                          ["Instagram", "Facebook", "WhatsApp/Telegram", "ManyChat (DM)"],
                          default=["Instagram", "Facebook", "WhatsApp/Telegram", "ManyChat (DM)"])
    st.divider()
    st.warning("⚠️ **DICA:** Não esqueça a **MARCA D'ÁGUA**!")

# Entrada de Dados
st.subheader("📝 Detalhes do Produto")
if nicho == "ProDentim (USA/English)":
    nome_prod = "ProDentim"
    preco_prod = st.text_input("Offer Price (ex: $49/bottle):")
    vitrine_final = st.selectbox("Select Destination:", ["ProDentim Presell 🦷", "ProDentim Systeme.io 🚀"])
else:
    nome_prod = st.text_input("Nome do Produto:")
    preco_prod = st.text_input("Preço (R$):")
    vitrine_final = st.selectbox("Escolha a vitrine:", ["Shopee 🛍️", "Centralizador 🌐", "Mercado Livre 📦"])

link_final = links_luhvee[vitrine_final]

# --- LÓGICA DE COPYWRITING (FRASES PERSUASIVAS) ---
def gerar_copy(nicho, produto, preco, rede):
    # Dicionário de Gatilhos Mentais
    if nicho == "Cozinha e Casa":
        frase = f"🍳 Chega de sofrer na cozinha! O(a) {produto} é o braço direito que faltava. Praticidade pura por R${preco}! ✨"
    elif nicho == "Limpeza Prática":
        frase = f"🧹 Limpeza num piscar de olhos! Com esse(a) {produto}, sua casa brilha sem esforço. Só R${preco}! 💎"
    elif nicho == "Moda":
        frase = f"💃 O look perfeito existe! Esse(a) {produto} vai te deixar ainda mais maravilhosa por apenas R${preco}. 😍"
    elif nicho == "Beleza":
        frase = f"✨ Realce sua beleza com o que há de melhor! O(a) {produto} chegou para transformar sua rotina por R${preco}. 💖"
    elif nicho == "Eletrônicos":
        frase = f"🚀 Tecnologia de ponta no seu bolso! O(a) {produto} é o upgrade que você merece. Garanta o seu por R${preco}! ⚡"
    elif nicho == "ProDentim (USA/English)":
        frase = f"🦷 Stop hiding your smile! Rebuild your oral health with ProDentim. Only {preco}! 🛍️"
    else:
        frase = f"🔥 Achadinho imperdível! O(a) {produto} por apenas R${preco}. Você não pode perder! 🛍️"

    return frase

if st.button("🚀 GERAR SCRIPTS DE VENDA"):
    if preco_prod:
        st.balloons()
        copy_base = gerar_copy(nicho, nome_prod, preco_prod, "Geral")
        
        # --- INSTAGRAM ---
        if "Instagram" in redes:
            st.subheader("📸 Instagram (Persuasivo + Trava 120)")
            legenda_insta = f"{copy_base} Link na Bio! #luhvee #oferta"
            st.code(legenda_insta[:120])

        # --- FACEBOOK ---
        if "Facebook" in redes:
            st.subheader("🔵 Facebook (Gatilho de Urgência)")
            txt_fb = f"📢 VOCÊ PRECISA DISSO: {nome_prod}!\n{copy_base}\n📍 Compre aqui agora: {link_final}\n✅ Siga LuhVee Stores para não perder!"
            st.code(txt_fb)

        # --- WHATSAPP ---
        if "WhatsApp/Telegram" in redes:
            st.subheader("📲 WhatsApp (Direto ao ponto)")
            txt_wa = f"🔥 *OFERTA EXCLUSIVA!* \n\n*Produto:* {nome_prod}\n{copy_base}\n\n🔗 *Link Promocional:* {link_final}"
            st.code(txt_wa)

        # --- MANYCHAT ---
        if "ManyChat (DM)" in redes:
            st.subheader("🤖 ManyChat (Atendimento VIP)")
            txt_dm = f"Oi! ✨ Ótima escolha! O(a) {nome_prod} é um dos nossos campeões de vendas.\n\nAqui está o seu link: {link_final} \n\nAproveite! 😊"
            st.code(txt_dm)
    else:
        st.error("Preencha o preço para gerar a copy!")

st.divider()
st.caption("LuhVee Stores - Inteligência em Vendas v5.0")
