import streamlit as st

# Configuração da página
st.set_page_config(page_title="Robô Luana - Central de Automação", page_icon="🛍️")

# --- BANCO DE LINKS ---
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

st.title("🤖 Robô Luana: Sua Agência de Vendas")
st.markdown("---")

# Menu Lateral
with st.sidebar:
    st.header("⚙️ Configurações")
    nicho = st.selectbox("Nicho do Produto:", 
                        ["Achadinhos Brasil", "ProDentim (USA/English)", "Cozinha", "Beleza", "Limpeza"])
    
    canal = st.multiselect("Gerar para quais redes?", 
                          ["Instagram", "Facebook", "WhatsApp/Telegram", "ManyChat (DM)"],
                          default=["Instagram", "Facebook", "WhatsApp/Telegram", "ManyChat (DM)"])
    
    st.divider()
    st.warning("⚠️ **AVISO:** Aplique sua **MARCA D'ÁGUA** antes de publicar!")

# Entrada de Dados
st.subheader("📝 Detalhes da Oferta")
col_1, col_2 = st.columns(2)

with col_1:
    if nicho == "ProDentim (USA/English)":
        nome_prod = "ProDentim"
        st.info("🌎 Mode: English Active")
    else:
        nome_prod = st.text_input("Nome do Produto:")
with col_2:
    preco_prod = st.text_input("Preço:")

# Escolha da Vitrine
vitrine_escolhida = st.selectbox("Enviar para qual link?", list(links_luhvee.keys()))
link_final = links_luhvee[vitrine_escolhida]

if st.button("🚀 GERAR ROTEIRO COMPLETO"):
    if preco_prod:
        st.balloons()
        st.markdown("---")
        
        # --- INSTAGRAM (COM GATILHO INFO + 120 LETRAS) ---
        if "Instagram" in canal:
            st.subheader("📸 Legenda Instagram (Gatilho INFO)")
            if nicho == "ProDentim (USA/English)":
                txt_insta = f"🦷 Stop hiding your smile! Rebuild oral health. 🛍️ Comment INFO for the link! #prodentim #smile"
            else:
                txt_insta = f"🤩 {nome_prod} por R${preco_prod}! ✨ Mudou minha rotina! 🚀 Comente INFO que te mando o link no Direct!"
            
            legenda_final = txt_insta[:120] # TRAVA DE 120 CARACTERES
            st.code(legenda_final)
            st.caption(f"Tamanho: {len(legenda_final)}/120")

        # --- FACEBOOK ---
        if "Facebook" in canal:
            st.subheader("🔵 Post para Facebook")
            if nicho == "ProDentim (USA/English)":
                txt_fb = f"📢 Tired of gum issues? Try ProDentim! 🦷✨\n💰 Price: {preco_prod}\n📍 Get it here: {link_final}"
            else:
                txt_fb = f"📢 ACHADINHO: {nome_prod}\n💰 Apenas R${preco_prod}\n📍 Link: {link_final}\n✅ Siga LuhVee Stores!"
            st.code(txt_fb)

        # --- WHATSAPP ---
        if "WhatsApp/Telegram" in canal:
            st.subheader("📲 Para WhatsApp / Grupos")
            if nicho == "ProDentim (USA/English)":
                txt_wa = f"⭐ *PRODENTIM OFFER* ⭐\n\nAdvanced Oral Care!\n🔗 *Link:* {link_final}"
            else:
                txt_wa = f"🔥 *OFERTA LUHVEE STORES* 🔥\n\n*Produto:* {nome_prod}\n*Valor:* R${preco_prod}\n🔗 *Link:* {link_final}"
            st.code(txt_wa)

        # --- MANYCHAT (DM AUTOMÁTICA) ---
        if "ManyChat (DM)" in canal:
            st.subheader("🤖 Resposta do ManyChat (Direct)")
            if nicho == "ProDentim (USA/English)":
                txt_dm = f"Hi! ✨ Here is your link for ProDentim: \n\n🔗 {link_final} \n\nEnjoy! 😊"
            else:
                txt_dm = f"Olá! ✨ Fico feliz com seu interesse no(a) {nome_prod}!\n\nAqui está o seu link exclusivo: \n🔗 {link_final}\n\nBoas compras! 😊"
            st.code(txt_dm)
            
    else:
        st.error("Preencha o preço para gerar o conteúdo!")

st.divider()
st.caption("LuhVee Stores - Automação Total v6.0")
