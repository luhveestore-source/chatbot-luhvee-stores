import streamlit as st

# Configuração da página
st.set_page_config(page_title="Robô Luana - Global Marketing", page_icon="🛍️")

# --- BANCO DE LINKS (ATUALIZADO) ---
links_luhvee = {
    "Shopee 🛍️": "https://collshp.com/luhveestores?view=storefront",
    "Centralizador 🌐": "https://luhveestore-unbgvh5h.manus.space",
    "Mercado Livre 📦": "https://www.mercadolivre.com.br/social/axwelloliveira",
    "ProDentim Presell 🦷": "http://exclusive-dental-deal.netlify.netlify.app",
    "ProDentim Systeme.io 🚀": "https://luhvee-store.systeme.io/prodentim-special"
}

# --- LOGO ---
try:
    st.image("1000396187.jpg", width=200)
except:
    st.title("💖 LUHVEE STORES")

st.title("🤖 Robô Luana: Global Sales Agency")
st.markdown("---")

# Menu Lateral
with st.sidebar:
    st.header("⚙️ Settings / Configurações")
    nicho = st.selectbox("Product / Nicho:", 
                        ["Achadinhos Brasil", "ProDentim (USA/English)"])
    
    canal = st.multiselect("Social Media:", 
                          ["Instagram", "Facebook", "WhatsApp", "ManyChat"],
                          default=["Instagram", "Facebook"])
    
    st.divider()
    st.warning("⚠️ **REMINDER:** Apply your WATERMARK to all images before posting!")

# Entrada de Dados
st.subheader("📝 Campaign Details")

if nicho == "ProDentim (USA/English)":
    st.info("🌎 Mode: English Language Active")
    nome_produto = "ProDentim - Advanced Oral Care"
    preco_produto = st.text_input("Offer Price (ex: $49/bottle):")
    vitrine_escolhida = st.selectbox("Select Destination:", ["ProDentim Presell 🦷", "ProDentim Systeme.io 🚀"])
else:
    nome_produto = st.text_input("Nome do Produto:")
    preco_produto = st.text_input("Preço (R$):")
    vitrine_escolhida = st.selectbox("Escolha a vitrine:", ["Shopee 🛍️", "Centralizador 🌐", "Mercado Livre 📦"])

link_final = links_luhvee[vitrine_escolhida]

if st.button("🚀 GENERATE SCRIPT & CELEBRATE"):
    if preco_produto:
        st.balloons()
        
        # --- LÓGICA PRODENTIM (INGLÊS) ---
        if nicho == "ProDentim (USA/English)":
            if "Instagram" in canal:
                st.subheader("📸 Instagram Caption (120 chars limit)")
                # Legenda em Inglês com limite de 120
                eng_insta = f"🦷 Healthy teeth & gums! ✨ Discover ProDentim's secret. 🛍️ LINK IN BIO! #oralhealth #prodentim #white-teeth"
                st.code(eng_insta[:120])
                
            if "Facebook" in canal:
                st.subheader("🔵 Facebook Ad Copy")
                st.code(f"📢 Tired of gum issues? Try ProDentim! 🦷✨\n✅ Fresh breath & strong teeth.\n💰 Special Offer: {preco_produto}\n📍 Get yours here: {link_final}")
            
            if "ManyChat" in canal:
                st.subheader("🤖 ManyChat / DM Response")
                st.code(f"Hi! ✨ Here is your exclusive link for ProDentim: \n\n🔗 {link_final} \n\nHave a great day! 😊")

        # --- LÓGICA ACHADINHOS (PORTUGUÊS) ---
        else:
            if "Instagram" in canal:
                st.subheader("📸 Legenda Instagram (Máx 120 letras)")
                pt_insta = f"🔥 {nome_produto} por R${preco_produto}! ✨ Praticidade pra sua casa. 🛍️ LINK NA BIO! #luhvee #achadinhos"
                st.code(pt_insta[:120])

            if "Facebook" in canal:
                st.subheader("🔵 Post Facebook")
                st.code(f"📢 ACHADINHO: {nome_produto}\n💰 Por apenas R${preco_produto}\n📍 Confira: {link_final}\n✅ Siga LuhVee Stores!")

st.divider()
st.caption("LuhVee Stores - Global Marketing Automation")
