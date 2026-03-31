import streamlit as st

# Configuração da página
st.set_page_config(page_title="Robô Luana - Central Multi-Vendas", page_icon="🛍️")

# --- BANCO DE LINKS (TUDO UNIFICADO) ---
links_luhvee = {
    "Shopee 🛍️": "https://collshp.com/luhveestores?view=storefront",
    "Centralizador 🌐": "https://luhveestore-unbgvh5h.manus.space",
    "Mercado Livre 📦": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "ProDentim Presell 🦷": "http://exclusive-dental-deal.netlify.app",
    "ProDentim Systeme.io 🚀": "https://luhvee-store.systeme.io/prodentim-special"
}

# --- EXIBIÇÃO DO LOGO ---
try:
    st.image("1000396187.jpg", width=200)
except:
    st.title("💖 LUHVEE STORES")

st.title("🤖 Robô Luana: Sua Agência Digital")
st.markdown("---")

# Menu Lateral para Organização
with st.sidebar:
    st.header("⚙️ Configurações")
    nicho = st.selectbox("Escolha o Nicho / Product:", 
                        ["Achadinhos Brasil", "ProDentim (USA/English)", "Cozinha", "Beleza", "Eletrônicos"])
    
    redes = st.multiselect("Gerar para quais redes?", 
                          ["Instagram", "Facebook", "WhatsApp/Telegram", "ManyChat (DM)"],
                          default=["Instagram", "Facebook", "WhatsApp/Telegram", "ManyChat (DM)"])
    
    st.divider()
    st.warning("⚠️ **LEMBRETE:** Aplique sua **MARCA D'ÁGUA** em todas as imagens antes de publicar!")

# Entrada de Dados
st.subheader("📝 Detalhes do Produto")

if nicho == "ProDentim (USA/English)":
    st.info("🌎 Mode: English Language Active")
    nome_produto = "ProDentim - Advanced Oral Care"
    preco_produto = st.text_input("Offer Price (ex: $49/bottle):")
    vitrine_final = st.selectbox("Select Destination:", ["ProDentim Presell 🦷", "ProDentim Systeme.io 🚀"])
else:
    nome_produto = st.text_input("Nome do Produto:")
    preco_produto = st.text_input("Preço (R$):")
    vitrine_final = st.selectbox("Escolha a vitrine:", ["Shopee 🛍️", "Centralizador 🌐", "Mercado Livre 📦"])

link_escolhido = links_luhvee[vitrine_final]

if st.button("🚀 GERAR ROTEIRO E COMEMORAR"):
    if preco_produto:
        st.balloons()
        st.markdown("---")
        
        # --- SEÇÃO 1: INSTAGRAM (COM TRAVA DE 120 CARACTERES) ---
        if "Instagram" in redes:
            st.subheader("📸 Legenda Instagram (Máx 120 letras)")
            if nicho == "ProDentim (USA/English)":
                texto_insta = f"🦷 Healthy teeth & gums! ✨ Discover ProDentim's secret. 🛍️ LINK IN BIO! #oralhealth #prodentim #whiteteeth"
            else:
                texto_insta = f"🔥 {nome_produto} por R${preco_produto}! ✨ Praticidade pra sua casa. 🛍️ LINK NA BIO! #luhvee #achadinhos"
            
            legenda_final = texto_insta[:120]
            st.code(legenda_final)
            st.caption(f"Caracteres: {len(legenda_final)}/120")

        # --- SEÇÃO 2: FACEBOOK ---
        if "Facebook" in redes:
            st.subheader("🔵 Post Facebook")
            if nicho == "ProDentim (USA/English)":
                txt_fb = f"📢 Tired of gum issues? Try ProDentim! 🦷✨\n✅ Fresh breath & strong teeth.\n💰 Special Offer: {preco_produto}\n📍 Get yours here: {link_escolhido}"
            else:
                txt_fb = f"📢 ACHADINHO: {nome_produto}\n💰 Por apenas R${preco_produto}\n📍 Confira: {link_escolhido}\n✅ Siga LuhVee Stores!"
            st.code(txt_fb)

        # --- SEÇÃO 3: WHATSAPP / TELEGRAM ---
        if "WhatsApp/Telegram" in redes:
            st.subheader("📲 Para WhatsApp / Telegram")
            if nicho == "ProDentim (USA/English)":
                txt_wa = f"⭐ *PRODENTIM SPECIAL OFFER* ⭐\n\nAdvanced Oral Care for you!\n💰 *Price:* {preco_produto}\n🔗 *Link:* {link_escolhido}"
            else:
                txt_wa = f"⭐ *OFERTA LUHVEE STORES* ⭐\n\n*Produto:* {nome_produto}\n*Valor:* R${preco_produto}\n🔗 *Link:* {link_escolhido}\n\n_Aproveite agora!_"
            st.code(txt_wa)

        # --- SEÇÃO 4: MANYCHAT (DM) ---
        if "ManyChat (DM)" in redes:
            st.subheader("🤖 Para ManyChat (Automação)")
            if nicho == "ProDentim (USA/English)":
                txt_dm = f"Hi! ✨ Here is the link for ProDentim you requested: \n\n🔗 {link_escolhido} \n\nAny questions, just ask! 😊"
            else:
                txt_dm = f"Olá! ✨ Aqui está o link do(a) {nome_produto} que você viu: \n\n🔗 {link_escolhido} \n\nBoas compras! 😊"
            st.code(txt_dm)
            
    else:
        st.error("❌ Por favor, preencha os detalhes do preço para gerar o conteúdo.")

st.markdown("---")
st.caption("LuhVee Stores - Central de Automação Global v4.0")
